from setuptools import setup

with open("README.md") as f:
    readme = f.read()

with open("LICENSE") as f:
    license = f.read()

setup(
    name="vpype-perspective",
    version="0.1.0-alpha.0",
    description="",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="Antoine Beyeler",
    url="",
    license=license,
    packages=["vpype_perspective"],
    install_requires=[
        "click",
        "numpy",
        "vpype[all] @ git+https://github.com/abey79/vpype@master#egg=vpype",
    ],
    entry_points="""
            [vpype.plugins]
            perspective=vpype_perspective.perspective:perspective
            pspread=vpype_perspective.commands:pspread
            protate=vpype_perspective.commands:protate
            ptranslate=vpype_perspective.commands:ptranslate
            pscale=vpype_perspective.commands:pscale
        """,
)
