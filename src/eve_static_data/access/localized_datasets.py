"""A Lazy loader for localized datasets."""

from pathlib import Path

from eve_static_data.models import localized_datasets as LDS
from eve_static_data.models import sde_pydantic as PM
from eve_static_data.models import sde_pydantic_localized as PML
from eve_static_data.models.localized_dataset_files import LocalizedDatasetFiles
from eve_static_data.models.market_path import MarketPath, MarketPathsDataset
from eve_static_data.models.normalized_eve_type import (
    NormalizedEveType,
    NormalizedEveTypesDataset,
)


class LocalizedDatasets:
    def __init__(self, datasets_path: Path):
        """A lazy loader for localized datasets."""
        self.datasets_path = datasets_path
        self.ancestries_dataset: LDS.AncestriesDataset | None = None
        self.blueprints_dataset: LDS.BlueprintsDataset | None = None
        self.categories_dataset: LDS.CategoriesDataset | None = None
        self.groups_dataset: LDS.GroupsDataset | None = None
        self.map_regions_dataset: LDS.MapRegionsDataset | None = None
        self.map_solarsystems_dataset: LDS.MapSolarSystemsDataset | None = None
        self.market_groups_dataset: LDS.MarketGroupsDataset | None = None
        self.meta_groups_dataset: LDS.MetaGroupsDataset | None = None
        self.type_materials_dataset: LDS.TypeMaterialsDataset | None = None
        self.eve_types_dataset: LDS.EveTypesDataset | None = None

        # ------------------------------------------
        # Derived datasets
        # ------------------------------------------

        self.market_paths_dataset: MarketPathsDataset | None = None
        self.normalized_eve_types_dataset: NormalizedEveTypesDataset | None = None
        self.normalized_eve_types_published_dataset: (
            NormalizedEveTypesDataset | None
        ) = None

    def ancestries(self) -> dict[int, PML.AncestriesLocalized]:
        """Ancestries dataset, lazily loaded from disk."""
        if self.ancestries_dataset is None:
            self.ancestries_dataset = LDS.AncestriesDataset.load_from_disk(
                self.datasets_path / LocalizedDatasetFiles.ANCESTRIES
            )
        return self.ancestries_dataset.data

    def blueprints(self) -> dict[int, PM.Blueprints]:
        """Blueprints dataset, lazily loaded from disk."""
        if self.blueprints_dataset is None:
            self.blueprints_dataset = LDS.BlueprintsDataset.load_from_disk(
                self.datasets_path / LocalizedDatasetFiles.BLUEPRINTS
            )
        return self.blueprints_dataset.data

    def categories(self) -> dict[int, PML.CategoriesLocalized]:
        """Categories dataset, lazily loaded from disk."""
        if self.categories_dataset is None:
            self.categories_dataset = LDS.CategoriesDataset.load_from_disk(
                self.datasets_path / LocalizedDatasetFiles.CATEGORIES
            )
        return self.categories_dataset.data

    def groups(self) -> dict[int, PML.GroupsLocalized]:
        """Groups dataset, lazily loaded from disk."""
        if self.groups_dataset is None:
            self.groups_dataset = LDS.GroupsDataset.load_from_disk(
                self.datasets_path / LocalizedDatasetFiles.GROUPS
            )
        return self.groups_dataset.data

    def map_regions(self) -> dict[int, PML.MapRegionsLocalized]:
        """Map regions dataset, lazily loaded from disk."""
        if self.map_regions_dataset is None:
            self.map_regions_dataset = LDS.MapRegionsDataset.load_from_disk(
                self.datasets_path / LocalizedDatasetFiles.MAP_REGIONS
            )
        return self.map_regions_dataset.data

    def map_solarsystems(self) -> dict[int, PML.MapSolarSystemsLocalized]:
        """Map solar systems dataset, lazily loaded from disk."""
        if self.map_solarsystems_dataset is None:
            self.map_solarsystems_dataset = LDS.MapSolarSystemsDataset.load_from_disk(
                self.datasets_path / LocalizedDatasetFiles.MAP_SOLARSYSTEMS
            )
        return self.map_solarsystems_dataset.data

    def market_groups(self) -> dict[int, PML.MarketGroupsLocalized]:
        """Market groups dataset, lazily loaded from disk."""
        if self.market_groups_dataset is None:
            self.market_groups_dataset = LDS.MarketGroupsDataset.load_from_disk(
                self.datasets_path / LocalizedDatasetFiles.MARKET_GROUPS
            )
        return self.market_groups_dataset.data

    def meta_groups(self) -> dict[int, PML.MetaGroupsLocalized]:
        """Meta groups dataset, lazily loaded from disk."""
        if self.meta_groups_dataset is None:
            self.meta_groups_dataset = LDS.MetaGroupsDataset.load_from_disk(
                self.datasets_path / LocalizedDatasetFiles.META_GROUPS
            )
        return self.meta_groups_dataset.data

    def type_materials(self) -> dict[int, PM.TypeMaterials]:
        """Type materials dataset, lazily loaded from disk."""
        if self.type_materials_dataset is None:
            self.type_materials_dataset = LDS.TypeMaterialsDataset.load_from_disk(
                self.datasets_path / LocalizedDatasetFiles.TYPE_MATERIALS
            )
        return self.type_materials_dataset.data

    def eve_types(self) -> dict[int, PML.EveTypesLocalized]:
        """Eve types dataset, lazily loaded from disk."""
        if self.eve_types_dataset is None:
            self.eve_types_dataset = LDS.EveTypesDataset.load_from_disk(
                self.datasets_path / LocalizedDatasetFiles.EVE_TYPES
            )
        return self.eve_types_dataset.data

    # --------------------------------------------------
    # Derived datasets
    # --------------------------------------------------

    def market_paths(self) -> dict[int, MarketPath]:
        """Market paths dataset, lazily loaded from disk."""
        if self.market_paths_dataset is None:
            self.market_paths_dataset = MarketPathsDataset.load_from_disk(
                self.datasets_path / LocalizedDatasetFiles.MARKET_PATHS
            )
        return self.market_paths_dataset.data

    def normalized_eve_types(self) -> dict[int, NormalizedEveType]:
        """Normalized Eve types dataset, lazily loaded from disk."""
        if self.normalized_eve_types_dataset is None:
            self.normalized_eve_types_dataset = (
                NormalizedEveTypesDataset.load_from_disk(
                    self.datasets_path / LocalizedDatasetFiles.NORMALIZED_EVE_TYPES
                )
            )
        return self.normalized_eve_types_dataset.data

    def normalized_eve_types_published(self) -> dict[int, NormalizedEveType]:
        """Normalized Eve types published dataset, lazily loaded from disk."""
        if self.normalized_eve_types_published_dataset is None:
            self.normalized_eve_types_published_dataset = (
                NormalizedEveTypesDataset.load_from_disk(
                    self.datasets_path
                    / LocalizedDatasetFiles.NORMALIZED_EVE_TYPES_PUBLISHED
                )
            )
        return self.normalized_eve_types_published_dataset.data
