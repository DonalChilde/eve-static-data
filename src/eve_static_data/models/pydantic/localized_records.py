"""Models for localized records in the EVE Static Data Export (SDE)."""

from eve_static_data.models.dataset_filenames import SdeDatasetFiles
from eve_static_data.models.pydantic import records as PM
from eve_static_data.models.type_defs import Lang
from eve_static_data.transformers import LocalizationTransformer


class LocalizableRecord(PM.SdeDatasetRecord):
    """A record that can be localized to multiple languages."""

    @classmethod
    def get_transformer(cls, lang: Lang) -> LocalizationTransformer:
        """Get a transformer for this record class and the specified language."""
        raise NotImplementedError("This method should be implemented by subclasses.")


class AncestriesLocalized(LocalizableRecord, PM.Ancestries):
    """Ancestries model with localized fields."""

    name: str  # type: ignore
    description: str  # type: ignore

    @classmethod
    def get_transformer(cls, lang: Lang) -> LocalizationTransformer:
        """Get a transformer for this record class and the specified language."""
        return LocalizationTransformer(
            localized_fields=["name", "description"], lang=lang
        )


class BloodlinesLocalized(LocalizableRecord, PM.Bloodlines):
    """Bloodlines model with localized fields."""

    name: str  # type: ignore
    description: str  # type: ignore

    @classmethod
    def get_transformer(cls, lang: Lang) -> LocalizationTransformer:
        """Get a transformer for this record class and the specified language."""
        return LocalizationTransformer(
            localized_fields=["name", "description"], lang=lang
        )


class CategoriesLocalized(LocalizableRecord, PM.Categories):
    """Categories model with localized fields."""

    name: str  # type: ignore

    @classmethod
    def get_transformer(cls, lang: Lang) -> LocalizationTransformer:
        """Get a transformer for this record class and the specified language."""
        return LocalizationTransformer(localized_fields=["name"], lang=lang)


class CertificatesLocalized(LocalizableRecord, PM.Certificates):
    """Certificates model with localized fields."""

    name: str  # type: ignore
    description: str  # type: ignore

    @classmethod
    def get_transformer(cls, lang: Lang) -> LocalizationTransformer:
        """Get a transformer for this record class and the specified language."""
        return LocalizationTransformer(
            localized_fields=["name", "description"], lang=lang
        )


class CharacterAttributesLocalized(LocalizableRecord, PM.CharacterAttributes):
    """CharacterAttributes model with localized fields."""

    name: str  # type: ignore

    @classmethod
    def get_transformer(cls, lang: Lang) -> LocalizationTransformer:
        """Get a transformer for this record class and the specified language."""
        return LocalizationTransformer(localized_fields=["name"], lang=lang)


class CorporationActivitiesLocalized(LocalizableRecord, PM.CorporationActivities):
    """CorporationActivities model with localized fields."""

    name: str  # type: ignore

    @classmethod
    def get_transformer(cls, lang: Lang) -> LocalizationTransformer:
        """Get a transformer for this record class and the specified language."""
        return LocalizationTransformer(localized_fields=["name"], lang=lang)


class DebuffCollectionsLocalized(LocalizableRecord, PM.DebuffCollections):
    """DebuffCollections model with localized fields."""

    displayName: str  # type: ignore

    @classmethod
    def get_transformer(cls, lang: Lang) -> LocalizationTransformer:
        """Get a transformer for this record class and the specified language."""
        return LocalizationTransformer(localized_fields=["displayName"], lang=lang)


class DogmaAttributesLocalized(LocalizableRecord, PM.DogmaAttributes):
    """DogmaAttributes model with localized fields."""

    displayName: str  # type: ignore
    tooltipDescription: str  # type: ignore
    tooltipTitle: str  # type: ignore

    @classmethod
    def get_transformer(cls, lang: Lang) -> LocalizationTransformer:
        """Get a transformer for this record class and the specified language."""
        return LocalizationTransformer(
            localized_fields=["displayName", "tooltipDescription", "tooltipTitle"],
            lang=lang,
        )


