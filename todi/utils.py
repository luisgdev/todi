"""Utils module"""

import time
from pathlib import Path
from shutil import copy

from todi.constants import (
    BACKUP_DIRECTORY,
    DATE_FORMAT,
    DB_DIRECTORY,
    DB_FILE_PATH,
    DB_FILENAME,
    TIME_FORMAT,
)


def get_iso_date() -> str:
    """
    Get current date in ISO format.
    :return: String with the date.
    """
    return time.strftime(DATE_FORMAT)


def get_time() -> str:
    """
    Get current date and time.
    :return: String with the date.
    """
    return time.strftime("T".join((DATE_FORMAT, TIME_FORMAT)))


def check_db_dir() -> None:
    """
    Create db directory if it doesn't exists and
    move file from old to new directory.
    :return: None.
    """
    Path(DB_DIRECTORY).mkdir(exist_ok=True, parents=True)
    Path(BACKUP_DIRECTORY).mkdir(exist_ok=True, parents=True)


def export_db() -> None:
    """
    Export database file to backup directory.
    :return: None.
    """
    check_db_dir()
    current_time: str = get_time()
    new_name: str = f"db_{current_time}"
    db_file = Path(DB_FILE_PATH)
    if db_file.exists():
        copy(str(db_file), BACKUP_DIRECTORY)
        new_file = Path(BACKUP_DIRECTORY, DB_FILENAME)
        new_file.rename(Path(BACKUP_DIRECTORY, new_name))
        print(f"Database exported to: {str(Path(BACKUP_DIRECTORY, new_name))}")
    else:
        print("There is no todi database yet.")
