"""Models for localized records in the EVE Static Data Export (SDE)."""

import logging
from collections.abc import Iterable
from copy import deepcopy
from pathlib import Path
from typing import Any, Self, TypedDict

from pydantic import ValidationError

from eve_static_data.models.dataset_filenames import SdeDatasetFiles
from eve_static_data.models.pydantic import records as PM
from eve_static_data.models.type_defs import Lang

logger = logging.getLogger(__name__)


class LocalizedString(TypedDict):
    """The shape of a localized string.

    The languages are defined in the SDE file: translationLanguages.jsonl
    """

    en: str
    de: str
    fr: str
    ja: str
    zh: str
    ru: str
    ko: str
    es: str


def localize_string_dict(string_dict: LocalizedString | None, lang: Lang = "en") -> str:
    """Extract the localized string from a LocalizedString.

    Args:
        string_dict: The LocalizedString to extract from.
        lang: The language code to extract (default is "en" for English).

    Returns:
        The localized string for the specified language, OR:
        - "TRANSLATIONS_NOT_PRESENT" if the input string_dict is None (indicating that the translations are not present in the dataset).
        - "TRANSLATION_NOT_PROVIDED" if the specified language is not found in the string_dict (indicating that the translation for that language is not provided).
    """
    if string_dict is None:
        return "TRANSLATIONS_NOT_PRESENT"
    if lang not in string_dict:
        logger.warning(
            f"Localized string for '{lang=}' not found. Available languages: {list(string_dict.keys())}"
        )
        return "TRANSLATION_NOT_PROVIDED"
    return string_dict[lang]


class LocalizableRecord(PM.SdeDatasetRecord):
    """A record that can be localized to multiple languages."""

    @classmethod
    def localize_dict(cls, record: dict[str, Any], lang: Lang) -> dict[str, Any]:
        """Return a localized version of the record for the given language."""
        raise NotImplementedError("This method should be implemented by subclasses.")

    @classmethod
    def localize(cls, file_path: str | Path, lang: Lang) -> Iterable[tuple[Self, int]]:
        """Read a JSONL file and yield localized records as instances of this class."""
        for record_dict, line_number in cls.lines_as_dict(file_path):
            try:
                localized_dict = cls.localize_dict(record_dict, lang)
                localized_record = cls.model_validate(localized_dict)
                yield localized_record, line_number
            except ValidationError as e:
                logger.exception(
                    "Validation error for line %d: %s in class %s For file %s",
                    line_number,
                    e,
                    cls.__name__,
                    file_path,
                )
                raise e
            except Exception as e:
                logger.exception(
                    "Unexpected error for line %d: %s in class %s For file %s",
                    line_number,
                    e,
                    cls.__name__,
                    file_path,
                )
                raise e


class AncestriesLocalized(LocalizableRecord, PM.Ancestries):
    """Ancestries model with localized fields."""

    name: str  # type: ignore
    description: str  # type: ignore

    @classmethod
    def localize_dict(cls, record: dict[str, Any], lang: Lang) -> dict[str, Any]:
        """Return a localized version of the Ancestries record for the given language."""
        localized_dict = deepcopy(record)
        localized_dict["name"] = localize_string_dict(localized_dict.get("name"), lang)
        localized_dict["description"] = localize_string_dict(
            localized_dict.get("description"), lang
        )
        return localized_dict


class BloodlinesLocalized(LocalizableRecord, PM.Bloodlines):
    """Bloodlines model with localized fields."""

    name: str  # type: ignore
    description: str  # type: ignore

    @classmethod
    def localize_dict(cls, record: dict[str, Any], lang: Lang) -> dict[str, Any]:
        """Return a localized version of the Bloodlines record for the given language."""
        localized_dict = deepcopy(record)
        localized_dict["name"] = localize_string_dict(localized_dict.get("name"), lang)
        localized_dict["description"] = localize_string_dict(
            localized_dict.get("description"), lang
        )
        return localized_dict


