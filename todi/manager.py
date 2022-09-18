"""Database manager"""

import os
from typing import List

from tinydb import Query, TinyDB, operations
from tinydb.table import Document

from todi import utils
from todi.constants import DB_DIR, DB_PATH
from todi.models import Status

if not os.path.exists(DB_DIR):
    os.makedirs(DB_DIR)
db = TinyDB(os.path.join(DB_DIR, DB_PATH))


def add_task(content: str) -> int:
    """
    Create a new task. \f
    :param content: String with the task content.
    :return: None
    """
    return db.insert(dict(content=content, status=Status.TODO, date=utils.get_date()))


def update_task(id_: int, content: str) -> List[int]:
    """
    Update a given task. \f
    :param id_: ID of the task.
    :param content: String with the task content.
    :return: None
    """
    return db.update(operations.set("content", content), doc_ids=[id_])


def update_status(id_: int, status: Status) -> List[int]:
    """
    Update a given task. \f
    :param id_: ID of the task.
    :param status: Status of the task.
    :return: None
    """
    return db.update(operations.set("status", status), doc_ids=[id_])


def delete_task(id_: int) -> List[int]:
    """
    Delete a given task. \f
    :param id_: ID of the task.
    :return: None
    """
    return db.remove(doc_ids=[id_])


def get_all() -> List[Document]:
    """
    Return all tasks. \f
    :return: None
    """
    return db.all()


def delete_done() -> List[int]:
    """
    Delete all completed (done) tasks. \f
    :return: None
    """
    return db.remove(Query().status == Status.DONE)


if __name__ == "__main__":
    pass
