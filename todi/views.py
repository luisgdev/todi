""" Views module """

from rich import box
from rich.console import Console
from rich.markdown import Markdown
from rich.table import Table

from todi import manager
from todi.models import Task

# pylint: disable=unnecessary-list-index-lookup


def all_tasks() -> None:
    """
    List all tasks.
    :return: None
    """
    console = Console()
    tasks = manager.get_all()
    if tasks:
        table = Table(show_header=True, box=box.SIMPLE, title="TODO List")
        table.add_column("ID")
        table.add_column("Description")
        table.add_column("Status")
        table.add_column("Date")
        for i, item in enumerate(tasks):
            task = Task(**item)
            table.add_row(
                str(tasks[i].doc_id), task.content, task.status, task.date
            )
        console.print(table)
    else:
        console.print(Markdown("No pending tasks!"))


if __name__ == "__main__":
    pass
