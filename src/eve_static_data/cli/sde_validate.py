"""Validate the SDE data."""

import asyncio
from pathlib import Path
from typing import Annotated

import typer
from rich.console import Console

from eve_static_data.cli.helpers import get_esd_settings_from_context

# from eve_static_data.validation import validation_report

app = typer.Typer(no_args_is_help=True)


@app.command()
def validate_json(
    ctx: typer.Context,
    sde_path: Annotated[
        Path,
        typer.Argument(
            help="The path to the json SDE data.",
        ),
    ],
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
    if not sde_path.exists():
        console.print(
            f"[bold red]Error:[/bold red] SDE path {sde_path} does not exist."
        )
        raise typer.Exit(code=1)
    if not sde_path.is_dir():
        console.print(
            f"[bold red]Error:[/bold red] SDE path {sde_path} is not a directory."
        )
        raise typer.Exit(code=1)
    sde_info_path = sde_path / "_sde.json"
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
        report_path = sde_path / "validation_reports"
    report_path.mkdir(parents=True, exist_ok=True)
    msg = f"Validating SDE data in {sde_path} and saving reports to {report_path}"
    console.print(f"[bold blue]{msg}[/bold blue]")
    # FIXME validation needs to be updated to work with the new SDE loading and model validation code, so commenting out for now
    # asyncio.run(
    #     validation_report(
    #         sde_path=sde_path,
    #         output_path=report_path,
    #         sde_tools=sde_tools,
    #         overwrite=overwrite,
    #         console=console,
    #     )
    # )
