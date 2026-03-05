"""Main CLI Typer app for eve-argus."""

import logging
from pathlib import Path

import typer

from eve_static_data import __app_name__, __version__
from eve_static_data.cli.helpers import SETTINGS_KEY, create_esd_settings
from eve_static_data.cli.sde_dev import app as sde_dev_app
from eve_static_data.cli.sde_io import app as sde_io_app
from eve_static_data.cli.sde_network import app as sde_network_app
from eve_static_data.logging_config import setup_logging
from eve_static_data.settings import get_settings

logger = logging.getLogger(__name__)

app = typer.Typer(no_args_is_help=True)
app.add_typer(sde_network_app, name="network", help="SDE internet related commands.")
app.add_typer(sde_dev_app, name="dev", help="SDE development commands.")
app.add_typer(sde_io_app, name="io", help="SDE import/export related commands.")


@app.callback(invoke_without_command=True)
def default_options(
    ctx: typer.Context,
):
    """Esi Link Command Line Interface.

    This CLI provides various commands for working with eve-static-data, including
    network operations, development tools, and import/export functionality.
    """
    settings = get_settings()
    setup_logging(log_dir=Path(settings.log_path))
    logger.info(f"Starting {__app_name__} v{__version__}")
    app_config = create_esd_settings(settings)
    ctx.obj = {SETTINGS_KEY: app_config}
