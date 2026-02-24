"""Localized pydantic models for the EVE Static Data Export (SDE).

LocalizedStrings are resolved to one language (default is English) in these models.
Optional fields that are None, and missing fields,  will be an empty string.

NOTE: The TypeBonus model is not localized yet, because the nested classes have LocalizedStrings,
and it's complicated to subclass that. I'll spend time on it when i need it.
"""

import logging
from copy import deepcopy
from typing import Any

from eve_static_data.access.sde_reader import SDERecordMetadata
from eve_static_data.models import sde_pydantic as PM
from eve_static_data.models import sde_typeddict as TDM

logger = logging.getLogger(__name__)


def localize_string_dict(
    string_dict: TDM.LocalizedString | None, localized: str = "en"
) -> str:
    """Extract the localized string from a LocalizedString.

    Args:
        string_dict: The LocalizedString to extract from.
        localized: The language code to extract (default is "en" for English).

    Returns:
        The localized string or an empty string if the language code is not found or if the input is None.
    """
    if string_dict is None:
        return ""
    if localized not in string_dict:
        logger.warning(
            f"Localized string for '{localized}' not found. Available languages: {list(string_dict.keys())}"
        )
        return ""
    return string_dict.get(localized, "")


class AncestriesLocalized(PM.Ancestries):
    """Ancestries model with localized fields."""

    name: str  # type: ignore
    description: str  # type: ignore

    @classmethod
    def from_sde(
        cls,
        record: dict[str, Any],
        metadata: SDERecordMetadata | None = None,
        localized: str = "en",
    ) -> "AncestriesLocalized":
        """Create an AncestriesLocalized instance from a SDE Ancestries.

        Args:
            record: The SDE Ancestries data.
            metadata: Optional metadata for error logging context.
            localized: The language code to extract (default is "en" for English).

        Returns:
            An AncestriesLocalized instance.
        """
        localized_dict = deepcopy(record)
        localized_dict["name"] = localize_string_dict(
            localized_dict.get("name"), localized
        )
        localized_dict["description"] = localize_string_dict(
            localized_dict.get("description"), localized
        )
        return PM.log_validation(cls, localized_dict, metadata)


class BloodlinesLocalized(PM.Bloodlines):
    """Bloodlines model with localized fields."""

    name: str  # type: ignore
    description: str  # type: ignore

    @classmethod
    def from_sde(
        cls,
        record: dict[str, Any],
        metadata: SDERecordMetadata | None = None,
        localized: str = "en",
    ) -> "BloodlinesLocalized":
        """Create a BloodlinesLocalized instance from a SDE Bloodlines.

        Args:
            record: The SDE Bloodlines data.
            metadata: Optional metadata for error logging context.
            localized: The language code to extract (default is "en" for English).

        Returns:
            A BloodlinesLocalized instance.
        """
        localized_dict = deepcopy(record)
        localized_dict["name"] = localize_string_dict(
            localized_dict.get("name"), localized
        )
        localized_dict["description"] = localize_string_dict(
            localized_dict.get("description"), localized
        )
        return PM.log_validation(cls, localized_dict, metadata)


class CategoriesLocalized(PM.Categories):
    """Categories model with localized fields."""

    name: str  # type: ignore

    @classmethod
    def from_sde(
        cls,
        record: dict[str, Any],
        metadata: SDERecordMetadata | None = None,
        localized: str = "en",
    ) -> "CategoriesLocalized":
        """Create a CategoriesLocalized instance from a SDE Categories.

        Args:
            record: The SDE Categories data.
            metadata: Optional metadata for error logging context.
            localized: The language code to extract (default is "en" for English).

        Returns:
            A CategoriesLocalized instance.
        """
        localized_dict = deepcopy(record)
        localized_dict["name"] = localize_string_dict(
            localized_dict.get("name"), localized
        )
        return PM.log_validation(cls, localized_dict, metadata)


