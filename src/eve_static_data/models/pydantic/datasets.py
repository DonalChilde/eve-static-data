"""Models for datasets in the EVE Static Data Export (SDE).

Single-record datasets have a `record` field, while multi-record datasets have a `records` field.

Nearly all the datasets use an int as the key for their records, but the
TranslationLanguages dataset uses a string as the key.

"""

from pydantic import BaseModel

from eve_static_data.models.dataset_filenames import SdeDatasetFiles
from eve_static_data.models.pydantic import records as PM


class SdeDataset(BaseModel):
    build_number: int
    release_date: str


class AgentsInSpaceDataset(SdeDataset):
    records: dict[int, PM.AgentsInSpace]


class AgentTypesDataset(SdeDataset):
    records: dict[int, PM.AgentTypes]


class AncestriesDataset(SdeDataset):
    records: dict[int, PM.Ancestries]


class BloodlinesDataset(SdeDataset):
    records: dict[int, PM.Bloodlines]


class BlueprintsDataset(SdeDataset):
    records: dict[int, PM.Blueprints]


class CategoriesDataset(SdeDataset):
    records: dict[int, PM.Categories]


class CertificatesDataset(SdeDataset):
    records: dict[int, PM.Certificates]


class CharacterAttributesDataset(SdeDataset):
    records: dict[int, PM.CharacterAttributes]


class CloneGradesDataset(SdeDataset):
    records: dict[int, PM.CloneGrades]


class CompressibleTypesDataset(SdeDataset):
    records: dict[int, PM.CompressibleTypes]


class ContrabandTypesDataset(SdeDataset):
    records: dict[int, PM.ContrabandTypes]


class ControlTowerResourcesDataset(SdeDataset):
    records: dict[int, PM.ControlTowerResources]


class CorporationActivitiesDataset(SdeDataset):
    records: dict[int, PM.CorporationActivities]


class DebuffCollectionsDataset(SdeDataset):
    records: dict[int, PM.DebuffCollections]


class DogmaAttributeCategoriesDataset(SdeDataset):
    records: dict[int, PM.DogmaAttributeCategories]


class DogmaAttributesDataset(SdeDataset):
    records: dict[int, PM.DogmaAttributes]


class DogmaEffectsDataset(SdeDataset):
    records: dict[int, PM.DogmaEffects]


class DogmaUnitsDataset(SdeDataset):
    records: dict[int, PM.DogmaUnits]


class DynamicItemAttributesDataset(SdeDataset):
    records: dict[int, PM.DynamicItemAttributes]


class FactionsDataset(SdeDataset):
    records: dict[int, PM.Factions]


class FreelanceJobSchemasDataset(SdeDataset):
    record: PM.FreelanceJobSchemas


class GraphicsDataset(SdeDataset):
    records: dict[int, PM.Graphics]


class GroupsDataset(SdeDataset):
    records: dict[int, PM.Groups]


class IconsDataset(SdeDataset):
    records: dict[int, PM.Icons]


class LandmarksDataset(SdeDataset):
    records: dict[int, PM.Landmarks]


class MapAsteroidBeltsDataset(SdeDataset):
    records: dict[int, PM.MapAsteroidBelts]


class MapConstellationsDataset(SdeDataset):
    records: dict[int, PM.MapConstellations]


class MapMoonsDataset(SdeDataset):
    records: dict[int, PM.MapMoons]


class MapPlanetsDataset(SdeDataset):
    records: dict[int, PM.MapPlanets]


class MapRegionsDataset(SdeDataset):
    records: dict[int, PM.MapRegions]


class MapSolarSystemsDataset(SdeDataset):
    records: dict[int, PM.MapSolarSystems]


class MapStargatesDataset(SdeDataset):
    records: dict[int, PM.MapStargates]


class MapStarsDataset(SdeDataset):
    records: dict[int, PM.MapStars]


class MarketGroupsDataset(SdeDataset):
    records: dict[int, PM.MarketGroups]


class MasteriesDataset(SdeDataset):
    records: dict[int, PM.Masteries]


class MetaGroupsDataset(SdeDataset):
    records: dict[int, PM.MetaGroups]


class MercenaryTacticalOperationsDataset(SdeDataset):
    records: dict[int, PM.MercenaryTacticalOperations]


class NpcCharactersDataset(SdeDataset):
    records: dict[int, PM.NpcCharacters]


class NpcCorporationDivisionsDataset(SdeDataset):
    records: dict[int, PM.NpcCorporationDivisions]


class NpcCorporationsDataset(SdeDataset):
    records: dict[int, PM.NpcCorporations]


class NpcStationsDataset(SdeDataset):
    records: dict[int, PM.NpcStations]


class PlanetResourcesDataset(SdeDataset):
    records: dict[int, PM.PlanetResources]


class PlanetSchematicsDataset(SdeDataset):
    records: dict[int, PM.PlanetSchematics]


class RacesDataset(SdeDataset):
    records: dict[int, PM.Races]


class SdeInfoDataset(SdeDataset):
    record: PM.SdeInfo


class SkinLicensesDataset(SdeDataset):
    records: dict[int, PM.SkinLicenses]


class SkinMaterialsDataset(SdeDataset):
    records: dict[int, PM.SkinMaterials]


class SkinsDataset(SdeDataset):
    records: dict[int, PM.Skins]


class SovereigntyUpgradesDataset(SdeDataset):
    records: dict[int, PM.SovereigntyUpgrades]


class StationOperationsDataset(SdeDataset):
    records: dict[int, PM.StationOperations]


class StationServicesDataset(SdeDataset):
    records: dict[int, PM.StationServices]


