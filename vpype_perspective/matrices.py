from __future__ import annotations

import math

import numpy as np
import vpype

DEFAULT_DELTA_Z = vpype.convert_length("1cm")


def layer_id_to_z(layer_id: int, delta_z: float) -> float:
    return (layer_id - 1) * delta_z


def base_position(layer_id: int, delta_z: float) -> np.ndarray:
    return np.array([0.0, 0.0, layer_id_to_z(layer_id, delta_z), 1.0], dtype=float)


def translate(dx: float, dy: float, dz: float = 0.0) -> np.ndarray:
    return np.array(
        [
            [1, 0, 0, dx],
            [0, 1, 0, dy],
            [0, 0, 1, dz],
            [0, 0, 0, 1],
        ],
        dtype=float,
    )


def scale(sx: float, sy: float | None = None, sz: float | None = None) -> np.ndarray:
    if sy is None:
        sy = sx
    if sz is None:
        sz = sx

    return np.array(
        [
            [sx, 0, 0, 0],
            [0, sy, 0, 0],
            [0, 0, sz, 0],
            [0, 0, 0, 1],
        ],
        dtype=float,
    )


def rotate_x(angle_deg: float) -> np.ndarray:
    angle_rad = math.radians(angle_deg)
    return np.array(
        [
            [1, 0, 0, 0],
            [0, math.cos(angle_rad), -math.sin(angle_rad), 0],
            [0, math.sin(angle_rad), math.cos(angle_rad), 0],
            [0, 0, 0, 1],
        ],
        dtype=float,
    )


def rotate_y(angle_deg: float) -> np.ndarray:
    angle_rad = math.radians(angle_deg)
    return np.array(
        [
            [math.cos(angle_rad), 0, math.sin(angle_rad), 0],
            [0, 1, 0, 0],
            [-math.sin(angle_rad), 0, math.cos(angle_rad), 0],
            [0, 0, 0, 1],
        ],
        dtype=float,
    )


def rotate_z(angle_deg: float) -> np.ndarray:
    angle_rad = math.radians(angle_deg)
    return np.array(
        [
            [math.cos(angle_rad), -math.sin(angle_rad), 0, 0],
            [math.sin(angle_rad), math.cos(angle_rad), 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1],
        ],
        dtype=float,
    )


def perspective_matrix(f: float) -> np.ndarray:
    return np.array(
        [
            [f, 0, 0, 0],
            [0, f, 0, 0],
            [0, 0, f, 0],
            [0, 0, 1, 0],
        ],
        dtype=float,
    )
