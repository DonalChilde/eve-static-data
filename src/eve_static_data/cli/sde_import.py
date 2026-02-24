import typer

app = typer.Typer(no_args_is_help=True)


@app.command()
def zip():
    """Import SDE data from a zip file."""
    typer.echo("Importing SDE data from zip file...")
    # Implementation of SDE import from zip file goes here


@app.command()
def dir():
    """Import SDE data from an unzipped directory."""
    typer.echo("Importing SDE data from unzipped directory...")
    # Implementation of SDE import from unzipped directory goes here
