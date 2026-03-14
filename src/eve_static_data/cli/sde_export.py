"""CLI for exporting SDE data to JSON files."""

from pathlib import Path
from typing import Annotated

import typer
from rich.console import Console

from eve_static_data.models.dataset_filenames import SdeDatasetFiles
from eve_static_data.models.type_defs import Lang, LangEnum

app = typer.Typer(no_args_is_help=True)

# STUBS
# TODO make a dispatcher for the export commands that can call the appropriate export
# functions based on the command and options, maybe SDESdeDatasetFiles? or something like that.


@app.command()
def derived_datasets(
    sde_path: Annotated[
        Path,
        typer.Argument(
            help="The path to the SDE data directory.",
            exists=True,
            dir_okay=True,
        ),
    ],
    output_dir: Annotated[
        Path,
        typer.Argument(
            help="The directory to save the exported derived datasets.",
            file_okay=False,
        ),
    ],
    lang: Annotated[
        list[LangEnum] | None,
        typer.Option(
            "-l",
            "--lang",
            help="The one or more languages to export the localized datasets in. If not "
            "provided, 'en' will be used.",
            show_default=True,
        ),
    ] = None,
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
    """Export derived SDE datasets to JSON files."""
    console = Console()
    console.print("[bold green]Exporting Derived SDE Data[/bold green]")
    # reader = SdeReader(sde_path)
    # export_derived_datasets(reader, output_dir, overwrite)


@app.command()
def datasets(
    sde_path: Annotated[
        Path,
        typer.Argument(
            help="The path to the SDE data directory.",
            exists=True,
            dir_okay=True,
        ),
    ],
    output_dir: Annotated[
        Path,
        typer.Argument(
            help="The directory to save the exported datasets.",
            file_okay=False,
        ),
    ],
    datasets: Annotated[
        list[SdeDatasetFiles] | None,
        typer.Option(
            "-d",
            "--datasets",
            help="The one or more datasets to export. If not provided, all datasets will be exported.",
            show_default=True,
        ),
    ] = None,
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
    """Export SDE data to JSON files."""
    console = Console()
    console.print("[bold green]Exporting SDE Data[/bold green]")
    # reader = SdeReader(sde_path)
    # export_datasets(reader, output_dir, overwrite)


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
    output_dir: Annotated[
        Path,
        typer.Argument(
            help="The directory to save the exported localized datasets.",
            file_okay=False,
        ),
    ],
    lang: Annotated[
        list[LangEnum] | None,
        typer.Option(
            "-l",
            "--lang",
            help="The one or more languages to export the localized datasets in. If not "
            "provided, 'en' will be used.",
            show_default=True,
        ),
    ] = None,
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
    # reader = SdeReader(sde_path)
    # export_localized_datasets(reader, localized_path, overwrite)
