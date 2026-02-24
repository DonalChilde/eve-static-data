"""Factory methods for creating Pydantic models from SDE records.

model_validate errors are logged with dataset and record information before being raised,
to aid in debugging data issues.
"""

import logging
from collections.abc import Iterable

from eve_static_data.access.sde_reader import SdeReader
from eve_static_data.models import sde_pydantic as PM
from eve_static_data.models.sde_dataset_files import SdeDatasetFiles

logger = logging.getLogger(__name__)


def agents_in_space(
    reader: SdeReader, file_name: str | None = None
) -> Iterable[PM.AgentsInSpace]:
    """Records from the agentsInSpace.jsonl dataset."""
    for item, metadata in reader.records(SdeDatasetFiles.AGENTS_IN_SPACE, file_name):
        yield PM.AgentsInSpace.from_sde(item, metadata)


def agent_types(
    reader: SdeReader, file_name: str | None = None
) -> Iterable[PM.AgentTypes]:
    """Records from the agentTypes.jsonl dataset."""
    for item in reader.records(SdeDatasetFiles.AGENT_TYPES, file_name):
        yield PM.AgentTypes.model_validate(item)


def ancestries(
    reader: SdeReader, file_name: str | None = None
) -> Iterable[PM.Ancestries]:
    """Records from the ancestries.jsonl dataset."""
    for item in reader.records(SdeDatasetFiles.ANCESTRIES, file_name):
        yield PM.Ancestries.model_validate(item)


def bloodlines(
    reader: SdeReader, file_name: str | None = None
) -> Iterable[PM.Bloodlines]:
    """Records from the bloodlines.jsonl dataset."""
    for item in reader.records(SdeDatasetFiles.BLOODLINES, file_name):
        yield PM.Bloodlines.model_validate(item)


def blueprints(
    reader: SdeReader, file_name: str | None = None
) -> Iterable[PM.Blueprints]:
    """Records from the blueprints.jsonl dataset."""
    for item in reader.records(SdeDatasetFiles.BLUEPRINTS, file_name):
        yield PM.Blueprints.model_validate(item)


def categories(
    reader: SdeReader, file_name: str | None = None
) -> Iterable[PM.Categories]:
    """Records from the categories.jsonl dataset."""
    for item in reader.records(SdeDatasetFiles.CATEGORIES, file_name):
        yield PM.Categories.model_validate(item)


def certificates(
    reader: SdeReader, file_name: str | None = None
) -> Iterable[PM.Certificates]:
    """Records from the certificates.jsonl dataset."""
    for item in reader.records(SdeDatasetFiles.CERTIFICATES, file_name):
        yield PM.Certificates.model_validate(item)


def character_attributes(
    reader: SdeReader, file_name: str | None = None
) -> Iterable[PM.CharacterAttributes]:
    """Records from the characterAttributes.jsonl dataset."""
    for item in reader.records(SdeDatasetFiles.CHARACTER_ATTRIBUTES, file_name):
        yield PM.CharacterAttributes.model_validate(item)


def clone_grades(
    reader: SdeReader, file_name: str | None = None
) -> Iterable[PM.CloneGrades]:
    """Records from the cloneGrades.jsonl dataset."""
    for item in reader.records(SdeDatasetFiles.CLONE_GRADES, file_name):
        yield PM.CloneGrades.model_validate(item)


def compressible_types(
    reader: SdeReader, file_name: str | None = None
) -> Iterable[PM.CompressibleTypes]:
    """Records from the compressibleTypes.jsonl dataset."""
    for item in reader.records(SdeDatasetFiles.COMPRESSIBLE_TYPES, file_name):
        yield PM.CompressibleTypes.model_validate(item)


def contraband_types(
    reader: SdeReader, file_name: str | None = None
) -> Iterable[PM.ContrabandTypes]:
    """Records from the contrabandTypes.jsonl dataset."""
    for item in reader.records(SdeDatasetFiles.CONTRABAND_TYPES, file_name):
        yield PM.ContrabandTypes.model_validate(item)


def control_tower_resources(
    reader: SdeReader, file_name: str | None = None
) -> Iterable[PM.ControlTowerResources]:
    """Records from the controlTowerResources.jsonl dataset."""
    for item in reader.records(SdeDatasetFiles.CONTROL_TOWER_RESOURCES, file_name):
        yield PM.ControlTowerResources.model_validate(item)


def corporation_activities(
    reader: SdeReader, file_name: str | None = None
) -> Iterable[PM.CorporationActivities]:
    """Records from the corporationActivities.jsonl dataset."""
    for item in reader.records(SdeDatasetFiles.CORPORATION_ACTIVITIES, file_name):
        yield PM.CorporationActivities.model_validate(item)


