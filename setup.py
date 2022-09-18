""" Setup file """

from typing import List

from setuptools import find_packages, setup

from todi import __app_name__, __version__


def get_readme() -> str:
    """
    Read README file.
    :return: String with the content.
    """
    with open(file="README.md", mode="r", encoding="utf-8") as content:
        return content.read()


def get_requirements() -> List[str]:
    """
    Read Requirements file.
    :return: List of strings with dependencies.
    """
    with open(file="requirements.txt", mode="r", encoding="utf-8") as content:
        return list(content.read().split("\n"))


setup(
    name=__app_name__,
    version=__version__,
    description="Minimal CLI TODO app.",
    long_description=get_readme(),
    long_description_content_type="text/markdown",
    author="Luis Ch.",
    author_email="email@luisch.com",
    packages=find_packages(include=[__app_name__]),
    install_requires=get_requirements(),
    url="https://github.com/luisgdev/todi",
    entry_points={
        "console_scripts": [
            f"{__app_name__} = {__app_name__}.__main__:main",
        ]
    },
)