class CategoriesLocalized(LocalizableRecord, PM.Categories):
    """Categories model with localized fields."""

    name: str  # type: ignore

    @classmethod
    def localize_dict(cls, record: dict[str, Any], lang: Lang) -> dict[str, Any]:
        """Return a localized version of the Categories record for the given language."""
        localized_dict = deepcopy(record)
        localized_dict["name"] = localize_string_dict(localized_dict.get("name"), lang)
        return localized_dict


class CertificatesLocalized(LocalizableRecord, PM.Certificates):
    """Certificates model with localized fields."""

    name: str  # type: ignore
    description: str  # type: ignore

    @classmethod
    def localize_dict(cls, record: dict[str, Any], lang: Lang) -> dict[str, Any]:
        """Return a localized version of the Certificates record for the given language."""
        localized_dict = deepcopy(record)
        localized_dict["name"] = localize_string_dict(localized_dict.get("name"), lang)
        localized_dict["description"] = localize_string_dict(
            localized_dict.get("description"), lang
        )
        return localized_dict


class CharacterAttributesLocalized(LocalizableRecord, PM.CharacterAttributes):
    """CharacterAttributes model with localized fields."""

    name: str  # type: ignore

    @classmethod
    def localize_dict(cls, record: dict[str, Any], lang: Lang) -> dict[str, Any]:
        """Return a localized version of the CharacterAttributes record for the given language."""
        localized_dict = deepcopy(record)
        localized_dict["name"] = localize_string_dict(localized_dict.get("name"), lang)
        return localized_dict


class CorporationActivitiesLocalized(LocalizableRecord, PM.CorporationActivities):
    """CorporationActivities model with localized fields."""

    name: str  # type: ignore

    @classmethod
    def localize_dict(cls, record: dict[str, Any], lang: Lang) -> dict[str, Any]:
        """Return a localized version of the CorporationActivities record for the given language."""
        localized_dict = deepcopy(record)
        localized_dict["name"] = localize_string_dict(localized_dict.get("name"), lang)
        return localized_dict


class DebuffCollectionsLocalized(LocalizableRecord, PM.DebuffCollections):
    """DebuffCollections model with localized fields."""

    displayName: str  # type: ignore

    @classmethod
    def localize_dict(cls, record: dict[str, Any], lang: Lang) -> dict[str, Any]:
        """Return a localized version of the DebuffCollections record for the given language."""
        localized_dict = deepcopy(record)
        localized_dict["displayName"] = localize_string_dict(
            localized_dict.get("displayName"), lang
        )
        return localized_dict


class DogmaAttributesLocalized(LocalizableRecord, PM.DogmaAttributes):
    """DogmaAttributes model with localized fields."""

    displayName: str  # type: ignore
    tooltipDescription: str  # type: ignore
    tooltipTitle: str  # type: ignore

    @classmethod
    def localize_dict(cls, record: dict[str, Any], lang: Lang) -> dict[str, Any]:
        """Return a localized version of the DogmaAttributes record for the given language."""
        localized_dict = deepcopy(record)
        localized_dict["displayName"] = localize_string_dict(
            localized_dict.get("displayName"), lang
        )
        localized_dict["tooltipDescription"] = localize_string_dict(
            localized_dict.get("tooltipDescription"), lang
        )
        localized_dict["tooltipTitle"] = localize_string_dict(
            localized_dict.get("tooltipTitle"), lang
        )
        return localized_dict


class DogmaEffectsLocalized(LocalizableRecord, PM.DogmaEffects):
    """DogmaEffects model with localized fields."""

    displayName: str  # type: ignore
    description: str  # type: ignore

    @classmethod
    def localize_dict(cls, record: dict[str, Any], lang: Lang) -> dict[str, Any]:
        """Return a localized version of the DogmaEffects record for the given language."""
        localized_dict = deepcopy(record)
        localized_dict["displayName"] = localize_string_dict(
            localized_dict.get("displayName"), lang
        )
        localized_dict["description"] = localize_string_dict(
            localized_dict.get("description"), lang
        )
        return localized_dict


class DogmaUnitsLocalized(LocalizableRecord, PM.DogmaUnits):
    """DogmaUnits model with localized fields."""

    displayName: str  # type: ignore
    description: str  # type: ignore

    @classmethod
    def localize_dict(cls, record: dict[str, Any], lang: Lang) -> dict[str, Any]:
        """Return a localized version of the DogmaUnits record for the given language."""
        localized_dict = deepcopy(record)
        localized_dict["displayName"] = localize_string_dict(
            localized_dict.get("displayName"), lang
        )
        localized_dict["description"] = localize_string_dict(
            localized_dict.get("description"), lang
        )
        return localized_dict


