"""Raw JSON file access implementation for SDE build 3123381."""
# ruff: noqa: D102

from collections.abc import Iterable
from pathlib import Path
from typing import Any, cast

from pydantic import TypeAdapter

from eve_static_data.helpers.jsonl_reader import read_jsonl_dicts
from eve_static_data.models import raw_td as RTD

from .raw_json_td_protocol import RawJsonTDProtocol
from .sde_file_names import SdeFileNames


class RawJsonFileAccess(RawJsonTDProtocol):
    def __init__(self, sde_dir: Path) -> None:
        self.sde_dir = sde_dir

    def agents_in_space(self, **kwargs: dict[str, Any]) -> Iterable[RTD.AgentsInSpace]:
        file_path = self.sde_dir / SdeFileNames.AGENTS_IN_SPACE
        for item in read_jsonl_dicts(file_path):
            yield cast(RTD.AgentsInSpace, item)

    def agent_types(self, **kwargs: dict[str, Any]) -> Iterable[RTD.AgentTypes]:
        file_path = self.sde_dir / SdeFileNames.AGENT_TYPES
        for item in read_jsonl_dicts(file_path):
            yield cast(RTD.AgentTypes, item)

    def ancestries(self, **kwargs: dict[str, Any]) -> Iterable[RTD.Ancestries]:
        file_path = self.sde_dir / SdeFileNames.ANCESTRIES
        for item in read_jsonl_dicts(file_path):
            yield cast(RTD.Ancestries, item)

    def bloodlines(self, **kwargs: dict[str, Any]) -> Iterable[RTD.Bloodlines]:
        file_path = self.sde_dir / SdeFileNames.BLOODLINES
        for item in read_jsonl_dicts(file_path):
            yield cast(RTD.Bloodlines, item)

    def blueprints(self, **kwargs: dict[str, Any]) -> Iterable[RTD.Blueprints]:
        file_path = self.sde_dir / SdeFileNames.BLUEPRINTS
        for item in read_jsonl_dicts(file_path):
            yield cast(RTD.Blueprints, item)

    def categories(self, **kwargs: dict[str, Any]) -> Iterable[RTD.Categories]:
        file_path = self.sde_dir / SdeFileNames.CATEGORIES
        for item in read_jsonl_dicts(file_path):
            yield cast(RTD.Categories, item)

    def certificates(self, **kwargs: dict[str, Any]) -> Iterable[RTD.Certificates]:
        file_path = self.sde_dir / SdeFileNames.CERTIFICATES
        for item in read_jsonl_dicts(file_path):
            yield cast(RTD.Certificates, item)

    def character_attributes(
        self, **kwargs: dict[str, Any]
    ) -> Iterable[RTD.CharacterAttributes]:
        file_path = self.sde_dir / SdeFileNames.CHARACTER_ATTRIBUTES
        for item in read_jsonl_dicts(file_path):
            yield cast(RTD.CharacterAttributes, item)

    def compressible_types(
        self, **kwargs: dict[str, Any]
    ) -> Iterable[RTD.CompressibleTypes]:
        file_path = self.sde_dir / SdeFileNames.COMPRESSIBLE_TYPES
        for item in read_jsonl_dicts(file_path):
            yield cast(RTD.CompressibleTypes, item)

    def contraband_types(
        self, **kwargs: dict[str, Any]
    ) -> Iterable[RTD.ContrabandTypes]:
        file_path = self.sde_dir / SdeFileNames.CONTRABAND_TYPES
        for item in read_jsonl_dicts(file_path):
            yield cast(RTD.ContrabandTypes, item)

    def control_tower_resources(
        self, **kwargs: dict[str, Any]
    ) -> Iterable[RTD.ControlTowerResources]:
        file_path = self.sde_dir / SdeFileNames.CONTROL_TOWER_RESOURCES
        for item in read_jsonl_dicts(file_path):
            yield cast(RTD.ControlTowerResources, item)

    def corporation_activities(
        self, **kwargs: dict[str, Any]
    ) -> Iterable[RTD.CorporationActivities]:
        file_path = self.sde_dir / SdeFileNames.CORPORATION_ACTIVITIES
        for item in read_jsonl_dicts(file_path):
            yield cast(RTD.CorporationActivities, item)

    def debuff_collections(
        self, **kwargs: dict[str, Any]
    ) -> Iterable[RTD.DebuffCollections]:
        file_path = self.sde_dir / SdeFileNames.DEBUFF_COLLECTIONS
        for item in read_jsonl_dicts(file_path):
            yield cast(RTD.DebuffCollections, item)

    def dogma_attribute_categories(
        self, **kwargs: dict[str, Any]
    ) -> Iterable[RTD.DogmaAttributeCategories]:
        file_path = self.sde_dir / SdeFileNames.DOGMA_ATTRIBUTE_CATEGORIES
        for item in read_jsonl_dicts(file_path):
            yield cast(RTD.DogmaAttributeCategories, item)

    def dogma_attributes(
        self, **kwargs: dict[str, Any]
    ) -> Iterable[RTD.DogmaAttributes]:
        file_path = self.sde_dir / SdeFileNames.DOGMA_ATTRIBUTES
        for item in read_jsonl_dicts(file_path):
            yield cast(RTD.DogmaAttributes, item)

    def dogma_effects(self, **kwargs: dict[str, Any]) -> Iterable[RTD.DogmaEffects]:
        file_path = self.sde_dir / SdeFileNames.DOGMA_EFFECTS
        for item in read_jsonl_dicts(file_path):
            yield cast(RTD.DogmaEffects, item)

    def dogma_units(self, **kwargs: dict[str, Any]) -> Iterable[RTD.DogmaUnits]:
        file_path = self.sde_dir / SdeFileNames.DOGMA_UNITS
        for item in read_jsonl_dicts(file_path):
            yield cast(RTD.DogmaUnits, item)

    def dynamic_item_attributes(
        self, **kwargs: dict[str, Any]
    ) -> Iterable[RTD.DynamicItemAttributes]:
        file_path = self.sde_dir / SdeFileNames.DYNAMIC_ITEM_ATTRIBUTES
        for item in read_jsonl_dicts(file_path):
            yield cast(RTD.DynamicItemAttributes, item)

    def factions(self, **kwargs: dict[str, Any]) -> Iterable[RTD.Factions]:
        file_path = self.sde_dir / SdeFileNames.FACTIONS
        for item in read_jsonl_dicts(file_path):
            yield cast(RTD.Factions, item)

    def freelance_job_schemas(
        self, **kwargs: dict[str, Any]
    ) -> RTD.FreelanceJobSchemas:
        file_path = self.sde_dir / SdeFileNames.FREELANCE_JOB_SCHEMAS
        return next(iter(read_jsonl_dicts(file_path)))

    def graphics(self, **kwargs: dict[str, Any]) -> Iterable[RTD.Graphics]:
        file_path = self.sde_dir / SdeFileNames.GRAPHICS
        for item in read_jsonl_dicts(file_path):
            yield cast(RTD.Graphics, item)

    def groups(self, **kwargs: dict[str, Any]) -> Iterable[RTD.Groups]:
        file_path = self.sde_dir / SdeFileNames.GROUPS
        for item in read_jsonl_dicts(file_path):
            yield cast(RTD.Groups, item)

    def icons(self, **kwargs: dict[str, Any]) -> Iterable[RTD.Icons]:
        file_path = self.sde_dir / SdeFileNames.ICONS
        for item in read_jsonl_dicts(file_path):
            yield cast(RTD.Icons, item)

    def landmarks(self, **kwargs: dict[str, Any]) -> Iterable[RTD.Landmarks]:
        file_path = self.sde_dir / SdeFileNames.LANDMARKS
        for item in read_jsonl_dicts(file_path):
            yield cast(RTD.Landmarks, item)

    def map_asteroid_belts(
        self, **kwargs: dict[str, Any]
    ) -> Iterable[RTD.MapAsteroidBelts]:
        file_path = self.sde_dir / SdeFileNames.MAP_ASTEROID_BELTS
        for item in read_jsonl_dicts(file_path):
            yield cast(RTD.MapAsteroidBelts, item)

    def map_constellations(
        self, **kwargs: dict[str, Any]
    ) -> Iterable[RTD.MapConstellations]:
        file_path = self.sde_dir / SdeFileNames.MAP_CONSTELLATIONS
        for item in read_jsonl_dicts(file_path):
            yield cast(RTD.MapConstellations, item)

    def map_moons(self, **kwargs: dict[str, Any]) -> Iterable[RTD.MapMoons]:
        file_path = self.sde_dir / SdeFileNames.MAP_MOONS
        for item in read_jsonl_dicts(file_path):
            yield cast(RTD.MapMoons, item)

    def map_planets(self, **kwargs: dict[str, Any]) -> Iterable[RTD.MapPlanets]:
        file_path = self.sde_dir / SdeFileNames.MAP_PLANETS
        for item in read_jsonl_dicts(file_path):
            yield cast(RTD.MapPlanets, item)

    def map_regions(self, **kwargs: dict[str, Any]) -> Iterable[RTD.MapRegions]:
        file_path = self.sde_dir / SdeFileNames.MAP_REGIONS
        for item in read_jsonl_dicts(file_path):
            yield cast(RTD.MapRegions, item)

    def map_solar_systems(
        self, **kwargs: dict[str, Any]
    ) -> Iterable[RTD.MapSolarSystems]:
        file_path = self.sde_dir / SdeFileNames.MAP_SOLAR_SYSTEMS
        for item in read_jsonl_dicts(file_path):
            yield cast(RTD.MapSolarSystems, item)

    def map_stargates(self, **kwargs: dict[str, Any]) -> Iterable[RTD.MapStargates]:
        file_path = self.sde_dir / SdeFileNames.MAP_STARGATES
        for item in read_jsonl_dicts(file_path):
            yield cast(RTD.MapStargates, item)

    def map_stars(self, **kwargs: dict[str, Any]) -> Iterable[RTD.MapStars]:
        file_path = self.sde_dir / SdeFileNames.MAP_STARS
        for item in read_jsonl_dicts(file_path):
            yield cast(RTD.MapStars, item)

    def market_groups(self, **kwargs: dict[str, Any]) -> Iterable[RTD.MarketGroups]:
        file_path = self.sde_dir / SdeFileNames.MARKET_GROUPS
        for item in read_jsonl_dicts(file_path):
            yield cast(RTD.MarketGroups, item)

    def masteries(self, **kwargs: dict[str, Any]) -> Iterable[RTD.Masteries]:
        file_path = self.sde_dir / SdeFileNames.MASTERIES
        for item in read_jsonl_dicts(file_path):
            yield cast(RTD.Masteries, item)

    def meta_groups(self, **kwargs: dict[str, Any]) -> Iterable[RTD.MetaGroups]:
        file_path = self.sde_dir / SdeFileNames.META_GROUPS
        for item in read_jsonl_dicts(file_path):
            yield cast(RTD.MetaGroups, item)

    def npc_characters(self, **kwargs: dict[str, Any]) -> Iterable[RTD.NpcCharacters]:
        file_path = self.sde_dir / SdeFileNames.NPC_CHARACTERS
        for item in read_jsonl_dicts(file_path):
            yield cast(RTD.NpcCharacters, item)

    def npc_corporation_divisions(
        self, **kwargs: dict[str, Any]
    ) -> Iterable[RTD.NpcCorporationDivisions]:
        file_path = self.sde_dir / SdeFileNames.NPC_CORPORATION_DIVISIONS
        for item in read_jsonl_dicts(file_path):
            yield cast(RTD.NpcCorporationDivisions, item)

    def npc_corporations(
        self, **kwargs: dict[str, Any]
    ) -> Iterable[RTD.NpcCorporations]:
        file_path = self.sde_dir / SdeFileNames.NPC_CORPORATIONS
        for item in read_jsonl_dicts(file_path):
            yield cast(RTD.NpcCorporations, item)

    def npc_stations(self, **kwargs: dict[str, Any]) -> Iterable[RTD.NpcStations]:
        file_path = self.sde_dir / SdeFileNames.NPC_STATIONS
        for item in read_jsonl_dicts(file_path):
            yield cast(RTD.NpcStations, item)

    def planet_resources(
        self, **kwargs: dict[str, Any]
    ) -> Iterable[RTD.PlanetResources]:
        file_path = self.sde_dir / SdeFileNames.PLANET_RESOURCES
        for item in read_jsonl_dicts(file_path):
            yield cast(RTD.PlanetResources, item)

    def planet_schematics(
        self, **kwargs: dict[str, Any]
    ) -> Iterable[RTD.PlanetSchematics]:
        file_path = self.sde_dir / SdeFileNames.PLANET_SCHEMATICS
        for item in read_jsonl_dicts(file_path):
            yield cast(RTD.PlanetSchematics, item)

    def races(self, **kwargs: dict[str, Any]) -> Iterable[RTD.Races]:
        file_path = self.sde_dir / SdeFileNames.RACES
        for item in read_jsonl_dicts(file_path):
            yield cast(RTD.Races, item)

    def sde_info(self, **kwargs: dict[str, Any]) -> RTD.SdeInfo:
        file_path = self.sde_dir / SdeFileNames.SDE_INFO
        reader = read_jsonl_dicts(file_path)
        sde_info = next(iter(reader), None)
        if sde_info is None:
            raise ValueError("SDE info file is empty.")
        if "buildNumber" not in sde_info:
            raise ValueError("SDE info file is missing 'buildNumber' key.")
        return cast(RTD.SdeInfo, sde_info)

    def skin_licenses(self, **kwargs: dict[str, Any]) -> Iterable[RTD.SkinLicenses]:
        file_path = self.sde_dir / SdeFileNames.SKIN_LICENSES
        for item in read_jsonl_dicts(file_path):
            yield cast(RTD.SkinLicenses, item)

    def skin_materials(self, **kwargs: dict[str, Any]) -> Iterable[RTD.SkinMaterials]:
        file_path = self.sde_dir / SdeFileNames.SKIN_MATERIALS
        for item in read_jsonl_dicts(file_path):
            yield cast(RTD.SkinMaterials, item)

    def skins(self, **kwargs: dict[str, Any]) -> Iterable[RTD.Skins]:
        file_path = self.sde_dir / SdeFileNames.SKINS
        for item in read_jsonl_dicts(file_path):
            yield cast(RTD.Skins, item)

    def sovereignty_upgrades(
        self, **kwargs: dict[str, Any]
    ) -> Iterable[RTD.SovereigntyUpgrades]:
        file_path = self.sde_dir / SdeFileNames.SOVEREIGNTY_UPGRADES
        for item in read_jsonl_dicts(file_path):
            yield cast(RTD.SovereigntyUpgrades, item)

    def station_operations(
        self, **kwargs: dict[str, Any]
    ) -> Iterable[RTD.StationOperations]:
        file_path = self.sde_dir / SdeFileNames.STATION_OPERATIONS
        for item in read_jsonl_dicts(file_path):
            yield cast(RTD.StationOperations, item)

    def station_services(
        self, **kwargs: dict[str, Any]
    ) -> Iterable[RTD.StationServices]:
        file_path = self.sde_dir / SdeFileNames.STATION_SERVICES
        for item in read_jsonl_dicts(file_path):
            yield cast(RTD.StationServices, item)

    def translation_languages(
        self, **kwargs: dict[str, Any]
    ) -> Iterable[RTD.TranslationLanguages]:
        file_path = self.sde_dir / SdeFileNames.TRANSLATION_LANGUAGES
        for item in read_jsonl_dicts(file_path):
            yield cast(RTD.TranslationLanguages, item)

    def type_bonus(self, **kwargs: dict[str, Any]) -> Iterable[RTD.TypeBonus]:
        file_path = self.sde_dir / SdeFileNames.TYPE_BONUS
        for item in read_jsonl_dicts(file_path):
            yield cast(RTD.TypeBonus, item)

    def type_dogma(self, **kwargs: dict[str, Any]) -> Iterable[RTD.TypeDogma]:
        file_path = self.sde_dir / SdeFileNames.TYPE_DOGMA
        for item in read_jsonl_dicts(file_path):
            yield cast(RTD.TypeDogma, item)

    def type_materials(self, **kwargs: dict[str, Any]) -> Iterable[RTD.TypeMaterials]:
        file_path = self.sde_dir / SdeFileNames.TYPE_MATERIALS
        for item in read_jsonl_dicts(file_path):
            yield cast(RTD.TypeMaterials, item)

    def eve_types(self, **kwargs: dict[str, Any]) -> Iterable[RTD.EveTypes]:
        file_path = self.sde_dir / SdeFileNames.TYPES
        for item in read_jsonl_dicts(file_path):
            yield cast(RTD.EveTypes, item)


