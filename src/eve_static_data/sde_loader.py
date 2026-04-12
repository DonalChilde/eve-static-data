"""Loader for ESD datasets."""

from pathlib import Path

from eve_static_data.access.derived_datasets import DerivedDatasetLoader
from eve_static_data.access.localized_datasets import LocalizedDatasetLoader
from eve_static_data.access.sde_datasets import SdeDatasetLoader
from eve_static_data.models.pydantic.datasets import SdeInfoDataset


class SDELoader:
    """Loader for SDE datasets."""

    def __init__(
        self,
        sde_path: Path,
        derived_datasets_path: Path | None = None,
    ):
        """Loader for SDE datasets.

        Args:
            sde_path: Path to the unpacked SDE directory.
            derived_datasets_path: Optional path to the directory where derived datasets
                are stored. If provided, the derived datasets will be loaded from this path
                if available, and automatically saved to this path if regenerated. If not
                provided, the derived datasets are rebuilt from the SDE on each load.

        Raises:
            FileNotFoundError: If the SDE info dataset is not found in the provided SDE path.


        """
        self._sde = SdeDatasetLoader(sde_path)
        self._localized = LocalizedDatasetLoader(sde_path)
        self._derived = DerivedDatasetLoader(sde_path, derived_datasets_path)
        # will raise if the SDE info dataset is not present, which is desirable to fail early in that case
        self._sde_info: SdeInfoDataset = self._sde.sde_info()

    @property
    def build_number(self) -> int:
        """Get the build number of the SDE."""
        return self._sde_info.build_number

    @property
    def release_date(self) -> str:
        """Get the release date of the SDE."""
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
