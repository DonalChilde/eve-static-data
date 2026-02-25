"""loaders for derived datasets."""

from eve_static_data.models.datasets.sde_dataset_files import DerivedDatasetFiles
from eve_static_data.models.derived.market_path import MarketPathsDataset
from eve_static_data.models.derived.normalized_eve_type import NormalizedEveTypesDataset
from eve_static_data.models.derived.region_names import RegionNames
from eve_static_data.models.derived.system_names import SystemNames
from eve_static_data.settings import get_settings


class DerivedLazyLoader:
    """A class for lazily loading derived datasets for a specific build number."""

    def __init__(self, build_number: int | None = None, localized: str = "en"):
        self.build_number = build_number
        self.localized = localized
        self.settings = get_settings()
        if self.build_number is None:
            self.build_number = self.settings.latest_build()
        self.derived_path = self.settings.build_data_derived_dir(self.build_number)
        self._market_paths: MarketPathsDataset | None = None
        self._normalized_eve_types: NormalizedEveTypesDataset | None = None
        self._normalized_eve_types_published: NormalizedEveTypesDataset | None = None
        self._region_names: RegionNames | None = None
        self._system_names: SystemNames | None = None

    def market_paths(self) -> MarketPathsDataset:
        if self._market_paths is None:
            file_name = DerivedDatasetFiles.MARKET_PATHS.localized(self.localized)
            dataset_path = self.derived_path / file_name
            self._market_paths = MarketPathsDataset.load_from_disk(dataset_path)
        return self._market_paths

    def normalized_eve_types(self) -> NormalizedEveTypesDataset:
        if self._normalized_eve_types is None:
            file_name = DerivedDatasetFiles.NORMALIZED_EVE_TYPES.localized(
                self.localized
            )
            dataset_path = self.derived_path / file_name
            self._normalized_eve_types = NormalizedEveTypesDataset.load_from_disk(
                dataset_path
            )
        return self._normalized_eve_types

    def normalized_eve_types_published(self) -> NormalizedEveTypesDataset:
        if self._normalized_eve_types_published is None:
            file_name = DerivedDatasetFiles.NORMALIZED_EVE_TYPES_PUBLISHED.localized(
                self.localized
            )
            dataset_path = self.derived_path / file_name
            self._normalized_eve_types_published = (
                NormalizedEveTypesDataset.load_from_disk(dataset_path)
            )
        return self._normalized_eve_types_published

    def region_names(self) -> RegionNames:
        if self._region_names is None:
            file_name = DerivedDatasetFiles.REGION_NAMES.localized(self.localized)
            dataset_path = self.derived_path / file_name
            self._region_names = RegionNames.load_from_disk(dataset_path)
        return self._region_names

    def system_names(self) -> SystemNames:
        if self._system_names is None:
            file_name = DerivedDatasetFiles.SYSTEM_NAMES.localized(self.localized)
            dataset_path = self.derived_path / file_name
            self._system_names = SystemNames.load_from_disk(dataset_path)
        return self._system_names
