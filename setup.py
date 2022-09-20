""" Setup file """

import os
from typing import List

from setuptools import find_packages, setup

from todi import __app_name__, __version__


def _get_readme() -> str:
    """
    Get README.md content.
    :return: String with the content.
    """
    with open(
        file=os.path.join(
            os.path.abspath(os.path.dirname(__file__)), "README.md"
        ),
        mode="r",
        encoding="utf-8",
    ) as content:
        return content.read()


def _get_requirements() -> List[str]:
    """
    Get Requirements list.
    :return: List of strings with dependencies.
    """
    with open(
        file=os.path.join(
            os.path.abspath(os.path.dirname(__file__)), "requirements.txt"
        ),
        mode="r",
        encoding="utf-8",
    ) as content:
        return list(content.read().split("\n"))


setup(
    name=__app_name__,
    version=__version__,
    description="Minimal CLI TODO app.",
    long_description=_get_readme(),
    long_description_content_type="text/markdown",
    author="Luis Ch.",
    author_email="email@luisch.com",
    packages=find_packages(include=[__app_name__]),
    install_requires=_get_requirements(),
    url="https://github.com/luisgdev/todi",
    entry_points={
        "console_scripts": [
            f"{__app_name__} = {__app_name__}.__main__:main",
        ]
    },
)
