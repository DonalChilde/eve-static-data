"""Settings module for Eve Argus."""

from pathlib import Path

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

from eve_static_data import DEFAULT_APP_DIR, __app_name__, __description__, __version__

_app_env_prefix = "PFMSOFT_EVE_STATIC_DATA_"


class EveStaticDataSettings(BaseSettings):
    """Settings for Eve Static Data application."""

    model_config = SettingsConfigDict(
        env_prefix=_app_env_prefix,
        env_file=".eve-static-data.env",
        env_file_encoding="utf-8",
    )

    app_name: str = Field(
        default=__app_name__, description="The name of the application."
    )
    version: str = Field(
        default=__version__, description="The version of the application."
    )
    description: str = Field(
        default=__description__,
        description="A brief description of the application.",
    )
    app_dir: str = Field(
        default=str(DEFAULT_APP_DIR),
        description="The application directory path.",
    )

    @property
    def log_path(self) -> Path:
        """The directory where log files are stored."""
        return Path(self.app_dir) / "logs"

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
    settings = EveStaticDataSettings()
    # Ensure that the application directories exist.
    Path(settings.app_dir).mkdir(parents=True, exist_ok=True)
    Path(settings.log_path).mkdir(parents=True, exist_ok=True)
    return settings
