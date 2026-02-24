"""Lookup for pydantic models corresponding to SDE datasets.

Used in validation.
"""

from typing import TypedDict

import eve_static_data.models.records.sde_pydantic as PM
import eve_static_data.models.records.sde_typeddict as TDM
from eve_static_data.models.datasets.sde_dataset_files import SdeDatasetFiles

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


# def dataset_pydantic_model_lookup(
#     dataset: SdeDatasetFiles,
# ) -> type[PM.SdeDatasetRecord]:
#     """Lookup the pydantic model for a given dataset."""
#     if dataset not in DatasetPydanticModels:
#         raise ValueError(f"No pydantic model found for dataset: {dataset}")
#     return DatasetPydanticModels[dataset]


# def dataset_td_model_lookup(dataset: SdeDatasetFiles) -> type[TypedDict]:  # type: ignore
#     """Lookup the TypedDict model for a given dataset."""
#     if dataset not in DatasetTDModels:
#         raise ValueError(f"No TypedDict model found for dataset: {dataset}")
#     return DatasetTDModels[dataset]


def dataset_td_model_lookup(dataset: SdeDatasetFiles) -> type[TypedDict]:  # type: ignore
    """Lookup the TypedDict model for a given dataset."""
    match dataset:
        case SdeDatasetFiles.AGENTS_IN_SPACE:
            return TDM.AgentsInSpace
        case SdeDatasetFiles.AGENT_TYPES:
            return TDM.AgentTypes
        case SdeDatasetFiles.ANCESTRIES:
            return TDM.Ancestries
        case SdeDatasetFiles.BLOODLINES:
            return TDM.Bloodlines
        case SdeDatasetFiles.BLUEPRINTS:
            return TDM.Blueprints
        case SdeDatasetFiles.CATEGORIES:
            return TDM.Categories
        case SdeDatasetFiles.CERTIFICATES:
            return TDM.Certificates
        case SdeDatasetFiles.CHARACTER_ATTRIBUTES:
            return TDM.CharacterAttributes
        case SdeDatasetFiles.CLONE_GRADES:
            return TDM.CloneGrades
        case SdeDatasetFiles.COMPRESSIBLE_TYPES:
            return TDM.CompressibleTypes
        case SdeDatasetFiles.CONTRABAND_TYPES:
            return TDM.ContrabandTypes
        case SdeDatasetFiles.CONTROL_TOWER_RESOURCES:
            return TDM.ControlTowerResources
        case SdeDatasetFiles.CORPORATION_ACTIVITIES:
            return TDM.CorporationActivities
        case SdeDatasetFiles.DEBUFF_COLLECTIONS:
            return TDM.DebuffCollections
        case SdeDatasetFiles.DOGMA_ATTRIBUTE_CATEGORIES:
            return TDM.DogmaAttributeCategories
        case SdeDatasetFiles.DOGMA_ATTRIBUTES:
            return TDM.DogmaAttributes
        case SdeDatasetFiles.DOGMA_EFFECTS:
            return TDM.DogmaEffects
        case SdeDatasetFiles.DOGMA_UNITS:
            return TDM.DogmaUnits
        case SdeDatasetFiles.DYNAMIC_ITEM_ATTRIBUTES:
            return TDM.DynamicItemAttributes
        case SdeDatasetFiles.FACTIONS:
            return TDM.Factions
        case SdeDatasetFiles.FREELANCE_JOB_SCHEMAS:
            return TDM.FreelanceJobSchemas
        case SdeDatasetFiles.GRAPHICS:
            return TDM.Graphics
        case SdeDatasetFiles.GROUPS:
            return TDM.Groups
        case SdeDatasetFiles.ICONS:
            return TDM.Icons
        case SdeDatasetFiles.LANDMARKS:
            return TDM.Landmarks
        case SdeDatasetFiles.MAP_ASTEROID_BELTS:
            return TDM.MapAsteroidBelts
        case SdeDatasetFiles.MAP_CONSTELLATIONS:
            return TDM.MapConstellations
        case SdeDatasetFiles.MAP_MOONS:
            return TDM.MapMoons
        case SdeDatasetFiles.MAP_PLANETS:
            return TDM.MapPlanets
        case SdeDatasetFiles.MAP_REGIONS:
            return TDM.MapRegions
        case SdeDatasetFiles.MAP_SOLAR_SYSTEMS:
            return TDM.MapSolarSystems
        case SdeDatasetFiles.MAP_STARGATES:
            return TDM.MapStargates
        case SdeDatasetFiles.MAP_STARS:
            return TDM.MapStars
        case SdeDatasetFiles.MARKET_GROUPS:
            return TDM.MarketGroups
        case SdeDatasetFiles.MASTERIES:
            return TDM.Masteries
        case SdeDatasetFiles.META_GROUPS:
            return TDM.MetaGroups
        case SdeDatasetFiles.NPC_CHARACTERS:
            return TDM.NpcCharacters
        case SdeDatasetFiles.NPC_CORPORATION_DIVISIONS:
            return TDM.NpcCorporationDivisions
        case SdeDatasetFiles.NPC_CORPORATIONS:
            return TDM.NpcCorporations
        case SdeDatasetFiles.NPC_STATIONS:
            return TDM.NpcStations
        case SdeDatasetFiles.PLANET_RESOURCES:
            return TDM.PlanetResources
        case SdeDatasetFiles.PLANET_SCHEMATICS:
            return TDM.PlanetSchematics
        case SdeDatasetFiles.RACES:
            return TDM.Races
        case SdeDatasetFiles.SDE_INFO:
            return TDM.SdeInfo
        case SdeDatasetFiles.SKIN_LICENSES:
            return TDM.SkinLicenses
        case SdeDatasetFiles.SKIN_MATERIALS:
            return TDM.SkinMaterials
        case SdeDatasetFiles.SKINS:
            return TDM.Skins
        case SdeDatasetFiles.SOVEREIGNTY_UPGRADES:
            return TDM.SovereigntyUpgrades
        case SdeDatasetFiles.STATION_OPERATIONS:
            return TDM.StationOperations
        case SdeDatasetFiles.STATION_SERVICES:
            return TDM.StationServices
        case SdeDatasetFiles.TRANSLATION_LANGUAGES:
            return TDM.TranslationLanguages
        case SdeDatasetFiles.TYPE_BONUS:
            return TDM.TypeBonus
        case SdeDatasetFiles.TYPE_DOGMA:
            return TDM.TypeDogma
        case SdeDatasetFiles.TYPE_MATERIALS:
            return TDM.TypeMaterials
        case SdeDatasetFiles.TYPES:
            return TDM.EveTypes
        case _:
            raise ValueError(f"No TypedDict model found for dataset: {dataset}")


