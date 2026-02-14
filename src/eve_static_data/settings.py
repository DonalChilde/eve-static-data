"""Settings module for Eve Argus."""

from pathlib import Path
from string import Template

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
    config_dir: str = Field(
        default=f"{DEFAULT_APP_DIR}/config",
        description="The directory where configuration files are stored.",
    )
    log_path: str = Field(
        default=f"{DEFAULT_APP_DIR}/logs",
        description="The directory where log files are stored.",
    )
    sde_base_url: str = Field(
        default="https://developers.eveonline.com/static-data",
        description="The base URL to download the latest SDE data.",
    )
    sde_latest_info: str = Field(
        default="/tranquility/latest.jsonl",
        description="The URL to get information about the latest SDE data.",
    )
    sde_file_template: str = Field(
        default="/tranquility/eve-online-static-data-${build_number}-${variant}.zip",
        description="The URL template to download the SDE data file. build-number can be any valid build number or latest. variant can be jsonl or yaml",
    )
    sde_schema_changelog_url: str = Field(
        default="/tranquility/schema-changelog.yaml",
        description="The URL to get the SDE schema changelog.",
    )

    def resolve_sde_download_url(self, build_number: int, variant: str) -> str:
        """Resolve the SDE download URL for a specific build number and variant."""
        url_template = Template(self.sde_file_template)
        url = f"{self.sde_base_url}{url_template.substitute(variant=variant, build_number=build_number)}"
        return url

    def resolve_sde_latest_info_url(self) -> str:
        """Resolve the URL to get the latest SDE information."""
        url = f"{self.sde_base_url}{self.sde_latest_info}"
        return url

    def resolve_sde_changelog_url(self) -> str:
        """Resolve the URL to get the SDE schema changelog."""
        url = f"{self.sde_base_url}{self.sde_schema_changelog_url}"
        return url

    def db_path(self, db_name: str = "eve-static-data") -> Path:
        """Get the path to a database file."""
        return Path(f"{self.app_dir}/data/{db_name}.db")

    def db_backup_path(
        self, build_number: int, db_name: str = "eve-static-data"
    ) -> Path:
        """Get the path to a database backup file."""
        return Path(f"{self.app_dir}/data/{db_name}_{build_number}_backup.db")


def get_settings() -> EveStaticDataSettings:
    """Get the Eve Static Data settings."""
    settings = EveStaticDataSettings()
    # Ensure that the application directories exist.
    Path(settings.app_dir).mkdir(parents=True, exist_ok=True)
    Path(settings.config_dir).mkdir(parents=True, exist_ok=True)
    Path(settings.log_path).mkdir(parents=True, exist_ok=True)
    settings.db_path().parent.mkdir(parents=True, exist_ok=True)
    settings.db_backup_path(0).parent.mkdir(parents=True, exist_ok=True)
    return settings
