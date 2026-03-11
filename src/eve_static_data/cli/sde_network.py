"""SDE raw data CLI commands for eve-argus.

This module focuses on commands to work with the raw SDE data, such as downloading,
checking for the current version, checking the changelog, and printing the data.
"""

import asyncio
from pathlib import Path
from typing import Annotated, Literal, cast

import typer
from rich.console import Console
from yaml import safe_dump

from eve_static_data import network
from eve_static_data.cli.helpers import SETTINGS_KEY, ESDSettings
from eve_static_data.helpers import app_data as AD

app = typer.Typer(no_args_is_help=True)


@app.command()
def latest(
    ctx: typer.Context,
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
    settings = ctx.obj[SETTINGS_KEY]
    settings = cast(ESDSettings, settings)
    info = asyncio.run(network.current_sde_info(url=settings.sde_latest_info_url))
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
    ctx: typer.Context,
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
    settings = ctx.obj[SETTINGS_KEY]
    settings = cast(ESDSettings, settings)
    changelog = asyncio.run(
        network.get_sde_schema_changelog(url=settings.sde_schema_changelog_url)
    )
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
    ctx: typer.Context,
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
    """Show the changelog for the SDE data.

    Note the changelog for the SDE data is different from the changelog for the SDE schema.
    The SDE data changelog tracks changes in the actual data, while the SDE schema changelog
    tracks changes in the structure of the data.

    The data changelog is in JSONL format, where each line is a JSON object representing
    a change in the SDE data.
    """
    console = Console()
    console.print("[bold green]SDE Data Changelog[/bold green]")
    settings = ctx.obj[SETTINGS_KEY]
    settings = cast(ESDSettings, settings)
    if build_number is None:
        console.print("No build number provided, resolving latest build number...")

        latest_info = asyncio.run(
            network.current_sde_info(url=settings.sde_latest_info_url)
        )
        build_number = latest_info.get("buildNumber")
        if not build_number:
            console.print(
                "[bold red]Error:[/bold red] Could not resolve latest build number."
            )
            console.print(latest_info)
            raise typer.Exit(code=1)
        console.print(f"Resolved latest build number to: {build_number}")
    changelog = asyncio.run(
        network.get_sde_data_changes(
            url_template=settings.sde_changes_url_template, build_number=build_number
        )
    )
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
    ctx: typer.Context,
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
    settings = ctx.obj[SETTINGS_KEY]
    settings = cast(ESDSettings, settings)
    latest_info = asyncio.run(
        network.current_sde_info(url=settings.sde_latest_info_url)
    )
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

    url = AD.sde_download_url(
        settings.sde_download_url_template, build_number=build_number, variant=variant
    )
    output_filename = AD.sde_data_filename(
        settings.sde_data_filename_template, build_number=build_number, variant=variant
    )
    output_path = output_dir / output_filename
    console.print(f"Downloading SDE data.")
    console.print(f"URL: {url}")
    console.print(f"Output path: {output_path}")
    try:
        asyncio.run(
            network.download_sde_to_file(
                url_template_str=settings.sde_download_url_template,
                build_number=build_number,
                variant=variant,
                output_path=output_path,
                overwrite=overwrite,
            )
        )
    except Exception as e:
        console.print(f"[bold red]Error:[/bold red] Failed to download SDE data: {e}")
        raise typer.Exit(code=1) from e

    console.print("SDE data downloaded successfully.")
