""" Setup file """

import os

from typing import List

from setuptools import find_packages, setup

from todi import __app_name__, __version__


setup(
    name=__app_name__,
    version=__version__,
    description="Minimal CLI TODO app.",
    long_description="Another CLI To-Do app. Made to be simple and easy to use.",
    long_description_content_type="text/markdown",
    author="Luis Ch.",
    author_email="email@luisch.com",
    packages=find_packages(include=[__app_name__]),
    install_requires=["rich", "tinydb", "typer", "typing"],
    url="https://github.com/luisgdev/todi",
    entry_points={
        "console_scripts": [
            f"{__app_name__} = {__app_name__}.__main__:main",
        ]
    },
)
