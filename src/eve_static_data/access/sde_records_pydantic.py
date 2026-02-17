"""SDE dataset records access implementation with the data imported to Pydantic models."""
# ruff: noqa: D102

import logging
from collections.abc import Iterable
from pathlib import Path
from typing import Any

from eve_static_data.access.sde_records import SdeRecords
from eve_static_data.models import sde_pydantic as PM

logger = logging.getLogger(__name__)


class SDERecordsPydantic:
    """A file access class that reads raw JSON files and returns Pydantic models."""

    def __init__(self, sde_dir: Path) -> None:
        """Initialize SDE dataset file access.

        Args:
            sde_dir: Path to the SDE data directory.
        """
        self.sde_dir = sde_dir
        self.access = SdeRecords(sde_dir)

    def agents_in_space(self, **kwargs: dict[str, Any]) -> Iterable[PM.AgentsInSpace]:
        """Records from the agentsInSpace.jsonl dataset."""
        for item in self.access.agents_in_space():
            yield PM.AgentsInSpace.model_validate(item)

    def agent_types(self, **kwargs: dict[str, Any]) -> Iterable[PM.AgentTypes]:
        """Records from the agentTypes.jsonl dataset."""
        for item in self.access.agent_types():
            yield PM.AgentTypes.model_validate(item)

    def ancestries(self, **kwargs: dict[str, Any]) -> Iterable[PM.Ancestries]:
        """Records from the ancestries.jsonl dataset."""
        for item in self.access.ancestries():
            yield PM.Ancestries.model_validate(item)

    def bloodlines(self, **kwargs: dict[str, Any]) -> Iterable[PM.Bloodlines]:
        """Records from the bloodlines.jsonl dataset."""
        for item in self.access.bloodlines():
            yield PM.Bloodlines.model_validate(item)

    def blueprints(self, **kwargs: dict[str, Any]) -> Iterable[PM.Blueprints]:
        """Records from the blueprints.jsonl dataset."""
        for item in self.access.blueprints():
            yield PM.Blueprints.model_validate(item)

    def categories(self, **kwargs: dict[str, Any]) -> Iterable[PM.Categories]:
        """Records from the categories.jsonl dataset."""
        for item in self.access.categories():
            yield PM.Categories.model_validate(item)

    def certificates(self, **kwargs: dict[str, Any]) -> Iterable[PM.Certificates]:
        """Records from the certificates.jsonl dataset."""
        for item in self.access.certificates():
            yield PM.Certificates.model_validate(item)

    def character_attributes(
        self, **kwargs: dict[str, Any]
    ) -> Iterable[PM.CharacterAttributes]:
        """Records from the characterAttributes.jsonl dataset."""
        for item in self.access.character_attributes():
            yield PM.CharacterAttributes.model_validate(item)

    def clone_grades(self, **kwargs: dict[str, Any]) -> Iterable[PM.CloneGrades]:
        """Records from the cloneGrades.jsonl dataset."""
        for item in self.access.clone_grades():
            yield PM.CloneGrades.model_validate(item)

    def compressible_types(
        self, **kwargs: dict[str, Any]
    ) -> Iterable[PM.CompressibleTypes]:
        """Records from the compressibleTypes.jsonl dataset."""
        for item in self.access.compressible_types():
            yield PM.CompressibleTypes.model_validate(item)

    def contraband_types(
        self, **kwargs: dict[str, Any]
    ) -> Iterable[PM.ContrabandTypes]:
        """Records from the contrabandTypes.jsonl dataset."""
        for item in self.access.contraband_types():
            yield PM.ContrabandTypes.model_validate(item)

    def control_tower_resources(
        self, **kwargs: dict[str, Any]
    ) -> Iterable[PM.ControlTowerResources]:
        """Records from the controlTowerResources.jsonl dataset."""
        for item in self.access.control_tower_resources():
            yield PM.ControlTowerResources.model_validate(item)

    def corporation_activities(
        self, **kwargs: dict[str, Any]
    ) -> Iterable[PM.CorporationActivities]:
        """Records from the corporationActivities.jsonl dataset."""
        for item in self.access.corporation_activities():
            yield PM.CorporationActivities.model_validate(item)

    def debuff_collections(
        self, **kwargs: dict[str, Any]
    ) -> Iterable[PM.DebuffCollections]:
        """Records from the dbuffCollections.jsonl dataset."""
        for item in self.access.debuff_collections():
            yield PM.DebuffCollections.model_validate(item)

    def dogma_attribute_categories(
        self, **kwargs: dict[str, Any]
    ) -> Iterable[PM.DogmaAttributeCategories]:
        """Records from the dogmaAttributeCategories.jsonl dataset."""
        for item in self.access.dogma_attribute_categories():
            yield PM.DogmaAttributeCategories.model_validate(item)

    def dogma_attributes(
        self, **kwargs: dict[str, Any]
    ) -> Iterable[PM.DogmaAttributes]:
        """Records from the dogmaAttributes.jsonl dataset."""
        for item in self.access.dogma_attributes():
            yield PM.DogmaAttributes.model_validate(item)

    def dogma_effects(self, **kwargs: dict[str, Any]) -> Iterable[PM.DogmaEffects]:
        """Records from the dogmaEffects.jsonl dataset."""
        for item in self.access.dogma_effects():
            yield PM.DogmaEffects.model_validate(item)

    def dogma_units(self, **kwargs: dict[str, Any]) -> Iterable[PM.DogmaUnits]:
        """Records from the dogmaUnits.jsonl dataset."""
        for item in self.access.dogma_units():
            yield PM.DogmaUnits.model_validate(item)

    def dynamic_item_attributes(
        self, **kwargs: dict[str, Any]
    ) -> Iterable[PM.DynamicItemAttributes]:
        """Records from the dynamicItemAttributes.jsonl dataset."""
        for item in self.access.dynamic_item_attributes():
            yield PM.DynamicItemAttributes.model_validate(item)

    def factions(self, **kwargs: dict[str, Any]) -> Iterable[PM.Factions]:
        """Records from the factions.jsonl dataset."""
        for item in self.access.factions():
            yield PM.Factions.model_validate(item)

    def freelance_job_schemas(self, **kwargs: dict[str, Any]) -> PM.FreelanceJobSchemas:
        """Records from the freelanceJobSchemas.jsonl dataset."""
        return PM.FreelanceJobSchemas.model_validate(
            self.access.freelance_job_schemas()
        )

    def graphics(self, **kwargs: dict[str, Any]) -> Iterable[PM.Graphics]:
        """Records from the graphics.jsonl dataset."""
        for item in self.access.graphics():
            yield PM.Graphics.model_validate(item)

    def groups(self, **kwargs: dict[str, Any]) -> Iterable[PM.Groups]:
        """Records from the groups.jsonl dataset."""
        for item in self.access.groups():
            yield PM.Groups.model_validate(item)

    def icons(self, **kwargs: dict[str, Any]) -> Iterable[PM.Icons]:
        """Records from the icons.jsonl dataset."""
        for item in self.access.icons():
            yield PM.Icons.model_validate(item)

    def landmarks(self, **kwargs: dict[str, Any]) -> Iterable[PM.Landmarks]:
        """Records from the landmarks.jsonl dataset."""
        for item in self.access.landmarks():
            yield PM.Landmarks.model_validate(item)

    def map_asteroid_belts(
        self, **kwargs: dict[str, Any]
    ) -> Iterable[PM.MapAsteroidBelts]:
        """Records from the mapAsteroidBelts.jsonl dataset."""
        for item in self.access.map_asteroid_belts():
            yield PM.MapAsteroidBelts.model_validate(item)

    def map_constellations(
        self, **kwargs: dict[str, Any]
    ) -> Iterable[PM.MapConstellations]:
        """Records from the mapConstellations.jsonl dataset."""
        for item in self.access.map_constellations():
            yield PM.MapConstellations.model_validate(item)

    def map_moons(self, **kwargs: dict[str, Any]) -> Iterable[PM.MapMoons]:
        """Records from the mapMoons.jsonl dataset."""
        for item in self.access.map_moons():
            yield PM.MapMoons.model_validate(item)

    def map_planets(self, **kwargs: dict[str, Any]) -> Iterable[PM.MapPlanets]:
        """Records from the mapPlanets.jsonl dataset."""
        for item in self.access.map_planets():
            yield PM.MapPlanets.model_validate(item)

    def map_regions(self, **kwargs: dict[str, Any]) -> Iterable[PM.MapRegions]:
        """Records from the mapRegions.jsonl dataset."""
        for item in self.access.map_regions():
            yield PM.MapRegions.model_validate(item)

    def map_solar_systems(
        self, **kwargs: dict[str, Any]
    ) -> Iterable[PM.MapSolarSystems]:
        """Records from the mapSolarSystems.jsonl dataset."""
        for item in self.access.map_solar_systems():
            yield PM.MapSolarSystems.model_validate(item)

    def map_stargates(self, **kwargs: dict[str, Any]) -> Iterable[PM.MapStargates]:
        """Records from the mapStargates.jsonl dataset."""
        for item in self.access.map_stargates():
            yield PM.MapStargates.model_validate(item)

    def map_stars(self, **kwargs: dict[str, Any]) -> Iterable[PM.MapStars]:
        """Records from the mapStars.jsonl dataset."""
        for item in self.access.map_stars():
            yield PM.MapStars.model_validate(item)

    def market_groups(self, **kwargs: dict[str, Any]) -> Iterable[PM.MarketGroups]:
        """Records from the marketGroups.jsonl dataset."""
        for item in self.access.market_groups():
            yield PM.MarketGroups.model_validate(item)

    def masteries(self, **kwargs: dict[str, Any]) -> Iterable[PM.Masteries]:
        """Records from the masteries.jsonl dataset."""
        for item in self.access.masteries():
            yield PM.Masteries.model_validate(item)

    def meta_groups(self, **kwargs: dict[str, Any]) -> Iterable[PM.MetaGroups]:
        """Records from the metaGroups.jsonl dataset."""
        for item in self.access.meta_groups():
            yield PM.MetaGroups.model_validate(item)

    def npc_characters(self, **kwargs: dict[str, Any]) -> Iterable[PM.NpcCharacters]:
        """Records from the npcCharacters.jsonl dataset."""
        for item in self.access.npc_characters():
            yield PM.NpcCharacters.model_validate(item)

    def npc_corporation_divisions(
        self, **kwargs: dict[str, Any]
    ) -> Iterable[PM.NpcCorporationDivisions]:
        """Records from the npcCorporationDivisions.jsonl dataset."""
        for item in self.access.npc_corporation_divisions():
            yield PM.NpcCorporationDivisions.model_validate(item)

    def npc_corporations(
        self, **kwargs: dict[str, Any]
    ) -> Iterable[PM.NpcCorporations]:
        """Records from the npcCorporations.jsonl dataset."""
        for item in self.access.npc_corporations():
            yield PM.NpcCorporations.model_validate(item)

    def npc_stations(self, **kwargs: dict[str, Any]) -> Iterable[PM.NpcStations]:
        """Records from the npcStations.jsonl dataset."""
        for item in self.access.npc_stations():
            yield PM.NpcStations.model_validate(item)

    def planet_resources(
        self, **kwargs: dict[str, Any]
    ) -> Iterable[PM.PlanetResources]:
        """Records from the planetResources.jsonl dataset."""
        for item in self.access.planet_resources():
            yield PM.PlanetResources.model_validate(item)

    def planet_schematics(
        self, **kwargs: dict[str, Any]
    ) -> Iterable[PM.PlanetSchematics]:
        """Records from the planetSchematics.jsonl dataset."""
        for item in self.access.planet_schematics():
            yield PM.PlanetSchematics.model_validate(item)

    def races(self, **kwargs: dict[str, Any]) -> Iterable[PM.Races]:
        """Records from the races.jsonl dataset."""
        for item in self.access.races():
            yield PM.Races.model_validate(item)

    def sde_info(self, **kwargs: dict[str, Any]) -> PM.SdeInfo:
        """Records from the _sde.jsonl dataset."""
        return PM.SdeInfo.model_validate(self.access.sde_info())

    def skin_licenses(self, **kwargs: dict[str, Any]) -> Iterable[PM.SkinLicenses]:
        """Records from the skinLicenses.jsonl dataset."""
        for item in self.access.skin_licenses():
            yield PM.SkinLicenses.model_validate(item)

    def skin_materials(self, **kwargs: dict[str, Any]) -> Iterable[PM.SkinMaterials]:
        """Records from the skinMaterials.jsonl dataset."""
        for item in self.access.skin_materials():
            yield PM.SkinMaterials.model_validate(item)

    def skins(self, **kwargs: dict[str, Any]) -> Iterable[PM.Skins]:
        """Records from the skins.jsonl dataset."""
        for item in self.access.skins():
            yield PM.Skins.model_validate(item)

    def sovereignty_upgrades(
        self, **kwargs: dict[str, Any]
    ) -> Iterable[PM.SovereigntyUpgrades]:
        """Records from the sovereigntyUpgrades.jsonl dataset."""
        for item in self.access.sovereignty_upgrades():
            yield PM.SovereigntyUpgrades.model_validate(item)

    def station_operations(
        self, **kwargs: dict[str, Any]
    ) -> Iterable[PM.StationOperations]:
        """Records from the stationOperations.jsonl dataset."""
        for item in self.access.station_operations():
            yield PM.StationOperations.model_validate(item)

    def station_services(
        self, **kwargs: dict[str, Any]
    ) -> Iterable[PM.StationServices]:
        """Records from the stationServices.jsonl dataset."""
        for item in self.access.station_services():
            yield PM.StationServices.model_validate(item)

    def translation_languages(
        self, **kwargs: dict[str, Any]
    ) -> Iterable[PM.TranslationLanguages]:
        """Records from the translationLanguages.jsonl dataset."""
        for item in self.access.translation_languages():
            yield PM.TranslationLanguages.model_validate(item)

    def type_bonus(self, **kwargs: dict[str, Any]) -> Iterable[PM.TypeBonus]:
        """Records from the typeBonus.jsonl dataset."""
        for item in self.access.type_bonus():
            yield PM.TypeBonus.model_validate(item)

    def type_dogma(self, **kwargs: dict[str, Any]) -> Iterable[PM.TypeDogma]:
        """Records from the typeDogma.jsonl dataset."""
        for item in self.access.type_dogma():
            yield PM.TypeDogma.model_validate(item)

    def type_materials(self, **kwargs: dict[str, Any]) -> Iterable[PM.TypeMaterials]:
        """Records from the typeMaterials.jsonl dataset."""
        for item in self.access.type_materials():
            yield PM.TypeMaterials.model_validate(item)

    def eve_types(self, **kwargs: dict[str, Any]) -> Iterable[PM.EveTypes]:
        """Records from the types.jsonl dataset."""
        for item in self.access.eve_types():
            yield PM.EveTypes.model_validate(item)
