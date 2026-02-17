"""Lookup for pydantic models corresponding to SDE datasets."""

from typing import TypedDict

from pydantic import BaseModel

import eve_static_data.models.raw_pydantic as PM
import eve_static_data.models.raw_td as TDM
from eve_static_data.models.sde_datasets import SdeDatasets

DatasetPydanticModels: dict[SdeDatasets, type[BaseModel]] = {
    SdeDatasets.AGENTS_IN_SPACE: PM.AgentsInSpace,
    SdeDatasets.AGENT_TYPES: PM.AgentTypes,
    SdeDatasets.ANCESTRIES: PM.Ancestries,
    SdeDatasets.BLOODLINES: PM.Bloodlines,
    SdeDatasets.BLUEPRINTS: PM.Blueprints,
    SdeDatasets.CATEGORIES: PM.Categories,
    SdeDatasets.CERTIFICATES: PM.Certificates,
    SdeDatasets.CHARACTER_ATTRIBUTES: PM.CharacterAttributes,
    SdeDatasets.CLONE_GRADES: PM.CloneGrades,
    SdeDatasets.COMPRESSIBLE_TYPES: PM.CompressibleTypes,
    SdeDatasets.CONTRABAND_TYPES: PM.ContrabandTypes,
    SdeDatasets.CONTROL_TOWER_RESOURCES: PM.ControlTowerResources,
    SdeDatasets.CORPORATION_ACTIVITIES: PM.CorporationActivities,
    SdeDatasets.DEBUFF_COLLECTIONS: PM.DebuffCollections,
    SdeDatasets.DOGMA_ATTRIBUTE_CATEGORIES: PM.DogmaAttributeCategories,
    SdeDatasets.DOGMA_ATTRIBUTES: PM.DogmaAttributes,
    SdeDatasets.DOGMA_EFFECTS: PM.DogmaEffects,
    SdeDatasets.DOGMA_UNITS: PM.DogmaUnits,
    SdeDatasets.DYNAMIC_ITEM_ATTRIBUTES: PM.DynamicItemAttributes,
    SdeDatasets.FACTIONS: PM.Factions,
    SdeDatasets.FREELANCE_JOB_SCHEMAS: PM.FreelanceJobSchemas,
    SdeDatasets.GRAPHICS: PM.Graphics,
    SdeDatasets.GROUPS: PM.Groups,
    SdeDatasets.ICONS: PM.Icons,
    SdeDatasets.LANDMARKS: PM.Landmarks,
    SdeDatasets.MAP_ASTEROID_BELTS: PM.MapAsteroidBelts,
    SdeDatasets.MAP_CONSTELLATIONS: PM.MapConstellations,
    SdeDatasets.MAP_MOONS: PM.MapMoons,
    SdeDatasets.MAP_PLANETS: PM.MapPlanets,
    SdeDatasets.MAP_REGIONS: PM.MapRegions,
    SdeDatasets.MAP_SOLAR_SYSTEMS: PM.MapSolarSystems,
    SdeDatasets.MAP_STARGATES: PM.MapStargates,
    SdeDatasets.MAP_STARS: PM.MapStars,
    SdeDatasets.MARKET_GROUPS: PM.MarketGroups,
    SdeDatasets.MASTERIES: PM.Masteries,
    SdeDatasets.META_GROUPS: PM.MetaGroups,
    SdeDatasets.NPC_CHARACTERS: PM.NpcCharacters,
    SdeDatasets.NPC_CORPORATION_DIVISIONS: PM.NpcCorporationDivisions,
    SdeDatasets.NPC_CORPORATIONS: PM.NpcCorporations,
    SdeDatasets.NPC_STATIONS: PM.NpcStations,
    SdeDatasets.PLANET_RESOURCES: PM.PlanetResources,
    SdeDatasets.PLANET_SCHEMATICS: PM.PlanetSchematics,
    SdeDatasets.RACES: PM.Races,
    SdeDatasets.SDE_INFO: PM.SdeInfo,
    SdeDatasets.SKIN_LICENSES: PM.SkinLicenses,
    SdeDatasets.SKIN_MATERIALS: PM.SkinMaterials,
    SdeDatasets.SKINS: PM.Skins,
    SdeDatasets.SOVEREIGNTY_UPGRADES: PM.SovereigntyUpgrades,
    SdeDatasets.STATION_OPERATIONS: PM.StationOperations,
    SdeDatasets.STATION_SERVICES: PM.StationServices,
    SdeDatasets.TRANSLATION_LANGUAGES: PM.TranslationLanguages,
    SdeDatasets.TYPE_BONUS: PM.TypeBonus,
    SdeDatasets.TYPE_DOGMA: PM.TypeDogma,
    SdeDatasets.TYPE_MATERIALS: PM.TypeMaterials,
    SdeDatasets.TYPES: PM.EveTypes,
}
DatasetTDModels: dict[SdeDatasets, type[TypedDict]] = {  # type: ignore
    SdeDatasets.AGENTS_IN_SPACE: TDM.AgentsInSpace,
    SdeDatasets.AGENT_TYPES: TDM.AgentTypes,
    SdeDatasets.ANCESTRIES: TDM.Ancestries,
    SdeDatasets.BLOODLINES: TDM.Bloodlines,
    SdeDatasets.BLUEPRINTS: TDM.Blueprints,
    SdeDatasets.CATEGORIES: TDM.Categories,
    SdeDatasets.CERTIFICATES: TDM.Certificates,
    SdeDatasets.CHARACTER_ATTRIBUTES: TDM.CharacterAttributes,
    SdeDatasets.CLONE_GRADES: TDM.CloneGrades,
    SdeDatasets.COMPRESSIBLE_TYPES: TDM.CompressibleTypes,
    SdeDatasets.CONTRABAND_TYPES: TDM.ContrabandTypes,
    SdeDatasets.CONTROL_TOWER_RESOURCES: TDM.ControlTowerResources,
    SdeDatasets.CORPORATION_ACTIVITIES: TDM.CorporationActivities,
    SdeDatasets.DEBUFF_COLLECTIONS: TDM.DebuffCollections,
    SdeDatasets.DOGMA_ATTRIBUTE_CATEGORIES: TDM.DogmaAttributeCategories,
    SdeDatasets.DOGMA_ATTRIBUTES: TDM.DogmaAttributes,
    SdeDatasets.DOGMA_EFFECTS: TDM.DogmaEffects,
    SdeDatasets.DOGMA_UNITS: TDM.DogmaUnits,
    SdeDatasets.DYNAMIC_ITEM_ATTRIBUTES: TDM.DynamicItemAttributes,
    SdeDatasets.FACTIONS: TDM.Factions,
    SdeDatasets.FREELANCE_JOB_SCHEMAS: TDM.FreelanceJobSchemas,
    SdeDatasets.GRAPHICS: TDM.Graphics,
    SdeDatasets.GROUPS: TDM.Groups,
    SdeDatasets.ICONS: TDM.Icons,
    SdeDatasets.LANDMARKS: TDM.Landmarks,
    SdeDatasets.MAP_ASTEROID_BELTS: TDM.MapAsteroidBelts,
    SdeDatasets.MAP_CONSTELLATIONS: TDM.MapConstellations,
    SdeDatasets.MAP_MOONS: TDM.MapMoons,
    SdeDatasets.MAP_PLANETS: TDM.MapPlanets,
    SdeDatasets.MAP_REGIONS: TDM.MapRegions,
    SdeDatasets.MAP_SOLAR_SYSTEMS: TDM.MapSolarSystems,
    SdeDatasets.MAP_STARGATES: TDM.MapStargates,
    SdeDatasets.MAP_STARS: TDM.MapStars,
    SdeDatasets.MARKET_GROUPS: TDM.MarketGroups,
    SdeDatasets.MASTERIES: TDM.Masteries,
    SdeDatasets.META_GROUPS: TDM.MetaGroups,
    SdeDatasets.NPC_CHARACTERS: TDM.NpcCharacters,
    SdeDatasets.NPC_CORPORATION_DIVISIONS: TDM.NpcCorporationDivisions,
    SdeDatasets.NPC_CORPORATIONS: TDM.NpcCorporations,
    SdeDatasets.NPC_STATIONS: TDM.NpcStations,
    SdeDatasets.PLANET_RESOURCES: TDM.PlanetResources,
    SdeDatasets.PLANET_SCHEMATICS: TDM.PlanetSchematics,
    SdeDatasets.RACES: TDM.Races,
    SdeDatasets.SDE_INFO: TDM.SdeInfo,
    SdeDatasets.SKIN_LICENSES: TDM.SkinLicenses,
    SdeDatasets.SKIN_MATERIALS: TDM.SkinMaterials,
    SdeDatasets.SKINS: TDM.Skins,
    SdeDatasets.SOVEREIGNTY_UPGRADES: TDM.SovereigntyUpgrades,
    SdeDatasets.STATION_OPERATIONS: TDM.StationOperations,
    SdeDatasets.STATION_SERVICES: TDM.StationServices,
    SdeDatasets.TRANSLATION_LANGUAGES: TDM.TranslationLanguages,
    SdeDatasets.TYPE_BONUS: TDM.TypeBonus,
    SdeDatasets.TYPE_DOGMA: TDM.TypeDogma,
    SdeDatasets.TYPE_MATERIALS: TDM.TypeMaterials,
    SdeDatasets.TYPES: TDM.EveTypes,
}


def dataset_pydantic_model_lookup(dataset: SdeDatasets) -> type[BaseModel]:
    """Lookup the pydantic model for a given dataset."""
    if dataset not in DatasetPydanticModels:
        raise ValueError(f"No pydantic model found for dataset: {dataset}")
    return DatasetPydanticModels[dataset]


def dataset_td_model_lookup(dataset: SdeDatasets) -> type[TypedDict]:  # type: ignore
    """Lookup the TypedDict model for a given dataset."""
    if dataset not in DatasetTDModels:
        raise ValueError(f"No TypedDict model found for dataset: {dataset}")
    return DatasetTDModels[dataset]
