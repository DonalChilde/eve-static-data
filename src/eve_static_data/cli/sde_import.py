import shutil
from pathlib import Path
from typing import Annotated

import typer
from rich.console import Console
from rich.prompt import Confirm

from eve_static_data.cli.helpers import get_esd_settings_from_context
from eve_static_data.helpers.sde_info import load_sde_info

app = typer.Typer(no_args_is_help=True)


@app.command()
def import_sde(
    ctx: typer.Context,
    import_directory: Annotated[
        Path,
        typer.Argument(
            help="The path to the SDE data to import.",
        ),
    ],
):
    """Import SDE data from a directory."""
    console = Console()
    console.print("[bold green]Importing SDE Data[/bold green]")
    console.print(
        "Before importing, pls validate the SDE data using the `validate` command."
    )
    console.print(
        "Existing SDE data in the app directory will be replaced with the new data."
    )
    settings = get_esd_settings_from_context(ctx)

    try:
        current_info = load_sde_info(input_path=settings.sde_directory)
        console.print(f"Current SDE Info: {current_info}")
    except FileNotFoundError:
        console.print("No existing SDE data found in the app directory.")
    except Exception as e:
        console.print(f"[bold red]Error loading current SDE info:[/bold red] {e}")
        raise typer.Exit(code=1) from e
    try:
        new_info = load_sde_info(input_path=import_directory)
        console.print(f"New SDE Info: {new_info}")
    except FileNotFoundError as e:
        console.print(
            f"[bold red]Error:[/bold red] No _sde.jsonl file found in the import directory {import_directory}."
        )
        raise typer.Exit(code=1) from e
    except Exception as e:
        console.print(f"[bold red]Error loading new SDE info:[/bold red] {e}")
        raise typer.Exit(code=1) from e
    if not Confirm.ask("Do you want to proceed with importing the new SDE data?"):
        console.print("Import cancelled.")
        raise typer.Exit()
    shutil.rmtree(settings.sde_directory, ignore_errors=True)
    settings.sde_directory.mkdir(parents=True, exist_ok=True)
    shutil.copytree(import_directory, settings.sde_directory, dirs_exist_ok=True)
    console.print("[bold green]SDE data imported successfully.[/bold green]")
