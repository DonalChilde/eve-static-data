"""Main CLI Typer app for eve-argus."""

from pathlib import Path
from typing import Annotated

import typer
from rich.console import Console

from eve_static_data import __version__
from eve_static_data.cli.sde_dev import app as sde_dev_app
from eve_static_data.cli.sde_io import app as sde_io_app
from eve_static_data.cli.sde_network import app as sde_network_app
from eve_static_data.logging_config import setup_logging
from eve_static_data.settings import get_settings

app = typer.Typer(no_args_is_help=True)
app.add_typer(sde_network_app, name="network", help="SDE internet related commands.")
app.add_typer(sde_dev_app, name="dev", help="SDE development commands.")
app.add_typer(sde_io_app, name="io", help="SDE import/export related commands.")


@app.callback(invoke_without_command=True)
def default_options(
    ctx: typer.Context,
    debug: Annotated[bool, typer.Option(help="Enable debug output.")] = False,
    verbosity: Annotated[int, typer.Option("-v", help="Verbosity.", count=True)] = 1,
    silent: Annotated[
        bool,
        typer.Option(help="Enable silent mode. Only results and errors will be shown."),
    ] = False,
):
    """Esi Link Command Line Interface.

    Insert pithy saying here
    """
    console = Console()
    settings = get_settings()
    setup_logging(log_dir=Path(settings.log_path))

    welcome = f"""
    Welcome to Eve Static Data! Your CLI interface to the Eve Online Static Data.
    Application configuration data located at {Path(settings.app_dir)}
    
    """
    console.print(welcome)


@app.command()
def version():
    """Show the eve-static-data app version."""
    typer.echo(f"eve-static-data app version: {__version__}")


@app.command()
def settings():
    """Show the eve-static-data app settings."""
    console = Console()
    settings = get_settings()
    console.print(settings)
