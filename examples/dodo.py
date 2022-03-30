"""DoIt task file (https://pydoit.org/).
"""
import pathlib

SOURCES = list(pathlib.Path(".").glob("**/*.vpy"))
VPYPE_PERSPECTIVE_SOURCE = list(
    (pathlib.Path(__file__).parent.parent / "vpype_perspective").glob("**/*.py")
)
DOIT_CONFIG = {"default_tasks": ["svg"]}


def task_svg():
    """generate SVG"""
    for path in SOURCES:
        target = path.parent / (path.stem + ".svg")
        yield {
            "name": path.stem,
            "actions": [f"vpype -I '{path}' write '{target}'"],
            "file_dep": [path, *VPYPE_PERSPECTIVE_SOURCE],
            "targets": [target],
            "clean": True,
        }


def task_show():
    """display figure"""
    for path in SOURCES:
        yield {
            "name": path.stem,
            "actions": [f"vpype -I '{path}' show"],
        }
