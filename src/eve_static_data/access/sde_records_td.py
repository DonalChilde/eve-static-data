"""SDE dataset records access implementation with the data cast to TypedDicts."""
# ruff: noqa: D102

import logging
from collections.abc import Iterable
from pathlib import Path
from typing import Any, cast

from eve_static_data.access.sde_records import SdeRecords
from eve_static_data.models import sde_typeddict as RTD

logger = logging.getLogger(__name__)


class SDERecordsTD:
    """A file access class that reads raw JSON files and returns TypedDicts.

    This class is a convenience for devs, as all it does is cast the raw JSON dicts to the appropriate TypedDicts.
    """

    def __init__(self, sde_dir: Path) -> None:
        """Initialize SDE dataset file access.

        Args:
            sde_dir: Path to the SDE data directory.
        """
        self.sde_dir = sde_dir
        self.access = SdeRecords(sde_dir)

    def agents_in_space(self, **kwargs: dict[str, Any]) -> Iterable[RTD.AgentsInSpace]:
        """Records from the agentsInSpace.jsonl dataset."""
        for item in self.access.agents_in_space():
            yield cast(RTD.AgentsInSpace, item)

    def agent_types(self, **kwargs: dict[str, Any]) -> Iterable[RTD.AgentTypes]:
        """Records from the agentTypes.jsonl dataset."""
        for item in self.access.agent_types():
            yield cast(RTD.AgentTypes, item)

    def ancestries(self, **kwargs: dict[str, Any]) -> Iterable[RTD.Ancestries]:
        """Records from the ancestries.jsonl dataset."""
        for item in self.access.ancestries():
            yield cast(RTD.Ancestries, item)

    def bloodlines(self, **kwargs: dict[str, Any]) -> Iterable[RTD.Bloodlines]:
        """Records from the bloodlines.jsonl dataset."""
        for item in self.access.bloodlines():
            yield cast(RTD.Bloodlines, item)

    def blueprints(self, **kwargs: dict[str, Any]) -> Iterable[RTD.Blueprints]:
        """Records from the blueprints.jsonl dataset."""
        for item in self.access.blueprints():
            yield cast(RTD.Blueprints, item)

    def categories(self, **kwargs: dict[str, Any]) -> Iterable[RTD.Categories]:
        """Records from the categories.jsonl dataset."""
        for item in self.access.categories():
            yield cast(RTD.Categories, item)

    def certificates(self, **kwargs: dict[str, Any]) -> Iterable[RTD.Certificates]:
        """Records from the certificates.jsonl dataset."""
        for item in self.access.certificates():
            yield cast(RTD.Certificates, item)

    def character_attributes(
        self, **kwargs: dict[str, Any]
    ) -> Iterable[RTD.CharacterAttributes]:
        """Records from the characterAttributes.jsonl dataset."""
        for item in self.access.character_attributes():
            yield cast(RTD.CharacterAttributes, item)

    def clone_grades(self, **kwargs: dict[str, Any]) -> Iterable[RTD.CloneGrades]:
        """Records from the cloneGrades.jsonl dataset."""
        for item in self.access.clone_grades():
            yield cast(RTD.CloneGrades, item)

    def compressible_types(
        self, **kwargs: dict[str, Any]
    ) -> Iterable[RTD.CompressibleTypes]:
        """Records from the compressibleTypes.jsonl dataset."""
        for item in self.access.compressible_types():
            yield cast(RTD.CompressibleTypes, item)

    def contraband_types(
        self, **kwargs: dict[str, Any]
    ) -> Iterable[RTD.ContrabandTypes]:
        """Records from the contrabandTypes.jsonl dataset."""
        for item in self.access.contraband_types():
            yield cast(RTD.ContrabandTypes, item)

    def control_tower_resources(
        self, **kwargs: dict[str, Any]
    ) -> Iterable[RTD.ControlTowerResources]:
        """Records from the controlTowerResources.jsonl dataset."""
        for item in self.access.control_tower_resources():
            yield cast(RTD.ControlTowerResources, item)

    def corporation_activities(
        self, **kwargs: dict[str, Any]
    ) -> Iterable[RTD.CorporationActivities]:
        """Records from the corporationActivities.jsonl dataset."""
        for item in self.access.corporation_activities():
            yield cast(RTD.CorporationActivities, item)

    def debuff_collections(
        self, **kwargs: dict[str, Any]
    ) -> Iterable[RTD.DebuffCollections]:
        """Records from the dbuffCollections.jsonl dataset."""
        for item in self.access.debuff_collections():
            yield cast(RTD.DebuffCollections, item)

    def dogma_attribute_categories(
        self, **kwargs: dict[str, Any]
    ) -> Iterable[RTD.DogmaAttributeCategories]:
        """Records from the dogmaAttributeCategories.jsonl dataset."""
        for item in self.access.dogma_attribute_categories():
            yield cast(RTD.DogmaAttributeCategories, item)

    def dogma_attributes(
        self, **kwargs: dict[str, Any]
    ) -> Iterable[RTD.DogmaAttributes]:
        """Records from the dogmaAttributes.jsonl dataset."""
        for item in self.access.dogma_attributes():
            yield cast(RTD.DogmaAttributes, item)

    def dogma_effects(self, **kwargs: dict[str, Any]) -> Iterable[RTD.DogmaEffects]:
        """Records from the dogmaEffects.jsonl dataset."""
        for item in self.access.dogma_effects():
            yield cast(RTD.DogmaEffects, item)

    def dogma_units(self, **kwargs: dict[str, Any]) -> Iterable[RTD.DogmaUnits]:
        """Records from the dogmaUnits.jsonl dataset."""
        for item in self.access.dogma_units():
            yield cast(RTD.DogmaUnits, item)

    def dynamic_item_attributes(
        self, **kwargs: dict[str, Any]
    ) -> Iterable[RTD.DynamicItemAttributes]:
        """Records from the dynamicItemAttributes.jsonl dataset."""
        for item in self.access.dynamic_item_attributes():
            yield cast(RTD.DynamicItemAttributes, item)

    def factions(self, **kwargs: dict[str, Any]) -> Iterable[RTD.Factions]:
        """Records from the factions.jsonl dataset."""
        for item in self.access.factions():
            yield cast(RTD.Factions, item)

    def freelance_job_schemas(
        self, **kwargs: dict[str, Any]
    ) -> RTD.FreelanceJobSchemas:
        """Records from the freelanceJobSchemas.jsonl dataset."""
        return cast(
            RTD.FreelanceJobSchemas,
            next(iter(self.access.freelance_job_schemas())),
        )

    def graphics(self, **kwargs: dict[str, Any]) -> Iterable[RTD.Graphics]:
        """Records from the graphics.jsonl dataset."""
        for item in self.access.graphics():
            yield cast(RTD.Graphics, item)

    def groups(self, **kwargs: dict[str, Any]) -> Iterable[RTD.Groups]:
        """Records from the groups.jsonl dataset."""
        for item in self.access.groups():
            yield cast(RTD.Groups, item)

    def icons(self, **kwargs: dict[str, Any]) -> Iterable[RTD.Icons]:
        """Records from the icons.jsonl dataset."""
        for item in self.access.icons():
            yield cast(RTD.Icons, item)

    def landmarks(self, **kwargs: dict[str, Any]) -> Iterable[RTD.Landmarks]:
        """Records from the landmarks.jsonl dataset."""
        for item in self.access.landmarks():
            yield cast(RTD.Landmarks, item)

    def map_asteroid_belts(
        self, **kwargs: dict[str, Any]
    ) -> Iterable[RTD.MapAsteroidBelts]:
        """Records from the mapAsteroidBelts.jsonl dataset."""
        for item in self.access.map_asteroid_belts():
            yield cast(RTD.MapAsteroidBelts, item)

    def map_constellations(
        self, **kwargs: dict[str, Any]
    ) -> Iterable[RTD.MapConstellations]:
        """Records from the mapConstellations.jsonl dataset."""
        for item in self.access.map_constellations():
            yield cast(RTD.MapConstellations, item)

    def map_moons(self, **kwargs: dict[str, Any]) -> Iterable[RTD.MapMoons]:
        """Records from the mapMoons.jsonl dataset."""
        for item in self.access.map_moons():
            yield cast(RTD.MapMoons, item)

    def map_planets(self, **kwargs: dict[str, Any]) -> Iterable[RTD.MapPlanets]:
        """Records from the mapPlanets.jsonl dataset."""
        for item in self.access.map_planets():
            yield cast(RTD.MapPlanets, item)

    def map_regions(self, **kwargs: dict[str, Any]) -> Iterable[RTD.MapRegions]:
        """Records from the mapRegions.jsonl dataset."""
        for item in self.access.map_regions():
            yield cast(RTD.MapRegions, item)

    def map_solar_systems(
        self, **kwargs: dict[str, Any]
    ) -> Iterable[RTD.MapSolarSystems]:
        """Records from the mapSolarSystems.jsonl dataset."""
        for item in self.access.map_solar_systems():
            yield cast(RTD.MapSolarSystems, item)

    def map_stargates(self, **kwargs: dict[str, Any]) -> Iterable[RTD.MapStargates]:
        """Records from the mapStargates.jsonl dataset."""
        for item in self.access.map_stargates():
            yield cast(RTD.MapStargates, item)

    def map_stars(self, **kwargs: dict[str, Any]) -> Iterable[RTD.MapStars]:
        """Records from the mapStars.jsonl dataset."""
        for item in self.access.map_stars():
            yield cast(RTD.MapStars, item)

    def market_groups(self, **kwargs: dict[str, Any]) -> Iterable[RTD.MarketGroups]:
        """Records from the marketGroups.jsonl dataset."""
        for item in self.access.market_groups():
            yield cast(RTD.MarketGroups, item)

    def masteries(self, **kwargs: dict[str, Any]) -> Iterable[RTD.Masteries]:
        """Records from the masteries.jsonl dataset."""
        for item in self.access.masteries():
            yield cast(RTD.Masteries, item)

    def meta_groups(self, **kwargs: dict[str, Any]) -> Iterable[RTD.MetaGroups]:
        """Records from the metaGroups.jsonl dataset."""
        for item in self.access.meta_groups():
            yield cast(RTD.MetaGroups, item)

    def npc_characters(self, **kwargs: dict[str, Any]) -> Iterable[RTD.NpcCharacters]:
        """Records from the npcCharacters.jsonl dataset."""
        for item in self.access.npc_characters():
            yield cast(RTD.NpcCharacters, item)

    def npc_corporation_divisions(
        self, **kwargs: dict[str, Any]
    ) -> Iterable[RTD.NpcCorporationDivisions]:
        """Records from the npcCorporationDivisions.jsonl dataset."""
        for item in self.access.npc_corporation_divisions():
            yield cast(RTD.NpcCorporationDivisions, item)

    def npc_corporations(
        self, **kwargs: dict[str, Any]
    ) -> Iterable[RTD.NpcCorporations]:
        """Records from the npcCorporations.jsonl dataset."""
        for item in self.access.npc_corporations():
            yield cast(RTD.NpcCorporations, item)

    def npc_stations(self, **kwargs: dict[str, Any]) -> Iterable[RTD.NpcStations]:
        """Records from the npcStations.jsonl dataset."""
        for item in self.access.npc_stations():
            yield cast(RTD.NpcStations, item)

    def planet_resources(
        self, **kwargs: dict[str, Any]
    ) -> Iterable[RTD.PlanetResources]:
        """Records from the planetResources.jsonl dataset."""
        for item in self.access.planet_resources():
            yield cast(RTD.PlanetResources, item)

    def planet_schematics(
        self, **kwargs: dict[str, Any]
    ) -> Iterable[RTD.PlanetSchematics]:
        """Records from the planetSchematics.jsonl dataset."""
        for item in self.access.planet_schematics():
            yield cast(RTD.PlanetSchematics, item)

    def races(self, **kwargs: dict[str, Any]) -> Iterable[RTD.Races]:
        """Records from the races.jsonl dataset."""
        for item in self.access.races():
            yield cast(RTD.Races, item)

    def sde_info(self, **kwargs: dict[str, Any]) -> RTD.SdeInfo:
        """Records from the _sde.jsonl dataset."""
        return cast(RTD.SdeInfo, self.access.sde_info())

    def skin_licenses(self, **kwargs: dict[str, Any]) -> Iterable[RTD.SkinLicenses]:
        """Records from the skinLicenses.jsonl dataset."""
        for item in self.access.skin_licenses():
            yield cast(RTD.SkinLicenses, item)

    def skin_materials(self, **kwargs: dict[str, Any]) -> Iterable[RTD.SkinMaterials]:
        """Records from the skinMaterials.jsonl dataset."""
        for item in self.access.skin_materials():
            yield cast(RTD.SkinMaterials, item)

    def skins(self, **kwargs: dict[str, Any]) -> Iterable[RTD.Skins]:
        """Records from the skins.jsonl dataset."""
        for item in self.access.skins():
            yield cast(RTD.Skins, item)

    def sovereignty_upgrades(
        self, **kwargs: dict[str, Any]
    ) -> Iterable[RTD.SovereigntyUpgrades]:
        """Records from the sovereigntyUpgrades.jsonl dataset."""
        for item in self.access.sovereignty_upgrades():
            yield cast(RTD.SovereigntyUpgrades, item)

    def station_operations(
        self, **kwargs: dict[str, Any]
    ) -> Iterable[RTD.StationOperations]:
        """Records from the stationOperations.jsonl dataset."""
        for item in self.access.station_operations():
            yield cast(RTD.StationOperations, item)

    def station_services(
        self, **kwargs: dict[str, Any]
    ) -> Iterable[RTD.StationServices]:
        """Records from the stationServices.jsonl dataset."""
        for item in self.access.station_services():
            yield cast(RTD.StationServices, item)

    def translation_languages(
        self, **kwargs: dict[str, Any]
    ) -> Iterable[RTD.TranslationLanguages]:
        """Records from the translationLanguages.jsonl dataset."""
        for item in self.access.translation_languages():
            yield cast(RTD.TranslationLanguages, item)

    def type_bonus(self, **kwargs: dict[str, Any]) -> Iterable[RTD.TypeBonus]:
        """Records from the typeBonus.jsonl dataset."""
        for item in self.access.type_bonus():
            yield cast(RTD.TypeBonus, item)

    def type_dogma(self, **kwargs: dict[str, Any]) -> Iterable[RTD.TypeDogma]:
        """Records from the typeDogma.jsonl dataset."""
        for item in self.access.type_dogma():
            yield cast(RTD.TypeDogma, item)

    def type_materials(self, **kwargs: dict[str, Any]) -> Iterable[RTD.TypeMaterials]:
        """Records from the typeMaterials.jsonl dataset."""
        for item in self.access.type_materials():
            yield cast(RTD.TypeMaterials, item)

    def eve_types(self, **kwargs: dict[str, Any]) -> Iterable[RTD.EveTypes]:
        """Records from the types.jsonl dataset."""
        for item in self.access.eve_types():
            yield cast(RTD.EveTypes, item)
