# """SDE dataset records access implementation."""

# import logging
# from collections.abc import Iterable
# from pathlib import Path
# from typing import Any

# from eve_static_data.access.sde_reader import SdeReader
# from eve_static_data.models.sde_dataset_files import SdeDatasetFiles

# logger = logging.getLogger(__name__)


# class SdeRecords:
#     def __init__(self, sde_path: Path) -> None:
#         """Initialize SDE dataset records access.

#         Args:
#             sde_path: Path to the SDE data directory.
#         """
#         self.sde_path = sde_path
#         self.access = SdeReader(sde_path=sde_path)
#         self.build_number = self.access.build_number
#         self.release_date = self.access.release_date

#     def agents_in_space(self) -> Iterable[dict[str, Any]]:
#         """Records from the agentsInSpace.jsonl dataset."""
#         return self.access.records(SdeDatasetFiles.AGENTS_IN_SPACE)

#     def agent_types(self) -> Iterable[dict[str, Any]]:
#         """Records from the agentTypes.jsonl dataset."""
#         return self.access.records(SdeDatasetFiles.AGENT_TYPES)

#     def ancestries(self) -> Iterable[dict[str, Any]]:
#         """Records from the ancestries.jsonl dataset."""
#         return self.access.records(SdeDatasetFiles.ANCESTRIES)

#     def bloodlines(self) -> Iterable[dict[str, Any]]:
#         """Records from the bloodlines.jsonl dataset."""
#         return self.access.records(SdeDatasetFiles.BLOODLINES)

#     def blueprints(self) -> Iterable[dict[str, Any]]:
#         """Records from the blueprints.jsonl dataset."""
#         return self.access.records(SdeDatasetFiles.BLUEPRINTS)

#     def categories(self) -> Iterable[dict[str, Any]]:
#         """Records from the categories.jsonl dataset."""
#         return self.access.records(SdeDatasetFiles.CATEGORIES)

#     def certificates(self) -> Iterable[dict[str, Any]]:
#         """Records from the certificates.jsonl dataset."""
#         return self.access.records(SdeDatasetFiles.CERTIFICATES)

#     def character_attributes(self) -> Iterable[dict[str, Any]]:
#         """Records from the characterAttributes.jsonl dataset."""
#         return self.access.records(SdeDatasetFiles.CHARACTER_ATTRIBUTES)

#     def clone_grades(self) -> Iterable[dict[str, Any]]:
#         """Records from the cloneGrades.jsonl dataset."""
#         return self.access.records(SdeDatasetFiles.CLONE_GRADES)

#     def compressible_types(self) -> Iterable[dict[str, Any]]:
#         """Records from the compressibleTypes.jsonl dataset."""
#         return self.access.records(SdeDatasetFiles.COMPRESSIBLE_TYPES)

#     def contraband_types(self) -> Iterable[dict[str, Any]]:
#         """Records from the contrabandTypes.jsonl dataset."""
#         return self.access.records(SdeDatasetFiles.CONTRABAND_TYPES)

#     def control_tower_resources(self) -> Iterable[dict[str, Any]]:
#         """Records from the controlTowerResources.jsonl dataset."""
#         return self.access.records(SdeDatasetFiles.CONTROL_TOWER_RESOURCES)

#     def corporation_activities(self) -> Iterable[dict[str, Any]]:
#         """Records from the corporationActivities.jsonl dataset."""
#         return self.access.records(SdeDatasetFiles.CORPORATION_ACTIVITIES)

#     def debuff_collections(self) -> Iterable[dict[str, Any]]:
#         """Records from the dbuffCollections.jsonl dataset."""
#         return self.access.records(SdeDatasetFiles.DEBUFF_COLLECTIONS)

#     def dogma_attribute_categories(self) -> Iterable[dict[str, Any]]:
#         """Records from the dogmaAttributeCategories.jsonl dataset."""
#         return self.access.records(SdeDatasetFiles.DOGMA_ATTRIBUTE_CATEGORIES)

#     def dogma_attributes(self) -> Iterable[dict[str, Any]]:
#         """Records from the dogmaAttributes.jsonl dataset."""
#         return self.access.records(SdeDatasetFiles.DOGMA_ATTRIBUTES)