class DogmaEffectsLocalized(LocalizableRecord, PM.DogmaEffects):
    """DogmaEffects model with localized fields."""

    displayName: str  # type: ignore
    description: str  # type: ignore

    @classmethod
    def get_transformer(cls, lang: Lang) -> LocalizationTransformer:
        """Get a transformer for this record class and the specified language."""
        return LocalizationTransformer(
            localized_fields=["displayName", "description"], lang=lang
        )


class DogmaUnitsLocalized(LocalizableRecord, PM.DogmaUnits):
    """DogmaUnits model with localized fields."""

    displayName: str  # type: ignore
    description: str  # type: ignore

    @classmethod
    def get_transformer(cls, lang: Lang) -> LocalizationTransformer:
        """Get a transformer for this record class and the specified language."""
        return LocalizationTransformer(
            localized_fields=["displayName", "description"], lang=lang
        )


class FactionsLocalized(LocalizableRecord, PM.Factions):
    """Factions model with localized fields."""

    name: str  # type: ignore
    description: str  # type: ignore
    shortDescription: str  # type: ignore

    @classmethod
    def get_transformer(cls, lang: Lang) -> LocalizationTransformer:
        """Get a transformer for this record class and the specified language."""
        return LocalizationTransformer(
            localized_fields=["name", "description", "shortDescription"], lang=lang
        )


class GroupsLocalized(LocalizableRecord, PM.Groups):
    """Groups model with localized fields."""

    name: str  # type: ignore

    @classmethod
    def get_transformer(cls, lang: Lang) -> LocalizationTransformer:
        """Get a transformer for this record class and the specified language."""
        return LocalizationTransformer(localized_fields=["name"], lang=lang)


class LandmarksLocalized(LocalizableRecord, PM.Landmarks):
    """Landmarks model with localized fields."""

    name: str  # type: ignore
    description: str  # type: ignore

    @classmethod
    def get_transformer(cls, lang: Lang) -> LocalizationTransformer:
        """Get a transformer for this record class and the specified language."""
        return LocalizationTransformer(
            localized_fields=["name", "description"], lang=lang
        )


class MapAsteroidBeltsLocalized(LocalizableRecord, PM.MapAsteroidBelts):
    """MapAsteroidBelts model with localized fields."""

    uniqueName: str  # type: ignore

    @classmethod
    def get_transformer(cls, lang: Lang) -> LocalizationTransformer:
        """Get a transformer for this record class and the specified language."""
        return LocalizationTransformer(localized_fields=["uniqueName"], lang=lang)


class MapConstellationsLocalized(LocalizableRecord, PM.MapConstellations):
    """MapConstellations model with localized fields."""

    name: str  # type: ignore

    @classmethod
    def get_transformer(cls, lang: Lang) -> LocalizationTransformer:
        """Get a transformer for this record class and the specified language."""
        return LocalizationTransformer(localized_fields=["name"], lang=lang)


class MapMoonsLocalized(LocalizableRecord, PM.MapMoons):
    """MapMoons model with localized fields."""

    uniqueName: str  # type: ignore

    @classmethod
    def get_transformer(cls, lang: Lang) -> LocalizationTransformer:
        """Get a transformer for this record class and the specified language."""
        return LocalizationTransformer(localized_fields=["uniqueName"], lang=lang)


class MapPlanetsLocalized(LocalizableRecord, PM.MapPlanets):
    """MapPlanets model with localized fields."""

    uniqueName: str  # type: ignore

    @classmethod
    def get_transformer(cls, lang: Lang) -> LocalizationTransformer:
        """Get a transformer for this record class and the specified language."""
        return LocalizationTransformer(localized_fields=["uniqueName"], lang=lang)


class MapRegionsLocalized(LocalizableRecord, PM.MapRegions):
    """MapRegions model with localized fields."""

    name: str  # type: ignore
    description: str  # type: ignore

    @classmethod
    def get_transformer(cls, lang: Lang) -> LocalizationTransformer:
        """Get a transformer for this record class and the specified language."""
        return LocalizationTransformer(
            localized_fields=["name", "description"], lang=lang
        )


