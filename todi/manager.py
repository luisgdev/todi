"""Database manager"""

from typing import List

from tinydb import Query, TinyDB, operations
from tinydb.table import Document

from todi import utils
from todi.constants import DB_FILE_PATH
from todi.models import Status, Task

# Prepare db
db = TinyDB(DB_FILE_PATH)


def add_task(content: str, status: str = Status.TODO) -> int:
    """
    Create a new task. \f
    :param content: String with the task content.
    :param status: Status of the task.
    :return: ID of the task (int).
    """
    return db.insert(
        dict(content=content, status=status, date=utils.get_iso_date())
    )


def update_task(id_: int, content: str) -> List[int]:
    """
    Update a given task. \f
    :param id_: ID of the task.
    :param content: String with the task content.
    :return: List of IDs.
    """
    return db.update(operations.set("content", content), doc_ids=[id_])


def update_status(id_: int, status: str) -> List[int]:
    """
    Update a given task. \f
    :param id_: ID of the task.
    :param status: Status of the task.
    :return: List of IDs.
    """
    return db.update(operations.set("status", status), doc_ids=[id_])


def delete_task(id_: int) -> List[int]:
    """
    Delete a given task. \f
    :param id_: ID of the task.
    :return: List of IDs.
    """
    return db.remove(doc_ids=[id_])


def get_all(db_: TinyDB = db) -> List[Document]:
    """
    Return all tasks. \f
    :param id_: Database to query.
    :return: List of Document objects.
    """
    return db_.all()


def delete_done() -> List[int]:
    """
    Delete all completed (done) tasks. \f
    :return: List of IDs.
    """
    return db.remove(Query().status == Status.DONE)


def import_db(file_path: str) -> None:
    """
    Import a todi backup. \f
    :param file_path: Database file path.
    :return: None
    """
    tmp_db = TinyDB(file_path)
    items = get_all(db_=tmp_db)
    if items:
        for item in items:
            task = Task(**item)
            add_task(content=task.content, status=task.status)


if __name__ == "__main__":
    pass