class RawJsonFileAccessValidator(RawJsonTDProtocol):
    def __init__(self, dir_path: Path) -> None:
        self.dir_path = dir_path

    def agents_in_space(self, **kwargs: dict[str, Any]) -> Iterable[RTD.AgentsInSpace]:
        file_path = self.dir_path / SdeFileNames.AGENTS_IN_SPACE
        adapter = TypeAdapter(RTD.AgentsInSpace)
        for item in read_jsonl_dicts(file_path):
            yield adapter.validate_python(item, extra="forbid")
        return

    def agent_types(self, **kwargs: dict[str, Any]) -> Iterable[RTD.AgentTypes]:
        file_path = self.dir_path / SdeFileNames.AGENT_TYPES

        adapter = TypeAdapter(RTD.AgentTypes)
        for item in read_jsonl_dicts(file_path):
            yield adapter.validate_python(item, extra="forbid")
        return

    def ancestries(self, **kwargs: dict[str, Any]) -> Iterable[RTD.Ancestries]:
        file_path = self.dir_path / SdeFileNames.ANCESTRIES

        adapter = TypeAdapter(RTD.Ancestries)
        for item in read_jsonl_dicts(file_path):
            yield adapter.validate_python(item, extra="forbid")
        return

    def bloodlines(self, **kwargs: dict[str, Any]) -> Iterable[RTD.Bloodlines]:
        file_path = self.dir_path / SdeFileNames.BLOODLINES

        adapter = TypeAdapter(RTD.Bloodlines)
        for item in read_jsonl_dicts(file_path):
            yield adapter.validate_python(item, extra="forbid")
        return

    def blueprints(self, **kwargs: dict[str, Any]) -> Iterable[RTD.Blueprints]:
        file_path = self.dir_path / SdeFileNames.BLUEPRINTS

        adapter = TypeAdapter(RTD.Blueprints)
        for item in read_jsonl_dicts(file_path):
            yield adapter.validate_python(item, extra="forbid")
        return

    def categories(self, **kwargs: dict[str, Any]) -> Iterable[RTD.Categories]:
        file_path = self.dir_path / SdeFileNames.CATEGORIES

        adapter = TypeAdapter(RTD.Categories)
        for item in read_jsonl_dicts(file_path):
            yield adapter.validate_python(item, extra="forbid")
        return

    def certificates(self, **kwargs: dict[str, Any]) -> Iterable[RTD.Certificates]:
        file_path = self.dir_path / SdeFileNames.CERTIFICATES

        adapter = TypeAdapter(RTD.Certificates)
        for item in read_jsonl_dicts(file_path):
            yield adapter.validate_python(item, extra="forbid")
        return

    def character_attributes(
        self, **kwargs: dict[str, Any]
    ) -> Iterable[RTD.CharacterAttributes]:
        file_path = self.dir_path / SdeFileNames.CHARACTER_ATTRIBUTES

        adapter = TypeAdapter(RTD.CharacterAttributes)
        for item in read_jsonl_dicts(file_path):
            yield adapter.validate_python(item, extra="forbid")
        return

    def compressible_types(
        self, **kwargs: dict[str, Any]
    ) -> Iterable[RTD.CompressibleTypes]:
        file_path = self.dir_path / SdeFileNames.COMPRESSIBLE_TYPES

        adapter = TypeAdapter(RTD.CompressibleTypes)
        for item in read_jsonl_dicts(file_path):
            yield adapter.validate_python(item, extra="forbid")
        return

    def contraband_types(
        self, **kwargs: dict[str, Any]
    ) -> Iterable[RTD.ContrabandTypes]:
        file_path = self.dir_path / SdeFileNames.CONTRABAND_TYPES

        adapter = TypeAdapter(RTD.ContrabandTypes)
        for item in read_jsonl_dicts(file_path):
            yield adapter.validate_python(item, extra="forbid")
        return

    def control_tower_resources(
        self, **kwargs: dict[str, Any]
    ) -> Iterable[RTD.ControlTowerResources]:
        file_path = self.dir_path / SdeFileNames.CONTROL_TOWER_RESOURCES

        adapter = TypeAdapter(RTD.ControlTowerResources)
        for item in read_jsonl_dicts(file_path):
            yield adapter.validate_python(item, extra="forbid")
        return

    def corporation_activities(
        self, **kwargs: dict[str, Any]
    ) -> Iterable[RTD.CorporationActivities]:
        file_path = self.dir_path / SdeFileNames.CORPORATION_ACTIVITIES

        adapter = TypeAdapter(RTD.CorporationActivities)
        for item in read_jsonl_dicts(file_path):
            yield adapter.validate_python(item, extra="forbid")
        return

    def debuff_collections(
        self, **kwargs: dict[str, Any]
    ) -> Iterable[RTD.DebuffCollections]:
        file_path = self.dir_path / SdeFileNames.DEBUFF_COLLECTIONS

        adapter = TypeAdapter(RTD.DebuffCollections)
        for item in read_jsonl_dicts(file_path):
            yield adapter.validate_python(item, extra="forbid")
        return

    def dogma_attribute_categories(
        self, **kwargs: dict[str, Any]
    ) -> Iterable[RTD.DogmaAttributeCategories]:
        file_path = self.dir_path / SdeFileNames.DOGMA_ATTRIBUTE_CATEGORIES

        adapter = TypeAdapter(RTD.DogmaAttributeCategories)
        for item in read_jsonl_dicts(file_path):
            yield adapter.validate_python(item, extra="forbid")
        return

    def dogma_attributes(
        self, **kwargs: dict[str, Any]
    ) -> Iterable[RTD.DogmaAttributes]:
        file_path = self.dir_path / SdeFileNames.DOGMA_ATTRIBUTES

        adapter = TypeAdapter(RTD.DogmaAttributes)
        for item in read_jsonl_dicts(file_path):
            yield adapter.validate_python(item, extra="forbid")
        return

    def dogma_effects(self, **kwargs: dict[str, Any]) -> Iterable[RTD.DogmaEffects]:
        file_path = self.dir_path / SdeFileNames.DOGMA_EFFECTS

        adapter = TypeAdapter(RTD.DogmaEffects)
        for item in read_jsonl_dicts(file_path):
            yield adapter.validate_python(item, extra="forbid")
        return

    def dogma_units(self, **kwargs: dict[str, Any]) -> Iterable[RTD.DogmaUnits]:
        file_path = self.dir_path / SdeFileNames.DOGMA_UNITS

        adapter = TypeAdapter(RTD.DogmaUnits)
        for item in read_jsonl_dicts(file_path):
            yield adapter.validate_python(item, extra="forbid")
        return

    def dynamic_item_attributes(
        self, **kwargs: dict[str, Any]
    ) -> Iterable[RTD.DynamicItemAttributes]:
        file_path = self.dir_path / SdeFileNames.DYNAMIC_ITEM_ATTRIBUTES

        adapter = TypeAdapter(RTD.DynamicItemAttributes)
        for item in read_jsonl_dicts(file_path):
            yield adapter.validate_python(item, extra="forbid")
        return

    def factions(self, **kwargs: dict[str, Any]) -> Iterable[RTD.Factions]:
        file_path = self.dir_path / SdeFileNames.FACTIONS

        adapter = TypeAdapter(RTD.Factions)
        for item in read_jsonl_dicts(file_path):
            yield adapter.validate_python(item, extra="forbid")
        return

    def freelance_job_schemas(
        self, **kwargs: dict[str, Any]
    ) -> RTD.FreelanceJobSchemas:
        file_path = self.dir_path / SdeFileNames.FREELANCE_JOB_SCHEMAS
        return next(iter(read_jsonl_dicts(file_path)))

    def graphics(self, **kwargs: dict[str, Any]) -> Iterable[RTD.Graphics]:
        file_path = self.dir_path / SdeFileNames.GRAPHICS

        adapter = TypeAdapter(RTD.Graphics)
        for item in read_jsonl_dicts(file_path):
            yield adapter.validate_python(item, extra="forbid")
        return

    def groups(self, **kwargs: dict[str, Any]) -> Iterable[RTD.Groups]:
        file_path = self.dir_path / SdeFileNames.GROUPS

        adapter = TypeAdapter(RTD.Groups)
        for item in read_jsonl_dicts(file_path):
            yield adapter.validate_python(item, extra="forbid")
        return

    def icons(self, **kwargs: dict[str, Any]) -> Iterable[RTD.Icons]:
        file_path = self.dir_path / SdeFileNames.ICONS

        adapter = TypeAdapter(RTD.Icons)
        for item in read_jsonl_dicts(file_path):
            yield adapter.validate_python(item, extra="forbid")
        return

    def landmarks(self, **kwargs: dict[str, Any]) -> Iterable[RTD.Landmarks]:
        file_path = self.dir_path / SdeFileNames.LANDMARKS

        adapter = TypeAdapter(RTD.Landmarks)
        for item in read_jsonl_dicts(file_path):
            yield adapter.validate_python(item, extra="forbid")
        return

    def map_asteroid_belts(
        self, **kwargs: dict[str, Any]
    ) -> Iterable[RTD.MapAsteroidBelts]:
        file_path = self.dir_path / SdeFileNames.MAP_ASTEROID_BELTS

        adapter = TypeAdapter(RTD.MapAsteroidBelts)
        for item in read_jsonl_dicts(file_path):
            yield adapter.validate_python(item, extra="forbid")
        return

    def map_constellations(
        self, **kwargs: dict[str, Any]
    ) -> Iterable[RTD.MapConstellations]:
        file_path = self.dir_path / SdeFileNames.MAP_CONSTELLATIONS

        adapter = TypeAdapter(RTD.MapConstellations)
        for item in read_jsonl_dicts(file_path):
            yield adapter.validate_python(item, extra="forbid")
        return

    def map_moons(self, **kwargs: dict[str, Any]) -> Iterable[RTD.MapMoons]:
        file_path = self.dir_path / SdeFileNames.MAP_MOONS

        adapter = TypeAdapter(RTD.MapMoons)
        for item in read_jsonl_dicts(file_path):
            yield adapter.validate_python(item, extra="forbid")
        return

    def map_planets(self, **kwargs: dict[str, Any]) -> Iterable[RTD.MapPlanets]:
        file_path = self.dir_path / SdeFileNames.MAP_PLANETS

        adapter = TypeAdapter(RTD.MapPlanets)
        for item in read_jsonl_dicts(file_path):
            yield adapter.validate_python(item, extra="forbid")
        return

    def map_regions(self, **kwargs: dict[str, Any]) -> Iterable[RTD.MapRegions]:
        file_path = self.dir_path / SdeFileNames.MAP_REGIONS

        adapter = TypeAdapter(RTD.MapRegions)
        for item in read_jsonl_dicts(file_path):
            yield adapter.validate_python(item, extra="forbid")
        return

    def map_solar_systems(
        self, **kwargs: dict[str, Any]
    ) -> Iterable[RTD.MapSolarSystems]:
        file_path = self.dir_path / SdeFileNames.MAP_SOLAR_SYSTEMS

        adapter = TypeAdapter(RTD.MapSolarSystems)
        for item in read_jsonl_dicts(file_path):
            yield adapter.validate_python(item, extra="forbid")
        return

    def map_stargates(self, **kwargs: dict[str, Any]) -> Iterable[RTD.MapStargates]:
        file_path = self.dir_path / SdeFileNames.MAP_STARGATES

        adapter = TypeAdapter(RTD.MapStargates)
        for item in read_jsonl_dicts(file_path):
            yield adapter.validate_python(item, extra="forbid")
        return

    def map_stars(self, **kwargs: dict[str, Any]) -> Iterable[RTD.MapStars]:
        file_path = self.dir_path / SdeFileNames.MAP_STARS

        adapter = TypeAdapter(RTD.MapStars)
        for item in read_jsonl_dicts(file_path):
            yield adapter.validate_python(item, extra="forbid")
        return

    def market_groups(self, **kwargs: dict[str, Any]) -> Iterable[RTD.MarketGroups]:
        file_path = self.dir_path / SdeFileNames.MARKET_GROUPS

        adapter = TypeAdapter(RTD.MarketGroups)
        for item in read_jsonl_dicts(file_path):
            yield adapter.validate_python(item, extra="forbid")
        return

    def masteries(self, **kwargs: dict[str, Any]) -> Iterable[RTD.Masteries]:
        file_path = self.dir_path / SdeFileNames.MASTERIES

        adapter = TypeAdapter(RTD.Masteries)
        for item in read_jsonl_dicts(file_path):
            yield adapter.validate_python(item, extra="forbid")
        return

    def meta_groups(self, **kwargs: dict[str, Any]) -> Iterable[RTD.MetaGroups]:
        file_path = self.dir_path / SdeFileNames.META_GROUPS

        adapter = TypeAdapter(RTD.MetaGroups)
        for item in read_jsonl_dicts(file_path):
            yield adapter.validate_python(item, extra="forbid")
        return

    def npc_characters(self, **kwargs: dict[str, Any]) -> Iterable[RTD.NpcCharacters]:
        file_path = self.dir_path / SdeFileNames.NPC_CHARACTERS

        adapter = TypeAdapter(RTD.NpcCharacters)
        for item in read_jsonl_dicts(file_path):
            yield adapter.validate_python(item, extra="forbid")
        return

    def npc_corporation_divisions(
        self, **kwargs: dict[str, Any]
    ) -> Iterable[RTD.NpcCorporationDivisions]:
        file_path = self.dir_path / SdeFileNames.NPC_CORPORATION_DIVISIONS

        adapter = TypeAdapter(RTD.NpcCorporationDivisions)
        for item in read_jsonl_dicts(file_path):
            yield adapter.validate_python(item, extra="forbid")
        return

    def npc_corporations(
        self, **kwargs: dict[str, Any]
    ) -> Iterable[RTD.NpcCorporations]:
        file_path = self.dir_path / SdeFileNames.NPC_CORPORATIONS

        adapter = TypeAdapter(RTD.NpcCorporations)
        for item in read_jsonl_dicts(file_path):
            yield adapter.validate_python(item, extra="forbid")
        return

    def npc_stations(self, **kwargs: dict[str, Any]) -> Iterable[RTD.NpcStations]:
        file_path = self.dir_path / SdeFileNames.NPC_STATIONS

        adapter = TypeAdapter(RTD.NpcStations)
        for item in read_jsonl_dicts(file_path):
            yield adapter.validate_python(item, extra="forbid")
        return

    def planet_resources(
        self, **kwargs: dict[str, Any]
    ) -> Iterable[RTD.PlanetResources]:
        file_path = self.dir_path / SdeFileNames.PLANET_RESOURCES

        adapter = TypeAdapter(RTD.PlanetResources)
        for item in read_jsonl_dicts(file_path):
            yield adapter.validate_python(item, extra="forbid")
        return

    def planet_schematics(
        self, **kwargs: dict[str, Any]
    ) -> Iterable[RTD.PlanetSchematics]:
        file_path = self.dir_path / SdeFileNames.PLANET_SCHEMATICS

        adapter = TypeAdapter(RTD.PlanetSchematics)
        for item in read_jsonl_dicts(file_path):
            yield adapter.validate_python(item, extra="forbid")
        return

    def races(self, **kwargs: dict[str, Any]) -> Iterable[RTD.Races]:
        file_path = self.dir_path / SdeFileNames.RACES

        adapter = TypeAdapter(RTD.Races)
        for item in read_jsonl_dicts(file_path):
            yield adapter.validate_python(item, extra="forbid")
        return

    def sde_info(self, **kwargs: dict[str, Any]) -> RTD.SdeInfo:
        file_path = self.dir_path / SdeFileNames.SDE_INFO
        reader = read_jsonl_dicts(file_path)
        sde_info = next(iter(reader), None)

        adapter = TypeAdapter(RTD.SdeInfo)
        sde_info = adapter.validate_python(sde_info, extra="forbid")
        return sde_info

    def skin_licenses(self, **kwargs: dict[str, Any]) -> Iterable[RTD.SkinLicenses]:
        file_path = self.dir_path / SdeFileNames.SKIN_LICENSES

        adapter = TypeAdapter(RTD.SkinLicenses)
        for item in read_jsonl_dicts(file_path):
            yield adapter.validate_python(item, extra="forbid")
        return

    def skin_materials(self, **kwargs: dict[str, Any]) -> Iterable[RTD.SkinMaterials]:
        file_path = self.dir_path / SdeFileNames.SKIN_MATERIALS

        adapter = TypeAdapter(RTD.SkinMaterials)
        for item in read_jsonl_dicts(file_path):
            yield adapter.validate_python(item, extra="forbid")
        return

    def skins(self, **kwargs: dict[str, Any]) -> Iterable[RTD.Skins]:
        file_path = self.dir_path / SdeFileNames.SKINS

        adapter = TypeAdapter(RTD.Skins)
        for item in read_jsonl_dicts(file_path):
            yield adapter.validate_python(item, extra="forbid")
        return

    def sovereignty_upgrades(
        self, **kwargs: dict[str, Any]
    ) -> Iterable[RTD.SovereigntyUpgrades]:
        file_path = self.dir_path / SdeFileNames.SOVEREIGNTY_UPGRADES

        adapter = TypeAdapter(RTD.SovereigntyUpgrades)
        for item in read_jsonl_dicts(file_path):
            yield adapter.validate_python(item, extra="forbid")
        return

    def station_operations(
        self, **kwargs: dict[str, Any]
    ) -> Iterable[RTD.StationOperations]:
        file_path = self.dir_path / SdeFileNames.STATION_OPERATIONS

        adapter = TypeAdapter(RTD.StationOperations)
        for item in read_jsonl_dicts(file_path):
            yield adapter.validate_python(item, extra="forbid")
        return

    def station_services(
        self, **kwargs: dict[str, Any]
    ) -> Iterable[RTD.StationServices]:
        file_path = self.dir_path / SdeFileNames.STATION_SERVICES

        adapter = TypeAdapter(RTD.StationServices)
        for item in read_jsonl_dicts(file_path):
            yield adapter.validate_python(item, extra="forbid")
        return

    def translation_languages(
        self, **kwargs: dict[str, Any]
    ) -> Iterable[RTD.TranslationLanguages]:
        file_path = self.dir_path / SdeFileNames.TRANSLATION_LANGUAGES

        adapter = TypeAdapter(RTD.TranslationLanguages)
        for item in read_jsonl_dicts(file_path):
            yield adapter.validate_python(item, extra="forbid")
        return

    def type_bonus(self, **kwargs: dict[str, Any]) -> Iterable[RTD.TypeBonus]:
        file_path = self.dir_path / SdeFileNames.TYPE_BONUS

        adapter = TypeAdapter(RTD.TypeBonus)
        for item in read_jsonl_dicts(file_path):
            yield adapter.validate_python(item, extra="forbid")
        return

    def type_dogma(self, **kwargs: dict[str, Any]) -> Iterable[RTD.TypeDogma]:
        file_path = self.dir_path / SdeFileNames.TYPE_DOGMA

        adapter = TypeAdapter(RTD.TypeDogma)
        for item in read_jsonl_dicts(file_path):
            yield adapter.validate_python(item, extra="forbid")
        return

    def type_materials(self, **kwargs: dict[str, Any]) -> Iterable[RTD.TypeMaterials]:
        file_path = self.dir_path / SdeFileNames.TYPE_MATERIALS

        adapter = TypeAdapter(RTD.TypeMaterials)
        for item in read_jsonl_dicts(file_path):
            yield adapter.validate_python(item, extra="forbid")
        return

    def eve_types(self, **kwargs: dict[str, Any]) -> Iterable[RTD.EveTypes]:
        file_path = self.dir_path / SdeFileNames.TYPES

        adapter = TypeAdapter(RTD.EveTypes)
        for item in read_jsonl_dicts(file_path):
            yield adapter.validate_python(item, extra="forbid")
        return

    def validate(self, file_name: SdeFileNames) -> None:
        """Validate a specific SDE file."""
        match file_name:
            case SdeFileNames.AGENTS_IN_SPACE:
                _ = list(self.agents_in_space())
            case SdeFileNames.AGENT_TYPES:
                _ = list(self.agent_types())
            case SdeFileNames.ANCESTRIES:
                _ = list(self.ancestries())
            case SdeFileNames.BLOODLINES:
                _ = list(self.bloodlines())
            case SdeFileNames.BLUEPRINTS:
                _ = list(self.blueprints())
            case SdeFileNames.CATEGORIES:
                _ = list(self.categories())
            case SdeFileNames.CERTIFICATES:
                _ = list(self.certificates())
            case SdeFileNames.CHARACTER_ATTRIBUTES:
                _ = list(self.character_attributes())
            case SdeFileNames.COMPRESSIBLE_TYPES:
                _ = list(self.compressible_types())
            case SdeFileNames.CONTRABAND_TYPES:
                _ = list(self.contraband_types())
            case SdeFileNames.CONTROL_TOWER_RESOURCES:
                _ = list(self.control_tower_resources())
            case SdeFileNames.CORPORATION_ACTIVITIES:
                _ = list(self.corporation_activities())
            case SdeFileNames.DEBUFF_COLLECTIONS:
                _ = list(self.debuff_collections())
            case SdeFileNames.DOGMA_ATTRIBUTE_CATEGORIES:
                _ = list(self.dogma_attribute_categories())
            case SdeFileNames.DOGMA_ATTRIBUTES:
                _ = list(self.dogma_attributes())
            case SdeFileNames.DOGMA_EFFECTS:
                _ = list(self.dogma_effects())
            case SdeFileNames.DOGMA_UNITS:
                _ = list(self.dogma_units())
            case SdeFileNames.DYNAMIC_ITEM_ATTRIBUTES:
                _ = list(self.dynamic_item_attributes())
            case SdeFileNames.FACTIONS:
                _ = list(self.factions())
            case SdeFileNames.FREELANCE_JOB_SCHEMAS:
                _ = self.freelance_job_schemas()
            case SdeFileNames.GRAPHICS:
                _ = list(self.graphics())
            case SdeFileNames.GROUPS:
                _ = list(self.groups())
            case SdeFileNames.ICONS:
                _ = list(self.icons())
            case SdeFileNames.LANDMARKS:
                _ = list(self.landmarks())
            case SdeFileNames.MAP_ASTEROID_BELTS:
                _ = list(self.map_asteroid_belts())
            case SdeFileNames.MAP_CONSTELLATIONS:
                _ = list(self.map_constellations())
            case SdeFileNames.MAP_MOONS:
                _ = list(self.map_moons())
            case SdeFileNames.MAP_PLANETS:
                _ = list(self.map_planets())
            case SdeFileNames.MAP_REGIONS:
                _ = list(self.map_regions())
            case SdeFileNames.MAP_SOLAR_SYSTEMS:
                _ = list(self.map_solar_systems())
            case SdeFileNames.MAP_STARGATES:
                _ = list(self.map_stargates())
            case SdeFileNames.MAP_STARS:
                _ = list(self.map_stars())
            case SdeFileNames.MARKET_GROUPS:
                _ = list(self.market_groups())
            case SdeFileNames.MASTERIES:
                _ = list(self.masteries())
            case SdeFileNames.META_GROUPS:
                _ = list(self.meta_groups())
            case SdeFileNames.NPC_CHARACTERS:
                _ = list(self.npc_characters())
            case SdeFileNames.NPC_CORPORATION_DIVISIONS:
                _ = list(self.npc_corporation_divisions())
            case SdeFileNames.NPC_CORPORATIONS:
                _ = list(self.npc_corporations())
            case SdeFileNames.NPC_STATIONS:
                _ = list(self.npc_stations())
            case SdeFileNames.PLANET_RESOURCES:
                _ = list(self.planet_resources())
            case SdeFileNames.PLANET_SCHEMATICS:
                _ = list(self.planet_schematics())
            case SdeFileNames.RACES:
                _ = list(self.races())
            case SdeFileNames.SDE_INFO:
                _ = self.sde_info()
            case SdeFileNames.SKIN_LICENSES:
                _ = list(self.skin_licenses())
            case SdeFileNames.SKIN_MATERIALS:
                _ = list(self.skin_materials())
            case SdeFileNames.SKINS:
                _ = list(self.skins())
            case SdeFileNames.SOVEREIGNTY_UPGRADES:
                _ = list(self.sovereignty_upgrades())
            case SdeFileNames.STATION_OPERATIONS:
                _ = list(self.station_operations())
            case SdeFileNames.STATION_SERVICES:
                _ = list(self.station_services())
            case SdeFileNames.TRANSLATION_LANGUAGES:
                _ = list(self.translation_languages())
            case SdeFileNames.TYPE_BONUS:
                _ = list(self.type_bonus())
            case SdeFileNames.TYPE_DOGMA:
                _ = list(self.type_dogma())
            case SdeFileNames.TYPE_MATERIALS:
                _ = list(self.type_materials())
            case SdeFileNames.TYPES:
                _ = list(self.eve_types())
            case _:
                raise ValueError(f"Unknown SDE file name: {file_name}")

    def validate_all(self) -> None:
        """Validate all SDE files."""
        for file_name in SdeFileNames:
            self.validate(file_name)