def debuff_collections(
    reader: SdeReader, file_name: str | None = None
) -> Iterable[PM.DebuffCollections]:
    """Records from the dbuffCollections.jsonl dataset."""
    for item in reader.records(SdeDatasetFiles.DEBUFF_COLLECTIONS, file_name):
        yield PM.DebuffCollections.model_validate(item)


def dogma_attribute_categories(
    reader: SdeReader, file_name: str | None = None
) -> Iterable[PM.DogmaAttributeCategories]:
    """Records from the dogmaAttributeCategories.jsonl dataset."""
    for item in reader.records(SdeDatasetFiles.DOGMA_ATTRIBUTE_CATEGORIES, file_name):
        yield PM.DogmaAttributeCategories.model_validate(item)


def dogma_attributes(
    reader: SdeReader, file_name: str | None = None
) -> Iterable[PM.DogmaAttributes]:
    """Records from the dogmaAttributes.jsonl dataset."""
    for item in reader.records(SdeDatasetFiles.DOGMA_ATTRIBUTES, file_name):
        yield PM.DogmaAttributes.model_validate(item)


def dogma_effects(
    reader: SdeReader, file_name: str | None = None
) -> Iterable[PM.DogmaEffects]:
    """Records from the dogmaEffects.jsonl dataset."""
    for item in reader.records(SdeDatasetFiles.DOGMA_EFFECTS, file_name):
        yield PM.DogmaEffects.model_validate(item)


def dogma_units(
    reader: SdeReader, file_name: str | None = None
) -> Iterable[PM.DogmaUnits]:
    """Records from the dogmaUnits.jsonl dataset."""
    for item in reader.records(SdeDatasetFiles.DOGMA_UNITS, file_name):
        yield PM.DogmaUnits.model_validate(item)


def dynamic_item_attributes(
    reader: SdeReader, file_name: str | None = None
) -> Iterable[PM.DynamicItemAttributes]:
    """Records from the dynamicItemAttributes.jsonl dataset."""
    for item in reader.records(SdeDatasetFiles.DYNAMIC_ITEM_ATTRIBUTES, file_name):
        yield PM.DynamicItemAttributes.model_validate(item)


def factions(reader: SdeReader, file_name: str | None = None) -> Iterable[PM.Factions]:
    """Records from the factions.jsonl dataset."""
    for item in reader.records(SdeDatasetFiles.FACTIONS, file_name):
        yield PM.Factions.model_validate(item)


def freelance_job_schemas(
    reader: SdeReader, file_name: str | None = None
) -> PM.FreelanceJobSchemas:
    """Records from the freelanceJobSchemas.jsonl dataset."""
    return PM.FreelanceJobSchemas.model_validate(
        reader.records(SdeDatasetFiles.FREELANCE_JOB_SCHEMAS, file_name)
    )


def graphics(reader: SdeReader, file_name: str | None = None) -> Iterable[PM.Graphics]:
    """Records from the graphics.jsonl dataset."""
    for item in reader.records(SdeDatasetFiles.GRAPHICS, file_name):
        yield PM.Graphics.model_validate(item)


def groups(reader: SdeReader, file_name: str | None = None) -> Iterable[PM.Groups]:
    """Records from the groups.jsonl dataset."""
    for item in reader.records(SdeDatasetFiles.GROUPS, file_name):
        yield PM.Groups.model_validate(item)


def icons(reader: SdeReader, file_name: str | None = None) -> Iterable[PM.Icons]:
    """Records from the icons.jsonl dataset."""
    for item in reader.records(SdeDatasetFiles.ICONS, file_name):
        yield PM.Icons.model_validate(item)


def landmarks(
    reader: SdeReader, file_name: str | None = None
) -> Iterable[PM.Landmarks]:
    """Records from the landmarks.jsonl dataset."""
    for item in reader.records(SdeDatasetFiles.LANDMARKS, file_name):
        yield PM.Landmarks.model_validate(item)


def map_asteroid_belts(
    reader: SdeReader, file_name: str | None = None
) -> Iterable[PM.MapAsteroidBelts]:
    """Records from the mapAsteroidBelts.jsonl dataset."""
    for item in reader.records(SdeDatasetFiles.MAP_ASTEROID_BELTS, file_name):
        yield PM.MapAsteroidBelts.model_validate(item)


def map_constellations(
    reader: SdeReader, file_name: str | None = None
) -> Iterable[PM.MapConstellations]:
    """Records from the mapConstellations.jsonl dataset."""
    for item in reader.records(SdeDatasetFiles.MAP_CONSTELLATIONS, file_name):
        yield PM.MapConstellations.model_validate(item)