class FactionsLocalized(LocalizableRecord, PM.Factions):
    """Factions model with localized fields."""

    name: str  # type: ignore
    description: str  # type: ignore
    shortDescription: str  # type: ignore

    @classmethod
    def localize_dict(cls, record: dict[str, Any], lang: Lang) -> dict[str, Any]:
        """Return a localized version of the Factions record for the given language."""
        localized_dict = deepcopy(record)
        localized_dict["name"] = localize_string_dict(localized_dict.get("name"), lang)
        localized_dict["description"] = localize_string_dict(
            localized_dict.get("description"), lang
        )
        localized_dict["shortDescription"] = localize_string_dict(
            localized_dict.get("shortDescription"), lang
        )
        return localized_dict


class GroupsLocalized(LocalizableRecord, PM.Groups):
    """Groups model with localized fields."""

    name: str  # type: ignore

    @classmethod
    def localize_dict(cls, record: dict[str, Any], lang: Lang) -> dict[str, Any]:
        """Return a localized version of the Groups record for the given language."""
        localized_dict = deepcopy(record)
        localized_dict["name"] = localize_string_dict(localized_dict.get("name"), lang)
        return localized_dict


class LandmarksLocalized(LocalizableRecord, PM.Landmarks):
    """Landmarks model with localized fields."""

    name: str  # type: ignore
    description: str  # type: ignore

    @classmethod
    def localize_dict(cls, record: dict[str, Any], lang: Lang) -> dict[str, Any]:
        """Return a localized version of the Landmarks record for the given language."""
        localized_dict = deepcopy(record)
        localized_dict["name"] = localize_string_dict(localized_dict.get("name"), lang)
        localized_dict["description"] = localize_string_dict(
            localized_dict.get("description"), lang
        )
        return localized_dict


class MapAsteroidBeltsLocalized(LocalizableRecord, PM.MapAsteroidBelts):
    """MapAsteroidBelts model with localized fields."""

    uniqueName: str  # type: ignore

    @classmethod
    def localize_dict(cls, record: dict[str, Any], lang: Lang) -> dict[str, Any]:
        """Return a localized version of the MapAsteroidBelts record for the given language."""
        localized_dict = deepcopy(record)
        localized_dict["uniqueName"] = localize_string_dict(
            localized_dict.get("uniqueName"), lang
        )
        return localized_dict


class MapConstellationsLocalized(LocalizableRecord, PM.MapConstellations):
    """MapConstellations model with localized fields."""

    name: str  # type: ignore

    @classmethod
    def localize_dict(cls, record: dict[str, Any], lang: Lang) -> dict[str, Any]:
        """Return a localized version of the MapConstellations record for the given language."""
        localized_dict = deepcopy(record)
        localized_dict["name"] = localize_string_dict(localized_dict.get("name"), lang)
        return localized_dict


class MapMoonsLocalized(LocalizableRecord, PM.MapMoons):
    """MapMoons model with localized fields."""

    uniqueName: str  # type: ignore

    @classmethod
    def localize_dict(cls, record: dict[str, Any], lang: Lang) -> dict[str, Any]:
        """Return a localized version of the MapMoons record for the given language."""
        localized_dict = deepcopy(record)
        localized_dict["uniqueName"] = localize_string_dict(
            localized_dict.get("uniqueName"), lang
        )
        return localized_dict


class MapPlanetsLocalized(LocalizableRecord, PM.MapPlanets):
    """MapPlanets model with localized fields."""

    uniqueName: str  # type: ignore

    @classmethod
    def localize_dict(cls, record: dict[str, Any], lang: Lang) -> dict[str, Any]:
        """Return a localized version of the MapPlanets record for the given language."""
        localized_dict = deepcopy(record)
        localized_dict["uniqueName"] = localize_string_dict(
            localized_dict.get("uniqueName"), lang
        )
        return localized_dict


