"""Lookup for pydantic models corresponding to SDE datasets."""

from typing import TypedDict

import eve_static_data.models.sde_pydantic as PM
import eve_static_data.models.sde_typeddict as TDM
from eve_static_data.models.sde_dataset_files import SdeDatasetFiles

DatasetPydanticModels: dict[SdeDatasetFiles, type[PM.SdeDatasetRecord]] = {
    SdeDatasetFiles.AGENTS_IN_SPACE: PM.AgentsInSpace,
    SdeDatasetFiles.AGENT_TYPES: PM.AgentTypes,
    SdeDatasetFiles.ANCESTRIES: PM.Ancestries,
    SdeDatasetFiles.BLOODLINES: PM.Bloodlines,
    SdeDatasetFiles.BLUEPRINTS: PM.Blueprints,
    SdeDatasetFiles.CATEGORIES: PM.Categories,
    SdeDatasetFiles.CERTIFICATES: PM.Certificates,
    SdeDatasetFiles.CHARACTER_ATTRIBUTES: PM.CharacterAttributes,
    SdeDatasetFiles.CLONE_GRADES: PM.CloneGrades,
    SdeDatasetFiles.COMPRESSIBLE_TYPES: PM.CompressibleTypes,
    SdeDatasetFiles.CONTRABAND_TYPES: PM.ContrabandTypes,
    SdeDatasetFiles.CONTROL_TOWER_RESOURCES: PM.ControlTowerResources,
    SdeDatasetFiles.CORPORATION_ACTIVITIES: PM.CorporationActivities,
    SdeDatasetFiles.DEBUFF_COLLECTIONS: PM.DebuffCollections,
    SdeDatasetFiles.DOGMA_ATTRIBUTE_CATEGORIES: PM.DogmaAttributeCategories,
    SdeDatasetFiles.DOGMA_ATTRIBUTES: PM.DogmaAttributes,
    SdeDatasetFiles.DOGMA_EFFECTS: PM.DogmaEffects,
    SdeDatasetFiles.DOGMA_UNITS: PM.DogmaUnits,
    SdeDatasetFiles.DYNAMIC_ITEM_ATTRIBUTES: PM.DynamicItemAttributes,
    SdeDatasetFiles.FACTIONS: PM.Factions,
    SdeDatasetFiles.FREELANCE_JOB_SCHEMAS: PM.FreelanceJobSchemas,
    SdeDatasetFiles.GRAPHICS: PM.Graphics,
    SdeDatasetFiles.GROUPS: PM.Groups,
    SdeDatasetFiles.ICONS: PM.Icons,
    SdeDatasetFiles.LANDMARKS: PM.Landmarks,
    SdeDatasetFiles.MAP_ASTEROID_BELTS: PM.MapAsteroidBelts,
    SdeDatasetFiles.MAP_CONSTELLATIONS: PM.MapConstellations,
    SdeDatasetFiles.MAP_MOONS: PM.MapMoons,
    SdeDatasetFiles.MAP_PLANETS: PM.MapPlanets,
    SdeDatasetFiles.MAP_REGIONS: PM.MapRegions,
    SdeDatasetFiles.MAP_SOLAR_SYSTEMS: PM.MapSolarSystems,
    SdeDatasetFiles.MAP_STARGATES: PM.MapStargates,
    SdeDatasetFiles.MAP_STARS: PM.MapStars,
    SdeDatasetFiles.MARKET_GROUPS: PM.MarketGroups,
    SdeDatasetFiles.MASTERIES: PM.Masteries,
    SdeDatasetFiles.META_GROUPS: PM.MetaGroups,
    SdeDatasetFiles.NPC_CHARACTERS: PM.NpcCharacters,
    SdeDatasetFiles.NPC_CORPORATION_DIVISIONS: PM.NpcCorporationDivisions,
    SdeDatasetFiles.NPC_CORPORATIONS: PM.NpcCorporations,
    SdeDatasetFiles.NPC_STATIONS: PM.NpcStations,
    SdeDatasetFiles.PLANET_RESOURCES: PM.PlanetResources,
    SdeDatasetFiles.PLANET_SCHEMATICS: PM.PlanetSchematics,
    SdeDatasetFiles.RACES: PM.Races,
    SdeDatasetFiles.SDE_INFO: PM.SdeInfo,
    SdeDatasetFiles.SKIN_LICENSES: PM.SkinLicenses,
    SdeDatasetFiles.SKIN_MATERIALS: PM.SkinMaterials,
    SdeDatasetFiles.SKINS: PM.Skins,
    SdeDatasetFiles.SOVEREIGNTY_UPGRADES: PM.SovereigntyUpgrades,
    SdeDatasetFiles.STATION_OPERATIONS: PM.StationOperations,
    SdeDatasetFiles.STATION_SERVICES: PM.StationServices,
    SdeDatasetFiles.TRANSLATION_LANGUAGES: PM.TranslationLanguages,
    SdeDatasetFiles.TYPE_BONUS: PM.TypeBonus,
    SdeDatasetFiles.TYPE_DOGMA: PM.TypeDogma,
    SdeDatasetFiles.TYPE_MATERIALS: PM.TypeMaterials,
    SdeDatasetFiles.TYPES: PM.EveTypes,
}
DatasetTDModels: dict[SdeDatasetFiles, type[TypedDict]] = {  # type: ignore
    SdeDatasetFiles.AGENTS_IN_SPACE: TDM.AgentsInSpace,
    SdeDatasetFiles.AGENT_TYPES: TDM.AgentTypes,
    SdeDatasetFiles.ANCESTRIES: TDM.Ancestries,
    SdeDatasetFiles.BLOODLINES: TDM.Bloodlines,
    SdeDatasetFiles.BLUEPRINTS: TDM.Blueprints,
    SdeDatasetFiles.CATEGORIES: TDM.Categories,
    SdeDatasetFiles.CERTIFICATES: TDM.Certificates,
    SdeDatasetFiles.CHARACTER_ATTRIBUTES: TDM.CharacterAttributes,
    SdeDatasetFiles.CLONE_GRADES: TDM.CloneGrades,
    SdeDatasetFiles.COMPRESSIBLE_TYPES: TDM.CompressibleTypes,
    SdeDatasetFiles.CONTRABAND_TYPES: TDM.ContrabandTypes,
    SdeDatasetFiles.CONTROL_TOWER_RESOURCES: TDM.ControlTowerResources,
    SdeDatasetFiles.CORPORATION_ACTIVITIES: TDM.CorporationActivities,
    SdeDatasetFiles.DEBUFF_COLLECTIONS: TDM.DebuffCollections,
    SdeDatasetFiles.DOGMA_ATTRIBUTE_CATEGORIES: TDM.DogmaAttributeCategories,
    SdeDatasetFiles.DOGMA_ATTRIBUTES: TDM.DogmaAttributes,
    SdeDatasetFiles.DOGMA_EFFECTS: TDM.DogmaEffects,
    SdeDatasetFiles.DOGMA_UNITS: TDM.DogmaUnits,
    SdeDatasetFiles.DYNAMIC_ITEM_ATTRIBUTES: TDM.DynamicItemAttributes,
    SdeDatasetFiles.FACTIONS: TDM.Factions,
    SdeDatasetFiles.FREELANCE_JOB_SCHEMAS: TDM.FreelanceJobSchemas,
    SdeDatasetFiles.GRAPHICS: TDM.Graphics,
    SdeDatasetFiles.GROUPS: TDM.Groups,
    SdeDatasetFiles.ICONS: TDM.Icons,
    SdeDatasetFiles.LANDMARKS: TDM.Landmarks,
    SdeDatasetFiles.MAP_ASTEROID_BELTS: TDM.MapAsteroidBelts,
    SdeDatasetFiles.MAP_CONSTELLATIONS: TDM.MapConstellations,
    SdeDatasetFiles.MAP_MOONS: TDM.MapMoons,
    SdeDatasetFiles.MAP_PLANETS: TDM.MapPlanets,
    SdeDatasetFiles.MAP_REGIONS: TDM.MapRegions,
    SdeDatasetFiles.MAP_SOLAR_SYSTEMS: TDM.MapSolarSystems,
    SdeDatasetFiles.MAP_STARGATES: TDM.MapStargates,
    SdeDatasetFiles.MAP_STARS: TDM.MapStars,
    SdeDatasetFiles.MARKET_GROUPS: TDM.MarketGroups,
    SdeDatasetFiles.MASTERIES: TDM.Masteries,
    SdeDatasetFiles.META_GROUPS: TDM.MetaGroups,
    SdeDatasetFiles.NPC_CHARACTERS: TDM.NpcCharacters,
    SdeDatasetFiles.NPC_CORPORATION_DIVISIONS: TDM.NpcCorporationDivisions,
    SdeDatasetFiles.NPC_CORPORATIONS: TDM.NpcCorporations,
    SdeDatasetFiles.NPC_STATIONS: TDM.NpcStations,
    SdeDatasetFiles.PLANET_RESOURCES: TDM.PlanetResources,
    SdeDatasetFiles.PLANET_SCHEMATICS: TDM.PlanetSchematics,
    SdeDatasetFiles.RACES: TDM.Races,
    SdeDatasetFiles.SDE_INFO: TDM.SdeInfo,
    SdeDatasetFiles.SKIN_LICENSES: TDM.SkinLicenses,
    SdeDatasetFiles.SKIN_MATERIALS: TDM.SkinMaterials,
    SdeDatasetFiles.SKINS: TDM.Skins,
    SdeDatasetFiles.SOVEREIGNTY_UPGRADES: TDM.SovereigntyUpgrades,
    SdeDatasetFiles.STATION_OPERATIONS: TDM.StationOperations,
    SdeDatasetFiles.STATION_SERVICES: TDM.StationServices,
    SdeDatasetFiles.TRANSLATION_LANGUAGES: TDM.TranslationLanguages,
    SdeDatasetFiles.TYPE_BONUS: TDM.TypeBonus,
    SdeDatasetFiles.TYPE_DOGMA: TDM.TypeDogma,
    SdeDatasetFiles.TYPE_MATERIALS: TDM.TypeMaterials,
    SdeDatasetFiles.TYPES: TDM.EveTypes,
}


def dataset_pydantic_model_lookup(
    dataset: SdeDatasetFiles,
) -> type[PM.SdeDatasetRecord]:
    """Lookup the pydantic model for a given dataset."""
    if dataset not in DatasetPydanticModels:
        raise ValueError(f"No pydantic model found for dataset: {dataset}")
    return DatasetPydanticModels[dataset]


def dataset_td_model_lookup(dataset: SdeDatasetFiles) -> type[TypedDict]:  # type: ignore
    """Lookup the TypedDict model for a given dataset."""
    if dataset not in DatasetTDModels:
        raise ValueError(f"No TypedDict model found for dataset: {dataset}")
    return DatasetTDModels[dataset]