class MapSolarSystemsLocalized(LocalizableRecord, PM.MapSolarSystems):
    """MapSolarSystems model with localized fields."""

    name: str  # type: ignore

    @classmethod
    def get_transformer(cls, lang: Lang) -> LocalizationTransformer:
        """Get a transformer for this record class and the specified language."""
        return LocalizationTransformer(localized_fields=["name"], lang=lang)


class MarketGroupsLocalized(LocalizableRecord, PM.MarketGroups):
    """MarketGroups model with localized fields."""

    name: str  # type: ignore
    description: str  # type: ignore

    @classmethod
    def get_transformer(cls, lang: Lang) -> LocalizationTransformer:
        """Get a transformer for this record class and the specified language."""
        return LocalizationTransformer(
            localized_fields=["name", "description"], lang=lang
        )


class MetaGroupsLocalized(LocalizableRecord, PM.MetaGroups):
    """MetaGroups model with localized fields."""

    name: str  # type: ignore
    description: str  # type: ignore

    @classmethod
    def get_transformer(cls, lang: Lang) -> LocalizationTransformer:
        """Get a transformer for this record class and the specified language."""
        return LocalizationTransformer(
            localized_fields=["name", "description"], lang=lang
        )


class NpcCharactersLocalized(LocalizableRecord, PM.NpcCharacters):
    """NpcCharacters model with localized fields."""

    name: str  # type: ignore

    @classmethod
    def get_transformer(cls, lang: Lang) -> LocalizationTransformer:
        """Get a transformer for this record class and the specified language."""
        return LocalizationTransformer(localized_fields=["name"], lang=lang)


class NpcCorporationDivisionsLocalized(LocalizableRecord, PM.NpcCorporationDivisions):
    """NpcCorporationDivisions model with localized fields."""

    name: str  # type: ignore
    description: str  # type: ignore
    leaderTypeName: str  # type: ignore

    @classmethod
    def get_transformer(cls, lang: Lang) -> LocalizationTransformer:
        """Get a transformer for this record class and the specified language."""
        return LocalizationTransformer(
            localized_fields=["name", "description", "leaderTypeName"], lang=lang
        )


class NpcCorporationsLocalized(LocalizableRecord, PM.NpcCorporations):
    """NpcCorporations model with localized fields."""

    name: str  # type: ignore
    description: str  # type: ignore

    @classmethod
    def get_transformer(cls, lang: Lang) -> LocalizationTransformer:
        """Get a transformer for this record class and the specified language."""
        return LocalizationTransformer(
            localized_fields=["name", "description"], lang=lang
        )


class PlanetSchematicsLocalized(LocalizableRecord, PM.PlanetSchematics):
    """PlanetSchematics model with localized fields."""

    name: str  # type: ignore

    @classmethod
    def get_transformer(cls, lang: Lang) -> LocalizationTransformer:
        """Get a transformer for this record class and the specified language."""
        return LocalizationTransformer(localized_fields=["name"], lang=lang)


class RacesLocalized(LocalizableRecord, PM.Races):
    """Races model with localized fields."""

    name: str  # type: ignore
    description: str  # type: ignore

    @classmethod
    def get_transformer(cls, lang: Lang) -> LocalizationTransformer:
        """Get a transformer for this record class and the specified language."""
        return LocalizationTransformer(
            localized_fields=["name", "description"], lang=lang
        )


class SkinMaterialsLocalized(LocalizableRecord, PM.SkinMaterials):
    """SkinMaterials model with localized fields."""

    displayName: str  # type: ignore

    @classmethod
    def get_transformer(cls, lang: Lang) -> LocalizationTransformer:
        """Get a transformer for this record class and the specified language."""
        return LocalizationTransformer(localized_fields=["displayName"], lang=lang)


class SkinsLocalized(LocalizableRecord, PM.Skins):
    """Skins model with localized fields."""

    skinDescription: str  # type: ignore

    @classmethod
    def get_transformer(cls, lang: Lang) -> LocalizationTransformer:
        """Get a transformer for this record class and the specified language."""
        return LocalizationTransformer(localized_fields=["skinDescription"], lang=lang)


