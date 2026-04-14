"""Datasets derived from the SDE and localized datasets.

Subsets or combinations of data in a more useful or quicker loading form.

For best performance, generate these once, and save them to disk.
"""

import logging
from pathlib import Path

from eve_static_data.access import localized_datasets as LDA
from eve_static_data.access import sde_datasets as SDE
from eve_static_data.access.sde_datasets import sde_info as load_sde_info_2
from eve_static_data.models.dataset_filenames import (
    DerivedDatasetFiles,
    SdeDatasetFiles,
)
from eve_static_data.models.derived.bill_of_materials import (
    BillsOfMaterialsDataset,
)
from eve_static_data.models.derived.market_path import MarketPathsDataset
from eve_static_data.models.derived.meta_level import TypesMetaLevelsDataset
from eve_static_data.models.derived.normalized_eve_type import NormalizedEveTypesDataset
from eve_static_data.models.derived.published_blueprints import (
    PublishedBlueprintsDataset,
)
from eve_static_data.models.derived.region_names import RegionNames
from eve_static_data.models.derived.system_names import SystemNames
from eve_static_data.models.pydantic.datasets import SdeDataset
from eve_static_data.models.pydantic.localized_datasets import SdeDatasetLocalized
from eve_static_data.models.type_defs import Lang

logger = logging.getLogger(__name__)


def bill_of_materials(
    sde_path: Path,
    only_published: bool = True,
    skip_validation_failures: bool = False,
) -> BillsOfMaterialsDataset:
    """Load the bill of materials dataset for the specified language."""
    eve_types = LDA.eve_types_localized(
        sde_path,
        lang="en",
        only_published=only_published,
        skip_validation_failures=skip_validation_failures,
    )
    blueprints = published_blueprints(
        sde_path,
        lang="en",
        only_published=only_published,
        skip_validation_failures=skip_validation_failures,
    )
    bill_of_materials = BillsOfMaterialsDataset.from_datasets(
        blueprints=blueprints,
        eve_types=eve_types,
    )
    return bill_of_materials


def market_paths(
    sde_path: Path,
    lang: Lang,
    only_published: bool = True,
    skip_validation_failures: bool = False,
) -> MarketPathsDataset:
    """Load the market paths dataset for the specified language."""
    market_groups = LDA.market_groups_localized(
        sde_path,
        lang,
        only_published=only_published,
        skip_validation_failures=skip_validation_failures,
    )
    market_paths = MarketPathsDataset.from_dataset(market_groups)
    return market_paths


def meta_levels(
    sde_path: Path,
    lang: Lang,
    only_published: bool = True,
    skip_validation_failures: bool = False,
) -> TypesMetaLevelsDataset:
    """Load the type meta levels dataset for the specified language."""
    eve_types = LDA.eve_types_localized(
        sde_path,
        lang,
        only_published=only_published,
        skip_validation_failures=skip_validation_failures,
    )
    type_dogma = SDE.type_dogma(
        sde_path,
        only_published=only_published,
        skip_validation_failures=skip_validation_failures,
    )
    meta_levels = TypesMetaLevelsDataset.from_datasets(
        type_dogma_dataset=type_dogma,
        eve_types_dataset=eve_types,
    )
    return meta_levels


def normalized_eve_types(
    sde_path: Path,
    lang: Lang,
    only_published: bool = True,
    skip_validation_failures: bool = False,
) -> NormalizedEveTypesDataset:
    """Load the normalized eve types dataset for the specified language."""
    eve_types = LDA.eve_types_localized(
        sde_path,
        lang,
        only_published=only_published,
        skip_validation_failures=skip_validation_failures,
    )

    categories = LDA.categories_localized(
        sde_path,
        lang,
        only_published=only_published,
        skip_validation_failures=skip_validation_failures,
    )
    groups = LDA.groups_localized(
        sde_path,
        lang,
        only_published=only_published,
        skip_validation_failures=skip_validation_failures,
    )
    meta_groups = LDA.meta_groups_localized(
        sde_path,
        lang,
        only_published=only_published,
        skip_validation_failures=skip_validation_failures,
    )
    market_groups = LDA.market_groups_localized(
        sde_path,
        lang,
        only_published=only_published,
        skip_validation_failures=skip_validation_failures,
    )
    type_dogma = SDE.type_dogma(
        sde_path,
        only_published=only_published,
        skip_validation_failures=skip_validation_failures,
    )
    normalized_eve_types = NormalizedEveTypesDataset.from_datasets(
        eve_types_dataset=eve_types,
        categories_dataset=categories,
        groups_dataset=groups,
        meta_groups_dataset=meta_groups,
        market_groups_dataset=market_groups,
        type_dogma_dataset=type_dogma,
    )
    return normalized_eve_types


