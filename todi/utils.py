"""Utils module"""

import time

from todi.constants import DATE_FORMAT


def get_date() -> str:
    """
    Get current date in ISO format.
    :return: String with the date.
    """
    return time.strftime(DATE_FORMAT)


if __name__ == "__main__":
    pass