class MapRegionsLocalized(LocalizableRecord, PM.MapRegions):
    """MapRegions model with localized fields."""

    name: str  # type: ignore
    description: str  # type: ignore

    @classmethod
    def localize_dict(cls, record: dict[str, Any], lang: Lang) -> dict[str, Any]:
        """Return a localized version of the MapRegions record for the given language."""
        localized_dict = deepcopy(record)
        localized_dict["name"] = localize_string_dict(localized_dict.get("name"), lang)
        localized_dict["description"] = localize_string_dict(
            localized_dict.get("description"), lang
        )
        return localized_dict


class MapSolarSystemsLocalized(LocalizableRecord, PM.MapSolarSystems):
    """MapSolarSystems model with localized fields."""

    name: str  # type: ignore

    @classmethod
    def localize_dict(cls, record: dict[str, Any], lang: Lang) -> dict[str, Any]:
        """Return a localized version of the MapSolarSystems record for the given language."""
        localized_dict = deepcopy(record)
        localized_dict["name"] = localize_string_dict(localized_dict.get("name"), lang)
        return localized_dict


class MarketGroupsLocalized(LocalizableRecord, PM.MarketGroups):
    """MarketGroups model with localized fields."""

    name: str  # type: ignore
    description: str  # type: ignore

    @classmethod
    def localize_dict(cls, record: dict[str, Any], lang: Lang) -> dict[str, Any]:
        """Return a localized version of the MarketGroups record for the given language."""
        localized_dict = deepcopy(record)
        localized_dict["name"] = localize_string_dict(localized_dict.get("name"), lang)
        localized_dict["description"] = localize_string_dict(
            localized_dict.get("description"), lang
        )
        return localized_dict


class MetaGroupsLocalized(LocalizableRecord, PM.MetaGroups):
    """MetaGroups model with localized fields."""

    name: str  # type: ignore
    description: str  # type: ignore

    @classmethod
    def localize_dict(cls, record: dict[str, Any], lang: Lang) -> dict[str, Any]:
        """Return a localized version of the MetaGroups record for the given language."""
        localized_dict = deepcopy(record)
        localized_dict["name"] = localize_string_dict(localized_dict.get("name"), lang)
        localized_dict["description"] = localize_string_dict(
            localized_dict.get("description"), lang
        )
        return localized_dict


class NpcCharactersLocalized(LocalizableRecord, PM.NpcCharacters):
    """NpcCharacters model with localized fields."""

    name: str  # type: ignore

    @classmethod
    def localize_dict(cls, record: dict[str, Any], lang: Lang) -> dict[str, Any]:
        """Return a localized version of the NpcCharacters record for the given language."""
        localized_dict = deepcopy(record)
        localized_dict["name"] = localize_string_dict(localized_dict.get("name"), lang)
        return localized_dict


class NpcCorporationDivisionsLocalized(LocalizableRecord, PM.NpcCorporationDivisions):
    """NpcCorporationDivisions model with localized fields."""

    name: str  # type: ignore
    description: str  # type: ignore
    leaderTypeName: str  # type: ignore

    @classmethod
    def localize_dict(cls, record: dict[str, Any], lang: Lang) -> dict[str, Any]:
        """Return a localized version of the NpcCorporationDivisions record for the given language."""
        localized_dict = deepcopy(record)
        localized_dict["name"] = localize_string_dict(localized_dict.get("name"), lang)
        localized_dict["description"] = localize_string_dict(
            localized_dict.get("description"), lang
        )
        localized_dict["leaderTypeName"] = localize_string_dict(
            localized_dict.get("leaderTypeName"), lang
        )
        return localized_dict


class NpcCorporationsLocalized(LocalizableRecord, PM.NpcCorporations):
    """NpcCorporations model with localized fields."""

    name: str  # type: ignore
    description: str  # type: ignore

    @classmethod
    def localize_dict(cls, record: dict[str, Any], lang: Lang) -> dict[str, Any]:
        """Return a localized version of the NpcCorporations record for the given language."""
        localized_dict = deepcopy(record)
        localized_dict["name"] = localize_string_dict(localized_dict.get("name"), lang)
        localized_dict["description"] = localize_string_dict(
            localized_dict.get("description"), lang
        )
        return localized_dict


