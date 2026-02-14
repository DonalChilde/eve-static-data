"""CLI commands for working with the SDE database."""

import typer
from sqlalchemy import select
from sqlalchemy.orm import Session

import eve_static_data.models.db as DBM
from eve_static_data.helpers.db import create_db, db_exists, engine_factory
from eve_static_data.settings import get_settings

app = typer.Typer(no_args_is_help=True)


@app.command(name="import")
def import_db():
    """Import the SDE database."""
    settings = get_settings()
    if settings.db_path().exists():
        typer.echo("The SDE database already exists.")
        backup_prompt = typer.prompt(
            "Do you want to backup the existing database? [y/N]", default="N"
        )
        if backup_prompt.lower() == "y":
            typer.echo("Please use the Backup command to backup the database.")
            raise typer.Exit(code=1)
        overwrite_prompt = typer.prompt(
            "Do you want to overwrite it? [y/N]", default="N"
        )
        if overwrite_prompt.lower() != "y":
            raise typer.Exit(code=1)
        settings.db_path().unlink()
    engine = engine_factory(str(settings.db_path()))
    typer.echo("Creating the SDE database...")
    create_db(engine)
    typer.echo("Importing the SDE database...")
    # TODO: Add the actual import logic here


@app.command()
def stats():
    """Check the stats of the SDE database."""
    settings = get_settings()
    if not settings.db_path().exists():
        typer.echo("The SDE database does not exist.")
        raise typer.Exit(code=1)
    if not db_exists(engine_factory(str(settings.db_path()))):
        typer.echo("The SDE database is empty or does not have the necessary tables.")
        raise typer.Exit(code=1)
    engine = engine_factory(str(settings.db_path()))

    with Session(engine) as session:
        app_info = session.execute(select(DBM.AppInfo)).scalar_one_or_none()
        if app_info is None:
            typer.echo("The SDE database does not exist or is empty.")
            raise typer.Exit(code=1)

        typer.echo(f"Database created by: {app_info.name} v{app_info.version}")
        typer.echo(f"Import date: {app_info.import_date}")
        sde_info = session.execute(select(DBM.SdeInfo)).scalar_one_or_none()
        if sde_info is None:
            typer.echo("The SDE database does not have SDE information.")
            raise typer.Exit(code=1)
        typer.echo(f"SDE build number: {sde_info.buildNumber}")
        typer.echo(f"SDE release date: {sde_info.releaseDate}")


@app.command()
def backup():
    """Backup the SDE database."""
    settings = get_settings()
    typer.echo("Backing up the SDE database...")
    raise NotImplementedError(
        "SDE database backup functionality is not implemented yet."
    )
