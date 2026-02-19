"""CLI for exporting SDE data to JSON files."""

from pathlib import Path
from typing import Annotated

import typer
from rich.console import Console

from eve_static_data.access.sde_records_td import SDERecordsTD
from eve_static_data.export.localized_datasets import export_localized_datasets

app = typer.Typer(no_args_is_help=True)


@app.command()
def localized(
    sde_path: Annotated[
        Path,
        typer.Argument(
            help="The path to the SDE data directory.",
            exists=True,
            dir_okay=True,
        ),
    ],
    localized_path: Annotated[
        Path,
        typer.Argument(
            help="The directory to save the exported localized datasets.",
            file_okay=False,
        ),
    ],
    overwrite: Annotated[
        bool,
        typer.Option(
            "-o",
            "--overwrite",
            help="Whether to overwrite existing files in the output directory.",
            show_default=True,
        ),
    ] = False,
):
    """Export localized SDE data to JSON files."""
    console = Console()
    console.print("[bold green]Exporting Localized SDE Data[/bold green]")
    access = SDERecordsTD(sde_path)
    export_localized_datasets(access, localized_path, overwrite)