class CertificatesLocalized(PM.Certificates):
    """Certificates model with localized fields."""

    name: str  # type: ignore
    description: str  # type: ignore

    @classmethod
    def from_sde(
        cls,
        record: dict[str, Any],
        metadata: SDERecordMetadata | None = None,
        localized: str = "en",
    ) -> "CertificatesLocalized":
        """Create a CertificatesLocalized instance from a SDE Certificates.

        Args:
            record: The SDE Certificates data.
            metadata: Optional metadata for error logging context.
            localized: The language code to extract (default is "en" for English).

        Returns:
            A CertificatesLocalized instance.
        """
        localized_dict = deepcopy(record)
        localized_dict["name"] = localize_string_dict(
            localized_dict.get("name"), localized
        )
        localized_dict["description"] = localize_string_dict(
            localized_dict.get("description"), localized
        )
        return PM.log_validation(cls, localized_dict, metadata)


class CharacterAttributesLocalized(PM.CharacterAttributes):
    """CharacterAttributes model with localized fields."""

    name: str  # type: ignore

    @classmethod
    def from_sde(
        cls,
        record: dict[str, Any],
        metadata: SDERecordMetadata | None = None,
        localized: str = "en",
    ) -> "CharacterAttributesLocalized":
        """Create a CharacterAttributesLocalized instance from a SDE CharacterAttributes.

        Args:
            record: The SDE CharacterAttributes data.
            metadata: Optional metadata for error logging context.
            localized: The language code to extract (default is "en" for English).

        Returns:
            A CharacterAttributesLocalized instance.
        """
        localized_dict = deepcopy(record)
        localized_dict["name"] = localize_string_dict(
            localized_dict.get("name"), localized
        )
        return PM.log_validation(cls, localized_dict, metadata)


class CorporationActivitiesLocalized(PM.CorporationActivities):
    """CorporationActivities model with localized fields."""

    name: str  # type: ignore

    @classmethod
    def from_sde(
        cls,
        record: dict[str, Any],
        metadata: SDERecordMetadata | None = None,
        localized: str = "en",
    ) -> "CorporationActivitiesLocalized":
        """Create a CorporationActivitiesLocalized instance from a SDE CorporationActivities.

        Args:
            record: The SDE CorporationActivities data.
            metadata: Optional metadata for error logging context.
            localized: The language code to extract (default is "en" for English).

        Returns:
            A CorporationActivitiesLocalized instance.
        """
        localized_dict = deepcopy(record)
        localized_dict["name"] = localize_string_dict(
            localized_dict.get("name"), localized
        )
        return PM.log_validation(cls, localized_dict, metadata)


class DebuffCollectionsLocalized(PM.DebuffCollections):
    """DebuffCollections model with localized fields."""

    displayName: str  # type: ignore

    @classmethod
    def from_sde(
        cls,
        record: dict[str, Any],
        metadata: SDERecordMetadata | None = None,
        localized: str = "en",
    ) -> "DebuffCollectionsLocalized":
        """Create a DebuffCollectionsLocalized instance from a SDE DebuffCollections.

        Args:
            record: The SDE DebuffCollections data.
            metadata: Optional metadata for error logging context.
            localized: The language code to extract (default is "en" for English).

        Returns:
            A DebuffCollectionsLocalized instance.
        """
        localized_dict = deepcopy(record)
        localized_dict["displayName"] = localize_string_dict(
            localized_dict.get("displayName"), localized
        )
        return PM.log_validation(cls, localized_dict, metadata)


class DogmaAttributesLocalized(PM.DogmaAttributes):
    """DogmaAttributes model with localized fields."""

    displayName: str  # type: ignore
    tooltipDescription: str  # type: ignore
    tooltipTitle: str  # type: ignore

    @classmethod
    def from_sde(
        cls,
        record: dict[str, Any],
        metadata: SDERecordMetadata | None = None,
        localized: str = "en",
    ) -> "DogmaAttributesLocalized":
        """Create a DogmaAttributesLocalized instance from a SDE DogmaAttributes.

        Args:
            record: The SDE DogmaAttributes data.
            metadata: Optional metadata for error logging context.
            localized: The language code to extract (default is "en" for English).

        Returns:
            A DogmaAttributesLocalized instance.
        """
        localized_dict = deepcopy(record)
        localized_dict["displayName"] = localize_string_dict(
            localized_dict.get("displayName"), localized
        )
        localized_dict["tooltipDescription"] = localize_string_dict(
            localized_dict.get("tooltipDescription"), localized
        )
        localized_dict["tooltipTitle"] = localize_string_dict(
            localized_dict.get("tooltipTitle"), localized
        )
        return PM.log_validation(cls, localized_dict, metadata)