def dataset_pydantic_model_lookup(
    dataset: SdeDatasetFiles,
) -> type[PM.SdeDatasetRecord]:
    """Lookup the pydantic model for a given dataset."""
    match dataset:
        case SdeDatasetFiles.AGENTS_IN_SPACE:
            return PM.AgentsInSpace
        case SdeDatasetFiles.AGENT_TYPES:
            return PM.AgentTypes
        case SdeDatasetFiles.ANCESTRIES:
            return PM.Ancestries
        case SdeDatasetFiles.BLOODLINES:
            return PM.Bloodlines
        case SdeDatasetFiles.BLUEPRINTS:
            return PM.Blueprints
        case SdeDatasetFiles.CATEGORIES:
            return PM.Categories
        case SdeDatasetFiles.CERTIFICATES:
            return PM.Certificates
        case SdeDatasetFiles.CHARACTER_ATTRIBUTES:
            return PM.CharacterAttributes
        case SdeDatasetFiles.CLONE_GRADES:
            return PM.CloneGrades
        case SdeDatasetFiles.COMPRESSIBLE_TYPES:
            return PM.CompressibleTypes
        case SdeDatasetFiles.CONTRABAND_TYPES:
            return PM.ContrabandTypes
        case SdeDatasetFiles.CONTROL_TOWER_RESOURCES:
            return PM.ControlTowerResources
        case SdeDatasetFiles.CORPORATION_ACTIVITIES:
            return PM.CorporationActivities
        case SdeDatasetFiles.DEBUFF_COLLECTIONS:
            return PM.DebuffCollections
        case SdeDatasetFiles.DOGMA_ATTRIBUTE_CATEGORIES:
            return PM.DogmaAttributeCategories
        case SdeDatasetFiles.DOGMA_ATTRIBUTES:
            return PM.DogmaAttributes
        case SdeDatasetFiles.DOGMA_EFFECTS:
            return PM.DogmaEffects
        case SdeDatasetFiles.DOGMA_UNITS:
            return PM.DogmaUnits
        case SdeDatasetFiles.DYNAMIC_ITEM_ATTRIBUTES:
            return PM.DynamicItemAttributes
        case SdeDatasetFiles.FACTIONS:
            return PM.Factions
        case SdeDatasetFiles.FREELANCE_JOB_SCHEMAS:
            return PM.FreelanceJobSchemas
        case SdeDatasetFiles.GRAPHICS:
            return PM.Graphics
        case SdeDatasetFiles.GROUPS:
            return PM.Groups
        case SdeDatasetFiles.ICONS:
            return PM.Icons
        case SdeDatasetFiles.LANDMARKS:
            return PM.Landmarks
        case SdeDatasetFiles.MAP_ASTEROID_BELTS:
            return PM.MapAsteroidBelts
        case SdeDatasetFiles.MAP_CONSTELLATIONS:
            return PM.MapConstellations
        case SdeDatasetFiles.MAP_MOONS:
            return PM.MapMoons
        case SdeDatasetFiles.MAP_PLANETS:
            return PM.MapPlanets
        case SdeDatasetFiles.MAP_REGIONS:
            return PM.MapRegions
        case SdeDatasetFiles.MAP_SOLAR_SYSTEMS:
            return PM.MapSolarSystems
        case SdeDatasetFiles.MAP_STARGATES:
            return PM.MapStargates
        case SdeDatasetFiles.MAP_STARS:
            return PM.MapStars
        case SdeDatasetFiles.MARKET_GROUPS:
            return PM.MarketGroups
        case SdeDatasetFiles.MASTERIES:
            return PM.Masteries
        case SdeDatasetFiles.META_GROUPS:
            return PM.MetaGroups
        case SdeDatasetFiles.NPC_CHARACTERS:
            return PM.NpcCharacters
        case SdeDatasetFiles.NPC_CORPORATION_DIVISIONS:
            return PM.NpcCorporationDivisions
        case SdeDatasetFiles.NPC_CORPORATIONS:
            return PM.NpcCorporations
        case SdeDatasetFiles.NPC_STATIONS:
            return PM.NpcStations
        case SdeDatasetFiles.PLANET_RESOURCES:
            return PM.PlanetResources
        case SdeDatasetFiles.PLANET_SCHEMATICS:
            return PM.PlanetSchematics
        case SdeDatasetFiles.RACES:
            return PM.Races
        case SdeDatasetFiles.SDE_INFO:
            return PM.SdeInfo
        case SdeDatasetFiles.SKIN_LICENSES:
            return PM.SkinLicenses
        case SdeDatasetFiles.SKIN_MATERIALS:
            return PM.SkinMaterials
        case SdeDatasetFiles.SKINS:
            return PM.Skins
        case SdeDatasetFiles.SOVEREIGNTY_UPGRADES:
            return PM.SovereigntyUpgrades
        case SdeDatasetFiles.STATION_OPERATIONS:
            return PM.StationOperations
        case SdeDatasetFiles.STATION_SERVICES:
            return PM.StationServices
        case SdeDatasetFiles.TRANSLATION_LANGUAGES:
            return PM.TranslationLanguages
        case SdeDatasetFiles.TYPE_BONUS:
            return PM.TypeBonus
        case SdeDatasetFiles.TYPE_DOGMA:
            return PM.TypeDogma
        case SdeDatasetFiles.TYPE_MATERIALS:
            return PM.TypeMaterials
        case SdeDatasetFiles.TYPES:
            return PM.EveTypes
        case _:
            raise ValueError(f"No pydantic model found for dataset: {dataset}")
