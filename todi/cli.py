"""CLI for todi"""

from pathlib import Path
from typing import Optional

import typer
from rich.console import Console

from todi import __app_name__, __version__, manager, views
from todi.models import Status
from todi.utils import export_db

app = typer.Typer()
console = Console()


@app.callback(invoke_without_command=True)
def main(
    _: Optional[bool] = typer.Option(
        None,
        "-v",
        "--version",
    )
) -> None:
    """
    Todi is a CLI to manage TODO tasks. Simple and easy to use. \f
    :return: None
    """
    console.print(f"{__app_name__} {__version__}")
    typer.Exit()


@app.command(name="list", help="Show a list of the tasks.")
def list_tasks() -> None:
    """
    List the tasks.
    :return: None
    """
    views.all_tasks()


@app.command(help="Create a new TODO task.")
def add(
    content: str = typer.Argument(..., help="Content of the task.")
) -> None:
    """
    Create a new task.
    :param content: String with the task content.
    :return: None
    """
    manager.add_task(content=content)
    views.all_tasks()


@app.command(help="Update the content of an existing task.")
def update(
    id_: int = typer.Argument(..., help="ID of the task."),
    content: str = typer.Argument(..., help="New content for the task."),
) -> None:
    """
    Update the content of a task.
    :param id_: Task ID.
    :param content: String with the task content.
    :return: None
    """
    manager.update_task(id_=id_, content=content)
    views.all_tasks()


@app.command(help="Update status of an existing task to DONE.")
def done(
    id_: int = typer.Argument(..., help="ID of the task."),
) -> None:
    """
    Update status of the task to DONE.
    :param id_: Task ID.
    :return: None
    """
    manager.update_status(id_=id_, status=Status.DONE)
    views.all_tasks()


@app.command(help="Update status of the task to DOING.")
def doing(
    id_: int = typer.Argument(..., help="ID of the task."),
) -> None:
    """
    Update status of the task to DOING.
    :param id_: Task ID.
    :return: None
    """
    manager.update_status(id_=id_, status=Status.DOING)
    views.all_tasks()


@app.command(help="Update status of the task to default (TODO).")
def todo(
    id_: int = typer.Argument(..., help="ID of the task."),
) -> None:
    """
    Update status of the task to default.
    :param id_: Task ID.
    :return: None
    """
    manager.update_status(id_=id_, status=Status.TODO)
    views.all_tasks()


@app.command(help="Delete an existing task.")
def delete(id_: int = typer.Argument(..., help="ID of the task.")) -> None:
    """
    Delete a specific task.
    :param id_: Task ID.
    :return: None
    """
    manager.delete_task(id_=id_)
    views.all_tasks()


@app.command(help="Delete all completed (DONE) tasks.")
def clean() -> None:
    """
    Delete completed (done) tasks.
    :return: None
    """
    manager.delete_done()
    views.all_tasks()


@app.command(name="import", help="Import an existing todi database.")
def import_backup(
    file_path: Path = typer.Argument(..., help="Database path.")
) -> None:
    """
    Import a backup of tasks.
    :param file_path: Database file path.
    :return: None
    """
    print(Path(file_path).exists())
    manager.import_db(file_path=str(file_path))


@app.command(name="export", help="Export the current todi database.")
def export_backup() -> None:
    """
    Export a backup of tasks.
    :return: None
    """
    export_db()


if __name__ == "__main__":
    pass
