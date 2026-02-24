"""Factory methods for creating TypedDict models from SDE records.

The factory functions return a tuple of the TypedDict instance and the SDE record metadata,
which includes the file path and record count, which corresponds to the line number in
the source file.
"""
# ruff: noqa: D102

# FIXME Evaluate whether these factory functions are necessary or useful in any way.

import logging
from collections.abc import Iterable
from typing import cast

from eve_static_data.access.sde_reader import SdeReader, SDERecordMetadata
from eve_static_data.models.datasets.sde_dataset_files import SdeDatasetFiles
from eve_static_data.models.records import sde_typeddict as RTD

logger = logging.getLogger(__name__)


def agents_in_space(
    reader: SdeReader, file_name: str | None = None
) -> Iterable[tuple[RTD.AgentsInSpace, SDERecordMetadata]]:
    """Records from the agentsInSpace.jsonl dataset."""
    for item, metadata in reader.records(SdeDatasetFiles.AGENTS_IN_SPACE, file_name):
        yield cast(RTD.AgentsInSpace, item), metadata


def agent_types(
    reader: SdeReader, file_name: str | None = None
) -> Iterable[tuple[RTD.AgentTypes, SDERecordMetadata]]:
    """Records from the agentTypes.jsonl dataset."""
    for item, metadata in reader.records(SdeDatasetFiles.AGENT_TYPES, file_name):
        yield cast(RTD.AgentTypes, item), metadata


def ancestries(
    reader: SdeReader, file_name: str | None = None
) -> Iterable[tuple[RTD.Ancestries, SDERecordMetadata]]:
    """Records from the ancestries.jsonl dataset."""
    for item, metadata in reader.records(SdeDatasetFiles.ANCESTRIES, file_name):
        yield cast(RTD.Ancestries, item), metadata


def bloodlines(
    reader: SdeReader, file_name: str | None = None
) -> Iterable[tuple[RTD.Bloodlines, SDERecordMetadata]]:
    """Records from the bloodlines.jsonl dataset."""
    for item, metadata in reader.records(SdeDatasetFiles.BLOODLINES, file_name):
        yield cast(RTD.Bloodlines, item), metadata


def blueprints(
    reader: SdeReader, file_name: str | None = None
) -> Iterable[tuple[RTD.Blueprints, SDERecordMetadata]]:
    """Records from the blueprints.jsonl dataset."""
    for item, metadata in reader.records(SdeDatasetFiles.BLUEPRINTS, file_name):
        yield cast(RTD.Blueprints, item), metadata


def categories(
    reader: SdeReader, file_name: str | None = None
) -> Iterable[tuple[RTD.Categories, SDERecordMetadata]]:
    """Records from the categories.jsonl dataset."""
    for item, metadata in reader.records(SdeDatasetFiles.CATEGORIES, file_name):
        yield cast(RTD.Categories, item), metadata


def certificates(
    reader: SdeReader, file_name: str | None = None
) -> Iterable[tuple[RTD.Certificates, SDERecordMetadata]]:
    """Records from the certificates.jsonl dataset."""
    for item, metadata in reader.records(SdeDatasetFiles.CERTIFICATES, file_name):
        yield cast(RTD.Certificates, item), metadata


def character_attributes(
    reader: SdeReader, file_name: str | None = None
) -> Iterable[tuple[RTD.CharacterAttributes, SDERecordMetadata]]:
    """Records from the characterAttributes.jsonl dataset."""
    for item, metadata in reader.records(
        SdeDatasetFiles.CHARACTER_ATTRIBUTES, file_name
    ):
        yield cast(RTD.CharacterAttributes, item), metadata


def clone_grades(
    reader: SdeReader, file_name: str | None = None
) -> Iterable[tuple[RTD.CloneGrades, SDERecordMetadata]]:
    """Records from the cloneGrades.jsonl dataset."""
    for item, metadata in reader.records(SdeDatasetFiles.CLONE_GRADES, file_name):
        yield cast(RTD.CloneGrades, item), metadata


def compressible_types(
    reader: SdeReader, file_name: str | None = None
) -> Iterable[tuple[RTD.CompressibleTypes, SDERecordMetadata]]:
    """Records from the compressibleTypes.jsonl dataset."""
    for item, metadata in reader.records(SdeDatasetFiles.COMPRESSIBLE_TYPES, file_name):
        yield cast(RTD.CompressibleTypes, item), metadata


