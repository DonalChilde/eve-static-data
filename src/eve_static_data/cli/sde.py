"""SDE CLI commands for eve-argus."""

import typer
from rich.console import Console

from eve_static_data.cli.sde_dev import app as sde_dev_app
from eve_static_data.cli.sde_raw import app as sde_raw_app
from eve_static_data.settings import get_settings

app = typer.Typer(no_args_is_help=True)
app.add_typer(sde_dev_app, name="dev", help="SDE development commands.")
app.add_typer(sde_raw_app, name="raw", help="SDE raw data commands.")


@app.command(name="info")
def sde_info():
    """Show information about the currently loaded SDE data."""
    console = Console()
    console.print("[bold green]SDE Information[/bold green]")
    console.print("This command will display information about the SDE data.")
    raise NotImplementedError("SDE info functionality is not implemented yet.")


@app.command(name="import")
def import_sde():
    """Import SDE data into the system."""
    console = Console()
    console.print("[bold green]Importing SDE Data...[/bold green]")
    settings = get_settings()
    raise NotImplementedError("SDE import functionality is not implemented yet.")
    sde_path = settings.sde_file_template
    console.print("SDE data imported successfully.")


@app.command(name="compare")
def compare_sde():
    """Compare current SDE data with the available online version."""
    console = Console()
    console.print("[bold green]Comparing SDE Data...[/bold green]")
    raise NotImplementedError("SDE comparison functionality is not implemented yet.")
    # Placeholder for comparison logic
    console.print("SDE data comparison completed.")