class StationOperationsLocalized(LocalizableRecord, PM.StationOperations):
    """StationOperations model with localized fields."""

    operationName: str  # type: ignore
    description: str  # type: ignore

    @classmethod
    def get_transformer(cls, lang: Lang) -> LocalizationTransformer:
        """Get a transformer for this record class and the specified language."""
        return LocalizationTransformer(
            localized_fields=["operationName", "description"], lang=lang
        )


class StationServicesLocalized(LocalizableRecord, PM.StationServices):
    """StationServices model with localized fields."""

    serviceName: str  # type: ignore
    description: str  # type: ignore

    @classmethod
    def get_transformer(cls, lang: Lang) -> LocalizationTransformer:
        """Get a transformer for this record class and the specified language."""
        return LocalizationTransformer(
            localized_fields=["serviceName", "description"], lang=lang
        )


# NOTE the TypeBonus model is not localized yet, because the nested classes have LocalizedStrings,
# and it's complicated to subclass that. I'll spend time on it when i need it.


class EveTypesLocalized(LocalizableRecord, PM.EveTypes):
    """EveTypes model with localized fields."""

    name: str  # type: ignore
    description: str  # type: ignore

    @classmethod
    def get_transformer(cls, lang: Lang) -> LocalizationTransformer:
        """Get a transformer for this record class and the specified language."""
        return LocalizationTransformer(
            localized_fields=["name", "description"], lang=lang
        )


LOOKUP: dict[SdeDatasetFiles, type[LocalizableRecord]] = {
    SdeDatasetFiles.ANCESTRIES: AncestriesLocalized,
    SdeDatasetFiles.BLOODLINES: BloodlinesLocalized,
    SdeDatasetFiles.CATEGORIES: CategoriesLocalized,
    SdeDatasetFiles.CERTIFICATES: CertificatesLocalized,
    SdeDatasetFiles.CHARACTER_ATTRIBUTES: CharacterAttributesLocalized,
    SdeDatasetFiles.CORPORATION_ACTIVITIES: CorporationActivitiesLocalized,
    SdeDatasetFiles.DEBUFF_COLLECTIONS: DebuffCollectionsLocalized,
    SdeDatasetFiles.DOGMA_ATTRIBUTES: DogmaAttributesLocalized,
    SdeDatasetFiles.DOGMA_EFFECTS: DogmaEffectsLocalized,
    SdeDatasetFiles.DOGMA_UNITS: DogmaUnitsLocalized,
    SdeDatasetFiles.FACTIONS: FactionsLocalized,
    SdeDatasetFiles.GROUPS: GroupsLocalized,
    SdeDatasetFiles.LANDMARKS: LandmarksLocalized,
    SdeDatasetFiles.MAP_ASTEROID_BELTS: MapAsteroidBeltsLocalized,
    SdeDatasetFiles.MAP_CONSTELLATIONS: MapConstellationsLocalized,
    SdeDatasetFiles.MAP_MOONS: MapMoonsLocalized,
    SdeDatasetFiles.MAP_PLANETS: MapPlanetsLocalized,
    SdeDatasetFiles.MAP_REGIONS: MapRegionsLocalized,
    SdeDatasetFiles.MAP_SOLAR_SYSTEMS: MapSolarSystemsLocalized,
    SdeDatasetFiles.MARKET_GROUPS: MarketGroupsLocalized,
    SdeDatasetFiles.META_GROUPS: MetaGroupsLocalized,
    SdeDatasetFiles.NPC_CHARACTERS: NpcCharactersLocalized,
    SdeDatasetFiles.NPC_CORPORATION_DIVISIONS: NpcCorporationDivisionsLocalized,
    SdeDatasetFiles.NPC_CORPORATIONS: NpcCorporationsLocalized,
    SdeDatasetFiles.PLANET_SCHEMATICS: PlanetSchematicsLocalized,
    SdeDatasetFiles.SKIN_MATERIALS: SkinMaterialsLocalized,
    SdeDatasetFiles.SKINS: SkinsLocalized,
    SdeDatasetFiles.STATION_OPERATIONS: StationOperationsLocalized,
    SdeDatasetFiles.STATION_SERVICES: StationServicesLocalized,
    SdeDatasetFiles.TYPE_BONUS: EveTypesLocalized,
}
