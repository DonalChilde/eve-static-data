"""A Lazy loader for localized datasets."""

from pathlib import Path

from eve_static_data.models.datasets import localized_pydantic as LDS
from eve_static_data.models.datasets import sde_pydantic as ED
from eve_static_data.models.datasets.exported_dataset_files import (
    DerivedLocalizedDatasetFiles,
    ExportedDatasetFiles,
    ExportedLocalizedDatasetFiles,
)
from eve_static_data.models.derived.market_path import MarketPath, MarketPathsDataset
from eve_static_data.models.derived.normalized_eve_type import (
    NormalizedEveType,
    NormalizedEveTypesDataset,
)
from eve_static_data.models.records import sde_pydantic as PM
from eve_static_data.models.records import sde_pydantic_localized as PML


class LocalizedDatasets:
    def __init__(self, datasets_path: Path):
        """A lazy loader for localized datasets."""
        self.datasets_path = datasets_path
        self.ancestries_dataset: LDS.AncestriesLocalizedDataset | None = None
        self.blueprints_dataset: ED.BlueprintsDataset | None = None
        self.categories_dataset: LDS.CategoriesLocalizedDataset | None = None
        self.groups_dataset: LDS.GroupsLocalizedDataset | None = None
        self.map_regions_dataset: LDS.MapRegionsLocalizedDataset | None = None
        self.map_solarsystems_dataset: LDS.MapSolarSystemsLocalizedDataset | None = None
        self.market_groups_dataset: LDS.MarketGroupsLocalizedDataset | None = None
        self.meta_groups_dataset: LDS.MetaGroupsLocalizedDataset | None = None
        self.type_materials_dataset: ED.TypeMaterialsDataset | None = None
        self.eve_types_dataset: LDS.EveTypesLocalizedDataset | None = None

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
            self.ancestries_dataset = LDS.AncestriesLocalizedDataset.load_from_disk(
                self.datasets_path / ExportedLocalizedDatasetFiles.ANCESTRIES
            )
        return self.ancestries_dataset.data

    def blueprints(self) -> dict[int, PM.Blueprints]:
        """Blueprints dataset, lazily loaded from disk."""
        if self.blueprints_dataset is None:
            self.blueprints_dataset = ED.BlueprintsDataset.load_from_disk(
                self.datasets_path / ExportedDatasetFiles.BLUEPRINTS
            )
        return self.blueprints_dataset.data

    def categories(self) -> dict[int, PML.CategoriesLocalized]:
        """Categories dataset, lazily loaded from disk."""
        if self.categories_dataset is None:
            self.categories_dataset = LDS.CategoriesLocalizedDataset.load_from_disk(
                self.datasets_path / ExportedLocalizedDatasetFiles.CATEGORIES
            )
        return self.categories_dataset.data

    def groups(self) -> dict[int, PML.GroupsLocalized]:
        """Groups dataset, lazily loaded from disk."""
        if self.groups_dataset is None:
            self.groups_dataset = LDS.GroupsLocalizedDataset.load_from_disk(
                self.datasets_path / ExportedLocalizedDatasetFiles.GROUPS
            )
        return self.groups_dataset.data

    def map_regions(self) -> dict[int, PML.MapRegionsLocalized]:
        """Map regions dataset, lazily loaded from disk."""
        if self.map_regions_dataset is None:
            self.map_regions_dataset = LDS.MapRegionsLocalizedDataset.load_from_disk(
                self.datasets_path / ExportedLocalizedDatasetFiles.MAP_REGIONS
            )
        return self.map_regions_dataset.data

    def map_solarsystems(self) -> dict[int, PML.MapSolarSystemsLocalized]:
        """Map solar systems dataset, lazily loaded from disk."""
        if self.map_solarsystems_dataset is None:
            self.map_solarsystems_dataset = (
                LDS.MapSolarSystemsLocalizedDataset.load_from_disk(
                    self.datasets_path / ExportedLocalizedDatasetFiles.MAP_SOLARSYSTEMS
                )
            )
        return self.map_solarsystems_dataset.data

    def market_groups(self) -> dict[int, PML.MarketGroupsLocalized]:
        """Market groups dataset, lazily loaded from disk."""
        if self.market_groups_dataset is None:
            self.market_groups_dataset = (
                LDS.MarketGroupsLocalizedDataset.load_from_disk(
                    self.datasets_path / ExportedLocalizedDatasetFiles.MARKET_GROUPS
                )
            )
        return self.market_groups_dataset.data

    def meta_groups(self) -> dict[int, PML.MetaGroupsLocalized]:
        """Meta groups dataset, lazily loaded from disk."""
        if self.meta_groups_dataset is None:
            self.meta_groups_dataset = LDS.MetaGroupsLocalizedDataset.load_from_disk(
                self.datasets_path / ExportedLocalizedDatasetFiles.META_GROUPS
            )
        return self.meta_groups_dataset.data

    def type_materials(self) -> dict[int, PM.TypeMaterials]:
        """Type materials dataset, lazily loaded from disk."""
        if self.type_materials_dataset is None:
            self.type_materials_dataset = ED.TypeMaterialsDataset.load_from_disk(
                self.datasets_path / ExportedDatasetFiles.TYPE_MATERIALS
            )
        return self.type_materials_dataset.data

    def eve_types(self) -> dict[int, PML.EveTypesLocalized]:
        """Eve types dataset, lazily loaded from disk."""
        if self.eve_types_dataset is None:
            self.eve_types_dataset = LDS.EveTypesLocalizedDataset.load_from_disk(
                self.datasets_path / ExportedLocalizedDatasetFiles.EVE_TYPES
            )
        return self.eve_types_dataset.data

    # --------------------------------------------------
    # Derived datasets
    # --------------------------------------------------

    def market_paths(self) -> dict[int, MarketPath]:
        """Market paths dataset, lazily loaded from disk."""
        if self.market_paths_dataset is None:
            self.market_paths_dataset = MarketPathsDataset.load_from_disk(
                self.datasets_path / DerivedLocalizedDatasetFiles.MARKET_PATHS
            )
        return self.market_paths_dataset.data

    def normalized_eve_types(self) -> dict[int, NormalizedEveType]:
        """Normalized Eve types dataset, lazily loaded from disk."""
        if self.normalized_eve_types_dataset is None:
            self.normalized_eve_types_dataset = (
                NormalizedEveTypesDataset.load_from_disk(
                    self.datasets_path
                    / DerivedLocalizedDatasetFiles.NORMALIZED_EVE_TYPES
                )
            )
        return self.normalized_eve_types_dataset.data

    def normalized_eve_types_published(self) -> dict[int, NormalizedEveType]:
        """Normalized Eve types published dataset, lazily loaded from disk."""
        if self.normalized_eve_types_published_dataset is None:
            self.normalized_eve_types_published_dataset = (
                NormalizedEveTypesDataset.load_from_disk(
                    self.datasets_path
                    / DerivedLocalizedDatasetFiles.NORMALIZED_EVE_TYPES_PUBLISHED
                )
            )
        return self.normalized_eve_types_published_dataset.data
