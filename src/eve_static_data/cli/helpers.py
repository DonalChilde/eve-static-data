"""Helper functions and classes for ESD CLI commands."""

from dataclasses import dataclass
from pathlib import Path

from eve_static_data.settings import EveStaticDataSettings

SETTINGS_KEY = "eve-static-data-settings"


@dataclass
class ESDSettings:
    """Configuration for ESD CLI commands."""

    sde_latest_info_url: str
    sde_download_url_template: str
    sde_changes_url_template: str
    sde_schema_changelog_url: str
    sde_data_filename_template: str

    data_path: Path


def create_esd_settings(settings: EveStaticDataSettings) -> ESDSettings:
    """Create an ESDSettings instance from the app settings."""
    esd_settings = ESDSettings(
        sde_latest_info_url=settings.sde_latest_info_url,
        sde_download_url_template=settings.sde_download_url_template,
        sde_changes_url_template=settings.sde_changes_url_template,
        sde_schema_changelog_url=settings.sde_schema_changelog_url,
        sde_data_filename_template=settings.sde_data_filename_template,
        data_path=Path(settings.data_path),
    )
    return esd_settings
