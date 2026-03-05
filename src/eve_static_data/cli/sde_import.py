"""CLI commands for importing EVE Static Data Export (SDE) data."""

import logging
from pathlib import Path
from typing import Annotated, cast

import typer
from rich.console import Console

from eve_static_data import network
from eve_static_data.access.sde_reader import SdeReader
from eve_static_data.cli.helpers import SETTINGS_KEY, ESDSettings
from eve_static_data.helpers import app_data as AD
from eve_static_data.sde_data.available_builds import (
    generate_derived_datasets_for_build,
    import_unzipped_sde,
    import_zipped_sde,
)
from eve_static_data.sde_data.validation import validate_and_save_validation_results

logger = logging.getLogger(__name__)

app = typer.Typer(no_args_is_help=True)


@app.command()
def zip(
    ctx: typer.Context,
    file_path: Annotated[
        Path,
        typer.Argument(
            help="The path to the SDE zip file.",
            exists=True,
            file_okay=True,
            dir_okay=False,
        ),
    ],
):
    """Import SDE data from a zip file."""
    console = Console()
    console.print("Importing SDE data from zip file...")
    try:
        settings = ctx.obj[SETTINGS_KEY]
        settings = cast(ESDSettings, settings)

        build_number = import_zipped_sde(file_path, data_path=settings.data_path)
        after_import(build_number, settings=settings)
        console.print(f"SDE data imported successfully. Build number: {build_number}")
    except Exception as e:
        console.print(f"Error importing SDE data from zip file: {e}")
        raise typer.Exit(code=1) from e


@app.command()
def dir(
    ctx: typer.Context,
    dir_path: Annotated[
        Path,
        typer.Argument(
            help="The path to the unzipped SDE directory.",
            exists=True,
            file_okay=False,
            dir_okay=True,
        ),
    ],
):
    """Import SDE data from an unzipped directory."""
    console = Console()
    console.print("Importing SDE data from unzipped directory...")
    settings = ctx.obj[SETTINGS_KEY]
    settings = cast(ESDSettings, settings)
    try:
        build_number = import_unzipped_sde(dir_path, data_path=settings.data_path)
        after_import(build_number, settings=settings)
        console.print(f"SDE data imported successfully. Build number: {build_number}")
    except Exception as e:
        console.print(f"Error importing SDE data from unzipped directory: {e}")
        raise typer.Exit(code=1) from e


def after_import(build_number: int, settings: ESDSettings):
    """Perform any necessary cleanup or finalization after importing SDE data."""
    console = Console()

    sde_dir = AD.sde_dir(settings.data_path, build_number)
    validation_dir = AD.validation_dir(settings.data_path, build_number)

    console.print("Validating imported SDE data...")
    sde_reader = SdeReader(sde_dir)
    validate_and_save_validation_results(sde_reader, validation_dir)

    console.print("Generating derived datasets...")
    generate_derived_datasets_for_build(settings.data_path, build_number)

    # Download schema changelog and save to validation directory, fail gracefully in case offline.
    console.print("Downloading SDE changelog...")
    schema_changelog_path = validation_dir / "schema-changelog.yaml"
    try:
        network.save_sde_schema_changelog(schema_changelog_path, overwrite=False)
    except Exception as e:
        console.print(f"Error downloading SDE schema changelog: {e}")
        logger.error(f"Error downloading SDE schema changelog: {e}", exc_info=True)
        # Don't fail the entire import if we can't get the schema changelog, but log the error and continue.

    # Download data changelog and save to validation directory, fail gracefully in case offline.
    console.print("Downloading SDE data changelog...")
    data_changelog_path = validation_dir / f"data-changelog-{build_number}.yaml"
    try:
        network.save_sde_data_changelog(
            build_number, data_changelog_path, overwrite=False
        )
    except Exception as e:
        console.print(f"Error downloading SDE data changelog: {e}")
        logger.error(f"Error downloading SDE data changelog: {e}", exc_info=True)
        # Don't fail the entire import if we can't get the data changelog, but log the error and continue.
