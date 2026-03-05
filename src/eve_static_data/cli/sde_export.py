"""CLI for exporting SDE data to JSON files."""

from pathlib import Path
from typing import Annotated

import typer
from rich.console import Console

# from eve_static_data.access.sde_reader import SdeReader

app = typer.Typer(no_args_is_help=True)


# TODO This should work with sde data that has already been imported into the data directory,
# so it should use the get_sde_reader.reader function to get an SDEReader instance for the
# specified build number. It should also use the export_localized_datasets function from
# eve_static_data.api.export to export the localized datasets to JSON files in the specified
# output directory. The overwrite flag should determine whether to overwrite existing files
# in the output directory or skip exporting if files already exist.
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
    # reader = SdeReader(sde_path)
    # export_localized_datasets(reader, localized_path, overwrite)