def map_moons(reader: SdeReader, file_name: str | None = None) -> Iterable[PM.MapMoons]:
    """Records from the mapMoons.jsonl dataset."""
    for item in reader.records(SdeDatasetFiles.MAP_MOONS, file_name):
        yield PM.MapMoons.model_validate(item)


def map_planets(
    reader: SdeReader, file_name: str | None = None
) -> Iterable[PM.MapPlanets]:
    """Records from the mapPlanets.jsonl dataset."""
    for item in reader.records(SdeDatasetFiles.MAP_PLANETS, file_name):
        yield PM.MapPlanets.model_validate(item)


def map_regions(
    reader: SdeReader, file_name: str | None = None
) -> Iterable[PM.MapRegions]:
    """Records from the mapRegions.jsonl dataset."""
    for item in reader.records(SdeDatasetFiles.MAP_REGIONS, file_name):
        yield PM.MapRegions.model_validate(item)


def map_solar_systems(
    reader: SdeReader, file_name: str | None = None
) -> Iterable[PM.MapSolarSystems]:
    """Records from the mapSolarSystems.jsonl dataset."""
    for item in reader.records(SdeDatasetFiles.MAP_SOLAR_SYSTEMS, file_name):
        yield PM.MapSolarSystems.model_validate(item)


def map_stargates(
    reader: SdeReader, file_name: str | None = None
) -> Iterable[PM.MapStargates]:
    """Records from the mapStargates.jsonl dataset."""
    for item in reader.records(SdeDatasetFiles.MAP_STARGATES, file_name):
        yield PM.MapStargates.model_validate(item)


def map_stars(reader: SdeReader, file_name: str | None = None) -> Iterable[PM.MapStars]:
    """Records from the mapStars.jsonl dataset."""
    for item in reader.records(SdeDatasetFiles.MAP_STARS, file_name):
        yield PM.MapStars.model_validate(item)


def market_groups(
    reader: SdeReader, file_name: str | None = None
) -> Iterable[PM.MarketGroups]:
    """Records from the marketGroups.jsonl dataset."""
    for item in reader.records(SdeDatasetFiles.MARKET_GROUPS, file_name):
        yield PM.MarketGroups.model_validate(item)


def masteries(
    reader: SdeReader, file_name: str | None = None
) -> Iterable[PM.Masteries]:
    """Records from the masteries.jsonl dataset."""
    for item in reader.records(SdeDatasetFiles.MASTERIES, file_name):
        yield PM.Masteries.model_validate(item)


def meta_groups(
    reader: SdeReader, file_name: str | None = None
) -> Iterable[PM.MetaGroups]:
    """Records from the metaGroups.jsonl dataset."""
    for item in reader.records(SdeDatasetFiles.META_GROUPS, file_name):
        yield PM.MetaGroups.model_validate(item)


def npc_characters(
    reader: SdeReader, file_name: str | None = None
) -> Iterable[PM.NpcCharacters]:
    """Records from the npcCharacters.jsonl dataset."""
    for item in reader.records(SdeDatasetFiles.NPC_CHARACTERS, file_name):
        yield PM.NpcCharacters.model_validate(item)


def npc_corporation_divisions(
    reader: SdeReader, file_name: str | None = None
) -> Iterable[PM.NpcCorporationDivisions]:
    """Records from the npcCorporationDivisions.jsonl dataset."""
    for item in reader.records(SdeDatasetFiles.NPC_CORPORATION_DIVISIONS, file_name):
        yield PM.NpcCorporationDivisions.model_validate(item)


def npc_corporations(
    reader: SdeReader, file_name: str | None = None
) -> Iterable[PM.NpcCorporations]:
    """Records from the npcCorporations.jsonl dataset."""
    for item in reader.records(SdeDatasetFiles.NPC_CORPORATIONS, file_name):
        yield PM.NpcCorporations.model_validate(item)


def npc_stations(
    reader: SdeReader, file_name: str | None = None
) -> Iterable[PM.NpcStations]:
    """Records from the npcStations.jsonl dataset."""
    for item in reader.records(SdeDatasetFiles.NPC_STATIONS, file_name):
        yield PM.NpcStations.model_validate(item)


def planet_resources(
    reader: SdeReader, file_name: str | None = None
) -> Iterable[PM.PlanetResources]:
    """Records from the planetResources.jsonl dataset."""
    for item in reader.records(SdeDatasetFiles.PLANET_RESOURCES, file_name):
        yield PM.PlanetResources.model_validate(item)


