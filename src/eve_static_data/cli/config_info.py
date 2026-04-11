"""Commands for showing information about the eve-static-data app and its configuration."""

import typer
from rich.console import Console
from rich.text import Text

from eve_static_data import AFTER_BUILD_NUMBER, RELEASE_DATE, __app_name__, __version__
from eve_static_data.cli.helpers import get_esd_settings_from_context
from eve_static_data.helpers.sde_info import load_sde_info

app = typer.Typer(no_args_is_help=True)


@app.command()
def version(ctx: typer.Context):
    """Show the eve-static-data app version."""
    typer.echo(
        f"{__app_name__} v{__version__} (Schema -> After Build {AFTER_BUILD_NUMBER} - {RELEASE_DATE})"
    )


@app.command()
def status(ctx: typer.Context):
    """Show the eve-static-data app settings."""
    console = Console()
    console.rule(Text("Eve Static Data CLI Settings", style="bold cyan"))
    settings = get_esd_settings_from_context(ctx)
    console.print(settings)
    try:
        current_info = load_sde_info(input_path=settings.sde_directory)
        console.print(f"Current SDE Info: {current_info}")
    except FileNotFoundError:
        console.print("No existing SDE data found in the app directory.")
    except Exception as e:
        console.print(f"[bold red]Error loading current SDE info:[/bold red] {e}")
