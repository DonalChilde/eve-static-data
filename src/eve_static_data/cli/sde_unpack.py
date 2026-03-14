from pathlib import Path
from typing import Annotated

import typer
from rich.console import Console

from eve_static_data.helpers import sde_unpack

app = typer.Typer(no_args_is_help=True)


@app.command()
def unpack(
    sde_zip: Annotated[
        Path,
        typer.Argument(
            help="The path to the SDE data zip file.",
            exists=True,
            file_okay=True,
            dir_okay=False,
        ),
    ],
    output_path: Annotated[
        Path,
        typer.Argument(
            help="The directory to save the unpacked SDE data to.",
            file_okay=False,
            dir_okay=True,
        ),
    ],
    use_build_number: Annotated[
        bool,
        typer.Option(
            "-b",
            "--use-build-number",
            help="Whether to use the build number in the output directory structure. "
            "If True, the unpacked data will be saved to `<output_path>/<build_number>/`. "
            "If False, the unpacked data will be saved directly to `<output_path>/`.",
            show_default=True,
        ),
    ] = True,
):
    """Unpack the SDE data from a zip file."""
    console = Console()
    console.print("[bold green]Unpacking SDE Data[/bold green]")
    try:
        sde_path, sde_info = sde_unpack.unpack(sde_zip, output_path, use_build_number)
    except Exception as e:
        console.print(f"[bold red]Error:[/bold red] Failed to unpack SDE data: {e}")
        raise typer.Exit(code=1) from e
    console.print(
        f"Unpacked SDE {sde_info.get('buildNumber')} - {sde_info.get('releaseDate')} to {sde_path}"
    )
