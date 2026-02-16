"""Raw JSON file access implementation for SDE build 3123381."""

from collections.abc import Iterable
from pathlib import Path
from typing import Any

from eve_static_data.helpers.jsonl_reader import read_jsonl_dicts

from .raw_json_protocol import RawJsonProtocol
from .sde_file_names import SdeFileNames


class RawJsonFileAccess(RawJsonProtocol):
    def __init__(self, dir_path: Path) -> None:
        self.dir_path = dir_path

    def agents_in_space(self) -> Iterable[dict[str, Any]]:
        file_path = self.dir_path / SdeFileNames.AGENTS_IN_SPACE
        return read_jsonl_dicts(file_path)

    def agent_types(self) -> Iterable[dict[str, Any]]:
        file_path = self.dir_path / SdeFileNames.AGENT_TYPES
        return read_jsonl_dicts(file_path)

    def ancestries(self) -> Iterable[dict[str, Any]]:
        file_path = self.dir_path / SdeFileNames.ANCESTRIES
        return read_jsonl_dicts(file_path)

    def bloodlines(self) -> Iterable[dict[str, Any]]:
        file_path = self.dir_path / SdeFileNames.BLOODLINES
        return read_jsonl_dicts(file_path)

    def blueprints(self) -> Iterable[dict[str, Any]]:
        file_path = self.dir_path / SdeFileNames.BLUEPRINTS
        return read_jsonl_dicts(file_path)

    def categories(self) -> Iterable[dict[str, Any]]:
        file_path = self.dir_path / SdeFileNames.CATEGORIES
        return read_jsonl_dicts(file_path)

    def certificates(self) -> Iterable[dict[str, Any]]:
        file_path = self.dir_path / SdeFileNames.CERTIFICATES
        return read_jsonl_dicts(file_path)

    def character_attributes(self) -> Iterable[dict[str, Any]]:
        file_path = self.dir_path / SdeFileNames.CHARACTER_ATTRIBUTES
        return read_jsonl_dicts(file_path)

    def compressible_types(self) -> Iterable[dict[str, Any]]:
        file_path = self.dir_path / SdeFileNames.COMPRESSIBLE_TYPES
        return read_jsonl_dicts(file_path)

    def contraband_types(self) -> Iterable[dict[str, Any]]:
        file_path = self.dir_path / SdeFileNames.CONTRABAND_TYPES
        return read_jsonl_dicts(file_path)

    def control_tower_resources(self) -> Iterable[dict[str, Any]]:
        file_path = self.dir_path / SdeFileNames.CONTROL_TOWER_RESOURCES
        return read_jsonl_dicts(file_path)

    def corporation_activities(self) -> Iterable[dict[str, Any]]:
        file_path = self.dir_path / SdeFileNames.CORPORATION_ACTIVITIES
        return read_jsonl_dicts(file_path)

    def debuff_collections(self) -> Iterable[dict[str, Any]]:
        file_path = self.dir_path / SdeFileNames.DEBUFF_COLLECTIONS
        return read_jsonl_dicts(file_path)

    def dogma_attribute_categories(self) -> Iterable[dict[str, Any]]:
        file_path = self.dir_path / SdeFileNames.DOGMA_ATTRIBUTE_CATEGORIES
        return read_jsonl_dicts(file_path)

    def dogma_attributes(self) -> Iterable[dict[str, Any]]:
        file_path = self.dir_path / SdeFileNames.DOGMA_ATTRIBUTES
        return read_jsonl_dicts(file_path)

    def dogma_effects(self) -> Iterable[dict[str, Any]]:
        file_path = self.dir_path / SdeFileNames.DOGMA_EFFECTS
        return read_jsonl_dicts(file_path)

    def dogma_units(self) -> Iterable[dict[str, Any]]:
        file_path = self.dir_path / SdeFileNames.DOGMA_UNITS
        return read_jsonl_dicts(file_path)

    def dynamic_item_attributes(self) -> Iterable[dict[str, Any]]:
        file_path = self.dir_path / SdeFileNames.DYNAMIC_ITEM_ATTRIBUTES
        return read_jsonl_dicts(file_path)

    def factions(self) -> Iterable[dict[str, Any]]:
        file_path = self.dir_path / SdeFileNames.FACTIONS
        return read_jsonl_dicts(file_path)

    def freelance_job_schemas(self) -> dict[str, Any]:
        file_path = self.dir_path / SdeFileNames.FREELANCE_JOB_SCHEMAS
        return next(iter(read_jsonl_dicts(file_path)))

    def graphics(self) -> Iterable[dict[str, Any]]:
        file_path = self.dir_path / SdeFileNames.GRAPHICS
        return read_jsonl_dicts(file_path)

    def groups(self) -> Iterable[dict[str, Any]]:
        file_path = self.dir_path / SdeFileNames.GROUPS
        return read_jsonl_dicts(file_path)

    def icons(self) -> Iterable[dict[str, Any]]:
        file_path = self.dir_path / SdeFileNames.ICONS
        return read_jsonl_dicts(file_path)

    def landmarks(self) -> Iterable[dict[str, Any]]:
        file_path = self.dir_path / SdeFileNames.LANDMARKS
        return read_jsonl_dicts(file_path)

    def map_asteroid_belts(self) -> Iterable[dict[str, Any]]:
        file_path = self.dir_path / SdeFileNames.MAP_ASTEROID_BELTS
        return read_jsonl_dicts(file_path)

    def map_constellations(self) -> Iterable[dict[str, Any]]:
        file_path = self.dir_path / SdeFileNames.MAP_CONSTELLATIONS
        return read_jsonl_dicts(file_path)

    def map_moons(self) -> Iterable[dict[str, Any]]:
        file_path = self.dir_path / SdeFileNames.MAP_MOONS
        return read_jsonl_dicts(file_path)

    def map_planets(self) -> Iterable[dict[str, Any]]:
        file_path = self.dir_path / SdeFileNames.MAP_PLANETS
        return read_jsonl_dicts(file_path)

    def map_regions(self) -> Iterable[dict[str, Any]]:
        file_path = self.dir_path / SdeFileNames.MAP_REGIONS
        return read_jsonl_dicts(file_path)

    def map_solar_systems(self) -> Iterable[dict[str, Any]]:
        file_path = self.dir_path / SdeFileNames.MAP_SOLAR_SYSTEMS
        return read_jsonl_dicts(file_path)

    def map_stargates(self) -> Iterable[dict[str, Any]]:
        file_path = self.dir_path / SdeFileNames.MAP_STARGATES
        return read_jsonl_dicts(file_path)

    def map_stars(self) -> Iterable[dict[str, Any]]:
        file_path = self.dir_path / SdeFileNames.MAP_STARS
        return read_jsonl_dicts(file_path)

    def market_groups(self) -> Iterable[dict[str, Any]]:
        file_path = self.dir_path / SdeFileNames.MARKET_GROUPS
        return read_jsonl_dicts(file_path)

    def masteries(self) -> Iterable[dict[str, Any]]:
        file_path = self.dir_path / SdeFileNames.MASTERIES
        return read_jsonl_dicts(file_path)

    def meta_groups(self) -> Iterable[dict[str, Any]]:
        file_path = self.dir_path / SdeFileNames.META_GROUPS
        return read_jsonl_dicts(file_path)

    def npc_characters(self) -> Iterable[dict[str, Any]]:
        file_path = self.dir_path / SdeFileNames.NPC_CHARACTERS
        return read_jsonl_dicts(file_path)

    def npc_corporation_divisions(self) -> Iterable[dict[str, Any]]:
        file_path = self.dir_path / SdeFileNames.NPC_CORPORATION_DIVISIONS
        return read_jsonl_dicts(file_path)

    def npc_corporations(self) -> Iterable[dict[str, Any]]:
        file_path = self.dir_path / SdeFileNames.NPC_CORPORATIONS
        return read_jsonl_dicts(file_path)

    def npc_stations(self) -> Iterable[dict[str, Any]]:
        file_path = self.dir_path / SdeFileNames.NPC_STATIONS
        return read_jsonl_dicts(file_path)

    def planet_resources(self) -> Iterable[dict[str, Any]]:
        file_path = self.dir_path / SdeFileNames.PLANET_RESOURCES
        return read_jsonl_dicts(file_path)

    def planet_schematics(self) -> Iterable[dict[str, Any]]:
        file_path = self.dir_path / SdeFileNames.PLANET_SCHEMATICS
        return read_jsonl_dicts(file_path)

    def races(self) -> Iterable[dict[str, Any]]:
        file_path = self.dir_path / SdeFileNames.RACES
        return read_jsonl_dicts(file_path)

    def sde_info(self) -> dict[str, Any]:
        file_path = self.dir_path / SdeFileNames.SDE_INFO
        reader = read_jsonl_dicts(file_path)
        sde_info = next(iter(reader), None)
        if sde_info is None:
            raise ValueError("SDE info file is empty.")
        if not "buildNumber" in sde_info:
            raise ValueError("SDE info file is missing 'buildNumber' key.")
        return sde_info if sde_info else {}

    def skin_licenses(self) -> Iterable[dict[str, Any]]:
        file_path = self.dir_path / SdeFileNames.SKIN_LICENSES
        return read_jsonl_dicts(file_path)

    def skin_materials(self) -> Iterable[dict[str, Any]]:
        file_path = self.dir_path / SdeFileNames.SKIN_MATERIALS
        return read_jsonl_dicts(file_path)

    def skins(self) -> Iterable[dict[str, Any]]:
        file_path = self.dir_path / SdeFileNames.SKINS
        return read_jsonl_dicts(file_path)

    def sovereignty_upgrades(self) -> Iterable[dict[str, Any]]:
        file_path = self.dir_path / SdeFileNames.SOVEREIGNTY_UPGRADES
        return read_jsonl_dicts(file_path)

    def station_operations(self) -> Iterable[dict[str, Any]]:
        file_path = self.dir_path / SdeFileNames.STATION_OPERATIONS
        return read_jsonl_dicts(file_path)

    def station_services(self) -> Iterable[dict[str, Any]]:
        file_path = self.dir_path / SdeFileNames.STATION_SERVICES
        return read_jsonl_dicts(file_path)

    def translation_languages(self) -> Iterable[dict[str, Any]]:
        file_path = self.dir_path / SdeFileNames.TRANSLATION_LANGUAGES
        return read_jsonl_dicts(file_path)

    def type_bonus(self) -> Iterable[dict[str, Any]]:
        file_path = self.dir_path / SdeFileNames.TYPE_BONUS
        return read_jsonl_dicts(file_path)

    def type_dogma(self) -> Iterable[dict[str, Any]]:
        file_path = self.dir_path / SdeFileNames.TYPE_DOGMA
        return read_jsonl_dicts(file_path)

    def type_materials(self) -> Iterable[dict[str, Any]]:
        file_path = self.dir_path / SdeFileNames.TYPE_MATERIALS
        return read_jsonl_dicts(file_path)

    def eve_types(self) -> Iterable[dict[str, Any]]:
        file_path = self.dir_path / SdeFileNames.TYPES
        return read_jsonl_dicts(file_path)