class DogmaEffectsLocalized(PM.DogmaEffects):
    """DogmaEffects model with localized fields."""

    displayName: str  # type: ignore
    description: str  # type: ignore

    @classmethod
    def from_sde(
        cls,
        record: dict[str, Any],
        metadata: SDERecordMetadata | None = None,
        localized: str = "en",
    ) -> "DogmaEffectsLocalized":
        """Create a DogmaEffectsLocalized instance from a SDE DogmaEffects.

        Args:
            record: The SDE DogmaEffects data.
            metadata: Optional metadata for error logging context.
            localized: The language code to extract (default is "en" for English).

        Returns:
            A DogmaEffectsLocalized instance.
        """
        localized_dict = deepcopy(record)
        localized_dict["displayName"] = localize_string_dict(
            localized_dict.get("displayName"), localized
        )
        localized_dict["description"] = localize_string_dict(
            localized_dict.get("description"), localized
        )
        return PM.log_validation(cls, localized_dict, metadata)


class DogmaUnitsLocalized(PM.DogmaUnits):
    """DogmaUnits model with localized fields."""

    displayName: str  # type: ignore
    description: str  # type: ignore

    @classmethod
    def from_sde(
        cls,
        record: dict[str, Any],
        metadata: SDERecordMetadata | None = None,
        localized: str = "en",
    ) -> "DogmaUnitsLocalized":
        """Create a DogmaUnitsLocalized instance from a SDE DogmaUnits.

        Args:
            record: The SDE DogmaUnits data.
            metadata: Optional metadata for error logging context.
            localized: The language code to extract (default is "en" for English).

        Returns:
            A DogmaUnitsLocalized instance.
        """
        localized_dict = deepcopy(record)
        localized_dict["displayName"] = localize_string_dict(
            localized_dict.get("displayName"), localized
        )
        localized_dict["description"] = localize_string_dict(
            localized_dict.get("description"), localized
        )
        return PM.log_validation(cls, localized_dict, metadata)


class FactionsLocalized(PM.Factions):
    """Factions model with localized fields."""

    name: str  # type: ignore
    description: str  # type: ignore
    shortDescription: str  # type: ignore

    @classmethod
    def from_sde(
        cls,
        record: dict[str, Any],
        metadata: SDERecordMetadata | None = None,
        localized: str = "en",
    ) -> "FactionsLocalized":
        """Create a FactionsLocalized instance from a SDE Factions.

        Args:
            record: The SDE Factions data.
            metadata: Optional metadata for error logging context.
            localized: The language code to extract (default is "en" for English).

        Returns:
            A FactionsLocalized instance.
        """
        localized_dict = deepcopy(record)
        localized_dict["name"] = localize_string_dict(
            localized_dict.get("name"), localized
        )
        localized_dict["description"] = localize_string_dict(
            localized_dict.get("description"), localized
        )
        localized_dict["shortDescription"] = localize_string_dict(
            localized_dict.get("shortDescription"), localized
        )
        return PM.log_validation(cls, localized_dict, metadata)


class GroupsLocalized(PM.Groups):
    """Groups model with localized fields."""

    name: str  # type: ignore

    @classmethod
    def from_sde(
        cls,
        record: dict[str, Any],
        metadata: SDERecordMetadata | None = None,
        localized: str = "en",
    ) -> "GroupsLocalized":
        """Create a GroupsLocalized instance from a SDE Groups.

        Args:
            record: The SDE Groups data.
            metadata: Optional metadata for error logging context.
            localized: The language code to extract (default is "en" for English).

        Returns:
            A GroupsLocalized instance.
        """
        localized_dict = deepcopy(record)
        localized_dict["name"] = localize_string_dict(
            localized_dict.get("name"), localized
        )
        return PM.log_validation(cls, localized_dict, metadata)