def planet_schematics(
    reader: SdeReader, file_name: str | None = None
) -> Iterable[PM.PlanetSchematics]:
    """Records from the planetSchematics.jsonl dataset."""
    for item in reader.records(SdeDatasetFiles.PLANET_SCHEMATICS, file_name):
        yield PM.PlanetSchematics.model_validate(item)


def races(reader: SdeReader, file_name: str | None = None) -> Iterable[PM.Races]:
    """Records from the races.jsonl dataset."""
    for item in reader.records(SdeDatasetFiles.RACES, file_name):
        yield PM.Races.model_validate(item)


def sde_info(reader: SdeReader, file_name: str | None = None) -> PM.SdeInfo:
    """Records from the _sde.jsonl dataset."""
    result = next(iter(reader.records(SdeDatasetFiles.SDE_INFO, file_name)), None)
    if result is None:
        raise ValueError("SDE info file is empty.")
    record, metadata = result
    if "buildNumber" not in record:
        raise ValueError("SDE info file is missing 'buildNumber' key.")
    return PM.SdeInfo.from_sde(record, metadata)


def skin_licenses(
    reader: SdeReader, file_name: str | None = None
) -> Iterable[PM.SkinLicenses]:
    """Records from the skinLicenses.jsonl dataset."""
    for item in reader.records(SdeDatasetFiles.SKIN_LICENSES, file_name):
        yield PM.SkinLicenses.model_validate(item)


def skin_materials(
    reader: SdeReader, file_name: str | None = None
) -> Iterable[PM.SkinMaterials]:
    """Records from the skinMaterials.jsonl dataset."""
    for item in reader.records(SdeDatasetFiles.SKIN_MATERIALS, file_name):
        yield PM.SkinMaterials.model_validate(item)


def skins(reader: SdeReader, file_name: str | None = None) -> Iterable[PM.Skins]:
    """Records from the skins.jsonl dataset."""
    for item in reader.records(SdeDatasetFiles.SKINS, file_name):
        yield PM.Skins.model_validate(item)


def sovereignty_upgrades(
    reader: SdeReader, file_name: str | None = None
) -> Iterable[PM.SovereigntyUpgrades]:
    """Records from the sovereigntyUpgrades.jsonl dataset."""
    for item in reader.records(SdeDatasetFiles.SOVEREIGNTY_UPGRADES, file_name):
        yield PM.SovereigntyUpgrades.model_validate(item)


def station_operations(
    reader: SdeReader, file_name: str | None = None
) -> Iterable[PM.StationOperations]:
    """Records from the stationOperations.jsonl dataset."""
    for item in reader.records(SdeDatasetFiles.STATION_OPERATIONS, file_name):
        yield PM.StationOperations.model_validate(item)


def station_services(
    reader: SdeReader, file_name: str | None = None
) -> Iterable[PM.StationServices]:
    """Records from the stationServices.jsonl dataset."""
    for item in reader.records(SdeDatasetFiles.STATION_SERVICES, file_name):
        yield PM.StationServices.model_validate(item)


def translation_languages(
    reader: SdeReader, file_name: str | None = None
) -> Iterable[PM.TranslationLanguages]:
    """Records from the translationLanguages.jsonl dataset."""
    for item in reader.records(SdeDatasetFiles.TRANSLATION_LANGUAGES, file_name):
        yield PM.TranslationLanguages.model_validate(item)


def type_bonus(
    reader: SdeReader, file_name: str | None = None
) -> Iterable[PM.TypeBonus]:
    """Records from the typeBonus.jsonl dataset."""
    for item in reader.records(SdeDatasetFiles.TYPE_BONUS, file_name):
        yield PM.TypeBonus.model_validate(item)


def type_dogma(
    reader: SdeReader, file_name: str | None = None
) -> Iterable[PM.TypeDogma]:
    """Records from the typeDogma.jsonl dataset."""
    for item in reader.records(SdeDatasetFiles.TYPE_DOGMA, file_name):
        yield PM.TypeDogma.model_validate(item)


def type_materials(
    reader: SdeReader, file_name: str | None = None
) -> Iterable[PM.TypeMaterials]:
    """Records from the typeMaterials.jsonl dataset."""
    for item in reader.records(SdeDatasetFiles.TYPE_MATERIALS, file_name):
        yield PM.TypeMaterials.model_validate(item)


def eve_types(reader: SdeReader, file_name: str | None = None) -> Iterable[PM.EveTypes]:
    """Records from the types.jsonl dataset."""
    for item in reader.records(SdeDatasetFiles.TYPES, file_name):
        yield PM.EveTypes.model_validate(item)
