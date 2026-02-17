"""SDE raw data CLI commands for eve-argus.

This module focuses on commands to work with the raw SDE data, such as downloading,
checking for the current version, checking the changelog, and printing the data.
"""

from pathlib import Path
from typing import Annotated, Literal

import typer
from rich.console import Console

from eve_static_data.cli.sde_helpers import (
    download_sde_to_file,
    get_sde_changelog,
    get_sde_latest_info,
)
from eve_static_data.settings import get_settings

app = typer.Typer(no_args_is_help=True)


@app.command()
def latest():
    """Show information about the latest available SDE data."""
    console = Console()
    console.print("[bold green]Latest SDE Information[/bold green]")
    settings = get_settings()
    url = settings.resolve_sde_latest_info_url()
    console.print(f"The latest SDE data can be found at: {url}")
    info = get_sde_latest_info()
    console.print(info)


@app.command()
def changelog():
    """Show the changelog for the SDE data."""
    console = Console()
    console.print("[bold green]SDE Changelog[/bold green]")
    settings = get_settings()
    url = settings.resolve_sde_changelog_url()
    console.print(f"The SDE changelog can be found at: {url}")
    changelog = get_sde_changelog()
    console.print(changelog)


@app.command(name="download")
def download_sde(
    output_dir: Annotated[
        Path,
        typer.Argument(
            help="The directory to save the downloaded SDE data. The file name will be automatically generated, in the form of static-data-{build_number}-{variant}.zip",
            file_okay=False,
        ),
    ],
    variant: Annotated[
        Literal["jsonl", "yaml"],
        typer.Option(
            "-v",
            "--variant",
            help="The variant of the SDE to download",
            show_default=True,
        ),
    ] = "jsonl",
    build_number: Annotated[
        int,
        typer.Option(
            "-b",
            "--build-number",
            help="The build number of the SDE to download, or -1 to download the latest available build.",
            show_default=True,
        ),
    ] = -1,  # -1 will be resolved to latest build number
    overwrite: Annotated[
        bool,
        typer.Option(
            "-o", help="Whether to overwrite existing files", show_default=True
        ),
    ] = False,
):
    """Download the latest SDE data."""
    console = Console()
    console.print("[bold green]Downloading SDE Data...[/bold green]")
    settings = get_settings()
    latest_info = get_sde_latest_info()
    # Resolve latest build number if needed, because `latest` causes a 403 error.
    if build_number == -1:
        build_number = latest_info.get("buildNumber")
        if not build_number:
            console.print(
                "[bold red]Error:[/bold red] Could not resolve latest build number."
            )
            console.print(latest_info)
            raise typer.Exit(code=1)
        console.print(f"Resolved latest build number to: {build_number}")

    url = settings.resolve_sde_download_url(build_number=build_number, variant=variant)
    output_path = output_dir / f"static-data-{build_number}-{variant}.zip"
    console.print(f"Downloading SDE data.")
    console.print(f"URL: {url}")
    console.print(f"Output path: {output_path}")
    try:
        download_sde_to_file(
            build_number=build_number,
            variant=variant,
            output_path=output_path,
            overwrite=overwrite,
        )
    except Exception as e:
        console.print(f"[bold red]Error:[/bold red] Failed to download SDE data: {e}")
        raise typer.Exit(code=1) from e

    console.print("SDE data downloaded successfully.")


# @app.command(name="print")
# def print_sde(
#     name: Annotated[str, typer.Argument(help="The name of the SDE data to print")],
#     sde_directory: Annotated[
#         Path,
#         typer.Argument(
#             help="The directory where the decompressed SDE data is located",
#             file_okay=False,
#         ),
#     ],
# ):
#     """Print SDE data to the console."""
#     # TODO implement printing specific SDE data by line or range of lines
#     # -l line number (repeatable) -s start range -e end range?
#     console = Console()
#     console.print("[bold green]Printing SDE Data...[/bold green]")
#     access = RawJsonFileAccess(sde_directory=sde_directory)
#     try:
#         file_name_enum = SdeFileNames[name.upper()]
#     except KeyError as e:
#         console.print(f"[bold red]Error:[/bold red] Unknown SDE data name: {name}")
#         raise typer.Exit(code=1) from e
#     data_iter = access.jsonl_iter(file_name_enum)
#     for item in data_iter:
#         console.print(item)
#     # Placeholder for print logic
#     console.print("SDE data printed successfully.")