class LandmarksLocalized(PM.Landmarks):
    """Landmarks model with localized fields."""

    name: str  # type: ignore
    description: str  # type: ignore

    @classmethod
    def from_sde(
        cls,
        record: dict[str, Any],
        metadata: SDERecordMetadata | None = None,
        localized: str = "en",
    ) -> "LandmarksLocalized":
        """Create a LandmarksLocalized instance from a SDE Landmarks.

        Args:
            record: The SDE Landmarks data.
            metadata: Optional metadata for error logging context.
            localized: The language code to extract (default is "en" for English).

        Returns:
            A LandmarksLocalized instance.
        """
        localized_dict = deepcopy(record)
        localized_dict["name"] = localize_string_dict(
            localized_dict.get("name"), localized
        )
        localized_dict["description"] = localize_string_dict(
            localized_dict.get("description"), localized
        )
        return PM.log_validation(cls, localized_dict, metadata)


class MapAsteroidBeltsLocalized(PM.MapAsteroidBelts):
    """MapAsteroidBelts model with localized fields."""

    uniqueName: str  # type: ignore

    @classmethod
    def from_sde(
        cls,
        record: dict[str, Any],
        metadata: SDERecordMetadata | None = None,
        localized: str = "en",
    ) -> "MapAsteroidBeltsLocalized":
        """Create a MapAsteroidBeltsLocalized instance from a SDE MapAsteroidBelts.

        Args:
            record: The SDE MapAsteroidBelts data.
            metadata: Optional metadata for error logging context.
            localized: The language code to extract (default is "en" for English).

        Returns:
            A MapAsteroidBeltsLocalized instance.
        """
        localized_dict = deepcopy(record)
        localized_dict["uniqueName"] = localize_string_dict(
            localized_dict.get("uniqueName"), localized
        )
        return PM.log_validation(cls, localized_dict, metadata)


class MapConstellationsLocalized(PM.MapConstellations):
    """MapConstellations model with localized fields."""

    name: str  # type: ignore

    @classmethod
    def from_sde(
        cls,
        record: dict[str, Any],
        metadata: SDERecordMetadata | None = None,
        localized: str = "en",
    ) -> "MapConstellationsLocalized":
        """Create a MapConstellationsLocalized instance from a SDE MapConstellations.

        Args:
            record: The SDE MapConstellations data.
            metadata: Optional metadata for error logging context.
            localized: The language code to extract (default is "en" for English).

        Returns:
            A MapConstellationsLocalized instance.
        """
        localized_dict = deepcopy(record)
        localized_dict["name"] = localize_string_dict(
            localized_dict.get("name"), localized
        )
        return PM.log_validation(cls, localized_dict, metadata)


class MapMoonsLocalized(PM.MapMoons):
    """MapMoons model with localized fields."""

    uniqueName: str  # type: ignore

    @classmethod
    def from_sde(
        cls,
        record: dict[str, Any],
        metadata: SDERecordMetadata | None = None,
        localized: str = "en",
    ) -> "MapMoonsLocalized":
        """Create a MapMoonsLocalized instance from a SDE MapMoons.

        Args:
            record: The SDE MapMoons data.
            metadata: Optional metadata for error logging context.
            localized: The language code to extract (default is "en" for English).

        Returns:
            A MapMoonsLocalized instance.
        """
        localized_dict = deepcopy(record)
        localized_dict["uniqueName"] = localize_string_dict(
            localized_dict.get("uniqueName"), localized
        )
        return PM.log_validation(cls, localized_dict, metadata)


class MapPlanetsLocalized(PM.MapPlanets):
    """MapPlanets model with localized fields."""

    uniqueName: str  # type: ignore

    @classmethod
    def from_sde(
        cls,
        record: dict[str, Any],
        metadata: SDERecordMetadata | None = None,
        localized: str = "en",
    ) -> "MapPlanetsLocalized":
        """Create a MapPlanetsLocalized instance from a SDE MapPlanets.

        Args:
            record: The SDE MapPlanets data.
            metadata: Optional metadata for error logging context.
            localized: The language code to extract (default is "en" for English).

        Returns:
            A MapPlanetsLocalized instance.
        """
        localized_dict = deepcopy(record)
        localized_dict["uniqueName"] = localize_string_dict(
            localized_dict.get("uniqueName"), localized
        )
        return PM.log_validation(cls, localized_dict, metadata)