class PlanetSchematicsLocalized(LocalizableRecord, PM.PlanetSchematics):
    """PlanetSchematics model with localized fields."""

    name: str  # type: ignore

    @classmethod
    def localize_dict(cls, record: dict[str, Any], lang: Lang) -> dict[str, Any]:
        """Return a localized version of the PlanetSchematics record for the given language."""
        localized_dict = deepcopy(record)
        localized_dict["name"] = localize_string_dict(localized_dict.get("name"), lang)
        return localized_dict


class RacesLocalized(LocalizableRecord, PM.Races):
    """Races model with localized fields."""

    name: str  # type: ignore
    description: str  # type: ignore

    @classmethod
    def localize_dict(cls, record: dict[str, Any], lang: Lang) -> dict[str, Any]:
        """Return a localized version of the Races record for the given language."""
        localized_dict = deepcopy(record)
        localized_dict["name"] = localize_string_dict(localized_dict.get("name"), lang)
        localized_dict["description"] = localize_string_dict(
            localized_dict.get("description"), lang
        )
        return localized_dict


class SkinMaterialsLocalized(LocalizableRecord, PM.SkinMaterials):
    """SkinMaterials model with localized fields."""

    displayName: str  # type: ignore

    @classmethod
    def localize_dict(cls, record: dict[str, Any], lang: Lang) -> dict[str, Any]:
        """Return a localized version of the SkinMaterials record for the given language."""
        localized_dict = deepcopy(record)
        localized_dict["displayName"] = localize_string_dict(
            localized_dict.get("displayName"), lang
        )
        return localized_dict


class SkinsLocalized(LocalizableRecord, PM.Skins):
    """Skins model with localized fields."""

    skinDescription: str  # type: ignore

    @classmethod
    def localize_dict(cls, record: dict[str, Any], lang: Lang) -> dict[str, Any]:
        """Return a localized version of the Skins record for the given language."""
        localized_dict = deepcopy(record)
        localized_dict["skinDescription"] = localize_string_dict(
            localized_dict.get("skinDescription"), lang
        )
        return localized_dict


class StationOperationsLocalized(LocalizableRecord, PM.StationOperations):
    """StationOperations model with localized fields."""

    operationName: str  # type: ignore
    description: str  # type: ignore

    @classmethod
    def localize_dict(cls, record: dict[str, Any], lang: Lang) -> dict[str, Any]:
        """Return a localized version of the StationOperations record for the given language."""
        localized_dict = deepcopy(record)
        localized_dict["operationName"] = localize_string_dict(
            localized_dict.get("operationName"), lang
        )
        localized_dict["description"] = localize_string_dict(
            localized_dict.get("description"), lang
        )
        return localized_dict


class StationServicesLocalized(LocalizableRecord, PM.StationServices):
    """StationServices model with localized fields."""

    serviceName: str  # type: ignore
    description: str  # type: ignore

    @classmethod
    def localize_dict(cls, record: dict[str, Any], lang: Lang) -> dict[str, Any]:
        """Return a localized version of the StationServices record for the given language."""
        localized_dict = deepcopy(record)
        localized_dict["serviceName"] = localize_string_dict(
            localized_dict.get("serviceName"), lang
        )
        localized_dict["description"] = localize_string_dict(
            localized_dict.get("description"), lang
        )
        return localized_dict


# NOTE the TypeBonus model is not localized yet, because the nested classes have LocalizedStrings,
# and it's complicated to subclass that. I'll spend time on it when i need it.


class EveTypesLocalized(LocalizableRecord, PM.EveTypes):
    """EveTypes model with localized fields."""

    name: str  # type: ignore
    description: str  # type: ignore

    @classmethod
    def localize_dict(cls, record: dict[str, Any], lang: Lang) -> dict[str, Any]:
        """Return a localized version of the EveTypes record for the given language."""
        localized_dict = deepcopy(record)
        localized_dict["name"] = localize_string_dict(localized_dict.get("name"), lang)
        localized_dict["description"] = localize_string_dict(
            localized_dict.get("description"), lang
        )
        return localized_dict


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
