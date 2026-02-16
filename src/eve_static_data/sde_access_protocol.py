# """Protocol for SDE access implementations.

# The SDE access protocol defines the methods that any SDE access implementation
# must provide to interact with the SDE data source. This allows for different
# implementations to be used interchangeably within the application.

# Some possible backends could include:
# - Direct file access to the raw SDE jsonl files.
# - Access to processed SDE data, such as a database or directory of json files.
# """

# from collections.abc import Iterable
# from enum import StrEnum
# from typing import Any, Protocol


# class SdeFileNames(StrEnum):
#     AGENTS_IN_SPACE = "agentsInSpace.jsonl"
#     AGENT_TYPES = "agentTypes.jsonl"
#     ANCESTRIES = "ancestries.jsonl"
#     BLOODLINES = "bloodlines.jsonl"
#     BLUEPRINTS = "blueprints.jsonl"
#     CATEGORIES = "categories.jsonl"
#     CERTIFICATES = "certificates.jsonl"
#     CHARACTER_ATTRIBUTES = "characterAttributes.jsonl"
#     CONTRABAND_TYPES = "contrabandTypes.jsonl"
#     CONTROL_TOWER_RESOURCES = "controlTowerResources.jsonl"
#     CORPORATION_ACTIVITIES = "corporationActivities.jsonl"
#     DEBUFF_COLLECTIONS = "dbuffCollections.jsonl"
#     DOGMA_ATTRIBUTE_CATEGORIES = "dogmaAttributeCategories.jsonl"
#     DOGMA_ATTRIBUTES = "dogmaAttributes.jsonl"
#     DOGMA_EFFECTS = "dogmaEffects.jsonl"
#     DOGMA_UNITS = "dogmaUnits.jsonl"
#     DYNAMIC_ITEM_ATTRIBUTES = "dynamicItemAttributes.jsonl"
#     FACTIONS = "factions.jsonl"
#     GRAPHICS = "graphics.jsonl"
#     GROUPS = "groups.jsonl"
#     ICONS = "icons.jsonl"
#     LANDMARKS = "landmarks.jsonl"
#     MAP_ASTEROID_BELTS = "mapAsteroidBelts.jsonl"
#     MAP_CONSTELLATIONS = "mapConstellations.jsonl"
#     MAP_MOONS = "mapMoons.jsonl"
#     MAP_PLANETS = "mapPlanets.jsonl"
#     MAP_REGIONS = "mapRegions.jsonl"
#     MAP_SOLAR_SYSTEMS = "mapSolarSystems.jsonl"
#     MAP_STARGATES = "mapStargates.jsonl"
#     MAP_STARS = "mapStars.jsonl"
#     MARKET_GROUPS = "marketGroups.jsonl"
#     MASTERIES = "masteries.jsonl"
#     META_GROUPS = "metaGroups.jsonl"
#     NPC_CHARACTERS = "npcCharacters.jsonl"
#     NPC_CORPORATION_DIVISIONS = "npcCorporationDivisions.jsonl"
#     NPC_CORPORATIONS = "npcCorporations.jsonl"
#     NPC_STATIONS = "npcStations.jsonl"
#     PLANET_RESOURCES = "planetResources.jsonl"
#     PLANET_SCHEMATICS = "planetSchematics.jsonl"
#     RACES = "races.jsonl"
#     SDE_INFO = "_sde.jsonl"
#     SKIN_LICENSES = "skinLicenses.jsonl"
#     SKIN_MATERIALS = "skinMaterials.jsonl"
#     SKINS = "skins.jsonl"
#     SOVEREIGNTY_UPGRADES = "sovereigntyUpgrades.jsonl"
#     STATION_OPERATIONS = "stationOperations.jsonl"
#     STATION_SERVICES = "stationServices.jsonl"
#     TRANSLATION_LANGUAGES = "translationLanguages.jsonl"
#     TYPE_BONUS = "typeBonus.jsonl"
#     TYPE_DOGMA = "typeDogma.jsonl"
#     TYPE_MATERIALS = "typeMaterials.jsonl"
#     TYPES = "types.jsonl"


# class SdeAccessProtocol(Protocol):
#     def sde_info(self) -> dict[str, str | int]:
#         """Get the SDE info as a dictionary.

#         Returns:
#             The SDE info as a dictionary.
#         """
#         ...

#     def jsonl_iter(self, sde_file: SdeFileNames) -> Iterable[dict[str, Any]]:
#         """Get an iterator over the JSON objects in a JSONL SDE file.

#         Args:
#             sde_file: The SDE file to read.

#         Returns:
#             An iterator over the JSON objects in the file.
#         """
#         ...
