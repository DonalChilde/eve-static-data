"""Raw JSON file access implementation for SDE build 3123381."""

from collections.abc import Iterable
from pathlib import Path
from typing import Any

from eve_static_data.helpers.jsonl_reader import read_jsonl_dicts

from ..models import raw_td as RTD
from .raw_json_td_protocol import RawJsonTDProtocol
from .sde_file_names import SdeFileNames


class RawJsonFileAccess(RawJsonTDProtocol):
    def __init__(self, dir_path: Path) -> None:
        self.dir_path = dir_path

    def agents_in_space(self) -> Iterable[RTD.AgentsInSpace]:
        file_path = self.dir_path / SdeFileNames.AGENTS_IN_SPACE
        return read_jsonl_dicts(file_path)  # type: ignore

    def agent_types(self) -> Iterable[RTD.AgentTypes]:
        file_path = self.dir_path / SdeFileNames.AGENT_TYPES
        return read_jsonl_dicts(file_path)  # type: ignore

    def ancestries(self) -> Iterable[RTD.Ancestries]:
        file_path = self.dir_path / SdeFileNames.ANCESTRIES
        return read_jsonl_dicts(file_path)  # type: ignore

    def bloodlines(self) -> Iterable[RTD.Bloodlines]:
        file_path = self.dir_path / SdeFileNames.BLOODLINES
        return read_jsonl_dicts(file_path)  # type: ignore

    def blueprints(self) -> Iterable[RTD.Blueprints]:
        file_path = self.dir_path / SdeFileNames.BLUEPRINTS
        return read_jsonl_dicts(file_path)  # type: ignore

    def categories(self) -> Iterable[RTD.Categories]:
        file_path = self.dir_path / SdeFileNames.CATEGORIES
        return read_jsonl_dicts(file_path)  # type: ignore

    def certificates(self) -> Iterable[RTD.Certificates]:
        file_path = self.dir_path / SdeFileNames.CERTIFICATES
        return read_jsonl_dicts(file_path)  # type: ignore

    def character_attributes(self) -> Iterable[RTD.CharacterAttributes]:
        file_path = self.dir_path / SdeFileNames.CHARACTER_ATTRIBUTES
        return read_jsonl_dicts(file_path)  # type: ignore

    def compressible_types(self) -> Iterable[RTD.CompressibleTypes]:
        file_path = self.dir_path / SdeFileNames.COMPRESSIBLE_TYPES
        return read_jsonl_dicts(file_path)  # type: ignore

    def contraband_types(self) -> Iterable[RTD.ContrabandTypes]:
        file_path = self.dir_path / SdeFileNames.CONTRABAND_TYPES
        return read_jsonl_dicts(file_path)  # type: ignore

    def control_tower_resources(self) -> Iterable[RTD.ControlTowerResources]:
        file_path = self.dir_path / SdeFileNames.CONTROL_TOWER_RESOURCES
        return read_jsonl_dicts(file_path)  # type: ignore

    def corporation_activities(self) -> Iterable[RTD.CorporationActivities]:
        file_path = self.dir_path / SdeFileNames.CORPORATION_ACTIVITIES
        return read_jsonl_dicts(file_path)  # type: ignore

    def debuff_collections(self) -> Iterable[RTD.DebuffCollections]:
        file_path = self.dir_path / SdeFileNames.DEBUFF_COLLECTIONS
        return read_jsonl_dicts(file_path)  # type: ignore

    def dogma_attribute_categories(self) -> Iterable[RTD.DogmaAttributeCategories]:
        file_path = self.dir_path / SdeFileNames.DOGMA_ATTRIBUTE_CATEGORIES
        return read_jsonl_dicts(file_path)  # type: ignore

    def dogma_attributes(self) -> Iterable[RTD.DogmaAttributes]:
        file_path = self.dir_path / SdeFileNames.DOGMA_ATTRIBUTES
        return read_jsonl_dicts(file_path)  # type: ignore

    def dogma_effects(self) -> Iterable[RTD.DogmaEffects]:
        file_path = self.dir_path / SdeFileNames.DOGMA_EFFECTS
        return read_jsonl_dicts(file_path)  # type: ignore

    def dogma_units(self) -> Iterable[RTD.DogmaUnits]:
        file_path = self.dir_path / SdeFileNames.DOGMA_UNITS
        return read_jsonl_dicts(file_path)  # type: ignore

    def dynamic_item_attributes(self) -> Iterable[RTD.DynamicItemAttributes]:
        file_path = self.dir_path / SdeFileNames.DYNAMIC_ITEM_ATTRIBUTES
        return read_jsonl_dicts(file_path)  # type: ignore

    def factions(self) -> Iterable[RTD.Factions]:
        file_path = self.dir_path / SdeFileNames.FACTIONS
        return read_jsonl_dicts(file_path)  # type: ignore

    def freelance_job_schemas(self) -> dict[str, Any]:
        file_path = self.dir_path / SdeFileNames.FREELANCE_JOB_SCHEMAS
        return next(iter(read_jsonl_dicts(file_path)))

    def graphics(self) -> Iterable[RTD.Graphics]:
        file_path = self.dir_path / SdeFileNames.GRAPHICS
        return read_jsonl_dicts(file_path)  # type: ignore

    def groups(self) -> Iterable[RTD.Groups]:
        file_path = self.dir_path / SdeFileNames.GROUPS
        return read_jsonl_dicts(file_path)  # type: ignore

    def icons(self) -> Iterable[RTD.Icons]:
        file_path = self.dir_path / SdeFileNames.ICONS
        return read_jsonl_dicts(file_path)  # type: ignore

    def landmarks(self) -> Iterable[RTD.Landmarks]:
        file_path = self.dir_path / SdeFileNames.LANDMARKS
        return read_jsonl_dicts(file_path)  # type: ignore

    def map_asteroid_belts(self) -> Iterable[RTD.MapAsteroidBelts]:
        file_path = self.dir_path / SdeFileNames.MAP_ASTEROID_BELTS
        return read_jsonl_dicts(file_path)  # type: ignore

    def map_constellations(self) -> Iterable[RTD.MapConstellations]:
        file_path = self.dir_path / SdeFileNames.MAP_CONSTELLATIONS
        return read_jsonl_dicts(file_path)  # type: ignore

    def map_moons(self) -> Iterable[RTD.MapMoons]:
        file_path = self.dir_path / SdeFileNames.MAP_MOONS
        return read_jsonl_dicts(file_path)  # type: ignore

    def map_planets(self) -> Iterable[RTD.MapPlanets]:
        file_path = self.dir_path / SdeFileNames.MAP_PLANETS
        return read_jsonl_dicts(file_path)  # type: ignore

    def map_regions(self) -> Iterable[RTD.MapRegions]:
        file_path = self.dir_path / SdeFileNames.MAP_REGIONS
        return read_jsonl_dicts(file_path)  # type: ignore

    def map_solar_systems(self) -> Iterable[RTD.MapSolarSystems]:
        file_path = self.dir_path / SdeFileNames.MAP_SOLAR_SYSTEMS
        return read_jsonl_dicts(file_path)  # type: ignore

    def map_stargates(self) -> Iterable[RTD.MapStargates]:
        file_path = self.dir_path / SdeFileNames.MAP_STARGATES
        return read_jsonl_dicts(file_path)  # type: ignore

    def map_stars(self) -> Iterable[RTD.MapStars]:
        file_path = self.dir_path / SdeFileNames.MAP_STARS
        return read_jsonl_dicts(file_path)  # type: ignore

    def market_groups(self) -> Iterable[RTD.MarketGroups]:
        file_path = self.dir_path / SdeFileNames.MARKET_GROUPS
        return read_jsonl_dicts(file_path)  # type: ignore

    def masteries(self) -> Iterable[RTD.Masteries]:
        file_path = self.dir_path / SdeFileNames.MASTERIES
        return read_jsonl_dicts(file_path)  # type: ignore

    def meta_groups(self) -> Iterable[RTD.MetaGroups]:
        file_path = self.dir_path / SdeFileNames.META_GROUPS
        return read_jsonl_dicts(file_path)  # type: ignore

    def npc_characters(self) -> Iterable[RTD.NpcCharacters]:
        file_path = self.dir_path / SdeFileNames.NPC_CHARACTERS
        return read_jsonl_dicts(file_path)  # type: ignore

    def npc_corporation_divisions(self) -> Iterable[RTD.NpcCorporationDivisions]:
        file_path = self.dir_path / SdeFileNames.NPC_CORPORATION_DIVISIONS
        return read_jsonl_dicts(file_path)  # type: ignore

    def npc_corporations(self) -> Iterable[RTD.NpcCorporations]:
        file_path = self.dir_path / SdeFileNames.NPC_CORPORATIONS
        return read_jsonl_dicts(file_path)  # type: ignore

    def npc_stations(self) -> Iterable[RTD.NpcStations]:
        file_path = self.dir_path / SdeFileNames.NPC_STATIONS
        return read_jsonl_dicts(file_path)  # type: ignore

    def planet_resources(self) -> Iterable[RTD.PlanetResources]:
        file_path = self.dir_path / SdeFileNames.PLANET_RESOURCES
        return read_jsonl_dicts(file_path)  # type: ignore

    def planet_schematics(self) -> Iterable[RTD.PlanetSchematics]:
        file_path = self.dir_path / SdeFileNames.PLANET_SCHEMATICS
        return read_jsonl_dicts(file_path)  # type: ignore

    def races(self) -> Iterable[RTD.Races]:
        file_path = self.dir_path / SdeFileNames.RACES
        return read_jsonl_dicts(file_path)  # type: ignore

    def sde_info(self) -> RTD.SdeInfo:
        file_path = self.dir_path / SdeFileNames.SDE_INFO
        reader = read_jsonl_dicts(file_path)
        sde_info = next(iter(reader), None)
        if sde_info is None:
            raise ValueError("SDE info file is empty.")
        if not "buildNumber" in sde_info:
            raise ValueError("SDE info file is missing 'buildNumber' key.")
        return sde_info  # type: ignore

    def skin_licenses(self) -> Iterable[RTD.SkinLicenses]:
        file_path = self.dir_path / SdeFileNames.SKIN_LICENSES
        return read_jsonl_dicts(file_path)  # type: ignore

    def skin_materials(self) -> Iterable[RTD.SkinMaterials]:
        file_path = self.dir_path / SdeFileNames.SKIN_MATERIALS
        return read_jsonl_dicts(file_path)  # type: ignore

    def skins(self) -> Iterable[RTD.Skins]:
        file_path = self.dir_path / SdeFileNames.SKINS
        return read_jsonl_dicts(file_path)  # type: ignore

    def sovereignty_upgrades(self) -> Iterable[RTD.SovereigntyUpgrades]:
        file_path = self.dir_path / SdeFileNames.SOVEREIGNTY_UPGRADES
        return read_jsonl_dicts(file_path)  # type: ignore

    def station_operations(self) -> Iterable[RTD.StationOperations]:
        file_path = self.dir_path / SdeFileNames.STATION_OPERATIONS
        return read_jsonl_dicts(file_path)  # type: ignore

    def station_services(self) -> Iterable[RTD.StationServices]:
        file_path = self.dir_path / SdeFileNames.STATION_SERVICES
        return read_jsonl_dicts(file_path)  # type: ignore

    def translation_languages(self) -> Iterable[RTD.TranslationLanguages]:
        file_path = self.dir_path / SdeFileNames.TRANSLATION_LANGUAGES
        return read_jsonl_dicts(file_path)  # type: ignore

    def type_bonus(self) -> Iterable[RTD.TypeBonus]:
        file_path = self.dir_path / SdeFileNames.TYPE_BONUS
        return read_jsonl_dicts(file_path)  # type: ignore

    def type_dogma(self) -> Iterable[RTD.TypeDogma]:
        file_path = self.dir_path / SdeFileNames.TYPE_DOGMA
        return read_jsonl_dicts(file_path)  # type: ignore

    def type_materials(self) -> Iterable[RTD.TypeMaterials]:
        file_path = self.dir_path / SdeFileNames.TYPE_MATERIALS
        return read_jsonl_dicts(file_path)  # type: ignore

    def eve_types(self) -> Iterable[RTD.EveTypes]:
        file_path = self.dir_path / SdeFileNames.TYPES
        return read_jsonl_dicts(file_path)  # type: ignore