def published_blueprints(
    sde_path: Path,
    lang: Lang,
    only_published: bool = True,
    skip_validation_failures: bool = False,
) -> PublishedBlueprintsDataset:
    """Load the published blueprints dataset for the specified language."""
    eve_types = LDA.eve_types_localized(
        sde_path,
        lang,
        only_published=only_published,
        skip_validation_failures=skip_validation_failures,
    )
    blueprints = SDE.blueprints(sde_path)
    published_blueprints = PublishedBlueprintsDataset.from_datasets(
        blueprints_dataset=blueprints,
        eve_types_dataset=eve_types,
    )
    return published_blueprints


def region_names(
    sde_path: Path,
    lang: Lang,
    only_published: bool = True,
    skip_validation_failures: bool = False,
) -> RegionNames:
    """Load the region names dataset for the specified language."""
    map_regions = LDA.map_regions_localized(
        sde_path,
        lang,
        only_published=only_published,
        skip_validation_failures=skip_validation_failures,
    )
    region_names = RegionNames.from_datasets(map_regions)
    return region_names


def system_names(
    sde_path: Path,
    lang: Lang,
    only_published: bool = True,
    skip_validation_failures: bool = False,
) -> SystemNames:
    """Load the system names dataset for the specified language."""
    map_solar_systems = LDA.map_solar_systems_localized(
        sde_path,
        lang,
        only_published=only_published,
        skip_validation_failures=skip_validation_failures,
    )
    system_names = SystemNames.from_datasets(map_solar_systems)
    return system_names


