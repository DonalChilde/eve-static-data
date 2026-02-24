from pathlib import Path
from typing import Annotated

import typer

from eve_static_data.sde_data.available_builds import (
    import_unzipped_sde,
    import_zipped_sde,
)

app = typer.Typer(no_args_is_help=True)


@app.command()
def zip(
    file_path: Annotated[
        Path,
        typer.Argument(
            help="The path to the SDE zip file.",
            exists=True,
            file_okay=True,
            dir_okay=False,
        ),
    ],
):
    """Import SDE data from a zip file."""
    typer.echo("Importing SDE data from zip file...")
    try:
        import_zipped_sde(file_path)
    except Exception as e:
        typer.echo(f"Error importing SDE data from zip file: {e}")
        raise typer.Exit(code=1) from e


@app.command()
def dir(
    dir_path: Annotated[
        Path,
        typer.Argument(
            help="The path to the unzipped SDE directory.",
            exists=True,
            file_okay=False,
            dir_okay=True,
        ),
    ],
):
    """Import SDE data from an unzipped directory."""
    typer.echo("Importing SDE data from unzipped directory...")
    try:
        import_unzipped_sde(dir_path)
    except Exception as e:
        typer.echo(f"Error importing SDE data from unzipped directory: {e}")
        raise typer.Exit(code=1) from e