def contraband_types(
    reader: SdeReader, file_name: str | None = None
) -> Iterable[tuple[RTD.ContrabandTypes, SDERecordMetadata]]:
    """Records from the contrabandTypes.jsonl dataset."""
    for item, metadata in reader.records(SdeDatasetFiles.CONTRABAND_TYPES, file_name):
        yield cast(RTD.ContrabandTypes, item), metadata


def control_tower_resources(
    reader: SdeReader, file_name: str | None = None
) -> Iterable[tuple[RTD.ControlTowerResources, SDERecordMetadata]]:
    """Records from the controlTowerResources.jsonl dataset."""
    for item, metadata in reader.records(
        SdeDatasetFiles.CONTROL_TOWER_RESOURCES, file_name
    ):
        yield cast(RTD.ControlTowerResources, item), metadata


def corporation_activities(
    reader: SdeReader, file_name: str | None = None
) -> Iterable[tuple[RTD.CorporationActivities, SDERecordMetadata]]:
    """Records from the corporationActivities.jsonl dataset."""
    for item, metadata in reader.records(
        SdeDatasetFiles.CORPORATION_ACTIVITIES, file_name
    ):
        yield cast(RTD.CorporationActivities, item), metadata


def debuff_collections(
    reader: SdeReader, file_name: str | None = None
) -> Iterable[tuple[RTD.DebuffCollections, SDERecordMetadata]]:
    """Records from the dbuffCollections.jsonl dataset."""
    for item, metadata in reader.records(SdeDatasetFiles.DEBUFF_COLLECTIONS, file_name):
        yield cast(RTD.DebuffCollections, item), metadata


def dogma_attribute_categories(
    reader: SdeReader, file_name: str | None = None
) -> Iterable[tuple[RTD.DogmaAttributeCategories, SDERecordMetadata]]:
    """Records from the dogmaAttributeCategories.jsonl dataset."""
    for item, metadata in reader.records(
        SdeDatasetFiles.DOGMA_ATTRIBUTE_CATEGORIES, file_name
    ):
        yield cast(RTD.DogmaAttributeCategories, item), metadata


def dogma_attributes(
    reader: SdeReader, file_name: str | None = None
) -> Iterable[tuple[RTD.DogmaAttributes, SDERecordMetadata]]:
    """Records from the dogmaAttributes.jsonl dataset."""
    for item, metadata in reader.records(SdeDatasetFiles.DOGMA_ATTRIBUTES, file_name):
        yield cast(RTD.DogmaAttributes, item), metadata


def dogma_effects(
    reader: SdeReader, file_name: str | None = None
) -> Iterable[tuple[RTD.DogmaEffects, SDERecordMetadata]]:
    """Records from the dogmaEffects.jsonl dataset."""
    for item, metadata in reader.records(SdeDatasetFiles.DOGMA_EFFECTS, file_name):
        yield cast(RTD.DogmaEffects, item), metadata


def dogma_units(
    reader: SdeReader, file_name: str | None = None
) -> Iterable[tuple[RTD.DogmaUnits, SDERecordMetadata]]:
    """Records from the dogmaUnits.jsonl dataset."""
    for item, metadata in reader.records(SdeDatasetFiles.DOGMA_UNITS, file_name):
        yield cast(RTD.DogmaUnits, item), metadata


def dynamic_item_attributes(
    reader: SdeReader, file_name: str | None = None
) -> Iterable[tuple[RTD.DynamicItemAttributes, SDERecordMetadata]]:
    """Records from the dynamicItemAttributes.jsonl dataset."""
    for item, metadata in reader.records(
        SdeDatasetFiles.DYNAMIC_ITEM_ATTRIBUTES, file_name
    ):
        yield cast(RTD.DynamicItemAttributes, item), metadata


def factions(
    reader: SdeReader, file_name: str | None = None
) -> Iterable[tuple[RTD.Factions, SDERecordMetadata]]:
    """Records from the factions.jsonl dataset."""
    for item, metadata in reader.records(SdeDatasetFiles.FACTIONS, file_name):
        yield cast(RTD.Factions, item), metadata


def freelance_job_schemas(
    reader: SdeReader, file_name: str | None = None
) -> tuple[RTD.FreelanceJobSchemas, SDERecordMetadata]:
    """Records from the freelanceJobSchemas.jsonl dataset."""
    item, metadata = reader.record_at(
        SdeDatasetFiles.FREELANCE_JOB_SCHEMAS, index=1, file_name=file_name
    )
    return cast(RTD.FreelanceJobSchemas, item), metadata


