from __future__ import annotations

import logging
import math

import click
import numpy as np
import vpype as vp
import vpype_cli

from .matrices import (
    DEFAULT_DELTA_Z,
    layer_id_to_z,
    perspective_matrix,
    rotate_x,
    rotate_y,
    scale,
    translate,
)


@vpype_cli.cli.command(group="Perspective")
@click.option(
    "-l",
    "--layer",
    type=vpype_cli.LayerType(accept_multiple=True),
    default="all",
    help="Target layer(s).",
)
@click.option(
    "-f",
    "--hfov",
    type=vpype_cli.AngleType(),
    default=45.0,
    help="Horizontal field-of-view.",
)
@click.option(
    "-t",
    "--tilt",
    type=vpype_cli.AngleType(),
    default=0.0,
    help="Camera tilt above/bellow the origin.",
)
@click.option(
    "-p",
    "--pan",
    type=vpype_cli.AngleType(),
    default=0.0,
    help="Camera pan around the origin.",
)
@click.option(
    "-m",
    "--move",
    type=vpype_cli.LengthType(),
    nargs=3,
    default=(0.0, 0.0, 0.0),
    metavar="DX DY DZ",
    help="Camera displacement.",
)
@click.option(
    "-a",
    "--aiming-point",
    type=vpype_cli.LengthType(),
    nargs=3,
    metavar="PX PY PZ",
    help="Camera aiming point.",
)
@vpype_cli.global_processor
def perspective(
    doc: vp.Document,
    layer: int | list[int],
    hfov: float,
    tilt: float,
    pan: float,
    move: tuple[float, float, float],
    aiming_point: tuple[float, float, float] | None,
) -> vp.Document:
    """Project the geometries in perspective.

    This command constructs a 3D scene based on the geometries and project it using a
    perspective camera.

    By default, the 3D scene is constructed as a set of parallel vertical plans, with the
    camera pointed at the front-most plan (layer with the highest layer ID). The origin is
    placed at the mid-point between the furthest (layer 1) and front-most plans. Refer to the
    README for an illustration. Each plan is separated by DELTA_Z, which defaults to 1cm.

    The distance between the camera and the front-most plan is determined by the `--hfov`
    option.

    The camera position can be altered using `--tilt` (rotate the camera up/down around the
    origin), `--pan` (rotate the camera right/left around the origin), and `--move` (translate
    the camera along X, Y, and Z values with respect to the camera coordinate system) commands.

    The position, size, and orientation of each plan/layer may be altered using the
    `ptranslate`, `pscale`, and `protate` commands. Their z-position can be changed using the
    `pz` command.

    \f
    I wish click wouldn't destroy this illustration...

                        |\                             |\ |\
                        | \              | y           | \| \
         camera         |  \   ...    ___|       ...   |  \  \
                        \  |         z   \             \  |  |
                         \ |              \ x           \ |\ |
                          \|                             \| \|
                                       origin
                       layer N                      layer 2  layer 1
                      z=(N-1)*dz                       z=dz  z=0
    """

    lids = vpype_cli.multiple_to_layer_ids(layer, doc)

    # Compute the offset between vpype's origin (top-left corner) to the world origin (middle
    # of the layer quad.
    if doc.page_size:
        w, h = doc.page_size
        offset = -w / 2, -h / 2
    elif (bounds := doc.bounds(lids)) is not None:
        w = bounds[2] - bounds[0]
        h = bounds[3] - bounds[1]
        offset = -bounds[0] - w / 2, -bounds[1] - h / 2
    else:
        logging.warning("!!! perspective: cannot compute bounds")
        return doc

    # Convert from vpype coordinate to world coordinates
    # - the world origin is the middle of layer 1's quad, which is at z = 0
    # - y axis points up, x axis points left, z axis points toward the camera
    vpype_to_world = scale(1, -1, 1) @ translate(*offset, 0)
    world_to_vpype = np.linalg.inv(vpype_to_world)

    # Camera setup
    # For the perspective matrix to work, the camera must lie at the origin. As a result, the
    # camera matrix is a combination of multiple thing:
    #
    # - It moves everything in accordance to the desired direction of view (--pan, --tilt,
    #   --move parameters). Since the pan/tilt is around the aiming point (middle of the box
    #   defined by the furthest and front-most layer quads), the rotation must be surrounded
    #   by translations to set the rotation's origin. This is `camera_transform`.
    #
    # - It converts from world coordinates to camera coordinate, which involves translations
    #   from the world origin to the camera position as well as an inversion of the z-axis
    #   direction.
    #
    # - It applies the projection matrix.
    #
    # - It converts everything back to world coordinates.
    #
    #          focal            delta Z
    #         <----->            <-->
    #                    max_z
    #               <---------------->
    #
    #               +            +  +
    #              /|            |  |
    #             / |            |  |
    #            /  |            |  |
    #           /   |            |  |
    #          /    |            |  |
    # Camera  X-----+-------@----+--X world
    #          \    |   camera   |  |  origin
    #           \   |   aiming   |  |
    #            \  |    point   |  |
    #             \ |            |  |
    #              \|            |  |
    #               +            +  +
    #
    #             Layer  ...  Layer Layer
    #               N           2     1
    #

    delta_z = doc.property("prsp_dz")
    if delta_z is None:
        delta_z = DEFAULT_DELTA_Z

    # The focal is computed based on the provided horizontal FOV and the page width.
    focal = w / 2.0 / math.tan(math.radians(hfov) / 2.0)
    max_z = layer_id_to_z(max(lids), delta_z)
    if aiming_point is None:
        aiming_point = (0.0, 0.0, max_z / 2.0)
    camera_transform = (
        translate(-move[0], -move[1], -move[2])
        @ rotate_x(tilt)  # pointing camera "down" by default is more natural
        @ rotate_y(-pan)
        @ translate(-aiming_point[0], -aiming_point[1], -aiming_point[2])
    )
    world_to_camera = (
        translate(0, 0, focal) @ scale(1, 1, -1) @ translate(0, 0, -(max_z / 2.0))
    )
    camera_to_world = np.linalg.inv(world_to_camera)
    camera = camera_to_world @ perspective_matrix(focal) @ world_to_camera @ camera_transform

    for lid in lids:
        layer = doc.layers[lid]
        z = layer_id_to_z(lid, delta_z)
        new_lines = []

        # Extract the transformation matrix and compute the complete transformation matrix
        transform = layer.property("prsp_transform")
        if transform is None:
            transform = np.identity(4)
        matrix = world_to_vpype @ camera @ transform @ vpype_to_world

        for line in layer:
            # Nx1 array of complex -> Nx4 array of homogenous 3D coordinates
            line_homo = np.vstack(
                [line.real.T, line.imag.T, z * np.ones(len(line)), np.ones(len(line))]
            ).T.reshape(-1, 4, 1)
            line_homo = (matrix @ line_homo).reshape(-1, 4)
            new_lines.append(
                line_homo[:, 0] / line_homo[:, 3] + 1j * (line_homo[:, 1] / line_homo[:, 3])
            )
        doc.replace(new_lines, lid, with_metadata=False)

    return doc
