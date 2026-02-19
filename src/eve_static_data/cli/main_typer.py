"""Main CLI Typer app for eve-argus."""

import typer

from eve_static_data import __version__
from eve_static_data.cli.sde_dev import app as sde_dev_app
from eve_static_data.cli.sde_export import app as sde_export_app
from eve_static_data.cli.sde_raw import app as sde_app

app = typer.Typer(no_args_is_help=True)
app.add_typer(sde_app, name="sde", help="SDE related commands.")
app.add_typer(sde_dev_app, name="dev", help="SDE development commands.")
app.add_typer(sde_export_app, name="export", help="SDE export commands.")


@app.command()
def version():
    """Show the eve-static-data app version."""
    typer.echo(f"eve-static-data app version: {__version__}")
