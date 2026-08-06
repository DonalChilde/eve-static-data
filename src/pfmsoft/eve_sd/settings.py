"""Application settings for eve-sd.

This module defines two settings models:
- ``EveSDSettingsPydantic`` for loading values from environment variables
    and optional ``.env`` files.
- ``EveSDSettings`` as the runtime dataclass used by the app.
"""

from dataclasses import dataclass
from pathlib import Path
from uuid import NAMESPACE_DNS, uuid5

from pydantic_settings import BaseSettings, SettingsConfigDict
from typer import get_app_dir

from pfmsoft.eve_sd import (
    __app_name__,
    __url__,
    __version__,
)

# Typical application settings
USER_AGENT = f"{__app_name__}/{__version__} ({__url__})"
APP_DOMAIN = f"{__app_name__}"
APP_NAMESPACE = uuid5(NAMESPACE_DNS, __app_name__)
ENV_PREFIX = __app_name__.replace(".", "_").replace("-", "_").upper() + "_"
SETTINGS_KEY = ENV_PREFIX + "SETTINGS"

# Application settings for eve-sd.
SDE_URL_TEMPLATE: str = "https://developers.eveonline.com/static-data/tranquility/eve-online-static-data-${build_number}-${variant}.zip"
DATA_CHANGES_URL_TEMPLATE: str = "https://developers.eveonline.com/static-data/tranquility/changes/${build_number}.jsonl"
SCHEMA_CHANGELOG_URL: str = (
    "https://developers.eveonline.com/static-data/tranquility/schema-changelog.yaml"
)
LATEST_INFO_URL: str = (
    "https://developers.eveonline.com/static-data/tranquility/latest.jsonl"
)
DATA_FILENAME_TEMPLATE: str = "eve-online-static-data-${build_number}-${variant}.zip"


@dataclass(slots=True)
class EveSDSettings:
    """Runtime settings consumed by eve-sd components."""

    application_directory: Path
    """The directory where the application stores its data and logs."""
    logging_directory: Path
    """The directory where the application stores its log files."""
    sde_latest_info_url: str = LATEST_INFO_URL
    """The URL to fetch the latest SDE build information."""
    sde_download_url_template: str = SDE_URL_TEMPLATE
    """The template for constructing the SDE download URL."""
    sde_data_changes_url_template: str = DATA_CHANGES_URL_TEMPLATE
    """The template for constructing the SDE data changes URL."""
    sde_schema_changelog_url: str = SCHEMA_CHANGELOG_URL
    """The URL to fetch the SDE schema changelog."""
    sde_data_filename_template: str = DATA_FILENAME_TEMPLATE
    """The template for naming downloaded SDE data files."""


class ApplicationSettingsPydantic(BaseSettings):
    """Settings for the application loaded from environment variables and optional `.env` files.

    Values are read from environment variables prefixed with the application name,
    altered to uppercase and with non-alphanumeric characters replaced by underscores.
    Values are also read from `.env` or `.env.dev` when present.
    """

    model_config = SettingsConfigDict(
        env_prefix=ENV_PREFIX,
        env_file=(".env", ".env.dev"),
        env_file_encoding="utf-8",
    )

    application_directory: Path = Path(get_app_dir(__app_name__))


def get_settings(
    application_directory: Path | None = None,
) -> EveSDSettings:
    """Build runtime settings from a Pydantic settings model or application directory.

    Args:
        application_directory (Path | None): Optional application directory path.
            If not provided, the default application directory is used.

    Returns:
        Runtime settings dataclass used by the application.

    Raises:
        ValueError: If the provided application directory exists but is not a directory.
    """
    if application_directory is None:
        # If the application directory is not provided, use the value from the Pydantic
        # settings model. This allows for environment variable overrides and .env file loading.
        application_directory = ApplicationSettingsPydantic().application_directory
    application_directory = application_directory.expanduser().resolve()
    if application_directory.exists() and not application_directory.is_dir():
        raise ValueError(
            f"Application directory '{application_directory}' exists but is not a directory."
        )
    settings = _initialize_settings(application_directory)
    return settings


def _initialize_settings(application_directory: Path) -> EveSDSettings:
    """Build default runtime settings.

    Also ensures that the application directories exist.
    """
    settings = EveSDSettings(
        application_directory=application_directory,
        logging_directory=application_directory / "logs",
        sde_latest_info_url=LATEST_INFO_URL,
        sde_download_url_template=SDE_URL_TEMPLATE,
        sde_data_changes_url_template=DATA_CHANGES_URL_TEMPLATE,
        sde_schema_changelog_url=SCHEMA_CHANGELOG_URL,
        sde_data_filename_template=DATA_FILENAME_TEMPLATE,
    )
    # Ensure that the application directories exist.
    settings.application_directory.mkdir(parents=True, exist_ok=True)
    settings.logging_directory.mkdir(parents=True, exist_ok=True)
    return settings