class MapRegionsLocalized(PM.MapRegions):
    """MapRegions model with localized fields."""

    name: str  # type: ignore
    description: str  # type: ignore

    @classmethod
    def from_sde(
        cls,
        record: dict[str, Any],
        metadata: SDERecordMetadata | None = None,
        localized: str = "en",
    ) -> "MapRegionsLocalized":
        """Create a MapRegionsLocalized instance from a SDE MapRegions.

        Args:
            record: The SDE MapRegions data.
            metadata: Optional metadata for error logging context.
            localized: The language code to extract (default is "en" for English).

        Returns:
            A MapRegionsLocalized instance.
        """
        localized_dict = deepcopy(record)
        localized_dict["name"] = localize_string_dict(
            localized_dict.get("name"), localized
        )
        localized_dict["description"] = localize_string_dict(
            localized_dict.get("description"), localized
        )
        return PM.log_validation(cls, localized_dict, metadata)


class MapSolarSystemsLocalized(PM.MapSolarSystems):
    """MapSolarSystems model with localized fields."""

    name: str  # type: ignore

    @classmethod
    def from_sde(
        cls,
        record: dict[str, Any],
        metadata: SDERecordMetadata | None = None,
        localized: str = "en",
    ) -> "MapSolarSystemsLocalized":
        """Create a MapSolarSystemsLocalized instance from a SDE MapSolarSystems.

        Args:
            record: The SDE MapSolarSystems data.
            metadata: Optional metadata for error logging context.
            localized: The language code to extract (default is "en" for English).

        Returns:
            A MapSolarSystemsLocalized instance.
        """
        localized_dict = deepcopy(record)
        localized_dict["name"] = localize_string_dict(
            localized_dict.get("name"), localized
        )
        return PM.log_validation(cls, localized_dict, metadata)


class MarketGroupsLocalized(PM.MarketGroups):
    """MarketGroups model with localized fields."""

    name: str  # type: ignore
    description: str  # type: ignore

    @classmethod
    def from_sde(
        cls,
        record: dict[str, Any],
        metadata: SDERecordMetadata | None = None,
        localized: str = "en",
    ) -> "MarketGroupsLocalized":
        """Create a MarketGroupsLocalized instance from a SDE MarketGroups.

        Args:
            record: The SDE MarketGroups data.
            metadata: Optional metadata for error logging context.
            localized: The language code to extract (default is "en" for English).

        Returns:
            A MarketGroupsLocalized instance.
        """
        localized_dict = deepcopy(record)
        localized_dict["name"] = localize_string_dict(
            localized_dict.get("name"), localized
        )
        localized_dict["description"] = localize_string_dict(
            localized_dict.get("description"), localized
        )
        return PM.log_validation(cls, localized_dict, metadata)


class MetaGroupsLocalized(PM.MetaGroups):
    """MetaGroups model with localized fields."""

    name: str  # type: ignore
    description: str  # type: ignore

    @classmethod
    def from_sde(
        cls,
        record: dict[str, Any],
        metadata: SDERecordMetadata | None = None,
        localized: str = "en",
    ) -> "MetaGroupsLocalized":
        """Create a MetaGroupsLocalized instance from a SDE MetaGroups.

        Args:
            record: The SDE MetaGroups data.
            metadata: Optional metadata for error logging context.
            localized: The language code to extract (default is "en" for English).

        Returns:
            A MetaGroupsLocalized instance.
        """
        localized_dict = deepcopy(record)
        localized_dict["name"] = localize_string_dict(
            localized_dict.get("name"), localized
        )
        localized_dict["description"] = localize_string_dict(
            localized_dict.get("description"), localized
        )
        return PM.log_validation(cls, localized_dict, metadata)


class NpcCharactersLocalized(PM.NpcCharacters):
    """NpcCharacters model with localized fields."""

    name: str  # type: ignore

    @classmethod
    def from_sde(
        cls,
        record: dict[str, Any],
        metadata: SDERecordMetadata | None = None,
        localized: str = "en",
    ) -> "NpcCharactersLocalized":
        """Create a NpcCharactersLocalized instance from a SDE NpcCharacters.

        Args:
            record: The SDE NpcCharacters data.
            metadata: Optional metadata for error logging context.
            localized: The language code to extract (default is "en" for English).

        Returns:
            A NpcCharactersLocalized instance.
        """
        localized_dict = deepcopy(record)
        localized_dict["name"] = localize_string_dict(
            localized_dict.get("name"), localized
        )
        return PM.log_validation(cls, localized_dict, metadata)


