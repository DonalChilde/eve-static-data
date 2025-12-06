"""Raw JSON file access implementation for SDE build 3123381."""
# ruff: noqa: D102

from collections.abc import Iterable
from pathlib import Path

from pydantic import TypeAdapter

from eve_static_data.helpers.jsonl_reader import read_jsonl_dicts

from ..models import raw_td as RTD
from .raw_json_td_protocol import RawJsonTDProtocol
from .sde_file_names import SdeFileNames


class RawJsonFileAccess(RawJsonTDProtocol):
    def __init__(self, dir_path: Path) -> None:
        self.dir_path = dir_path

    def agents_in_space(self, validate: bool = False) -> Iterable[RTD.AgentsInSpace]:
        file_path = self.dir_path / SdeFileNames.AGENTS_IN_SPACE
        if validate:
            adapter = TypeAdapter(RTD.AgentsInSpace)
            for item in read_jsonl_dicts(file_path):
                yield adapter.validate_python(item, extra="forbid")
            return
        return read_jsonl_dicts(file_path)  # type: ignore

    def agent_types(self, validate: bool = False) -> Iterable[RTD.AgentTypes]:
        file_path = self.dir_path / SdeFileNames.AGENT_TYPES
        if validate:
            adapter = TypeAdapter(RTD.AgentTypes)
            for item in read_jsonl_dicts(file_path):
                yield adapter.validate_python(item, extra="forbid")
            return
        return read_jsonl_dicts(file_path)  # type: ignore

    def ancestries(self, validate: bool = False) -> Iterable[RTD.Ancestries]:
        file_path = self.dir_path / SdeFileNames.ANCESTRIES
        if validate:
            adapter = TypeAdapter(RTD.Ancestries)
            for item in read_jsonl_dicts(file_path):
                yield adapter.validate_python(item, extra="forbid")
            return
        return read_jsonl_dicts(file_path)  # type: ignore

    def bloodlines(self, validate: bool = False) -> Iterable[RTD.Bloodlines]:
        file_path = self.dir_path / SdeFileNames.BLOODLINES
        if validate:
            adapter = TypeAdapter(RTD.Bloodlines)
            for item in read_jsonl_dicts(file_path):
                yield adapter.validate_python(item, extra="forbid")
            return
        return read_jsonl_dicts(file_path)  # type: ignore

    def blueprints(self, validate: bool = False) -> Iterable[RTD.Blueprints]:
        file_path = self.dir_path / SdeFileNames.BLUEPRINTS
        if validate:
            adapter = TypeAdapter(RTD.Blueprints)
            for item in read_jsonl_dicts(file_path):
                yield adapter.validate_python(item, extra="forbid")
            return
        return read_jsonl_dicts(file_path)  # type: ignore

    def categories(self, validate: bool = False) -> Iterable[RTD.Categories]:
        file_path = self.dir_path / SdeFileNames.CATEGORIES
        if validate:
            adapter = TypeAdapter(RTD.Categories)
            for item in read_jsonl_dicts(file_path):
                yield adapter.validate_python(item, extra="forbid")
            return
        return read_jsonl_dicts(file_path)  # type: ignore

    def certificates(self, validate: bool = False) -> Iterable[RTD.Certificates]:
        file_path = self.dir_path / SdeFileNames.CERTIFICATES
        if validate:
            adapter = TypeAdapter(RTD.Certificates)
            for item in read_jsonl_dicts(file_path):
                yield adapter.validate_python(item, extra="forbid")
            return
        return read_jsonl_dicts(file_path)  # type: ignore

    def character_attributes(
        self, validate: bool = False
    ) -> Iterable[RTD.CharacterAttributes]:
        file_path = self.dir_path / SdeFileNames.CHARACTER_ATTRIBUTES
        if validate:
            adapter = TypeAdapter(RTD.CharacterAttributes)
            for item in read_jsonl_dicts(file_path):
                yield adapter.validate_python(item, extra="forbid")
            return
        return read_jsonl_dicts(file_path)  # type: ignore

    def compressible_types(
        self, validate: bool = False
    ) -> Iterable[RTD.CompressibleTypes]:
        file_path = self.dir_path / SdeFileNames.COMPRESSIBLE_TYPES
        if validate:
            adapter = TypeAdapter(RTD.CompressibleTypes)
            for item in read_jsonl_dicts(file_path):
                yield adapter.validate_python(item, extra="forbid")
            return
        return read_jsonl_dicts(file_path)  # type: ignore

    def contraband_types(self, validate: bool = False) -> Iterable[RTD.ContrabandTypes]:
        file_path = self.dir_path / SdeFileNames.CONTRABAND_TYPES
        if validate:
            adapter = TypeAdapter(RTD.ContrabandTypes)
            for item in read_jsonl_dicts(file_path):
                yield adapter.validate_python(item, extra="forbid")
            return
        return read_jsonl_dicts(file_path)  # type: ignore

    def control_tower_resources(
        self, validate: bool = False
    ) -> Iterable[RTD.ControlTowerResources]:
        file_path = self.dir_path / SdeFileNames.CONTROL_TOWER_RESOURCES
        if validate:
            adapter = TypeAdapter(RTD.ControlTowerResources)
            for item in read_jsonl_dicts(file_path):
                yield adapter.validate_python(item, extra="forbid")
            return
        return read_jsonl_dicts(file_path)  # type: ignore

    def corporation_activities(
        self, validate: bool = False
    ) -> Iterable[RTD.CorporationActivities]:
        file_path = self.dir_path / SdeFileNames.CORPORATION_ACTIVITIES
        if validate:
            adapter = TypeAdapter(RTD.CorporationActivities)
            for item in read_jsonl_dicts(file_path):
                yield adapter.validate_python(item, extra="forbid")
            return
        return read_jsonl_dicts(file_path)  # type: ignore

    def debuff_collections(
        self, validate: bool = False
    ) -> Iterable[RTD.DebuffCollections]:
        file_path = self.dir_path / SdeFileNames.DEBUFF_COLLECTIONS
        if validate:
            adapter = TypeAdapter(RTD.DebuffCollections)
            for item in read_jsonl_dicts(file_path):
                yield adapter.validate_python(item, extra="forbid")
            return
        return read_jsonl_dicts(file_path)  # type: ignore

    def dogma_attribute_categories(
        self, validate: bool = False
    ) -> Iterable[RTD.DogmaAttributeCategories]:
        file_path = self.dir_path / SdeFileNames.DOGMA_ATTRIBUTE_CATEGORIES
        if validate:
            adapter = TypeAdapter(RTD.DogmaAttributeCategories)
            for item in read_jsonl_dicts(file_path):
                yield adapter.validate_python(item, extra="forbid")
            return
        return read_jsonl_dicts(file_path)  # type: ignore

    def dogma_attributes(self, validate: bool = False) -> Iterable[RTD.DogmaAttributes]:
        file_path = self.dir_path / SdeFileNames.DOGMA_ATTRIBUTES
        if validate:
            adapter = TypeAdapter(RTD.DogmaAttributes)
            for item in read_jsonl_dicts(file_path):
                yield adapter.validate_python(item, extra="forbid")
            return
        return read_jsonl_dicts(file_path)  # type: ignore

    def dogma_effects(self, validate: bool = False) -> Iterable[RTD.DogmaEffects]:
        file_path = self.dir_path / SdeFileNames.DOGMA_EFFECTS
        if validate:
            adapter = TypeAdapter(RTD.DogmaEffects)
            for item in read_jsonl_dicts(file_path):
                yield adapter.validate_python(item, extra="forbid")
            return
        return read_jsonl_dicts(file_path)  # type: ignore

    def dogma_units(self, validate: bool = False) -> Iterable[RTD.DogmaUnits]:
        file_path = self.dir_path / SdeFileNames.DOGMA_UNITS
        if validate:
            adapter = TypeAdapter(RTD.DogmaUnits)
            for item in read_jsonl_dicts(file_path):
                yield adapter.validate_python(item, extra="forbid")
            return
        return read_jsonl_dicts(file_path)  # type: ignore

    def dynamic_item_attributes(
        self, validate: bool = False
    ) -> Iterable[RTD.DynamicItemAttributes]:
        file_path = self.dir_path / SdeFileNames.DYNAMIC_ITEM_ATTRIBUTES
        if validate:
            adapter = TypeAdapter(RTD.DynamicItemAttributes)
            for item in read_jsonl_dicts(file_path):
                yield adapter.validate_python(item, extra="forbid")
            return
        return read_jsonl_dicts(file_path)  # type: ignore

    def factions(self, validate: bool = False) -> Iterable[RTD.Factions]:
        file_path = self.dir_path / SdeFileNames.FACTIONS
        if validate:
            adapter = TypeAdapter(RTD.Factions)
            for item in read_jsonl_dicts(file_path):
                yield adapter.validate_python(item, extra="forbid")
            return
        return read_jsonl_dicts(file_path)  # type: ignore

    def freelance_job_schemas(self, validate: bool = False) -> RTD.FreelanceJobSchemas:
        file_path = self.dir_path / SdeFileNames.FREELANCE_JOB_SCHEMAS
        return next(iter(read_jsonl_dicts(file_path)))

    def graphics(self, validate: bool = False) -> Iterable[RTD.Graphics]:
        file_path = self.dir_path / SdeFileNames.GRAPHICS
        if validate:
            adapter = TypeAdapter(RTD.Graphics)
            for item in read_jsonl_dicts(file_path):
                yield adapter.validate_python(item, extra="forbid")
            return
        return read_jsonl_dicts(file_path)  # type: ignore

    def groups(self, validate: bool = False) -> Iterable[RTD.Groups]:
        file_path = self.dir_path / SdeFileNames.GROUPS
        if validate:
            adapter = TypeAdapter(RTD.Groups)
            for item in read_jsonl_dicts(file_path):
                yield adapter.validate_python(item, extra="forbid")
            return
        return read_jsonl_dicts(file_path)  # type: ignore

    def icons(self, validate: bool = False) -> Iterable[RTD.Icons]:
        file_path = self.dir_path / SdeFileNames.ICONS
        if validate:
            adapter = TypeAdapter(RTD.Icons)
            for item in read_jsonl_dicts(file_path):
                yield adapter.validate_python(item, extra="forbid")
            return
        return read_jsonl_dicts(file_path)  # type: ignore

    def landmarks(self, validate: bool = False) -> Iterable[RTD.Landmarks]:
        file_path = self.dir_path / SdeFileNames.LANDMARKS
        if validate:
            adapter = TypeAdapter(RTD.Landmarks)
            for item in read_jsonl_dicts(file_path):
                yield adapter.validate_python(item, extra="forbid")
            return
        return read_jsonl_dicts(file_path)  # type: ignore

    def map_asteroid_belts(
        self, validate: bool = False
    ) -> Iterable[RTD.MapAsteroidBelts]:
        file_path = self.dir_path / SdeFileNames.MAP_ASTEROID_BELTS
        if validate:
            adapter = TypeAdapter(RTD.MapAsteroidBelts)
            for item in read_jsonl_dicts(file_path):
                yield adapter.validate_python(item, extra="forbid")
            return
        return read_jsonl_dicts(file_path)  # type: ignore

    def map_constellations(
        self, validate: bool = False
    ) -> Iterable[RTD.MapConstellations]:
        file_path = self.dir_path / SdeFileNames.MAP_CONSTELLATIONS
        if validate:
            adapter = TypeAdapter(RTD.MapConstellations)
            for item in read_jsonl_dicts(file_path):
                yield adapter.validate_python(item, extra="forbid")
            return
        return read_jsonl_dicts(file_path)  # type: ignore

    def map_moons(self, validate: bool = False) -> Iterable[RTD.MapMoons]:
        file_path = self.dir_path / SdeFileNames.MAP_MOONS
        if validate:
            adapter = TypeAdapter(RTD.MapMoons)
            for item in read_jsonl_dicts(file_path):
                yield adapter.validate_python(item, extra="forbid")
            return
        return read_jsonl_dicts(file_path)  # type: ignore

    def map_planets(self, validate: bool = False) -> Iterable[RTD.MapPlanets]:
        file_path = self.dir_path / SdeFileNames.MAP_PLANETS
        if validate:
            adapter = TypeAdapter(RTD.MapPlanets)
            for item in read_jsonl_dicts(file_path):
                yield adapter.validate_python(item, extra="forbid")
            return
        return read_jsonl_dicts(file_path)  # type: ignore

    def map_regions(self, validate: bool = False) -> Iterable[RTD.MapRegions]:
        file_path = self.dir_path / SdeFileNames.MAP_REGIONS
        if validate:
            adapter = TypeAdapter(RTD.MapRegions)
            for item in read_jsonl_dicts(file_path):
                yield adapter.validate_python(item, extra="forbid")
            return
        return read_jsonl_dicts(file_path)  # type: ignore

    def map_solar_systems(
        self, validate: bool = False
    ) -> Iterable[RTD.MapSolarSystems]:
        file_path = self.dir_path / SdeFileNames.MAP_SOLAR_SYSTEMS
        if validate:
            adapter = TypeAdapter(RTD.MapSolarSystems)
            for item in read_jsonl_dicts(file_path):
                yield adapter.validate_python(item, extra="forbid")
            return
        return read_jsonl_dicts(file_path)  # type: ignore

    def map_stargates(self, validate: bool = False) -> Iterable[RTD.MapStargates]:
        file_path = self.dir_path / SdeFileNames.MAP_STARGATES
        if validate:
            adapter = TypeAdapter(RTD.MapStargates)
            for item in read_jsonl_dicts(file_path):
                yield adapter.validate_python(item, extra="forbid")
            return
        return read_jsonl_dicts(file_path)  # type: ignore

    def map_stars(self, validate: bool = False) -> Iterable[RTD.MapStars]:
        file_path = self.dir_path / SdeFileNames.MAP_STARS
        if validate:
            adapter = TypeAdapter(RTD.MapStars)
            for item in read_jsonl_dicts(file_path):
                yield adapter.validate_python(item, extra="forbid")
            return
        return read_jsonl_dicts(file_path)  # type: ignore

    def market_groups(self, validate: bool = False) -> Iterable[RTD.MarketGroups]:
        file_path = self.dir_path / SdeFileNames.MARKET_GROUPS
        if validate:
            adapter = TypeAdapter(RTD.MarketGroups)
            for item in read_jsonl_dicts(file_path):
                yield adapter.validate_python(item, extra="forbid")
            return
        return read_jsonl_dicts(file_path)  # type: ignore

    def masteries(self, validate: bool = False) -> Iterable[RTD.Masteries]:
        file_path = self.dir_path / SdeFileNames.MASTERIES
        if validate:
            adapter = TypeAdapter(RTD.Masteries)
            for item in read_jsonl_dicts(file_path):
                yield adapter.validate_python(item, extra="forbid")
            return
        return read_jsonl_dicts(file_path)  # type: ignore

    def meta_groups(self, validate: bool = False) -> Iterable[RTD.MetaGroups]:
        file_path = self.dir_path / SdeFileNames.META_GROUPS
        if validate:
            adapter = TypeAdapter(RTD.MetaGroups)
            for item in read_jsonl_dicts(file_path):
                yield adapter.validate_python(item, extra="forbid")
            return
        return read_jsonl_dicts(file_path)  # type: ignore

    def npc_characters(self, validate: bool = False) -> Iterable[RTD.NpcCharacters]:
        file_path = self.dir_path / SdeFileNames.NPC_CHARACTERS
        if validate:
            adapter = TypeAdapter(RTD.NpcCharacters)
            for item in read_jsonl_dicts(file_path):
                yield adapter.validate_python(item, extra="forbid")
            return
        return read_jsonl_dicts(file_path)  # type: ignore

    def npc_corporation_divisions(
        self, validate: bool = False
    ) -> Iterable[RTD.NpcCorporationDivisions]:
        file_path = self.dir_path / SdeFileNames.NPC_CORPORATION_DIVISIONS
        if validate:
            adapter = TypeAdapter(RTD.NpcCorporationDivisions)
            for item in read_jsonl_dicts(file_path):
                yield adapter.validate_python(item, extra="forbid")
            return
        return read_jsonl_dicts(file_path)  # type: ignore

    def npc_corporations(self, validate: bool = False) -> Iterable[RTD.NpcCorporations]:
        file_path = self.dir_path / SdeFileNames.NPC_CORPORATIONS
        if validate:
            adapter = TypeAdapter(RTD.NpcCorporations)
            for item in read_jsonl_dicts(file_path):
                yield adapter.validate_python(item, extra="forbid")
            return
        return read_jsonl_dicts(file_path)  # type: ignore

    def npc_stations(self, validate: bool = False) -> Iterable[RTD.NpcStations]:
        file_path = self.dir_path / SdeFileNames.NPC_STATIONS
        if validate:
            adapter = TypeAdapter(RTD.NpcStations)
            for item in read_jsonl_dicts(file_path):
                yield adapter.validate_python(item, extra="forbid")
            return
        return read_jsonl_dicts(file_path)  # type: ignore

    def planet_resources(self, validate: bool = False) -> Iterable[RTD.PlanetResources]:
        file_path = self.dir_path / SdeFileNames.PLANET_RESOURCES
        if validate:
            adapter = TypeAdapter(RTD.PlanetResources)
            for item in read_jsonl_dicts(file_path):
                yield adapter.validate_python(item, extra="forbid")
            return
        return read_jsonl_dicts(file_path)  # type: ignore

    def planet_schematics(
        self, validate: bool = False
    ) -> Iterable[RTD.PlanetSchematics]:
        file_path = self.dir_path / SdeFileNames.PLANET_SCHEMATICS
        if validate:
            adapter = TypeAdapter(RTD.PlanetSchematics)
            for item in read_jsonl_dicts(file_path):
                yield adapter.validate_python(item, extra="forbid")
            return
        return read_jsonl_dicts(file_path)  # type: ignore

    def races(self, validate: bool = False) -> Iterable[RTD.Races]:
        file_path = self.dir_path / SdeFileNames.RACES
        if validate:
            adapter = TypeAdapter(RTD.Races)
            for item in read_jsonl_dicts(file_path):
                yield adapter.validate_python(item, extra="forbid")
            return
        return read_jsonl_dicts(file_path)  # type: ignore

    def sde_info(self, validate: bool = False) -> RTD.SdeInfo:
        file_path = self.dir_path / SdeFileNames.SDE_INFO
        reader = read_jsonl_dicts(file_path)
        sde_info = next(iter(reader), None)
        if validate:
            adapter = TypeAdapter(RTD.SdeInfo)
            sde_info = adapter.validate_python(sde_info, extra="forbid")
            return sde_info
        if sde_info is None:
            raise ValueError("SDE info file is empty.")
        if not "buildNumber" in sde_info:
            raise ValueError("SDE info file is missing 'buildNumber' key.")
        return sde_info  # type: ignore

    def skin_licenses(self, validate: bool = False) -> Iterable[RTD.SkinLicenses]:
        file_path = self.dir_path / SdeFileNames.SKIN_LICENSES
        if validate:
            adapter = TypeAdapter(RTD.SkinLicenses)
            for item in read_jsonl_dicts(file_path):
                yield adapter.validate_python(item, extra="forbid")
            return
        return read_jsonl_dicts(file_path)  # type: ignore

    def skin_materials(self, validate: bool = False) -> Iterable[RTD.SkinMaterials]:
        file_path = self.dir_path / SdeFileNames.SKIN_MATERIALS
        if validate:
            adapter = TypeAdapter(RTD.SkinMaterials)
            for item in read_jsonl_dicts(file_path):
                yield adapter.validate_python(item, extra="forbid")
            return
        return read_jsonl_dicts(file_path)  # type: ignore

    def skins(self, validate: bool = False) -> Iterable[RTD.Skins]:
        file_path = self.dir_path / SdeFileNames.SKINS
        if validate:
            adapter = TypeAdapter(RTD.Skins)
            for item in read_jsonl_dicts(file_path):
                yield adapter.validate_python(item, extra="forbid")
            return
        return read_jsonl_dicts(file_path)  # type: ignore

    def sovereignty_upgrades(
        self, validate: bool = False
    ) -> Iterable[RTD.SovereigntyUpgrades]:
        file_path = self.dir_path / SdeFileNames.SOVEREIGNTY_UPGRADES
        if validate:
            adapter = TypeAdapter(RTD.SovereigntyUpgrades)
            for item in read_jsonl_dicts(file_path):
                yield adapter.validate_python(item, extra="forbid")
            return
        return read_jsonl_dicts(file_path)  # type: ignore

    def station_operations(
        self, validate: bool = False
    ) -> Iterable[RTD.StationOperations]:
        file_path = self.dir_path / SdeFileNames.STATION_OPERATIONS
        if validate:
            adapter = TypeAdapter(RTD.StationOperations)
            for item in read_jsonl_dicts(file_path):
                yield adapter.validate_python(item, extra="forbid")
            return
        return read_jsonl_dicts(file_path)  # type: ignore

    def station_services(self, validate: bool = False) -> Iterable[RTD.StationServices]:
        file_path = self.dir_path / SdeFileNames.STATION_SERVICES
        if validate:
            adapter = TypeAdapter(RTD.StationServices)
            for item in read_jsonl_dicts(file_path):
                yield adapter.validate_python(item, extra="forbid")
            return
        return read_jsonl_dicts(file_path)  # type: ignore

    def translation_languages(
        self, validate: bool = False
    ) -> Iterable[RTD.TranslationLanguages]:
        file_path = self.dir_path / SdeFileNames.TRANSLATION_LANGUAGES
        if validate:
            adapter = TypeAdapter(RTD.TranslationLanguages)
            for item in read_jsonl_dicts(file_path):
                yield adapter.validate_python(item, extra="forbid")
            return
        return read_jsonl_dicts(file_path)  # type: ignore

    def type_bonus(self, validate: bool = False) -> Iterable[RTD.TypeBonus]:
        file_path = self.dir_path / SdeFileNames.TYPE_BONUS
        if validate:
            adapter = TypeAdapter(RTD.TypeBonus)
            for item in read_jsonl_dicts(file_path):
                yield adapter.validate_python(item, extra="forbid")
            return
        return read_jsonl_dicts(file_path)  # type: ignore

    def type_dogma(self, validate: bool = False) -> Iterable[RTD.TypeDogma]:
        file_path = self.dir_path / SdeFileNames.TYPE_DOGMA
        if validate:
            adapter = TypeAdapter(RTD.TypeDogma)
            for item in read_jsonl_dicts(file_path):
                yield adapter.validate_python(item, extra="forbid")
            return
        return read_jsonl_dicts(file_path)  # type: ignore

    def type_materials(self, validate: bool = False) -> Iterable[RTD.TypeMaterials]:
        file_path = self.dir_path / SdeFileNames.TYPE_MATERIALS
        if validate:
            adapter = TypeAdapter(RTD.TypeMaterials)
            for item in read_jsonl_dicts(file_path):
                yield adapter.validate_python(item, extra="forbid")
            return
        return read_jsonl_dicts(file_path)  # type: ignore

    def eve_types(self, validate: bool = False) -> Iterable[RTD.EveTypes]:
        file_path = self.dir_path / SdeFileNames.TYPES
        if validate:
            adapter = TypeAdapter(RTD.EveTypes)
            for item in read_jsonl_dicts(file_path):
                yield adapter.validate_python(item, extra="forbid")
            return
        return read_jsonl_dicts(file_path)  # type: ignore

    def validate(self, file_name: SdeFileNames) -> None:
        """Validate a specific SDE file."""
        match file_name:
            case SdeFileNames.AGENTS_IN_SPACE:
                _ = list(self.agents_in_space(validate=True))
            case SdeFileNames.AGENT_TYPES:
                _ = list(self.agent_types(validate=True))
            case SdeFileNames.ANCESTRIES:
                _ = list(self.ancestries(validate=True))
            case SdeFileNames.BLOODLINES:
                _ = list(self.bloodlines(validate=True))
            case SdeFileNames.BLUEPRINTS:
                _ = list(self.blueprints(validate=True))
            case SdeFileNames.CATEGORIES:
                _ = list(self.categories(validate=True))
            case SdeFileNames.CERTIFICATES:
                _ = list(self.certificates(validate=True))
            case SdeFileNames.CHARACTER_ATTRIBUTES:
                _ = list(self.character_attributes(validate=True))
            case SdeFileNames.COMPRESSIBLE_TYPES:
                _ = list(self.compressible_types(validate=True))
            case SdeFileNames.CONTRABAND_TYPES:
                _ = list(self.contraband_types(validate=True))
            case SdeFileNames.CONTROL_TOWER_RESOURCES:
                _ = list(self.control_tower_resources(validate=True))
            case SdeFileNames.CORPORATION_ACTIVITIES:
                _ = list(self.corporation_activities(validate=True))
            case SdeFileNames.DEBUFF_COLLECTIONS:
                _ = list(self.debuff_collections(validate=True))
            case SdeFileNames.DOGMA_ATTRIBUTE_CATEGORIES:
                _ = list(self.dogma_attribute_categories(validate=True))
            case SdeFileNames.DOGMA_ATTRIBUTES:
                _ = list(self.dogma_attributes(validate=True))
            case SdeFileNames.DOGMA_EFFECTS:
                _ = list(self.dogma_effects(validate=True))
            case SdeFileNames.DOGMA_UNITS:
                _ = list(self.dogma_units(validate=True))
            case SdeFileNames.DYNAMIC_ITEM_ATTRIBUTES:
                _ = list(self.dynamic_item_attributes(validate=True))
            case SdeFileNames.FACTIONS:
                _ = list(self.factions(validate=True))
            case SdeFileNames.FREELANCE_JOB_SCHEMAS:
                _ = self.freelance_job_schemas(validate=True)
            case SdeFileNames.GRAPHICS:
                _ = list(self.graphics(validate=True))
            case SdeFileNames.GROUPS:
                _ = list(self.groups(validate=True))
            case SdeFileNames.ICONS:
                _ = list(self.icons(validate=True))
            case SdeFileNames.LANDMARKS:
                _ = list(self.landmarks(validate=True))
            case SdeFileNames.MAP_ASTEROID_BELTS:
                _ = list(self.map_asteroid_belts(validate=True))
            case SdeFileNames.MAP_CONSTELLATIONS:
                _ = list(self.map_constellations(validate=True))
            case SdeFileNames.MAP_MOONS:
                _ = list(self.map_moons(validate=True))
            case SdeFileNames.MAP_PLANETS:
                _ = list(self.map_planets(validate=True))
            case SdeFileNames.MAP_REGIONS:
                _ = list(self.map_regions(validate=True))
            case SdeFileNames.MAP_SOLAR_SYSTEMS:
                _ = list(self.map_solar_systems(validate=True))
            case SdeFileNames.MAP_STARGATES:
                _ = list(self.map_stargates(validate=True))
            case SdeFileNames.MAP_STARS:
                _ = list(self.map_stars(validate=True))
            case SdeFileNames.MARKET_GROUPS:
                _ = list(self.market_groups(validate=True))
            case SdeFileNames.MASTERIES:
                _ = list(self.masteries(validate=True))
            case SdeFileNames.META_GROUPS:
                _ = list(self.meta_groups(validate=True))
            case SdeFileNames.NPC_CHARACTERS:
                _ = list(self.npc_characters(validate=True))
            case SdeFileNames.NPC_CORPORATION_DIVISIONS:
                _ = list(self.npc_corporation_divisions(validate=True))
            case SdeFileNames.NPC_CORPORATIONS:
                _ = list(self.npc_corporations(validate=True))
            case SdeFileNames.NPC_STATIONS:
                _ = list(self.npc_stations(validate=True))
            case SdeFileNames.PLANET_RESOURCES:
                _ = list(self.planet_resources(validate=True))
            case SdeFileNames.PLANET_SCHEMATICS:
                _ = list(self.planet_schematics(validate=True))
            case SdeFileNames.RACES:
                _ = list(self.races(validate=True))
            case SdeFileNames.SDE_INFO:
                _ = self.sde_info(validate=True)
            case SdeFileNames.SKIN_LICENSES:
                _ = list(self.skin_licenses(validate=True))
            case SdeFileNames.SKIN_MATERIALS:
                _ = list(self.skin_materials(validate=True))
            case SdeFileNames.SKINS:
                _ = list(self.skins(validate=True))
            case SdeFileNames.SOVEREIGNTY_UPGRADES:
                _ = list(self.sovereignty_upgrades(validate=True))
            case SdeFileNames.STATION_OPERATIONS:
                _ = list(self.station_operations(validate=True))
            case SdeFileNames.STATION_SERVICES:
                _ = list(self.station_services(validate=True))
            case SdeFileNames.TRANSLATION_LANGUAGES:
                _ = list(self.translation_languages(validate=True))
            case SdeFileNames.TYPE_BONUS:
                _ = list(self.type_bonus(validate=True))
            case SdeFileNames.TYPE_DOGMA:
                _ = list(self.type_dogma(validate=True))
            case SdeFileNames.TYPE_MATERIALS:
                _ = list(self.type_materials(validate=True))
            case SdeFileNames.TYPES:
                _ = list(self.eve_types(validate=True))
            case _:
                raise ValueError(f"Unknown SDE file name: {file_name}")

    def validate_all(self) -> None:
        """Validate all SDE files."""
        for file_name in SdeFileNames:
            self.validate(file_name)
