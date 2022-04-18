from setuptools import setup

with open("README.md") as f:
    readme = f.read()

with open("LICENSE") as f:
    license = f.read()

setup(
    name="vpype-perspective",
    version="0.1.0-alpha.1",
    description="Put your art in perspective with vpype.",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="Antoine Beyeler",
    url="https://github.com/abey79/vpype-perspective",
    packages=["vpype_perspective"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Topic :: Multimedia :: Graphics",
        "Environment :: Plugins",
    ],
    setup_requires=["wheel"],
    install_requires=[
        "click",
        "numpy",
        "vpype[all]>=1.10",
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
