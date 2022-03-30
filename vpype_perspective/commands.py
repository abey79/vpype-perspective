import click
import numpy as np
import vpype as vp
import vpype_cli

from .matrices import (
    DEFAULT_DELTA_Z,
    base_position,
    rotate_x,
    rotate_y,
    rotate_z,
    scale,
    translate,
)


def _get_transform(layer: vp.LineCollection) -> np.ndarray:
    """Get the transform matrix attached to a layer."""
    transform = layer.property("prsp_transform")
    return transform if transform is not None else np.identity(4)


def _apply_transform(layer: vp.LineCollection, mat: np.ndarray) -> None:
    """Apply a transformation to a layer."""
    transform = _get_transform(layer)
    layer.set_property("prsp_transform", mat @ transform)


def _get_layer_center(layer: vp.LineCollection, state: vpype_cli.State) -> np.ndarray:
    """Get the center point of the layer quad.

    This function relies on the `prsp_dz` global property and uses the default value if it is
    not available.
    """
    delta_z = state.document.property("prsp_dz")
    pos = base_position(
        state.current_layer_id, delta_z if delta_z is not None else DEFAULT_DELTA_Z
    )
    transform = _get_transform(layer)
    return transform @ pos


@vpype_cli.cli.command(group="Perspective")
@click.argument("delta-z", metavar="DELTAZ", type=vpype_cli.LengthType())
@vpype_cli.global_processor
def pspread(doc: vp.Document, delta_z: float) -> vp.Document:
    """Set the spread distance.

    By default, layer quads are assumed to be spread with a distance (also called `delta z`) of
    1cm between them. A different value may be set with this command.

    Important: this command must be used *before* using any of the transform commands
    (`protate`, `ptranslate`, and `pscale`) as they rely on the delta z value.
    """
    doc.set_property("prsp_dz", delta_z)
    return doc


@vpype_cli.cli.command(group="Perspective")
@click.argument(
    "axis", metavar="AXIS", type=vpype_cli.ChoiceType(["x", "y", "z"], case_sensitive=False)
)
@click.option(
    "-o",
    "--origin",
    metavar="ORIGIN",
    type=vpype_cli.ChoiceType(choices=["layer", "world"]),
    default="layer",
    help="Origin to use for the rotation",
)
@click.argument("angle", type=vpype_cli.AngleType())
@vpype_cli.layer_processor
@vpype_cli.pass_state
def protate(
    state: vpype_cli.State, layer: vp.LineCollection, axis: str, angle: float, origin: str
) -> vp.LineCollection:
    """Rotate the layer quad(s).

    This command rotates the layer quad(s) by ANGLE degrees around axis AXIS (x, y, or z). The
    rotation is applied around the quad center (`--origin layer`, default) or the world origin
    (`--origin world`).
    """

    if axis == "x":
        transform = rotate_x(angle)
    elif axis == "y":
        transform = rotate_y(angle)
    elif axis == "z":
        transform = rotate_z(angle)
    else:
        raise click.BadParameter(f"invalid rotation axis {axis}")

    if origin == "layer":
        center = _get_layer_center(layer, state)
        transform = translate(*center[0:3]) @ transform @ translate(*-center[0:3])

    _apply_transform(layer, transform)
    return layer


@vpype_cli.cli.command(group="Perspective")
@click.argument("dx", type=vpype_cli.LengthType())
@click.argument("dy", type=vpype_cli.LengthType())
@click.argument("dz", type=vpype_cli.LengthType())
@click.option(
    "-a", "--absolute", is_flag=True, help="Use absolute instead of relative coordinates."
)
@vpype_cli.layer_processor
@vpype_cli.pass_state
def ptranslate(
    state: vpype_cli.State,
    layer: vp.LineCollection,
    dx: float,
    dy: float,
    dz: float,
    absolute: bool,
) -> vp.LineCollection:
    """Translate the layer quad(s).

    This command translates the layer quad(s) by the provided offsets in the world coordinate
    system.

    If `--absolute` is used, (DX, DY, DZ) are considered as absolute values and the
    quad is translated such that its center lies at the target position."""

    transform = translate(dx, dy, dz)
    if absolute:
        center = _get_layer_center(layer, state)
        transform = transform @ translate(*-center[0:3])

    _apply_transform(layer, transform)
    return layer


@vpype_cli.cli.command(group="Perspective")
@click.argument("sx", type=vpype_cli.LengthType())
@click.argument("sy", type=vpype_cli.LengthType())
@click.argument("sz", type=vpype_cli.LengthType())
@click.option(
    "-o",
    "--origin",
    metavar="ORIGIN",
    type=vpype_cli.ChoiceType(choices=["layer", "world"]),
    default="layer",
    help="Origin to use for the scaling.",
)
@vpype_cli.layer_processor
@vpype_cli.pass_state
def pscale(
    state: vpype_cli.State,
    layer: vp.LineCollection,
    sx: float,
    sy: float,
    sz: float,
    origin: str,
) -> vp.LineCollection:
    """Scale the layer's quad.

    This command scales the layer quad(s) by the provided scaling factors. The scaling is done
    along the world coordinate system axis and is applied around the quad center
    (`--origin layer`, default) or the world origin (`--origin world`).
    """

    transform = scale(sx, sy, sz)
    if origin == "layer":
        center = _get_layer_center(layer, state)
        transform = translate(*center[0:3]) @ transform @ translate(*-center[0:3])

    _apply_transform(layer, transform)
    return layer


@vpype_cli.cli.command(group="Perspective")
@vpype_cli.layer_processor
def preset(layer: vp.LineCollection) -> vp.LineCollection:
    """Reset the transformation attached to the target layer(s)."""
    layer.set_property("prsp_transform", np.identity(4))
    return layer
