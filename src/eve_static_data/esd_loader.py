"""Loader for ESD datasets."""

from pathlib import Path

from eve_static_data.access.derived_datasets import DerivedDatasetLoader
from eve_static_data.access.localized_datasets import LocalizedDatasetLoader
from eve_static_data.access.sde_datasets import SdeDatasetLoader
from eve_static_data.models.pydantic.datasets import SdeInfoDataset


class ESDLoader:
    """Loader for ESD datasets."""

    def __init__(
        self,
        sde_path: Path,
    ):
        """Loader for ESD datasets.

        Args:
            sde_path: Path to the unpacked SDE directory.

        """
        self._sde = SdeDatasetLoader(sde_path)
        self._localized = LocalizedDatasetLoader(sde_path)
        self._derived = DerivedDatasetLoader(sde_path)
        self._sde_info: SdeInfoDataset | None = None

    @property
    def build_number(self) -> int:
        """Get the build number of the SDE."""
        if self._sde_info is None:
            self._sde_info = self.sde_datasets.sde_info()
        return self._sde_info.build_number

    @property
    def release_date(self) -> str:
        """Get the release date of the SDE."""
        if self._sde_info is None:
            self._sde_info = self.sde_datasets.sde_info()
        return self._sde_info.release_date

    @property
    def sde_datasets(self) -> SdeDatasetLoader:
        """Access to SDE datasets."""
        return self._sde

    @property
    def localized_datasets(self) -> LocalizedDatasetLoader:
        """Access to localized datasets."""
        return self._localized

    @property
    def derived_datasets(self) -> DerivedDatasetLoader:
        """Access to derived datasets."""
        return self._derived
