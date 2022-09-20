"""CLI for todi"""

from typing import Optional

import typer
from rich.console import Console

from todi import __app_name__, __version__, manager, views
from todi.models import Status

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


@app.command(name="list")
def list_tasks() -> None:
    """
    List the tasks. \f
    :return: None
    """
    views.all_tasks()


@app.command()
def add(
    content: str = typer.Argument(..., help="Content of the task.")
) -> None:
    """
    Create a new task. \f
    :return: None
    """
    manager.add_task(content=content)
    views.all_tasks()


@app.command()
def update(
    id_: int = typer.Argument(..., help="ID of the task."),
    content: str = typer.Argument(..., help="New content for the task."),
) -> None:
    """
    Update the content of a task \f
    :return: None
    """
    manager.update_task(id_=id_, content=content)
    views.all_tasks()


@app.command()
def done(
    id_: int = typer.Argument(..., help="ID of the task."),
) -> None:
    """
    Update status of the task to DONE. \f
    :return: None
    """
    manager.update_status(id_=id_, status=Status.DONE)
    views.all_tasks()


@app.command()
def doing(
    id_: int = typer.Argument(..., help="ID of the task."),
) -> None:
    """
    Update status of the task to DOING. \f
    :return: None
    """
    manager.update_status(id_=id_, status=Status.DOING)
    views.all_tasks()


@app.command()
def todo(
    id_: int = typer.Argument(..., help="ID of the task."),
) -> None:
    """
    Update status of the task to default. \f
    :return: None
    """
    manager.update_status(id_=id_, status=Status.TODO)
    views.all_tasks()


@app.command()
def delete(id_: int = typer.Argument(..., help="ID of the task.")) -> None:
    """
    Delete a specific task. \f
    :return: None
    """
    manager.delete_task(id_=id_)
    views.all_tasks()


@app.command()
def clean() -> None:
    """
    Delete completed (done) tasks. \f
    :return: None
    """
    manager.delete_done()
    views.all_tasks()


if __name__ == "__main__":
    pass