class NpcCorporationDivisionsLocalized(PM.NpcCorporationDivisions):
    """NpcCorporationDivisions model with localized fields."""

    name: str  # type: ignore
    description: str  # type: ignore
    leaderTypeName: str  # type: ignore

    @classmethod
    def from_sde(
        cls,
        record: dict[str, Any],
        metadata: SDERecordMetadata | None = None,
        localized: str = "en",
    ) -> "NpcCorporationDivisionsLocalized":
        """Create a NpcCorporationDivisionsLocalized instance from a SDE NpcCorporationDivisions.

        Args:
            record: The SDE NpcCorporationDivisions data.
            metadata: Optional metadata for error logging context.
            localized: The language code to extract (default is "en" for English).

        Returns:
            A NpcCorporationDivisionsLocalized instance.
        """
        localized_dict = deepcopy(record)
        localized_dict["name"] = localize_string_dict(
            localized_dict.get("name"), localized
        )
        localized_dict["description"] = localize_string_dict(
            localized_dict.get("description"), localized
        )
        localized_dict["leaderTypeName"] = localize_string_dict(
            localized_dict.get("leaderTypeName"), localized
        )
        return PM.log_validation(cls, localized_dict, metadata)


class NpcCorporationsLocalized(PM.NpcCorporations):
    """NpcCorporations model with localized fields."""

    name: str  # type: ignore
    description: str  # type: ignore

    @classmethod
    def from_sde(
        cls,
        record: dict[str, Any],
        metadata: SDERecordMetadata | None = None,
        localized: str = "en",
    ) -> "NpcCorporationsLocalized":
        """Create a NpcCorporationsLocalized instance from a SDE NpcCorporations.

        Args:
            record: The SDE NpcCorporations data.
            metadata: Optional metadata for error logging context.
            localized: The language code to extract (default is "en" for English).

        Returns:
            A NpcCorporationsLocalized instance.
        """
        localized_dict = deepcopy(record)
        localized_dict["name"] = localize_string_dict(
            localized_dict.get("name"), localized
        )
        localized_dict["description"] = localize_string_dict(
            localized_dict.get("description"), localized
        )
        return PM.log_validation(cls, localized_dict, metadata)


class PlanetSchematicsLocalized(PM.PlanetSchematics):
    """PlanetSchematics model with localized fields."""

    name: str  # type: ignore

    @classmethod
    def from_sde(
        cls,
        record: dict[str, Any],
        metadata: SDERecordMetadata | None = None,
        localized: str = "en",
    ) -> "PlanetSchematicsLocalized":
        """Create a PlanetSchematicsLocalized instance from a SDE PlanetSchematics.

        Args:
            record: The SDE PlanetSchematics data.
            metadata: Optional metadata for error logging context.
            localized: The language code to extract (default is "en" for English).

        Returns:
            A PlanetSchematicsLocalized instance.
        """
        localized_dict = deepcopy(record)
        localized_dict["name"] = localize_string_dict(
            localized_dict.get("name"), localized
        )
        return PM.log_validation(cls, localized_dict, metadata)


class RacesLocalized(PM.Races):
    """Races model with localized fields."""

    name: str  # type: ignore
    description: str  # type: ignore

    @classmethod
    def from_sde(
        cls,
        record: dict[str, Any],
        metadata: SDERecordMetadata | None = None,
        localized: str = "en",
    ) -> "RacesLocalized":
        """Create a RacesLocalized instance from a SDE Races.

        Args:
            record: The SDE Races data.
            metadata: Optional metadata for error logging context.
            localized: The language code to extract (default is "en" for English).

        Returns:
            A RacesLocalized instance.
        """
        localized_dict = deepcopy(record)
        localized_dict["name"] = localize_string_dict(
            localized_dict.get("name"), localized
        )
        localized_dict["description"] = localize_string_dict(
            localized_dict.get("description"), localized
        )
        return PM.log_validation(cls, localized_dict, metadata)


