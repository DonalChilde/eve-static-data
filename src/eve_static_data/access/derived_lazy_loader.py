"""A Lazy loader for derived datasets."""

from pathlib import Path

from eve_static_data.models.dataset_filenames import DerivedDatasetFiles
from eve_static_data.models.derived.market_path import MarketPathsDataset
from eve_static_data.models.derived.normalized_eve_type import NormalizedEveTypesDataset
from eve_static_data.models.derived.region_names import RegionNames
from eve_static_data.models.derived.system_names import SystemNames


class DerivedLazyLoader:
    def __init__(self, input_dir: Path, localized: str = "en"):
        """A class for lazily loading derived datasets.

        Assumes that the derived datasets have already been generated and are stored in
        the specified input directory with the default file names.

        Args:
            input_dir: The directory where the derived datasets are stored.
            localized: The localization used by the datasets (default: "en").
        """
        self.input_dir = input_dir
        self.localized = localized

        self._market_paths: MarketPathsDataset | None = None
        self._normalized_eve_types: NormalizedEveTypesDataset | None = None
        self._normalized_eve_types_published: NormalizedEveTypesDataset | None = None
        self._region_names: RegionNames | None = None
        self._system_names: SystemNames | None = None

    def market_paths(self) -> MarketPathsDataset:
        """Lazily load the market paths dataset."""
        if self._market_paths is None:
            file_name = DerivedDatasetFiles.MARKET_PATHS.localized(self.localized)
            dataset_path = self.input_dir / file_name
            with open(dataset_path, "rb") as f:
                self._market_paths = MarketPathsDataset.model_validate(f.read())
        return self._market_paths

    def normalized_eve_types(self) -> NormalizedEveTypesDataset:
        """Lazily load the normalized EVE types dataset."""
        if self._normalized_eve_types is None:
            file_name = DerivedDatasetFiles.NORMALIZED_EVE_TYPES.localized(
                self.localized
            )
            dataset_path = self.input_dir / file_name
            with open(dataset_path, "rb") as f:
                self._normalized_eve_types = NormalizedEveTypesDataset.model_validate(
                    f.read()
                )
        return self._normalized_eve_types

    def normalized_eve_types_published(self) -> NormalizedEveTypesDataset:
        """Lazily load the published normalized EVE types dataset."""
        if self._normalized_eve_types_published is None:
            file_name = DerivedDatasetFiles.NORMALIZED_EVE_TYPES_PUBLISHED.localized(
                self.localized
            )
            dataset_path = self.input_dir / file_name
            with open(dataset_path, "rb") as f:
                self._normalized_eve_types_published = (
                    NormalizedEveTypesDataset.model_validate(f.read())
                )
        return self._normalized_eve_types_published

    def region_names(self) -> RegionNames:
        """Lazily load the region names dataset."""
        if self._region_names is None:
            file_name = DerivedDatasetFiles.REGION_NAMES.localized(self.localized)
            dataset_path = self.input_dir / file_name
            with open(dataset_path, "rb") as f:
                self._region_names = RegionNames.model_validate(f.read())
        return self._region_names

    def system_names(self) -> SystemNames:
        """Lazily load the system names dataset."""
        if self._system_names is None:
            file_name = DerivedDatasetFiles.SYSTEM_NAMES.localized(self.localized)
            dataset_path = self.input_dir / file_name
            with open(dataset_path, "rb") as f:
                self._system_names = SystemNames.model_validate(f.read())
        return self._system_names