#     def dogma_effects(self) -> Iterable[dict[str, Any]]:
#         """Records from the dogmaEffects.jsonl dataset."""
#         return self.access.records(SdeDatasetFiles.DOGMA_EFFECTS)

#     def dogma_units(self) -> Iterable[dict[str, Any]]:
#         """Records from the dogmaUnits.jsonl dataset."""
#         return self.access.records(SdeDatasetFiles.DOGMA_UNITS)

#     def dynamic_item_attributes(self) -> Iterable[dict[str, Any]]:
#         """Records from the dynamicItemAttributes.jsonl dataset."""
#         return self.access.records(SdeDatasetFiles.DYNAMIC_ITEM_ATTRIBUTES)

#     def factions(self) -> Iterable[dict[str, Any]]:
#         """Records from the factions.jsonl dataset."""
#         return self.access.records(SdeDatasetFiles.FACTIONS)

#     def freelance_job_schemas(self) -> dict[str, Any]:
#         """Records from the freelanceJobSchemas.jsonl dataset."""
#         return next(iter(self.access.records(SdeDatasetFiles.FREELANCE_JOB_SCHEMAS)))

#     def graphics(self) -> Iterable[dict[str, Any]]:
#         """Records from the graphics.jsonl dataset."""
#         return self.access.records(SdeDatasetFiles.GRAPHICS)

#     def groups(self) -> Iterable[dict[str, Any]]:
#         """Records from the groups.jsonl dataset."""
#         return self.access.records(SdeDatasetFiles.GROUPS)

#     def icons(self) -> Iterable[dict[str, Any]]:
#         """Records from the icons.jsonl dataset."""
#         return self.access.records(SdeDatasetFiles.ICONS)

#     def landmarks(self) -> Iterable[dict[str, Any]]:
#         """Records from the landmarks.jsonl dataset."""
#         return self.access.records(SdeDatasetFiles.LANDMARKS)

#     def map_asteroid_belts(self) -> Iterable[dict[str, Any]]:
#         """Records from the mapAsteroidBelts.jsonl dataset."""
#         return self.access.records(SdeDatasetFiles.MAP_ASTEROID_BELTS)

#     def map_constellations(self) -> Iterable[dict[str, Any]]:
#         """Records from the mapConstellations.jsonl dataset."""
#         return self.access.records(SdeDatasetFiles.MAP_CONSTELLATIONS)

#     def map_moons(self) -> Iterable[dict[str, Any]]:
#         """Records from the mapMoons.jsonl dataset."""
#         return self.access.records(SdeDatasetFiles.MAP_MOONS)

#     def map_planets(self) -> Iterable[dict[str, Any]]:
#         """Records from the mapPlanets.jsonl dataset."""
#         return self.access.records(SdeDatasetFiles.MAP_PLANETS)

#     def map_regions(self) -> Iterable[dict[str, Any]]:
#         """Records from the mapRegions.jsonl dataset."""
#         return self.access.records(SdeDatasetFiles.MAP_REGIONS)

#     def map_solar_systems(self) -> Iterable[dict[str, Any]]:
#         """Records from the mapSolarSystems.jsonl dataset."""
#         return self.access.records(SdeDatasetFiles.MAP_SOLAR_SYSTEMS)

#     def map_stargates(self) -> Iterable[dict[str, Any]]:
#         """Records from the mapStargates.jsonl dataset."""
#         return self.access.records(SdeDatasetFiles.MAP_STARGATES)

#     def map_stars(self) -> Iterable[dict[str, Any]]:
#         """Records from the mapStars.jsonl dataset."""
#         return self.access.records(SdeDatasetFiles.MAP_STARS)

#     def market_groups(self) -> Iterable[dict[str, Any]]:
#         """Records from the marketGroups.jsonl dataset."""
#         return self.access.records(SdeDatasetFiles.MARKET_GROUPS)

#     def masteries(self) -> Iterable[dict[str, Any]]:
#         """Records from the masteries.jsonl dataset."""
#         return self.access.records(SdeDatasetFiles.MASTERIES)

#     def meta_groups(self) -> Iterable[dict[str, Any]]:
#         """Records from the metaGroups.jsonl dataset."""
#         return self.access.records(SdeDatasetFiles.META_GROUPS)

