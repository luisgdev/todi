"""Test for models"""

from todi.models import Status, Task


def test_status() -> None:
    """
    Test Status object.
    :return: None
    """
    assert Status.TODO == "TODO"
    assert Status.DOING == "DOING"
    assert Status.DONE == "DONE"
    assert isinstance(Status.TODO, str)
    assert isinstance(Status.DOING, str)
    assert isinstance(Status.DONE, str)


def test_tasks() -> None:
    """
    Test tasks class.
    :return: None
    """
    tmp_content: str = "This is a temporary task"
    tmp_date: str = "today date"
    tmp_task: Task = Task(tmp_content, Status.TODO, tmp_date)
    assert isinstance(tmp_task, Task)
    assert tmp_content == tmp_task.content
    assert tmp_date == tmp_task.date
    assert tmp_task.status == Status.TODO
