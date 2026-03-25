"""Commands for showing information about the eve-static-data app and its configuration."""

from typing import cast

import typer
from rich.console import Console
from rich.text import Text

from eve_static_data import AFTER_BUILD_NUMBER, RELEASE_DATE, __app_name__, __version__
from eve_static_data.cli.helpers import SETTINGS_KEY, EsdCliSettings

app = typer.Typer(no_args_is_help=True)


@app.command()
def version(ctx: typer.Context):
    """Show the eve-static-data app version."""
    typer.echo(
        f"{__app_name__} v{__version__} (Schema -> After Build {AFTER_BUILD_NUMBER} - {RELEASE_DATE})"
    )


@app.command()
def settings(ctx: typer.Context):
    """Show the eve-static-data app settings."""
    console = Console()
    console.rule(Text("Eve Static Data CLI Settings", style="bold cyan"))
    settings = ctx.obj[SETTINGS_KEY]
    settings = cast(EsdCliSettings, settings)
    console.print(settings)
