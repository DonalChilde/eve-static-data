"""Validate the SDE data."""

import asyncio
from pathlib import Path
from typing import Annotated

import typer
from rich.console import Console

from eve_static_data.cli.helpers import get_esd_settings_from_context
from eve_static_data.validation import validation_report

app = typer.Typer(no_args_is_help=True)


@app.command()
def validate(
    ctx: typer.Context,
    sde_path: Annotated[
        Path | None,
        typer.Option(
            "--sde-path",
            help="The path to the SDE data. If not provided, the SDE directory from the "
            "settings will be used.",
        ),
    ] = None,
    report_path: Annotated[
        Path | None,
        typer.Option(
            "--report-path",
            help="The directory path to save the validation reports to. If not provided, "
            "the reports will be saved to the `<sde_path>/validation_reports` directory.",
            file_okay=False,
            dir_okay=True,
        ),
    ] = None,
    overwrite: Annotated[
        bool,
        typer.Option(
            "--overwrite",
            help="Whether to overwrite existing validation reports.",
        ),
    ] = False,
):
    """Validate the SDE files in a directory."""
    console = Console()
    console.print("[bold green]Validating SDE Data[/bold green]")
    settings = get_esd_settings_from_context(ctx)
    sde_tools = settings.sde_tools()
    if sde_path is None:
        data_path = settings.sde_directory
    else:
        data_path = sde_path
    if not data_path.exists():
        console.print(
            f"[bold red]Error:[/bold red] SDE path {data_path} does not exist."
        )
        raise typer.Exit(code=1)
    if not data_path.is_dir():
        console.print(
            f"[bold red]Error:[/bold red] SDE path {data_path} is not a directory."
        )
        raise typer.Exit(code=1)
    sde_info_path = data_path / "_sde.jsonl"
    if not sde_info_path.exists():
        if sde_path:
            console.print(
                f"[bold red]Error:[/bold red] SDE info file {sde_info_path} does not exist. Is this a valid SDE data directory?"
            )
        else:
            console.print(
                f"[bold red]Error:[/bold red]Application SDE info file {sde_info_path} does not exist. Download the SDE data first?"
            )

        raise typer.Exit(code=1)
    if report_path is None:
        report_path = data_path / "validation_reports"
    report_path.mkdir(parents=True, exist_ok=True)
    msg = f"Validating SDE data in {data_path} and saving reports to {report_path}"
    console.print(f"[bold blue]{msg}[/bold blue]")
    asyncio.run(
        validation_report(
            sde_path=data_path,
            output_path=report_path,
            sde_tools=sde_tools,
            overwrite=overwrite,
            console=console,
        )
    )