#     def npc_characters(self) -> Iterable[dict[str, Any]]:
#         """Records from the npcCharacters.jsonl dataset."""
#         return self.access.records(SdeDatasetFiles.NPC_CHARACTERS)

#     def npc_corporation_divisions(self) -> Iterable[dict[str, Any]]:
#         """Records from the npcCorporationDivisions.jsonl dataset."""
#         return self.access.records(SdeDatasetFiles.NPC_CORPORATION_DIVISIONS)

#     def npc_corporations(self) -> Iterable[dict[str, Any]]:
#         """Records from the npcCorporations.jsonl dataset."""
#         return self.access.records(SdeDatasetFiles.NPC_CORPORATIONS)

#     def npc_stations(self) -> Iterable[dict[str, Any]]:
#         """Records from the npcStations.jsonl dataset."""
#         return self.access.records(SdeDatasetFiles.NPC_STATIONS)

#     def planet_resources(self) -> Iterable[dict[str, Any]]:
#         """Records from the planetResources.jsonl dataset."""
#         return self.access.records(SdeDatasetFiles.PLANET_RESOURCES)

#     def planet_schematics(self) -> Iterable[dict[str, Any]]:
#         """Records from the planetSchematics.jsonl dataset."""
#         return self.access.records(SdeDatasetFiles.PLANET_SCHEMATICS)

#     def races(self) -> Iterable[dict[str, Any]]:
#         """Records from the races.jsonl dataset."""
#         return self.access.records(SdeDatasetFiles.RACES)

#     def sde_info(self) -> dict[str, Any]:
#         """Records from the _sde.jsonl dataset."""
#         reader = self.access.records(SdeDatasetFiles.SDE_INFO)
#         sde_info = next(iter(reader), None)
#         if sde_info is None:
#             raise ValueError("SDE info file is empty.")
#         if "buildNumber" not in sde_info:
#             raise ValueError("SDE info file is missing 'buildNumber' key.")
#         return sde_info if sde_info else {}

#     def skin_licenses(self) -> Iterable[dict[str, Any]]:
#         """Records from the skinLicenses.jsonl dataset."""
#         return self.access.records(SdeDatasetFiles.SKIN_LICENSES)

#     def skin_materials(self) -> Iterable[dict[str, Any]]:
#         """Records from the skinMaterials.jsonl dataset."""
#         return self.access.records(SdeDatasetFiles.SKIN_MATERIALS)

#     def skins(self) -> Iterable[dict[str, Any]]:
#         """Records from the skins.jsonl dataset."""
#         return self.access.records(SdeDatasetFiles.SKINS)

#     def sovereignty_upgrades(self) -> Iterable[dict[str, Any]]:
#         """Records from the sovereigntyUpgrades.jsonl dataset."""
#         return self.access.records(SdeDatasetFiles.SOVEREIGNTY_UPGRADES)

#     def station_operations(self) -> Iterable[dict[str, Any]]:
#         """Records from the stationOperations.jsonl dataset."""
#         return self.access.records(SdeDatasetFiles.STATION_OPERATIONS)

#     def station_services(self) -> Iterable[dict[str, Any]]:
#         """Records from the stationServices.jsonl dataset."""
#         return self.access.records(SdeDatasetFiles.STATION_SERVICES)

#     def translation_languages(self) -> Iterable[dict[str, Any]]:
#         """Records from the translationLanguages.jsonl dataset."""
#         return self.access.records(SdeDatasetFiles.TRANSLATION_LANGUAGES)

#     def type_bonus(self) -> Iterable[dict[str, Any]]:
#         """Records from the typeBonus.jsonl dataset."""
#         return self.access.records(SdeDatasetFiles.TYPE_BONUS)

#     def type_dogma(self) -> Iterable[dict[str, Any]]:
#         """Records from the typeDogma.jsonl dataset."""
#         return self.access.records(SdeDatasetFiles.TYPE_DOGMA)

#     def type_materials(self) -> Iterable[dict[str, Any]]:
#         """Records from the typeMaterials.jsonl dataset."""
#         return self.access.records(SdeDatasetFiles.TYPE_MATERIALS)

#     def eve_types(self) -> Iterable[dict[str, Any]]:
#         """Records from the types.jsonl dataset."""
#         return self.access.records(SdeDatasetFiles.TYPES)
