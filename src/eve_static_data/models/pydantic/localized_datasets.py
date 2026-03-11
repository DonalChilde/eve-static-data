"""An incomplete set of models for localized SDE datasets.

More models to be added as needed for use.
"""

from pydantic import BaseModel

from eve_static_data.models.dataset_filenames import SdeDatasetFiles
from eve_static_data.models.pydantic import localized_records as LPM
from eve_static_data.models.type_defs import Lang


class SdeDatasetLocalized(BaseModel):
    build_number: int
    release_date: str
    lang: Lang


class AncestriesLocalizedDataset(SdeDatasetLocalized):
    records: dict[int, LPM.AncestriesLocalized]


class CategoriesLocalizedDataset(SdeDatasetLocalized):
    records: dict[int, LPM.CategoriesLocalized]


class GroupsLocalizedDataset(SdeDatasetLocalized):
    records: dict[int, LPM.GroupsLocalized]


class MapRegionsLocalizedDataset(SdeDatasetLocalized):
    records: dict[int, LPM.MapRegionsLocalized]


class MapSolarSystemsLocalizedDataset(SdeDatasetLocalized):
    records: dict[int, LPM.MapSolarSystemsLocalized]


class MarketGroupsLocalizedDataset(SdeDatasetLocalized):
    records: dict[int, LPM.MarketGroupsLocalized]


class MetaGroupsLocalizedDataset(SdeDatasetLocalized):
    records: dict[int, LPM.MetaGroupsLocalized]


class EveTypesLocalizedDataset(SdeDatasetLocalized):
    records: dict[int, LPM.EveTypesLocalized]


LOOKUP: dict[SdeDatasetFiles, type[SdeDatasetLocalized]] = {
    SdeDatasetFiles.ANCESTRIES: AncestriesLocalizedDataset,
    SdeDatasetFiles.CATEGORIES: CategoriesLocalizedDataset,
    SdeDatasetFiles.GROUPS: GroupsLocalizedDataset,
    SdeDatasetFiles.MAP_REGIONS: MapRegionsLocalizedDataset,
    SdeDatasetFiles.MAP_SOLAR_SYSTEMS: MapSolarSystemsLocalizedDataset,
    SdeDatasetFiles.MARKET_GROUPS: MarketGroupsLocalizedDataset,
    SdeDatasetFiles.META_GROUPS: MetaGroupsLocalizedDataset,
    SdeDatasetFiles.TYPES: EveTypesLocalizedDataset,
}
