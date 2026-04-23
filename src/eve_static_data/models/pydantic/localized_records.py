"""Models for localized records in the EVE Static Data Export (SDE)."""

from collections.abc import Iterator
from pathlib import Path

from eve_static_data.helpers.jsonl_reader import read_jsonl_file
from eve_static_data.models.common import Lang
from eve_static_data.models.dataset_filenames import SdeDatasetFiles
from eve_static_data.models.pydantic import records as PM
from eve_static_data.transformers import LocalizationTransformer


class LocalizableRecord(PM.SdeDatasetRecord):
    """A record that can be localized to multiple languages."""

    @classmethod
    def localized_fields(cls) -> set[str]:
        """Get a set of field names that should be localized."""
        raise NotImplementedError("This method should be implemented by subclasses.")


class AncestriesLocalized(LocalizableRecord, PM.Ancestries):
    """Ancestries model with localized fields."""

    name: str  # type: ignore
    description: str  # type: ignore

    @classmethod
    def localized_fields(cls) -> set[str]:
        """Get a set of field names that should be localized."""
        return {"name", "description"}


class BloodlinesLocalized(LocalizableRecord, PM.Bloodlines):
    """Bloodlines model with localized fields."""

    name: str  # type: ignore
    description: str  # type: ignore

    @classmethod
    def localized_fields(cls) -> set[str]:
        """Get a set of field names that should be localized."""
        return {"name", "description"}


class CategoriesLocalized(LocalizableRecord, PM.Categories):
    """Categories model with localized fields."""

    name: str  # type: ignore

    @classmethod
    def localized_fields(cls) -> set[str]:
        """Get a set of field names that should be localized."""
        return {"name"}


class CertificatesLocalized(LocalizableRecord, PM.Certificates):
    """Certificates model with localized fields."""

    name: str  # type: ignore
    description: str  # type: ignore

    @classmethod
    def localized_fields(cls) -> set[str]:
        """Get a set of field names that should be localized."""
        return {"name", "description"}


class CharacterAttributesLocalized(LocalizableRecord, PM.CharacterAttributes):
    """CharacterAttributes model with localized fields."""

    name: str  # type: ignore

    @classmethod
    def localized_fields(cls) -> set[str]:
        """Get a set of field names that should be localized."""
        return {"name"}


class CorporationActivitiesLocalized(LocalizableRecord, PM.CorporationActivities):
    """CorporationActivities model with localized fields."""

    name: str  # type: ignore

    @classmethod
    def localized_fields(cls) -> set[str]:
        """Get a set of field names that should be localized."""
        return {"name"}


class DebuffCollectionsLocalized(LocalizableRecord, PM.DebuffCollections):
    """DebuffCollections model with localized fields."""

    displayName: str  # type: ignore

    @classmethod
    def localized_fields(cls) -> set[str]:
        """Get a set of field names that should be localized."""
        return {"displayName"}


class DogmaAttributesLocalized(LocalizableRecord, PM.DogmaAttributes):
    """DogmaAttributes model with localized fields."""

    displayName: str  # type: ignore
    tooltipDescription: str  # type: ignore
    tooltipTitle: str  # type: ignore

    @classmethod
    def localized_fields(cls) -> set[str]:
        """Get a set of field names that should be localized."""
        return {"displayName", "tooltipDescription", "tooltipTitle"}


class DogmaEffectsLocalized(LocalizableRecord, PM.DogmaEffects):
    """DogmaEffects model with localized fields."""

    displayName: str  # type: ignore
    description: str  # type: ignore

    @classmethod
    def localized_fields(cls) -> set[str]:
        """Get a set of field names that should be localized."""
        return {"displayName", "description"}


class DogmaUnitsLocalized(LocalizableRecord, PM.DogmaUnits):
    """DogmaUnits model with localized fields."""

    displayName: str  # type: ignore
    description: str  # type: ignore

    @classmethod
    def localized_fields(cls) -> set[str]:
        """Get a set of field names that should be localized."""
        return {"displayName", "description"}


class FactionsLocalized(LocalizableRecord, PM.Factions):
    """Factions model with localized fields."""

    name: str  # type: ignore
    description: str  # type: ignore
    shortDescription: str  # type: ignore

    @classmethod
    def localized_fields(cls) -> set[str]:
        """Get a set of field names that should be localized."""
        return {"name", "description", "shortDescription"}


class GroupsLocalized(LocalizableRecord, PM.Groups):
    """Groups model with localized fields."""

    name: str  # type: ignore

    @classmethod
    def localized_fields(cls) -> set[str]:
        """Get a set of field names that should be localized."""
        return {"name"}


