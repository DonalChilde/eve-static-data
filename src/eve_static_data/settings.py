"""Settings module for Eve Argus."""

from pathlib import Path
from string import Template

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict
from typing_extensions import Literal

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
    data_path: str = Field(
        default=f"{DEFAULT_APP_DIR}/data",
        description="The directory where data files are stored.",
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
    sde_changes_template: str = Field(
        default="/tranquility/changes/${build_number}.jsonl",
        description="The URL template to download the SDE changes file. build-number can be any valid build number or latest.",
    )
    sde_schema_changelog_url: str = Field(
        default="/tranquility/schema-changelog.yaml",
        description="The URL to get the SDE schema changelog.",
    )

    def resolve_sde_download_url(
        self, build_number: int, variant: Literal["jsonl", "yaml"]
    ) -> str:
        """Resolve the SDE download URL for a specific build number and variant."""
        url_template = Template(self.sde_file_template)
        url = f"{self.sde_base_url}{url_template.substitute(variant=variant, build_number=build_number)}"
        return url

    def resolve_sde_latest_info_url(self) -> str:
        """Resolve the URL to get the latest SDE information."""
        url = f"{self.sde_base_url}{self.sde_latest_info}"
        return url

    def resolve_sde_schema_changelog_url(self) -> str:
        """Resolve the URL to get the SDE schema changelog."""
        url = f"{self.sde_base_url}{self.sde_schema_changelog_url}"
        return url

    def resolve_sde_changes_url(self, build_number: int) -> str:
        """Resolve the URL to get the SDE changes for a specific build number."""
        url_template = Template(self.sde_changes_template)
        url = f"{self.sde_base_url}{url_template.substitute(build_number=build_number)}"
        return url

    def available_builds(self) -> list[int]:
        """Get a sorted list of available build numbers."""
        builds: list[int] = []
        for build_dir in Path(self.data_path).iterdir():
            if build_dir.is_dir() and build_dir.name.isdigit():
                builds.append(int(build_dir.name))
        return sorted(builds)

    def latest_build(self) -> int:
        """Get the latest available build number, or None if no builds are available."""
        builds = self.available_builds()
        if not builds:
            raise ValueError(
                f"No available builds found in data directory {self.data_path}"
            )
        return builds[-1]

    def build_data_dir(self, build_number: int, initialize: bool = False) -> Path:
        """Get the directory path for a specific build number."""
        build_dir = Path(f"{self.data_path}/{build_number}")
        if initialize:
            if build_dir.exists():
                raise FileExistsError(
                    f"Tried to initialize build data directory, but it already exists: {build_dir}"
                )
            build_dir.mkdir(parents=True, exist_ok=False)
            self.build_data_sde_dir(build_number).mkdir(parents=True, exist_ok=False)
            self.build_data_derived_dir(build_number).mkdir(
                parents=True, exist_ok=False
            )
            self.build_data_validation_dir(build_number).mkdir(
                parents=True, exist_ok=False
            )

        return build_dir

    def build_data_sde_dir(self, build_number: int) -> Path:
        """Get the directory path for the SDE data of a specific build number."""
        sde_dir = self.build_data_dir(build_number) / "sde"
        # Ensure that the SDE data directory exists for the specified build number.
        if not self.build_data_dir(build_number).exists():
            raise FileNotFoundError(
                f"Tried to get SDE data directory for build {build_number}, but it does not exist: {sde_dir}"
            )
        return sde_dir

    def build_data_derived_dir(self, build_number: int) -> Path:
        """Get the directory path for the derived data of a specific build number."""
        derived_dir = self.build_data_dir(build_number) / "derived"
        # Ensure that the derived data directory exists for the specified build number.
        if not self.build_data_dir(build_number).exists():
            raise FileNotFoundError(
                f"Tried to get derived data directory for build {build_number}, but it does not exist: {derived_dir}"
            )
        return derived_dir

    def build_data_validation_dir(self, build_number: int) -> Path:
        """Get the directory path for the validation data of a specific build number."""
        validation_dir = self.build_data_dir(build_number) / "validation"
        # Ensure that the validation data directory exists for the specified build number.
        if not self.build_data_dir(build_number).exists():
            raise FileNotFoundError(
                f"Tried to get validation data directory for build {build_number}, but it does not exist: {validation_dir}"
            )
        return validation_dir


def get_settings() -> EveStaticDataSettings:
    """Get the Eve Static Data settings."""
    settings = EveStaticDataSettings()
    # Ensure that the application directories exist.
    Path(settings.app_dir).mkdir(parents=True, exist_ok=True)
    Path(settings.config_dir).mkdir(parents=True, exist_ok=True)
    Path(settings.log_path).mkdir(parents=True, exist_ok=True)
    Path(settings.data_path).mkdir(parents=True, exist_ok=True)
    return settings
