"""Validate the SDE data."""

import asyncio
from pathlib import Path
from typing import Annotated

import typer
from rich.console import Console

from eve_static_data.validation import validation_report

app = typer.Typer(no_args_is_help=True)


@app.command()
def validate(
    sde_path: Annotated[Path, typer.Argument(help="The path to the SDE data.")],
    report_path: Annotated[
        Path | None,
        typer.Option(
            "-r",
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
            "-o",
            "--overwrite",
            help="Whether to overwrite existing validation reports.",
        ),
    ] = False,
):
    """Validate the SDE files in a directory."""
    console = Console()
    console.print("[bold green]Validating SDE Data[/bold green]")
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
    sde_info_path = sde_path / "_sde.jsonl"
    if not sde_info_path.exists():
        console.print(
            f"[bold red]Error:[/bold red] SDE info file {sde_info_path} does not exist. Is this a valid SDE data directory?"
        )
        raise typer.Exit(code=1)
    if report_path is None:
        report_path = sde_path / "validation_reports"
    report_path.mkdir(parents=True, exist_ok=True)
    msg = f"Validating SDE data in {sde_path} and saving reports to {report_path}"
    console.print(f"[bold blue]{msg}[/bold blue]")
    asyncio.run(
        validation_report(
            sde_path=sde_path,
            output_path=report_path,
            overwrite=overwrite,
            console=console,
        )
    )
