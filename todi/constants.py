"""Constants"""

from pathlib import Path

DATE_FORMAT: str = "%Y-%m-%d"
TIME_FORMAT: str = "%H:%M:%S"
DB_FILENAME: str = "data.json"

# Let's create directories


DB_DIRECTORY: Path = Path(Path.home(), ".todi")
DB_DIRECTORY.mkdir(exist_ok=True, parents=True)

backup_directory: Path = Path(Path.home(), "todi_backups")
backup_directory.mkdir(exist_ok=True, parents=True)

BACKUP_DIRECTORY: str = str(backup_directory)

DB_FILE_PATH: str = str(Path(DB_DIRECTORY, DB_FILENAME))


if __name__ == "__main__":
    pass
