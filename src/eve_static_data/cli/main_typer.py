"""Main CLI Typer app for eve-argus."""

import typer

from eve_static_data import __version__
from eve_static_data.cli.sde import app as sde_app

app = typer.Typer(no_args_is_help=True)
app.add_typer(sde_app, name="sde", help="SDE related commands.")


@app.command()
def version():
    """Show the eve-static-data app version."""
    typer.echo(f"eve-static-data app version: {__version__}")