class LandmarksLocalized(LocalizableRecord, PM.Landmarks):
    """Landmarks model with localized fields."""

    name: str  # type: ignore
    description: str  # type: ignore

    @classmethod
    def localized_fields(cls) -> set[str]:
        """Get a set of field names that should be localized."""
        return {"name", "description"}


class MapAsteroidBeltsLocalized(LocalizableRecord, PM.MapAsteroidBelts):
    """MapAsteroidBelts model with localized fields."""

    uniqueName: str  # type: ignore

    @classmethod
    def localized_fields(cls) -> set[str]:
        """Get a set of field names that should be localized."""
        return {"uniqueName"}


class MapConstellationsLocalized(LocalizableRecord, PM.MapConstellations):
    """MapConstellations model with localized fields."""

    name: str  # type: ignore

    @classmethod
    def localized_fields(cls) -> set[str]:
        """Get a set of field names that should be localized."""
        return {"name"}


class MapMoonsLocalized(LocalizableRecord, PM.MapMoons):
    """MapMoons model with localized fields."""

    uniqueName: str  # type: ignore

    @classmethod
    def localized_fields(cls) -> set[str]:
        """Get a set of field names that should be localized."""
        return {"uniqueName"}


class MapPlanetsLocalized(LocalizableRecord, PM.MapPlanets):
    """MapPlanets model with localized fields."""

    uniqueName: str  # type: ignore

    @classmethod
    def localized_fields(cls) -> set[str]:
        """Get a set of field names that should be localized."""
        return {"uniqueName"}


class MapRegionsLocalized(LocalizableRecord, PM.MapRegions):
    """MapRegions model with localized fields."""

    name: str  # type: ignore
    description: str  # type: ignore

    @classmethod
    def localized_fields(cls) -> set[str]:
        """Get a set of field names that should be localized."""
        return {"name", "description"}


class MapSolarSystemsLocalized(LocalizableRecord, PM.MapSolarSystems):
    """MapSolarSystems model with localized fields."""

    name: str  # type: ignore

    @classmethod
    def localized_fields(cls) -> set[str]:
        """Get a set of field names that should be localized."""
        return {"name"}


class MarketGroupsLocalized(LocalizableRecord, PM.MarketGroups):
    """MarketGroups model with localized fields."""

    name: str  # type: ignore
    description: str  # type: ignore

    @classmethod
    def localized_fields(cls) -> set[str]:
        """Get a set of field names that should be localized."""
        return {"name", "description"}


class MetaGroupsLocalized(LocalizableRecord, PM.MetaGroups):
    """MetaGroups model with localized fields."""

    name: str  # type: ignore
    description: str  # type: ignore

    @classmethod
    def localized_fields(cls) -> set[str]:
        """Get a set of field names that should be localized."""
        return {"name", "description"}


class MercenaryTacticalOperationsLocalized(
    LocalizableRecord, PM.MercenaryTacticalOperations
):
    """MercenaryTacticalOperations model with localized fields."""

    name: str  # type: ignore
    description: str  # type: ignore

    @classmethod
    def localized_fields(cls) -> set[str]:
        """Get a set of field names that should be localized."""
        return {"name", "description"}


class NpcCharactersLocalized(LocalizableRecord, PM.NpcCharacters):
    """NpcCharacters model with localized fields."""

    name: str  # type: ignore

    @classmethod
    def localized_fields(cls) -> set[str]:
        """Get a set of field names that should be localized."""
        return {"name"}


class NpcCorporationDivisionsLocalized(LocalizableRecord, PM.NpcCorporationDivisions):
    """NpcCorporationDivisions model with localized fields."""

    name: str  # type: ignore
    description: str  # type: ignore
    leaderTypeName: str  # type: ignore

    @classmethod
    def localized_fields(cls) -> set[str]:
        """Get a set of field names that should be localized."""
        return {"name", "description", "leaderTypeName"}


class NpcCorporationsLocalized(LocalizableRecord, PM.NpcCorporations):
    """NpcCorporations model with localized fields."""

    name: str  # type: ignore
    description: str  # type: ignore

    @classmethod
    def localized_fields(cls) -> set[str]:
        """Get a set of field names that should be localized."""
        return {"name", "description"}


class PlanetSchematicsLocalized(LocalizableRecord, PM.PlanetSchematics):
    """PlanetSchematics model with localized fields."""

    name: str  # type: ignore

    @classmethod
    def localized_fields(cls) -> set[str]:
        """Get a set of field names that should be localized."""
        return {"name"}