class SkinMaterialsLocalized(PM.SkinMaterials):
    """SkinMaterials model with localized fields."""

    displayName: str  # type: ignore

    @classmethod
    def from_sde(
        cls,
        record: dict[str, Any],
        metadata: SDERecordMetadata | None = None,
        localized: str = "en",
    ) -> "SkinMaterialsLocalized":
        """Create a SkinMaterialsLocalized instance from a SDE SkinMaterials.

        Args:
            record: The SDE SkinMaterials data.
            metadata: Optional metadata for error logging context.
            localized: The language code to extract (default is "en" for English).

        Returns:
            A SkinMaterialsLocalized instance.
        """
        localized_dict = deepcopy(record)
        localized_dict["displayName"] = localize_string_dict(
            localized_dict.get("displayName"), localized
        )
        return PM.log_validation(cls, localized_dict, metadata)


class SkinsLocalized(PM.Skins):
    """Skins model with localized fields."""

    skinDescription: str  # type: ignore

    @classmethod
    def from_sde(
        cls,
        record: dict[str, Any],
        metadata: SDERecordMetadata | None = None,
        localized: str = "en",
    ) -> "SkinsLocalized":
        """Create a SkinsLocalized instance from a SDE Skins.

        Args:
            record: The SDE Skins data.
            metadata: Optional metadata for error logging context.
            localized: The language code to extract (default is "en" for English).

        Returns:
            A SkinsLocalized instance.
        """
        localized_dict = deepcopy(record)
        localized_dict["skinDescription"] = localize_string_dict(
            localized_dict.get("skinDescription"), localized
        )
        return PM.log_validation(cls, localized_dict, metadata)


class StationOperationsLocalized(PM.StationOperations):
    """StationOperations model with localized fields."""

    operationName: str  # type: ignore
    description: str  # type: ignore

    @classmethod
    def from_sde(
        cls,
        record: dict[str, Any],
        metadata: SDERecordMetadata | None = None,
        localized: str = "en",
    ) -> "StationOperationsLocalized":
        """Create a StationOperationsLocalized instance from a SDE StationOperations.

        Args:
            record: The SDE StationOperations data.
            metadata: Optional metadata for error logging context.
            localized: The language code to extract (default is "en" for English).

        Returns:
            A StationOperationsLocalized instance.
        """
        localized_dict = deepcopy(record)
        localized_dict["operationName"] = localize_string_dict(
            localized_dict.get("operationName"), localized
        )
        localized_dict["description"] = localize_string_dict(
            localized_dict.get("description"), localized
        )
        return PM.log_validation(cls, localized_dict, metadata)


class StationServicesLocalized(PM.StationServices):
    """StationServices model with localized fields."""

    serviceName: str  # type: ignore
    description: str  # type: ignore

    @classmethod
    def from_sde(
        cls,
        record: dict[str, Any],
        metadata: SDERecordMetadata | None = None,
        localized: str = "en",
    ) -> "StationServicesLocalized":
        """Create a StationServicesLocalized instance from a SDE StationServices.

        Args:
            record: The SDE StationServices data.
            metadata: Optional metadata for error logging context.
            localized: The language code to extract (default is "en" for English).

        Returns:
            A StationServicesLocalized instance.
        """
        localized_dict = deepcopy(record)
        localized_dict["serviceName"] = localize_string_dict(
            localized_dict.get("serviceName"), localized
        )
        localized_dict["description"] = localize_string_dict(
            localized_dict.get("description"), localized
        )
        return PM.log_validation(cls, localized_dict, metadata)


# NOTE the TypeBonus model is not localized yet, because the nested classes have LocalizedStrings,
# and it's complicated to subclass that. I'll spend time on it when i need it.


class EveTypesLocalized(PM.EveTypes):
    """EveTypes model with localized fields."""

    name: str  # type: ignore
    description: str  # type: ignore

    @classmethod
    def from_sde(
        cls,
        record: dict[str, Any],
        metadata: SDERecordMetadata | None = None,
        localized: str = "en",
    ) -> "EveTypesLocalized":
        """Create an EveTypesLocalized instance from a SDE EveTypes.

        Args:
            record: The SDE EveTypes data.
            metadata: Optional metadata for error logging context.
            localized: The language code to extract (default is "en" for English).

        Returns:
            An EveTypesLocalized instance.
        """
        localized_dict = deepcopy(record)
        localized_dict["name"] = localize_string_dict(
            localized_dict.get("name"), localized
        )
        localized_dict["description"] = localize_string_dict(
            localized_dict.get("description"), localized
        )
        return PM.log_validation(cls, localized_dict, metadata)
