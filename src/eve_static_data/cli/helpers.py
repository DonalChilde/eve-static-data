"""Helper functions and classes for ESD CLI commands."""

from dataclasses import dataclass

from eve_static_data.settings import EveStaticDataSettings

SETTINGS_KEY = "eve-static-data-settings"


@dataclass(slots=True)
class EsdCliSettings:
    """Configuration for ESD CLI commands."""

    sde_latest_info_url: str
    sde_download_url_template: str
    sde_changes_url_template: str
    sde_schema_changelog_url: str
    sde_data_filename_template: str


def create_esd_settings(settings: EveStaticDataSettings) -> EsdCliSettings:
    """Create an EsdCliSettings instance from the app settings."""
    esd_settings = EsdCliSettings(
        sde_latest_info_url=settings.sde_latest_info_url,
        sde_download_url_template=settings.sde_download_url_template,
        sde_changes_url_template=settings.sde_data_changes_url_template,
        sde_schema_changelog_url=settings.sde_schema_changelog_url,
        sde_data_filename_template=settings.sde_data_filename_template,
    )
    return esd_settings
