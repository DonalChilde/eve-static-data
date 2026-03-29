"""Main CLI Typer app for esi-link."""

import logging
from pathlib import Path

import typer

from eve_static_data import __app_name__, __version__
from eve_static_data.cli.config_info import app as config_info_app
from eve_static_data.cli.helpers import SETTINGS_KEY, create_esd_settings
from eve_static_data.cli.sde_export import app as sde_export_app
from eve_static_data.cli.sde_network import app as sde_network_app
from eve_static_data.cli.sde_unpack import app as sde_unpack_app
from eve_static_data.cli.sde_validate import app as sde_validate_app
from eve_static_data.logging_config import setup_logging
from eve_static_data.settings import get_settings

logger = logging.getLogger(__name__)

app = typer.Typer(no_args_is_help=True)
app.add_typer(sde_network_app)
app.add_typer(sde_unpack_app)
app.add_typer(sde_validate_app)
app.add_typer(sde_export_app, name="export", help="Commands for exporting SDE data.")
app.add_typer(config_info_app)


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
