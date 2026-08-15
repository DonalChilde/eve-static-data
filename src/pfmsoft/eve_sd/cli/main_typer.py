"""Entrypoint for the eve-sd command-line interface."""

import logging
from pathlib import Path

import typer

from pfmsoft.eve_sd import __app_name__, __version__
from pfmsoft.eve_sd.cli import app as main_app
from pfmsoft.eve_sd.logging_config import setup_logging
from pfmsoft.eve_sd.settings import get_settings

logger = logging.getLogger(__name__)


def default_options(
    ctx: typer.Context,
):
    """Initialize shared CLI context before subcommands run.

    This callback configures application logging and stores loaded settings in
    the Typer context object so subcommands can reuse them.

    Args:
        ctx: Typer context used to share state between commands.
    """
    settings = get_settings()
    setup_logging(log_dir=Path(settings.logging_directory))
    logger.info(f"Starting {__app_name__} v{__version__}")
    ctx.obj = {"esd-settings": settings}


app = typer.Typer(
    no_args_is_help=True,
    callback=default_options,
    help=(
        "Work with EVE Online static data: fetch releases, unpack datasets, "
        "build/query databases, export formats, and inspect schemas."
    ),
)

app.add_typer(main_app)