class DerivedDatasetLoader:
    def __init__(
        self,
        sde_path: Path,
        derived_datasets_path: Path | None = None,
    ):
        """Loader for derived datasets.

        Provides optional caching to file for dervied datsets, as some datasets can require
        expensive processing to generate. If a derived dataset file exists for the current
        SDE build, it will be loaded instead of being regenerated. If the file is missing
        the dataset will be generated and saved to the specified path for future use.

        Args:
            sde_path: Path to the unpacked SDE directory.
            derived_datasets_path: Optional path to the directory where derived datasets
                are stored. If not provided, the derived datasets are rebuilt from the
                sde on each load.

        Raises:
            ValueError: If the SDE info cannot be loaded from the SDE info file, or if the
                loaded dataset's build number does not match the SDE build number.
        """
        self.sde_path = sde_path
        self.derived_datasets_path = derived_datasets_path

        sde_info_path = sde_path / SdeDatasetFiles.SDE_INFO.as_jsonl()
        try:
            sde_info_from_file = load_sde_info_2(sde_path)
            self.sde_info = sde_info_from_file
        except Exception as e:
            raise ValueError(
                f"Failed to load SDE info from {sde_info_path}: {e}"
            ) from e

    def bills_of_materials(
        self,
        lang: Lang = "en",
        only_published: bool = True,
        skip_validation_failures: bool = False,
    ) -> BillsOfMaterialsDataset:
        """Load the bill of materials dataset."""
        file_name = DerivedDatasetFiles.BILLS_OF_MATERIALS.localized_published(
            lang=lang, only_published=only_published
        )
        file_path, dataset = self._load_dataset_from_file(
            file_name=file_name,
            dataset_class=BillsOfMaterialsDataset,
        )
        if dataset is not None:
            return dataset
        dataset = bill_of_materials(
            self.sde_path,
            only_published=only_published,
            skip_validation_failures=skip_validation_failures,
        )
        if file_path is not None:
            self._save_dataset_to_file(file_path, dataset)
        return dataset

    def market_paths(
        self,
        lang: Lang = "en",
        only_published: bool = True,
        skip_validation_failures: bool = False,
    ) -> MarketPathsDataset:
        """Load the market paths dataset for the specified language."""
        file_name = DerivedDatasetFiles.MARKET_PATHS.localized_published(
            lang, only_published=only_published
        )
        file_path, dataset = self._load_dataset_from_file(
            file_name=file_name,
            dataset_class=MarketPathsDataset,
        )
        if dataset is not None:
            return dataset
        dataset = market_paths(
            self.sde_path,
            lang,
            only_published=only_published,
            skip_validation_failures=skip_validation_failures,
        )
        if file_path is not None:
            self._save_dataset_to_file(file_path, dataset)
        return dataset

    def meta_levels(
        self,
        lang: Lang = "en",
        only_published: bool = True,
        skip_validation_failures: bool = False,
    ) -> TypesMetaLevelsDataset:
        """Load the type meta levels dataset for the specified language."""
        file_name = DerivedDatasetFiles.TYPE_META_LEVELS.localized_published(
            lang, only_published=only_published
        )
        file_path, dataset = self._load_dataset_from_file(
            file_name=file_name,
            dataset_class=TypesMetaLevelsDataset,
        )
        if dataset is not None:
            return dataset
        dataset = meta_levels(
            self.sde_path,
            lang,
            only_published=only_published,
            skip_validation_failures=skip_validation_failures,
        )
        if file_path is not None:
            self._save_dataset_to_file(file_path, dataset)
        return dataset

    def normalized_eve_types(
        self,
        lang: Lang = "en",
        only_published: bool = True,
        skip_validation_failures: bool = False,
    ) -> NormalizedEveTypesDataset:
        """Load the normalized eve types dataset for the specified language."""
        file_name = DerivedDatasetFiles.NORMALIZED_EVE_TYPES.localized_published(
            lang, only_published=only_published
        )
        file_path, dataset = self._load_dataset_from_file(
            file_name=file_name,
            dataset_class=NormalizedEveTypesDataset,
        )
        if dataset is not None:
            return dataset
        dataset = normalized_eve_types(
            self.sde_path,
            lang,
            only_published=only_published,
            skip_validation_failures=skip_validation_failures,
        )
        if file_path is not None:
            self._save_dataset_to_file(file_path, dataset)
        return dataset

    def published_blueprints(
        self,
        lang: Lang = "en",
        only_published: bool = True,
        skip_validation_failures: bool = False,
    ) -> PublishedBlueprintsDataset:
        """Load the published blueprints dataset for the specified language."""
        file_name = DerivedDatasetFiles.PUBLISHED_BLUEPRINTS.localized_published(
            lang, only_published=only_published
        )
        file_path, dataset = self._load_dataset_from_file(
            file_name=file_name,
            dataset_class=PublishedBlueprintsDataset,
        )
        if dataset is not None:
            return dataset
        dataset = published_blueprints(
            self.sde_path,
            lang,
            only_published=only_published,
            skip_validation_failures=skip_validation_failures,
        )
        if file_path is not None:
            self._save_dataset_to_file(file_path, dataset)
        return dataset

    def region_names(
        self,
        lang: Lang = "en",
        only_published: bool = True,
        skip_validation_failures: bool = False,
    ) -> RegionNames:
        """Load the region names dataset for the specified language."""
        file_name = DerivedDatasetFiles.REGION_NAMES.localized_published(
            lang, only_published=only_published
        )
        file_path, dataset = self._load_dataset_from_file(
            file_name=file_name,
            dataset_class=RegionNames,
        )
        if dataset is not None:
            return dataset
        dataset = region_names(
            self.sde_path,
            lang,
            only_published=only_published,
            skip_validation_failures=skip_validation_failures,
        )
        if file_path is not None:
            self._save_dataset_to_file(file_path, dataset)
        return dataset

    def system_names(
        self,
        lang: Lang = "en",
        only_published: bool = True,
        skip_validation_failures: bool = False,
    ) -> SystemNames:
        """Load the system names dataset for the specified language."""
        file_name = DerivedDatasetFiles.SYSTEM_NAMES.localized_published(
            lang, only_published=only_published
        )
        file_path, dataset = self._load_dataset_from_file(
            file_name=file_name,
            dataset_class=SystemNames,
        )
        if dataset is not None:
            return dataset
        dataset = system_names(
            self.sde_path,
            lang,
            only_published=only_published,
            skip_validation_failures=skip_validation_failures,
        )
        if file_path is not None:
            self._save_dataset_to_file(file_path, dataset)
        return dataset

    def _save_dataset_to_file(
        self, file_path: Path, dataset: SdeDatasetLocalized | SdeDataset
    ) -> None:
        """Save a derived dataset to a file."""
        try:
            file_path.parent.mkdir(parents=True, exist_ok=True)
            file_path.write_text(dataset.model_dump_json(), encoding="utf-8")
        except Exception as e:
            logger.warning(
                "Failed to save %s dataset to %s (%s).",
                type(dataset).__name__,
                file_path,
                e,
            )

    def _load_dataset_from_file[T: SdeDatasetLocalized | SdeDataset](
        self,
        file_name: str,
        dataset_class: type[T],
    ) -> tuple[Path | None, T | None]:
        """Load a derived dataset from a file, validating the SDE build number."""
        if self.derived_datasets_path is None:
            return None, None
        dataset_path = self.derived_datasets_path / file_name
        if not dataset_path.is_file():
            return dataset_path, None
        try:
            dataset = dataset_class.model_validate_json(dataset_path.read_bytes())
            if dataset.build_number != self.sde_info.record.buildNumber:
                raise ValueError(
                    f"Dataset build number {dataset.build_number} does not match "
                    f"SDE build number {self.sde_info.record.buildNumber}"
                )
            return dataset_path, dataset
        except Exception as e:
            raise ValueError(
                f"Failed to load {dataset_class.__name__} from {dataset_path}: {e}"
            ) from e