# NOTE: The TranslationLanguages dataset is the only one that doesn't use an int as the
# key, so it gets its own class.
class TranslationLanguagesDataset(SdeDataset):
    records: dict[str, PM.TranslationLanguages]


class TypeBonusDataset(SdeDataset):
    records: dict[int, PM.TypeBonus]


class TypeDogmaDataset(SdeDataset):
    records: dict[int, PM.TypeDogma]


class TypeMaterialsDataset(SdeDataset):
    records: dict[int, PM.TypeMaterials]


class EveTypesDataset(SdeDataset):
    records: dict[int, PM.EveTypes]


LOOKUP: dict[SdeDatasetFiles, type[SdeDataset]] = {
    SdeDatasetFiles.AGENTS_IN_SPACE: AgentsInSpaceDataset,
    SdeDatasetFiles.AGENT_TYPES: AgentTypesDataset,
    SdeDatasetFiles.ANCESTRIES: AncestriesDataset,
    SdeDatasetFiles.BLOODLINES: BloodlinesDataset,
    SdeDatasetFiles.BLUEPRINTS: BlueprintsDataset,
    SdeDatasetFiles.CATEGORIES: CategoriesDataset,
    SdeDatasetFiles.CERTIFICATES: CertificatesDataset,
    SdeDatasetFiles.CHARACTER_ATTRIBUTES: CharacterAttributesDataset,
    SdeDatasetFiles.CLONE_GRADES: CloneGradesDataset,
    SdeDatasetFiles.COMPRESSIBLE_TYPES: CompressibleTypesDataset,
    SdeDatasetFiles.CONTRABAND_TYPES: ContrabandTypesDataset,
    SdeDatasetFiles.CONTROL_TOWER_RESOURCES: ControlTowerResourcesDataset,
    SdeDatasetFiles.CORPORATION_ACTIVITIES: CorporationActivitiesDataset,
    SdeDatasetFiles.DEBUFF_COLLECTIONS: DebuffCollectionsDataset,
    SdeDatasetFiles.DOGMA_ATTRIBUTE_CATEGORIES: DogmaAttributeCategoriesDataset,
    SdeDatasetFiles.DOGMA_ATTRIBUTES: DogmaAttributesDataset,
    SdeDatasetFiles.DOGMA_EFFECTS: DogmaEffectsDataset,
    SdeDatasetFiles.DOGMA_UNITS: DogmaUnitsDataset,
    SdeDatasetFiles.DYNAMIC_ITEM_ATTRIBUTES: DynamicItemAttributesDataset,
    SdeDatasetFiles.FACTIONS: FactionsDataset,
    SdeDatasetFiles.FREELANCE_JOB_SCHEMAS: FreelanceJobSchemasDataset,
    SdeDatasetFiles.GRAPHICS: GraphicsDataset,
    SdeDatasetFiles.GROUPS: GroupsDataset,
    SdeDatasetFiles.ICONS: IconsDataset,
    SdeDatasetFiles.LANDMARKS: LandmarksDataset,
    SdeDatasetFiles.MAP_ASTEROID_BELTS: MapAsteroidBeltsDataset,
    SdeDatasetFiles.MAP_CONSTELLATIONS: MapConstellationsDataset,
    SdeDatasetFiles.MAP_MOONS: MapMoonsDataset,
    SdeDatasetFiles.MAP_PLANETS: MapPlanetsDataset,
    SdeDatasetFiles.MAP_REGIONS: MapRegionsDataset,
    SdeDatasetFiles.MAP_SOLAR_SYSTEMS: MapSolarSystemsDataset,
    SdeDatasetFiles.MAP_STARGATES: MapStargatesDataset,
    SdeDatasetFiles.MAP_STARS: MapStarsDataset,
    SdeDatasetFiles.MARKET_GROUPS: MarketGroupsDataset,
    SdeDatasetFiles.MASTERIES: MasteriesDataset,
    SdeDatasetFiles.META_GROUPS: MetaGroupsDataset,
    SdeDatasetFiles.MERCENARY_TACTICAL_OPERATIONS: MercenaryTacticalOperationsDataset,
    SdeDatasetFiles.NPC_CHARACTERS: NpcCharactersDataset,
    SdeDatasetFiles.NPC_CORPORATION_DIVISIONS: NpcCorporationDivisionsDataset,
    SdeDatasetFiles.NPC_CORPORATIONS: NpcCorporationsDataset,
    SdeDatasetFiles.NPC_STATIONS: NpcStationsDataset,
    SdeDatasetFiles.PLANET_RESOURCES: PlanetResourcesDataset,
    SdeDatasetFiles.PLANET_SCHEMATICS: PlanetSchematicsDataset,
    SdeDatasetFiles.RACES: RacesDataset,
    SdeDatasetFiles.SDE_INFO: SdeInfoDataset,
    SdeDatasetFiles.SKIN_LICENSES: SkinLicensesDataset,
    SdeDatasetFiles.SKIN_MATERIALS: SkinMaterialsDataset,
    SdeDatasetFiles.SKINS: SkinsDataset,
    SdeDatasetFiles.SOVEREIGNTY_UPGRADES: SovereigntyUpgradesDataset,
    SdeDatasetFiles.STATION_OPERATIONS: StationOperationsDataset,
    SdeDatasetFiles.STATION_SERVICES: StationServicesDataset,
    SdeDatasetFiles.TRANSLATION_LANGUAGES: TranslationLanguagesDataset,
    SdeDatasetFiles.TYPE_BONUS: TypeBonusDataset,
    SdeDatasetFiles.TYPE_DOGMA: TypeDogmaDataset,
    SdeDatasetFiles.TYPE_MATERIALS: TypeMaterialsDataset,
    SdeDatasetFiles.TYPES: EveTypesDataset,
}
