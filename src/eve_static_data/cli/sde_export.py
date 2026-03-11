"""CLI for exporting SDE data to JSON files."""

import asyncio
from pathlib import Path
from typing import Annotated

import typer
from rich.console import Console

from eve_static_data.esd_tools import EsdTools
from eve_static_data.models.type_defs import Lang, LangEnum

app = typer.Typer(no_args_is_help=True)


# TODO This should work with sde data that has already been imported into the data directory,
# so it should use the get_sde_reader.reader function to get an SDEReader instance for the
# specified build number. It should also use the export_localized_datasets function from
# eve_static_data.api.export to export the localized datasets to JSON files in the specified
# output directory. The overwrite flag should determine whether to overwrite existing files
# in the output directory or skip exporting if files already exist.


@app.command()
def process(
    input_path: Annotated[
        Path, typer.Argument(help="The path to the SDE JSONL zip file.")
    ],
    output_path: Annotated[
        Path, typer.Argument(help="The path to save the processed SDE data.")
    ],
    langs: Annotated[
        list[LangEnum] | None,
        typer.Option(
            "-l",
            "--langs",
            help="The languages to include in the processed SDE data. If not provided defaults to `en`",
        ),
    ] = None,
):
    """Process the SDE data from the given input path zip file, and save the processed data to the given output path."""
    esd_tools = EsdTools()
    if not langs:
        lang: list[Lang] = [LangEnum.EN.value]
    else:
        lang = [lang.value for lang in langs]
    asyncio.run(esd_tools.process(input_path, output_path, lang))


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