def graphics(
    reader: SdeReader, file_name: str | None = None
) -> Iterable[tuple[RTD.Graphics, SDERecordMetadata]]:
    """Records from the graphics.jsonl dataset."""
    for item, metadata in reader.records(SdeDatasetFiles.GRAPHICS, file_name):
        yield cast(RTD.Graphics, item), metadata


def groups(
    reader: SdeReader, file_name: str | None = None
) -> Iterable[tuple[RTD.Groups, SDERecordMetadata]]:
    """Records from the groups.jsonl dataset."""
    for item, metadata in reader.records(SdeDatasetFiles.GROUPS, file_name):
        yield cast(RTD.Groups, item), metadata


def icons(
    reader: SdeReader, file_name: str | None = None
) -> Iterable[tuple[RTD.Icons, SDERecordMetadata]]:
    """Records from the icons.jsonl dataset."""
    for item, metadata in reader.records(SdeDatasetFiles.ICONS, file_name):
        yield cast(RTD.Icons, item), metadata


def landmarks(
    reader: SdeReader, file_name: str | None = None
) -> Iterable[tuple[RTD.Landmarks, SDERecordMetadata]]:
    """Records from the landmarks.jsonl dataset."""
    for item, metadata in reader.records(SdeDatasetFiles.LANDMARKS, file_name):
        yield cast(RTD.Landmarks, item), metadata


def map_asteroid_belts(
    reader: SdeReader, file_name: str | None = None
) -> Iterable[tuple[RTD.MapAsteroidBelts, SDERecordMetadata]]:
    """Records from the mapAsteroidBelts.jsonl dataset."""
    for item, metadata in reader.records(SdeDatasetFiles.MAP_ASTEROID_BELTS, file_name):
        yield cast(RTD.MapAsteroidBelts, item), metadata


def map_constellations(
    reader: SdeReader, file_name: str | None = None
) -> Iterable[tuple[RTD.MapConstellations, SDERecordMetadata]]:
    """Records from the mapConstellations.jsonl dataset."""
    for item, metadata in reader.records(SdeDatasetFiles.MAP_CONSTELLATIONS, file_name):
        yield cast(RTD.MapConstellations, item), metadata


def map_moons(
    reader: SdeReader, file_name: str | None = None
) -> Iterable[tuple[RTD.MapMoons, SDERecordMetadata]]:
    """Records from the mapMoons.jsonl dataset."""
    for item, metadata in reader.records(SdeDatasetFiles.MAP_MOONS, file_name):
        yield cast(RTD.MapMoons, item), metadata


def map_planets(
    reader: SdeReader, file_name: str | None = None
) -> Iterable[tuple[RTD.MapPlanets, SDERecordMetadata]]:
    """Records from the mapPlanets.jsonl dataset."""
    for item, metadata in reader.records(SdeDatasetFiles.MAP_PLANETS, file_name):
        yield cast(RTD.MapPlanets, item), metadata


def map_regions(
    reader: SdeReader, file_name: str | None = None
) -> Iterable[tuple[RTD.MapRegions, SDERecordMetadata]]:
    """Records from the mapRegions.jsonl dataset."""
    for item, metadata in reader.records(SdeDatasetFiles.MAP_REGIONS, file_name):
        yield cast(RTD.MapRegions, item), metadata


def map_solar_systems(
    reader: SdeReader, file_name: str | None = None
) -> Iterable[tuple[RTD.MapSolarSystems, SDERecordMetadata]]:
    """Records from the mapSolarSystems.jsonl dataset."""
    for item, metadata in reader.records(SdeDatasetFiles.MAP_SOLAR_SYSTEMS, file_name):
        yield cast(RTD.MapSolarSystems, item), metadata


def map_stargates(
    reader: SdeReader, file_name: str | None = None
) -> Iterable[tuple[RTD.MapStargates, SDERecordMetadata]]:
    """Records from the mapStargates.jsonl dataset."""
    for item, metadata in reader.records(SdeDatasetFiles.MAP_STARGATES, file_name):
        yield cast(RTD.MapStargates, item), metadata


