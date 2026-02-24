"""SDE raw data CLI commands for eve-argus.

This module focuses on commands to work with the raw SDE data, such as downloading,
checking for the current version, checking the changelog, and printing the data.
"""

from pathlib import Path
from typing import Annotated, Literal

import typer
from rich.console import Console
from yaml import safe_dump

from eve_static_data import network
from eve_static_data.settings import get_settings

app = typer.Typer(no_args_is_help=True)


@app.command()
def latest(
    file_out: Annotated[
        Path | None,
        typer.Option(
            "-f",
            "--file-out",
            help="The file to save the latest SDE information to a json file.",
            file_okay=True,
        ),
    ] = None,
):
    """Show information about the latest available SDE data."""
    console = Console()
    console.print("[bold green]Latest SDE Information[/bold green]")
    info = network.current_sde_info()
    console.print(info)
    if file_out:
        try:
            with file_out.open("w", encoding="utf-8") as f:
                f.write(str(info))
            console.print(f"Latest SDE information saved to {file_out}")
        except Exception as e:
            console.print(
                f"[bold red]Error:[/bold red] Failed to save latest SDE information to file: {e}"
            )
            raise typer.Exit(code=1) from e


@app.command()
def changelog(
    file_out: Annotated[
        Path | None,
        typer.Option(
            "-f",
            "--file-out",
            help="The file to save the SDE schema changelog information to a yaml file.",
            file_okay=True,
        ),
    ] = None,
):
    """Show the changelog for the SDE schema."""
    console = Console()
    console.print("[bold green]SDE Schema Changelog[/bold green]")
    changelog = network.get_sde_schema_changelog()
    console.print(changelog)
    if file_out:
        try:
            with file_out.open("w", encoding="utf-8") as f:
                yaml_str = safe_dump(changelog, sort_keys=False)
                f.write(yaml_str)
            console.print(f"SDE schema changelog saved to {file_out}")
        except Exception as e:
            console.print(
                f"[bold red]Error:[/bold red] Failed to save SDE schema changelog to file: {e}"
            )
            raise typer.Exit(code=1) from e


@app.command()
def data_changelog(
    build_number: Annotated[
        int | None,
        typer.Option(
            help="The build number of the SDE data to show the changelog for. If not "
            "provided, the changelog for the latest build will be shown."
        ),
    ] = None,
    file_out: Annotated[
        Path | None,
        typer.Option(
            "-f",
            "--file-out",
            help="The file to save the SDE data changelog information to a jsonl file.",
            file_okay=True,
        ),
    ] = None,
):
    """Show the changelog for the SDE data."""
    console = Console()
    console.print("[bold green]SDE Data Changelog[/bold green]")
    if build_number is None:
        console.print("No build number provided, resolving latest build number...")
        latest_info = network.current_sde_info()
        build_number = latest_info.get("buildNumber")
        if not build_number:
            console.print(
                "[bold red]Error:[/bold red] Could not resolve latest build number."
            )
            console.print(latest_info)
            raise typer.Exit(code=1)
        console.print(f"Resolved latest build number to: {build_number}")
    changelog = network.get_sde_data_changelog(build_number=build_number)
    console.print(changelog)
    if file_out:
        try:
            with file_out.open("w", encoding="utf-8") as f:
                f.write(str(changelog))
            console.print(f"SDE data changelog saved to {file_out}")
        except Exception as e:
            console.print(
                f"[bold red]Error:[/bold red] Failed to save SDE data changelog to file: {e}"
            )
            raise typer.Exit(code=1) from e


@app.command(name="download")
def download_sde(
    output_dir: Annotated[
        Path,
        typer.Argument(
            help="The directory to save the downloaded SDE data. The file name will "
            "be automatically generated, in the form of static-data-{build_number}-{variant}.zip",
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
        int | None,
        typer.Option(
            "-b",
            "--build-number",
            help="The build number of the SDE to download. If not provided, the latest "
            "build will be downloaded.",
            show_default=True,
        ),
    ] = None,  # None will be resolved to latest build number
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
    latest_info = network.current_sde_info()
    # Resolve latest build number if needed, because `latest` causes a 403 error.
    if build_number is None:
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
        network.download_sde_to_file(
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
