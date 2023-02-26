"""Utils module"""

import os
import shutil
import time

from todi.constants import DATE_FORMAT, DB_DIR, DB_NAME


def get_date() -> str:
    """
    Get current date in ISO format.
    :return: String with the date.
    """
    return time.strftime(DATE_FORMAT)


def check_db_dir() -> None:
    """
    Create db directory if it doesn't exists and
    move file from old to new directory.
    :return: None.
    """
    if not os.path.exists(DB_DIR):
        os.makedirs(DB_DIR)


if __name__ == "__main__":
    pass