class RacesLocalized(LocalizableRecord, PM.Races):
    """Races model with localized fields."""

    name: str  # type: ignore
    description: str  # type: ignore

    @classmethod
    def localized_fields(cls) -> set[str]:
        """Get a set of field names that should be localized."""
        return {"name", "description"}


class SkinMaterialsLocalized(LocalizableRecord, PM.SkinMaterials):
    """SkinMaterials model with localized fields."""

    displayName: str  # type: ignore

    @classmethod
    def localized_fields(cls) -> set[str]:
        """Get a set of field names that should be localized."""
        return {"displayName"}


class SkinsLocalized(LocalizableRecord, PM.Skins):
    """Skins model with localized fields."""

    skinDescription: str  # type: ignore

    @classmethod
    def localized_fields(cls) -> set[str]:
        """Get a set of field names that should be localized."""
        return {"skinDescription"}


class StationOperationsLocalized(LocalizableRecord, PM.StationOperations):
    """StationOperations model with localized fields."""

    operationName: str  # type: ignore
    description: str  # type: ignore

    @classmethod
    def localized_fields(cls) -> set[str]:
        """Get a set of field names that should be localized."""
        return {"operationName", "description"}


class StationServicesLocalized(LocalizableRecord, PM.StationServices):
    """StationServices model with localized fields."""

    serviceName: str  # type: ignore
    description: str  # type: ignore

    @classmethod
    def localized_fields(cls) -> set[str]:
        """Get a set of field names that should be localized."""
        return {"serviceName", "description"}


# NOTE the TypeBonus model is not localized yet, because the nested classes have LocalizedStrings,
# and it's complicated to subclass that. I'll spend time on it when i need it.


class EveTypesLocalized(LocalizableRecord, PM.EveTypes):
    """EveTypes model with localized fields."""

    name: str  # type: ignore
    description: str  # type: ignore

    @classmethod
    def localized_fields(cls) -> set[str]:
        """Get a set of field names that should be localized."""
        return {"name", "description"}


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
    SdeDatasetFiles.MERCENARY_TACTICAL_OPERATIONS: MercenaryTacticalOperationsLocalized,
    SdeDatasetFiles.NPC_CHARACTERS: NpcCharactersLocalized,
    SdeDatasetFiles.NPC_CORPORATION_DIVISIONS: NpcCorporationDivisionsLocalized,
    SdeDatasetFiles.NPC_CORPORATIONS: NpcCorporationsLocalized,
    SdeDatasetFiles.PLANET_SCHEMATICS: PlanetSchematicsLocalized,
    SdeDatasetFiles.SKIN_MATERIALS: SkinMaterialsLocalized,
    SdeDatasetFiles.SKINS: SkinsLocalized,
    SdeDatasetFiles.STATION_OPERATIONS: StationOperationsLocalized,
    SdeDatasetFiles.STATION_SERVICES: StationServicesLocalized,
    SdeDatasetFiles.TYPES: EveTypesLocalized,
}

REVERSE: dict[str, SdeDatasetFiles] = {v.__name__: k for k, v in LOOKUP.items()}


def get_model_for_dataset(dataset: SdeDatasetFiles) -> type[LocalizableRecord]:
    """Get the model class for a given dataset."""
    model = LOOKUP.get(dataset, None)
    if model is None:
        raise ValueError(f"No model found for dataset {dataset.value}")
    return model


def get_transformer[T: LocalizableRecord](
    model: type[T], lang: Lang, only_published: bool, skip_validation_failures: bool
) -> LocalizationTransformer[T]:
    """Get the transformer for a given model."""
    localizer = LocalizationTransformer(
        model=model,
        localized_fields=list(model.localized_fields()),
        lang=lang,
        only_published=only_published,
        skip_validation_failures=skip_validation_failures,
    )
    return localizer


def get_dataset_file_for_model[T: LocalizableRecord](model: type[T]) -> SdeDatasetFiles:
    """Get the dataset file for a given model."""
    dataset_file = REVERSE.get(model.__name__, None)
    if dataset_file is None:
        raise ValueError(f"No dataset file found for model {model.__name__}")
    return dataset_file


def read_records[T: LocalizableRecord](
    sde_path: Path,
    model: type[T],
    only_published: bool,
    lang: Lang,
    skip_validation_failures: bool,
) -> Iterator[tuple[int, T | None]]:
    """Read records of type T from the appropriate JSONL file in the SDE path."""
    dataset_file = get_dataset_file_for_model(model)
    transformer = get_transformer(
        model,
        lang=lang,
        only_published=only_published,
        skip_validation_failures=skip_validation_failures,
    )
    file_path = sde_path / dataset_file.as_jsonl()
    return read_jsonl_file(file_path, transformer)
