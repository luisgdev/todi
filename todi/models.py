"""Models"""

from typing import NamedTuple

# pylint: disable=too-few-public-methods


class Status:
    """
    Status of a task.
    """

    TODO: str = "TODO"
    DOING: str = "DOING"
    DONE: str = "DONE"


class Task(NamedTuple):
    """
    Task properties.
    """

    content: str
    status: str
    date: str


if __name__ == "__main__":
    pass
