"""Constants"""

import os
from pathlib import Path

DB_NAME: str = "data.json"
DATE_FORMAT: str = "%Y-%m-%d"
DB_DIR: str = "db"
NEW_DB_DIR: str = os.path.join(Path.home(), ".todi")


if __name__ == "__main__":
    pass