def map_stars(
    reader: SdeReader, file_name: str | None = None
) -> Iterable[tuple[RTD.MapStars, SDERecordMetadata]]:
    """Records from the mapStars.jsonl dataset."""
    for item, metadata in reader.records(SdeDatasetFiles.MAP_STARS, file_name):
        yield cast(RTD.MapStars, item), metadata


def market_groups(
    reader: SdeReader, file_name: str | None = None
) -> Iterable[tuple[RTD.MarketGroups, SDERecordMetadata]]:
    """Records from the marketGroups.jsonl dataset."""
    for item, metadata in reader.records(SdeDatasetFiles.MARKET_GROUPS, file_name):
        yield cast(RTD.MarketGroups, item), metadata


def masteries(
    reader: SdeReader, file_name: str | None = None
) -> Iterable[tuple[RTD.Masteries, SDERecordMetadata]]:
    """Records from the masteries.jsonl dataset."""
    for item, metadata in reader.records(SdeDatasetFiles.MASTERIES, file_name):
        yield cast(RTD.Masteries, item), metadata


def meta_groups(
    reader: SdeReader, file_name: str | None = None
) -> Iterable[tuple[RTD.MetaGroups, SDERecordMetadata]]:
    """Records from the metaGroups.jsonl dataset."""
    for item, metadata in reader.records(SdeDatasetFiles.META_GROUPS, file_name):
        yield cast(RTD.MetaGroups, item), metadata


def npc_characters(
    reader: SdeReader, file_name: str | None = None
) -> Iterable[tuple[RTD.NpcCharacters, SDERecordMetadata]]:
    """Records from the npcCharacters.jsonl dataset."""
    for item, metadata in reader.records(SdeDatasetFiles.NPC_CHARACTERS, file_name):
        yield cast(RTD.NpcCharacters, item), metadata


def npc_corporation_divisions(
    reader: SdeReader, file_name: str | None = None
) -> Iterable[tuple[RTD.NpcCorporationDivisions, SDERecordMetadata]]:
    """Records from the npcCorporationDivisions.jsonl dataset."""
    for item, metadata in reader.records(
        SdeDatasetFiles.NPC_CORPORATION_DIVISIONS, file_name
    ):
        yield cast(RTD.NpcCorporationDivisions, item), metadata


def npc_corporations(
    reader: SdeReader, file_name: str | None = None
) -> Iterable[tuple[RTD.NpcCorporations, SDERecordMetadata]]:
    """Records from the npcCorporations.jsonl dataset."""
    for item, metadata in reader.records(SdeDatasetFiles.NPC_CORPORATIONS, file_name):
        yield cast(RTD.NpcCorporations, item), metadata


def npc_stations(
    reader: SdeReader, file_name: str | None = None
) -> Iterable[tuple[RTD.NpcStations, SDERecordMetadata]]:
    """Records from the npcStations.jsonl dataset."""
    for item, metadata in reader.records(SdeDatasetFiles.NPC_STATIONS, file_name):
        yield cast(RTD.NpcStations, item), metadata


def planet_resources(
    reader: SdeReader, file_name: str | None = None
) -> Iterable[tuple[RTD.PlanetResources, SDERecordMetadata]]:
    """Records from the planetResources.jsonl dataset."""
    for item, metadata in reader.records(SdeDatasetFiles.PLANET_RESOURCES, file_name):
        yield cast(RTD.PlanetResources, item), metadata


def planet_schematics(
    reader: SdeReader, file_name: str | None = None
) -> Iterable[tuple[RTD.PlanetSchematics, SDERecordMetadata]]:
    """Records from the planetSchematics.jsonl dataset."""
    for item, metadata in reader.records(SdeDatasetFiles.PLANET_SCHEMATICS, file_name):
        yield cast(RTD.PlanetSchematics, item), metadata


def races(
    reader: SdeReader, file_name: str | None = None
) -> Iterable[tuple[RTD.Races, SDERecordMetadata]]:
    """Records from the races.jsonl dataset."""
    for item, metadata in reader.records(SdeDatasetFiles.RACES, file_name):
        yield cast(RTD.Races, item), metadata


def sde_info(
    reader: SdeReader, file_name: str | None = None
) -> tuple[RTD.SdeInfo, SDERecordMetadata]:
    """Records from the _sde.jsonl dataset."""
    sde_info, metadata = reader.record_at(
        SdeDatasetFiles.SDE_INFO, index=1, file_name=file_name
    )
    if "buildNumber" not in sde_info:
        raise ValueError("SDE info file is missing 'buildNumber' key.")
    return cast(RTD.SdeInfo, sde_info), metadata


