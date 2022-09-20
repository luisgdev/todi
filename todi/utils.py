"""Utils module"""

import os
import shutil
import time

from todi.constants import DATE_FORMAT, DB_DIR, DB_NAME, NEW_DB_DIR


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
    if not os.path.exists(NEW_DB_DIR):
        os.makedirs(NEW_DB_DIR)
    if os.path.exists(DB_DIR) and os.path.isfile(
        os.path.join(DB_DIR, DB_NAME)
    ):
        shutil.move(
            src=os.path.join(DB_DIR, DB_NAME),
            dst=os.path.join(NEW_DB_DIR, DB_NAME),
        )


if __name__ == "__main__":
    pass
