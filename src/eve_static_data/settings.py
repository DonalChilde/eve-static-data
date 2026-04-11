"""Settings module for Eve Argus."""

from dataclasses import dataclass
from pathlib import Path

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

from eve_static_data import DEFAULT_APP_DIR, __app_name__, __description__, __version__

_app_env_prefix = "PFMSOFT_EVE_STATIC_DATA_"


@dataclass(slots=True)
class EveStaticDataSettings:
    """Settings for Eve Static Data application."""

    application_directory: Path = DEFAULT_APP_DIR
    logging_directory: Path = DEFAULT_APP_DIR / "logs"
    sde_directory: Path = DEFAULT_APP_DIR / "sde"
    sde_latest_info_url: str = (
        "https://developers.eveonline.com/static-data/tranquility/latest.jsonl"
    )
    sde_download_url_template: str = "https://developers.eveonline.com/static-data/tranquility/eve-online-static-data-${build_number}-${variant}.zip"
    sde_data_changes_url_template: str = "https://developers.eveonline.com/static-data/tranquility/changes/${build_number}.jsonl"
    sde_schema_changelog_url: str = (
        "https://developers.eveonline.com/static-data/tranquility/schema-changelog.yaml"
    )
    sde_data_filename_template: str = (
        "eve-online-static-data-${build_number}-${variant}.zip"
    )


class EveStaticDataSettingsPydantic(BaseSettings):
    """Settings for Eve Static Data application.

    This class is used to load settings from environment variables and .env files using
    Pydantic. The get_settings function is then used to convert these settings to the
    EveStaticDataSettings dataclass for use in the application.
    """

    model_config = SettingsConfigDict(
        env_prefix=_app_env_prefix,
        env_file=".eve-static-data.env",
        env_file_encoding="utf-8",
    )

    application_directory: str = Field(
        default=str(DEFAULT_APP_DIR),
        description="The application directory path.",
    )
    sde_directory: str = Field(
        default=str(DEFAULT_APP_DIR / "sde"),
        description="The directory where the SDE data is stored.",
    )
    logging_directory: str = Field(
        default=str(DEFAULT_APP_DIR / "logs"),
        description="The directory where log files are stored.",
    )
    sde_latest_info_url: str = Field(
        default="https://developers.eveonline.com/static-data/tranquility/latest.jsonl",
        description="The URL to get information about the latest SDE data.",
    )
    sde_download_url_template: str = Field(
        default="https://developers.eveonline.com/static-data/tranquility/eve-online-static-data-${build_number}-${variant}.zip",
        description="The URL template to download the SDE data file. build-number can be any valid build number. variant can be jsonl or yaml",
    )
    sde_data_changes_url_template: str = Field(
        default="https://developers.eveonline.com/static-data/tranquility/changes/${build_number}.jsonl",
        description="The URL template to download the SDE changes file. build-number can be any valid build number.",
    )
    sde_schema_changelog_url: str = Field(
        default="https://developers.eveonline.com/static-data/tranquility/schema-changelog.yaml",
        description="The URL to get the SDE schema changelog.",
    )
    sde_data_filename_template: str = Field(
        default="eve-online-static-data-${build_number}-${variant}.zip",
        description="The filename template for the SDE data file. build-number can be any valid build number. variant can be jsonl or yaml",
    )


def get_settings() -> EveStaticDataSettings:
    """Get the Eve Static Data settings."""
    pydantic_settings = EveStaticDataSettingsPydantic()
    settings = EveStaticDataSettings(
        application_directory=Path(pydantic_settings.application_directory),
        logging_directory=Path(pydantic_settings.logging_directory),
        sde_directory=Path(pydantic_settings.sde_directory),
        sde_latest_info_url=pydantic_settings.sde_latest_info_url,
        sde_download_url_template=pydantic_settings.sde_download_url_template,
        sde_data_changes_url_template=pydantic_settings.sde_data_changes_url_template,
        sde_schema_changelog_url=pydantic_settings.sde_schema_changelog_url,
        sde_data_filename_template=pydantic_settings.sde_data_filename_template,
    )
    # Ensure that the application directories exist.
    Path(settings.application_directory).mkdir(parents=True, exist_ok=True)
    Path(settings.logging_directory).mkdir(parents=True, exist_ok=True)
    Path(settings.sde_directory).mkdir(parents=True, exist_ok=True)
    return settings