def skin_licenses(
    reader: SdeReader, file_name: str | None = None
) -> Iterable[tuple[RTD.SkinLicenses, SDERecordMetadata]]:
    """Records from the skinLicenses.jsonl dataset."""
    for item, metadata in reader.records(SdeDatasetFiles.SKIN_LICENSES, file_name):
        yield cast(RTD.SkinLicenses, item), metadata


def skin_materials(
    reader: SdeReader, file_name: str | None = None
) -> Iterable[tuple[RTD.SkinMaterials, SDERecordMetadata]]:
    """Records from the skinMaterials.jsonl dataset."""
    for item, metadata in reader.records(SdeDatasetFiles.SKIN_MATERIALS, file_name):
        yield cast(RTD.SkinMaterials, item), metadata


def skins(
    reader: SdeReader, file_name: str | None = None
) -> Iterable[tuple[RTD.Skins, SDERecordMetadata]]:
    """Records from the skins.jsonl dataset."""
    for item, metadata in reader.records(SdeDatasetFiles.SKINS, file_name):
        yield cast(RTD.Skins, item), metadata


def sovereignty_upgrades(
    reader: SdeReader, file_name: str | None = None
) -> Iterable[tuple[RTD.SovereigntyUpgrades, SDERecordMetadata]]:
    """Records from the sovereigntyUpgrades.jsonl dataset."""
    for item, metadata in reader.records(
        SdeDatasetFiles.SOVEREIGNTY_UPGRADES, file_name
    ):
        yield cast(RTD.SovereigntyUpgrades, item), metadata


def station_operations(
    reader: SdeReader, file_name: str | None = None
) -> Iterable[tuple[RTD.StationOperations, SDERecordMetadata]]:
    """Records from the stationOperations.jsonl dataset."""
    for item, metadata in reader.records(SdeDatasetFiles.STATION_OPERATIONS, file_name):
        yield cast(RTD.StationOperations, item), metadata


def station_services(
    reader: SdeReader, file_name: str | None = None
) -> Iterable[tuple[RTD.StationServices, SDERecordMetadata]]:
    """Records from the stationServices.jsonl dataset."""
    for item, metadata in reader.records(SdeDatasetFiles.STATION_SERVICES, file_name):
        yield cast(RTD.StationServices, item), metadata


def translation_languages(
    reader: SdeReader, file_name: str | None = None
) -> Iterable[tuple[RTD.TranslationLanguages, SDERecordMetadata]]:
    """Records from the translationLanguages.jsonl dataset."""
    for item, metadata in reader.records(
        SdeDatasetFiles.TRANSLATION_LANGUAGES, file_name
    ):
        yield cast(RTD.TranslationLanguages, item), metadata


def type_bonus(
    reader: SdeReader, file_name: str | None = None
) -> Iterable[tuple[RTD.TypeBonus, SDERecordMetadata]]:
    """Records from the typeBonus.jsonl dataset."""
    for item, metadata in reader.records(SdeDatasetFiles.TYPE_BONUS, file_name):
        yield cast(RTD.TypeBonus, item), metadata


def type_dogma(
    reader: SdeReader, file_name: str | None = None
) -> Iterable[tuple[RTD.TypeDogma, SDERecordMetadata]]:
    """Records from the typeDogma.jsonl dataset."""
    for item, metadata in reader.records(SdeDatasetFiles.TYPE_DOGMA, file_name):
        yield cast(RTD.TypeDogma, item), metadata


def type_materials(
    reader: SdeReader, file_name: str | None = None
) -> Iterable[tuple[RTD.TypeMaterials, SDERecordMetadata]]:
    """Records from the typeMaterials.jsonl dataset."""
    for item, metadata in reader.records(SdeDatasetFiles.TYPE_MATERIALS, file_name):
        yield cast(RTD.TypeMaterials, item), metadata


def eve_types(
    reader: SdeReader, file_name: str | None = None
) -> Iterable[tuple[RTD.EveTypes, SDERecordMetadata]]:
    """Records from the types.jsonl dataset."""
    for item, metadata in reader.records(SdeDatasetFiles.TYPES, file_name):
        yield cast(RTD.EveTypes, item), metadata
