"""Pydantic models for YAML SDE datasets.

These are useful, despite the greatly increased loading time, because the datamodel declares
more structure guarantees.

YAML allows integer keys in mappings, but JSON does not. This is the reason that the JSONL
and YAML SDE files have different models. The YAML model is easier to reason with, but the JSONL
model is more performant to load. If the YAML datasets are exported to JSON, the load time
decreases dramatically (60x), and the same models can be used for validation and parsing.
If the Pydantic RootModels are used to load the JSON files, then pydantic handles the
type conversion of the dict keys from string to int.

The addition of a `key_id` field to the dataclass models will allow the same models to be used
when returning records from the database. This field would be None when loading from the
YAML/JSON files, but would be populated with the appropriate key when loading from from the
database. This would allow the same models to be used for all three use cases, and would
eliminate the need for separate models for the YAML/JSON datasets and database records.

Some specific datasets may required a more complex database return model. TBD.
"""

from dataclasses import dataclass
from typing import Any

from pydantic import Field, RootModel

# ------------------------------------------------------------------------------
# Common model definitions.
# ------------------------------------------------------------------------------


@dataclass
class LocalizedString:
    """Type definition for LocalizedString.

    Source info: SDE file: translationLanguages.jsonl
    """

    en: str = "NOT_TRANSLATED"
    de: str = "NOT_TRANSLATED"
    fr: str = "NOT_TRANSLATED"
    ja: str = "NOT_TRANSLATED"
    zh: str = "NOT_TRANSLATED"
    ru: str = "NOT_TRANSLATED"
    ko: str = "NOT_TRANSLATED"
    es: str = "NOT_TRANSLATED"


@dataclass
class Materials:
    """Model used in multiple datasets for materials, e.g. in blueprints and typeMaterials."""

    typeID: int
    quantity: int


@dataclass
class Skills:
    """Model used in multiple datasets for skills, e.g. in blueprints and npcCharacters."""

    typeID: int
    level: int


@dataclass
class Color:
    """Model used in multiple datasets for color, e.g. in metaGroups."""

    b: float
    g: float
    r: float


@dataclass
class Position:
    """Model used in multiple datasets for position, e.g. in celestialObjects and npcCharacters."""

    x: float
    y: float
    z: float


@dataclass
class Position2D:
    """Model used in multiple datasets for 2D position, e.g. in mapSolarSystems."""

    x: float
    y: float


# ------------------------------------------------------------------------------
# File level Pydantic model definitions.
# ------------------------------------------------------------------------------


@dataclass(slots=True, kw_only=True)
class AgentsInSpace:
    """Model for the agentsInSpace.yaml dataset."""

    agents_in_space_id: int | None = None
    dungeonID: int
    solarSystemID: int
    spawnPointID: int
    typeID: int


@dataclass(slots=True, kw_only=True)
class AgentTypes:
    """Model for the agentTypes.yaml dataset."""

    agent_types_id: int | None = None
    name: str


@dataclass(slots=True, kw_only=True)
class Ancestries:
    """Model for the ancestries.yaml dataset."""

    ancestries_id: int | None = None
    bloodlineID: int
    charisma: int
    description: LocalizedString
    iconID: int | None = None
    intelligence: int
    memory: int
    name: LocalizedString
    perception: int
    shortDescription: str | None = None
    willpower: int


@dataclass(slots=True, kw_only=True)
class Bloodlines:
    """Model for the bloodlines.yaml dataset."""

    bloodlines_id: int | None = None
    charisma: int
    corporationID: int
    description: LocalizedString
    iconID: int | None = None
    intelligence: int
    memory: int
    name: LocalizedString
    perception: int
    raceID: int
    willpower: int


@dataclass(slots=True, kw_only=True)
class Blueprints_Products:
    """Nested model for the blueprints.jsonl SDE file."""

    typeID: int
    quantity: int
    probability: float | None = None


@dataclass(slots=True, kw_only=True)
class Blueprints_Activity:
    """Nested model for the blueprints.jsonl SDE file."""

    materials: list[Materials] | None = None
    skills: list[Skills] | None = None
    time: int
    products: list[Blueprints_Products] | None = None


@dataclass(slots=True, kw_only=True)
class Blueprints_Activities:
    """Nested model for the blueprints.jsonl SDE file."""

    copying: Blueprints_Activity | None = None
    invention: Blueprints_Activity | None = None
    manufacturing: Blueprints_Activity | None = None
    reaction: Blueprints_Activity | None = None
    research_material: Blueprints_Activity | None = None
    research_time: Blueprints_Activity | None = None


@dataclass(slots=True, kw_only=True)
class Blueprints:
    """Model for the blueprints.jsonl SDE file."""

    blueprints_id: int | None = None
    activities: Blueprints_Activities
    blueprintTypeID: int
    maxProductionLimit: int


@dataclass(slots=True, kw_only=True)
class Categories:
    """Model for the categories.jsonl SDE file."""

    categories_id: int | None = None
    name: LocalizedString
    published: bool
    iconID: int | None = None


@dataclass(slots=True, kw_only=True)
class Certificates_SkillType:
    """Nested model for the certificates.yaml SDE file."""

    basic: int
    standard: int
    improved: int
    advanced: int
    elite: int


@dataclass(slots=True, kw_only=True)
class Certificates:
    """Model for the certificates.yaml SDE file."""

    certificates_id: int | None = None
    description: LocalizedString
    groupID: int
    name: LocalizedString
    recommendedFor: list[int] | None = None
    skillTypes: dict[int, Certificates_SkillType]


@dataclass(slots=True, kw_only=True)
class CharacterAttributes:
    """Model for the characterAttributes.jsonl SDE file."""

    description: str
    iconID: int
    name: LocalizedString
    notes: str
    shortDescription: str


@dataclass(slots=True, kw_only=True)
class CloneGrades:
    """Model for the cloneGrades.jsonl SDE file."""

    name: str
    skills: list[Skills]


@dataclass(slots=True, kw_only=True)
class CompressibleTypes:
    """Model for the compressibleTypes.jsonl SDE file."""

    compressedTypeID: int


@dataclass(slots=True, kw_only=True)
class ContrabandTypes_Faction:
    """Nested model for the contrabandTypes.jsonl SDE file."""

    attackMinSec: float
    confiscateMinSec: float
    fineByValue: float
    standingLoss: float


@dataclass(slots=True, kw_only=True)
class ContrabandTypes:
    """Model for the contrabandTypes.jsonl SDE file."""

    factions: dict[int, ContrabandTypes_Faction]


@dataclass(slots=True, kw_only=True)
class ControlTowerResources_Resource:
    """Nested model for the controlTowerResources.jsonl SDE file."""

    factionID: int | None = None
    minSecurityLevel: float | None = None
    purpose: int
    quantity: int
    resourceTypeID: int


@dataclass(slots=True, kw_only=True)
class ControlTowerResources:
    """Model for the controlTowerResources.jsonl SDE file."""

    resources: list[ControlTowerResources_Resource]


@dataclass(slots=True, kw_only=True)
class CorporationActivities:
    """Model for the corporationActivities.jsonl SDE file."""

    name: LocalizedString


@dataclass(slots=True, kw_only=True)
class DebuffCollections_LocationGroupModifier:
    """Nested model for the dbuffCollections.jsonl SDE file."""

    dogmaAttributeID: int
    groupID: int


@dataclass(slots=True, kw_only=True)
class DebuffCollections_LocationModifier:
    """Nested model for the dbuffCollections.jsonl SDE file."""

    dogmaAttributeID: int


@dataclass(slots=True, kw_only=True)
class DebuffCollections_LocationRequiredSkillModifier:
    """Nested model for the dbuffCollections.jsonl SDE file."""

    dogmaAttributeID: int
    skillID: int


@dataclass(slots=True, kw_only=True)
class DebuffCollections_ItemModifier:
    """Nested model for the dbuffCollections.jsonl SDE file."""

    dogmaAttributeID: int


@dataclass(slots=True, kw_only=True)
class DebuffCollections:
    """Model for the dbuffCollections.jsonl SDE file."""

    aggregateMode: str
    developerDescription: str
    itemModifiers: list[DebuffCollections_ItemModifier] | None = None
    locationGroupModifiers: list[DebuffCollections_LocationGroupModifier] | None = None
    locationModifiers: list[DebuffCollections_LocationModifier] | None = None
    locationRequiredSkillModifiers: (
        list[DebuffCollections_LocationRequiredSkillModifier] | None
    ) = None
    operationName: str
    showOutputValueInUI: str
    displayName: LocalizedString | None = None


@dataclass(slots=True, kw_only=True)
class DogmaAttributeCategories:
    """Model for the dogmaAttributeCategories.jsonl SDE file."""

    description: str | None = None
    name: str


@dataclass(slots=True, kw_only=True)
class DogmaAttributes:
    """Model for the dogmaAttributes.jsonl SDE file."""

    attributeCategoryID: int | None = None
    dataType: int
    defaultValue: float
    description: str | None = None
    displayWhenZero: bool
    highIsGood: bool
    name: str
    published: bool
    stackable: bool
    displayName: LocalizedString | None = None
    iconID: int | None = None
    tooltipDescription: LocalizedString | None = None
    tooltipTitle: LocalizedString | None = None
    unitID: int | None = None
    chargeRechargeTimeID: int | None = None
    maxAttributeID: int | None = None
    minAttributeID: int | None = None


@dataclass(slots=True, kw_only=True)
class DogmaEffects_ModifierInfo:
    """Nested model for the dogmaEffects.jsonl SDE file."""

    domain: str
    effectID: int | None = None
    func: str
    groupID: int | None = None
    modifiedAttributeID: int | None = None
    modifyingAttributeID: int | None = None
    operation: int | None = None
    skillTypeID: int | None = None


@dataclass(slots=True, kw_only=True)
class DogmaEffects:
    """Model for the dogmaEffects.jsonl SDE file."""

    disallowAutoRepeat: bool
    dischargeAttributeID: int | None = None
    durationAttributeID: int | None = None
    effectCategoryID: int
    electronicChance: bool
    guid: str | None = None
    isAssistance: bool
    isOffensive: bool
    isWarpSafe: bool
    name: str
    propulsionChance: bool
    published: bool
    rangeChance: bool
    distribution: int | None = None
    falloffAttributeID: int | None = None
    rangeAttributeID: int | None = None
    trackingSpeedAttributeID: int | None = None
    description: LocalizedString | None = None
    displayName: LocalizedString | None = None
    iconID: int | None = None
    modifierInfo: list[DogmaEffects_ModifierInfo] | None = None
    npcUsageChanceAttributeID: int | None = None
    npcActivationChanceAttributeID: int | None = None
    fittingUsageChanceAttributeID: int | None = None
    resistanceAttributeID: int | None = None


@dataclass(slots=True, kw_only=True)
class DogmaUnits:
    """Model for the dogmaUnits.jsonl SDE file."""

    description: LocalizedString | None = None
    displayName: LocalizedString | None = None
    name: str


@dataclass(slots=True, kw_only=True)
class DynamicItemAttributes_AttributeID:
    """Nested model for the dynamicItemAttributes.jsonl SDE file."""

    highIsGood: bool | None = None
    max: float
    min: float


@dataclass(slots=True, kw_only=True)
class DynamicItemAttributes_InputOutputMapping:
    """Nested model for the dynamicItemAttributes.jsonl SDE file."""

    applicableTypes: list[int]
    resultingType: int


@dataclass(slots=True, kw_only=True)
class DynamicItemAttributes:
    """Model for the dynamicItemAttributes.jsonl SDE file."""

    attributeIDs: dict[int, DynamicItemAttributes_AttributeID]
    inputOutputMapping: list[DynamicItemAttributes_InputOutputMapping]


@dataclass(slots=True, kw_only=True)
class Factions:
    """Model for the factions.jsonl SDE file."""

    corporationID: int | None = None
    description: LocalizedString
    flatLogo: str | None = None
    flatLogoWithName: str | None = None
    iconID: int
    memberRaces: list[int]
    militiaCorporationID: int | None = None
    name: LocalizedString
    shortDescription: LocalizedString | None = None
    sizeFactor: float
    solarSystemID: int
    uniqueName: bool


# The freelanceJobSchemas.jsonl file has a more complex structure that doesn't fit well
# with the current RootModel[dict[int, Model]] pattern. It may require a custom parsing
# approach or a different model structure, so it's not included here yet.
# @dataclass(slots=True, kw_only=True)
# class FreelanceJobSchemas:
#     """Model for the freelanceJobSchemas.jsonl SDE file."""

#     value: list[dict[str, Any]] = Field(..., alias="_value")


@dataclass(slots=True, kw_only=True)
class Graphics:
    """Model for the graphics.jsonl SDE file."""

    graphicFile: str | None = None
    iconFolder: str | None = None
    sofFactionName: str | None = None
    sofHullName: str | None = None
    sofRaceName: str | None = None
    sofMaterialSetID: int | None = None
    sofLayout: list[str] | None = None


@dataclass(slots=True, kw_only=True)
class Groups:
    """Model for the groups.jsonl SDE file."""

    anchorable: bool
    anchored: bool
    categoryID: int
    fittableNonSingleton: bool
    name: LocalizedString
    published: bool
    useBasePrice: bool
    iconID: int | None = None


@dataclass(slots=True, kw_only=True)
class Icons:
    """Model for the icons.jsonl SDE file."""

    iconFile: str


@dataclass(slots=True, kw_only=True)
class Landmarks:
    """Model for the landmarks.jsonl SDE file."""

    description: LocalizedString
    name: LocalizedString
    position: Position
    iconID: int | None = None
    locationID: int | None = None


@dataclass(slots=True, kw_only=True)
class MapAsteroidBelts_Statistics:
    """Nested model for the mapAsteroidBelts.jsonl SDE file."""

    density: float
    eccentricity: float
    escapeVelocity: float
    locked: bool
    massDust: float
    massGas: float | None = None
    orbitPeriod: float
    orbitRadius: float
    rotationRate: float
    spectralClass: str
    surfaceGravity: float
    temperature: float


@dataclass(slots=True, kw_only=True)
class MapAsteroidBelts:
    """Model for the mapAsteroidBelts.jsonl SDE file."""

    celestialIndex: int
    orbitID: int
    orbitIndex: int
    position: Position
    radius: float | None = None
    solarSystemID: int
    statistics: MapAsteroidBelts_Statistics | None = None
    typeID: int
    uniqueName: LocalizedString | None = None


@dataclass(slots=True, kw_only=True)
class MapConstellations:
    """Model for the mapConstellations.jsonl SDE file."""

    factionID: int | None = None
    name: LocalizedString
    position: Position
    regionID: int
    solarSystemIDs: list[int]
    wormholeClassID: int | None = None


@dataclass(slots=True, kw_only=True)
class MapMoons_Attributes:
    """Nested model for the mapMoons.jsonl SDE file."""

    heightMap1: int
    heightMap2: int
    shaderPreset: int


@dataclass(slots=True, kw_only=True)
class MapMoons_Statistics:
    """Nested model for the mapMoons.jsonl SDE file."""

    density: float
    eccentricity: float
    escapeVelocity: float
    locked: bool
    massDust: float
    massGas: float | None = None
    orbitPeriod: float
    orbitRadius: float
    pressure: float
    rotationRate: float
    spectralClass: str
    surfaceGravity: float
    temperature: float


@dataclass(slots=True, kw_only=True)
class MapMoons:
    """Model for the mapMoons.jsonl SDE file."""

    attributes: MapMoons_Attributes
    celestialIndex: int
    orbitID: int
    orbitIndex: int
    position: Position
    radius: float
    solarSystemID: int
    statistics: MapMoons_Statistics | None = None
    typeID: int
    npcStationIDs: list[int] | None = None
    uniqueName: LocalizedString | None = None


@dataclass(slots=True, kw_only=True)
class MapPlanets_Attributes:
    """Nested model for the mapPlanets.jsonl SDE file."""

    heightMap1: int
    heightMap2: int
    population: bool
    shaderPreset: int


@dataclass(slots=True, kw_only=True)
class MapPlanets_Statistics:
    """Nested model for the mapPlanets.jsonl SDE file."""

    density: float
    eccentricity: float
    escapeVelocity: float
    locked: bool
    massDust: float
    massGas: float | None = None
    orbitPeriod: float | None = None
    orbitRadius: float | None = None
    pressure: float
    rotationRate: float
    spectralClass: str
    surfaceGravity: float | None = None
    temperature: float


@dataclass(slots=True, kw_only=True)
class MapPlanets:
    """Model for the mapPlanets.jsonl SDE file."""

    asteroidBeltIDs: list[int] | None = None
    attributes: MapPlanets_Attributes
    celestialIndex: int
    moonIDs: list[int] | None = None
    orbitID: int
    position: Position
    radius: int
    solarSystemID: int
    statistics: MapPlanets_Statistics | None = None
    typeID: int
    npcStationIDs: list[int] | None = None
    uniqueName: LocalizedString | None = None


@dataclass(slots=True, kw_only=True)
class MapRegions:
    """Model for the mapRegions.jsonl SDE file."""

    constellationIDs: list[int]
    description: LocalizedString | None = None
    factionID: int | None = None
    name: LocalizedString
    nebulaID: int
    position: Position
    wormholeClassID: int | None = None


@dataclass(slots=True, kw_only=True)
class MapSecondarySuns:
    """Model for the mapSecondarySuns.jsonl SDE file."""

    effectBeaconTypeID: int
    position: Position
    solarSystemID: int
    typeID: int


@dataclass(slots=True, kw_only=True)
class MapSolarSystems:
    """Model for the mapSolarSystems.jsonl SDE file."""

    border: bool | None = None
    constellationID: int
    corridor: bool | None = None
    disallowedAnchorCategories: list[int] | None = None
    disallowedAnchorGroups: list[int] | None = None
    factionID: int | None = None
    fringe: bool | None = None
    hub: bool | None = None
    international: bool | None = None
    luminosity: float | None = None
    name: LocalizedString
    planetIDs: list[int] | None = None
    position: Position
    position2D: Position2D | None = None
    radius: float
    regionID: int
    regional: bool | None = None
    securityClass: str | None = None
    securityStatus: float
    starID: int | None = None
    stargateIDs: list[int] | None = None
    visualEffect: str | None = None
    wormholeClassID: int | None = None


@dataclass(slots=True, kw_only=True)
class MapStargates_Destination:
    """Nested model for the mapStargates.jsonl SDE file."""

    solarSystemID: int
    stargateID: int


@dataclass(slots=True, kw_only=True)
class MapStargates:
    """Model for the mapStargates.jsonl SDE file."""

    destination: MapStargates_Destination
    position: Position
    solarSystemID: int
    typeID: int


@dataclass(slots=True, kw_only=True)
class MapStars_Statistics:
    """Nested model for the mapStars.jsonl SDE file."""

    age: float
    life: float
    luminosity: float
    spectralClass: str
    temperature: float


@dataclass(slots=True, kw_only=True)
class MapStars:
    """Model for the mapStars.jsonl SDE file."""

    radius: int
    solarSystemID: int
    statistics: MapStars_Statistics
    typeID: int


@dataclass(slots=True, kw_only=True)
class MarketGroups:
    """Model for the marketGroups.jsonl SDE file."""

    description: LocalizedString | None = None
    hasTypes: bool
    iconID: int | None = None
    name: LocalizedString
    parentGroupID: int | None = None


# These models wind up being so simple they are defined in the root model directly.

# @dataclass(slots=True, kw_only=True)
# class Masteries_Value:
#     """Nested model for the masteries.jsonl SDE file."""

#     value: list[int] = Field(..., alias="_value")


# @dataclass(slots=True, kw_only=True)
# class Masteries:
#     """Model for the masteries.jsonl SDE file."""

#     value: dict[int, Masteries_Value] = Field(..., alias="_value")


@dataclass(slots=True, kw_only=True)
class MetaGroups:
    """Model for the metaGroups.jsonl SDE file."""

    color: Color | None = None
    name: LocalizedString
    iconID: int | None = None
    iconSuffix: str | None = None
    description: LocalizedString | None = None


@dataclass(slots=True, kw_only=True)
class MercenaryTacticalOperations:
    """Model for the mercenaryTacticalOperations.jsonl SDE file."""

    anarchy_impact: int
    development_impact: int
    infomorph_bonus: int
    name: LocalizedString
    description: LocalizedString | None = None


@dataclass(slots=True, kw_only=True)
class NpcCharacters_Skill:
    """Nested model for the npcCharacters.jsonl SDE file."""

    typeID: int


@dataclass(slots=True, kw_only=True)
class NpcCharacters_Agent:
    """Nested model for the npcCharacters.jsonl SDE file."""

    agentTypeID: int
    divisionID: int
    isLocator: bool
    level: int


@dataclass(slots=True, kw_only=True)
class NpcCharacters:
    """Model for the npcCharacters.jsonl SDE file."""

    bloodlineID: int
    ceo: bool
    corporationID: int
    gender: bool
    locationID: int | None = None
    name: LocalizedString
    raceID: int
    startDate: str | None = None
    uniqueName: bool
    skills: list[NpcCharacters_Skill] | None = None
    ancestryID: int | None = None
    careerID: int | None = None
    schoolID: int | None = None
    specialityID: int | None = None
    agent: NpcCharacters_Agent | None = None
    description: str | None = None


@dataclass(slots=True, kw_only=True)
class NpcCorporationDivisions:
    """Model for the npcCorporationDivisions.jsonl SDE file."""

    displayName: str | None = None
    internalName: str
    leaderTypeName: LocalizedString
    name: LocalizedString
    description: LocalizedString | None = None


# @dataclass(slots=True, kw_only=True)
# class NpcCorporations_Trade:
#     """Nested model for the npcCorporations.jsonl SDE file."""

#     key: int = Field(..., alias="_key")
#     value: float = Field(..., alias="_value")


@dataclass(slots=True, kw_only=True)
class NpcCorporations_Divisions:
    """Nested model for the npcCorporations.jsonl SDE file."""

    divisionNumber: int
    leaderID: int
    size: int


# @dataclass(slots=True, kw_only=True)
# class NpcCorporations_Investors:
#     """Nested model for the npcCorporations.jsonl SDE file."""

#     key: int = Field(..., alias="_key")
#     value: int = Field(..., alias="_value")


# @dataclass(slots=True, kw_only=True)
# class NpcCorporations_ExchangeRates:
#     """Nested model for the npcCorporations.jsonl SDE file."""

#     key: int = Field(..., alias="_key")
#     value: float = Field(..., alias="_value")


@dataclass(slots=True, kw_only=True)
class NpcCorporations:
    """Model for the npcCorporations.jsonl SDE file."""

    ceoID: int | None = None
    deleted: bool
    description: LocalizedString | None = None
    extent: str
    hasPlayerPersonnelManager: bool
    initialPrice: int
    memberLimit: int
    minSecurity: float
    minimumJoinStanding: int
    name: LocalizedString
    sendCharTerminationMessage: bool
    shares: int
    size: str
    stationID: int | None = None
    taxRate: float
    tickerName: str
    uniqueName: bool
    allowedMemberRaces: list[int] | None = None
    corporationTrades: dict[int, float] | None = None
    divisions: dict[int, NpcCorporations_Divisions] | None = None
    enemyID: int | None = None
    factionID: int | None = None
    friendID: int | None = None
    iconID: int | None = None
    investors: dict[int, int] | None = None
    lpOfferTables: list[int] | None = None
    mainActivityID: int | None = None
    raceID: int | None = None
    sizeFactor: float | None = None
    solarSystemID: int | None = None
    secondaryActivityID: int | None = None
    exchangeRates: dict[int, float] | None = None


@dataclass(slots=True, kw_only=True)
class NpcStations:
    """Model for the npcStations.jsonl SDE file."""

    celestialIndex: int | None = None
    operationID: int
    orbitID: int
    orbitIndex: int | None = None
    ownerID: int
    position: Position
    reprocessingEfficiency: float
    reprocessingHangarFlag: int
    reprocessingStationsTake: float
    solarSystemID: int
    typeID: int
    useOperationName: bool


@dataclass(slots=True, kw_only=True)
class PlanetResources_Reagent:
    """Nested model for the planetResources.jsonl SDE file."""

    amount_per_cycle: int
    cycle_period: int
    secured_capacity: int
    type_id: int
    unsecured_capacity: int


@dataclass(slots=True, kw_only=True)
class PlanetResources:
    """Model for the planetResources.jsonl SDE file."""

    power: int | None = None
    workforce: int | None = None
    reagent: PlanetResources_Reagent | None = None


@dataclass(slots=True, kw_only=True)
class PlanetSchematics_Types:
    """Nested model for the planetSchematics.jsonl SDE file."""

    isInput: bool
    quantity: int


@dataclass(slots=True, kw_only=True)
class PlanetSchematics:
    """Model for the planetSchematics.jsonl SDE file."""

    cycleTime: int
    name: LocalizedString
    pins: list[int]
    types: dict[int, PlanetSchematics_Types]


@dataclass(slots=True, kw_only=True)
class Races:
    """Model for the races.jsonl SDE file."""

    description: LocalizedString | None = None
    iconID: int | None = None
    name: LocalizedString
    shipTypeID: int | None = None
    skills: dict[int, int] | None = None


@dataclass(slots=True, kw_only=True)
class SdeInfo:
    """Model for the sdeInfo.jsonl SDE file."""

    buildNumber: int
    releaseDate: str


@dataclass(slots=True, kw_only=True)
class SkinLicenses:
    """Model for the skinLicenses.jsonl SDE file."""

    duration: int
    licenseTypeID: int
    skinID: int
    isSingleUse: bool | None = None


@dataclass(slots=True, kw_only=True)
class SkinMaterials:
    """Model for the skinMaterials.jsonl SDE file."""

    displayName: LocalizedString | None = None
    materialSetID: int


@dataclass(slots=True, kw_only=True)
class Skins:
    """Model for the skins.jsonl SDE file."""

    allowCCPDevs: bool
    internalName: str
    skinMaterialID: int
    types: list[int]
    visibleSerenity: bool
    visibleTranquility: bool
    isStructureSkin: bool | None = None
    skinDescription: LocalizedString | None = None


@dataclass(slots=True, kw_only=True)
class SovereigntyUpgrades_Fuel:
    """Nested model for the sovereigntyUpgrades.jsonl SDE file."""

    hourly_upkeep: int
    startup_cost: int
    type_id: int


@dataclass(slots=True, kw_only=True)
class SovereigntyUpgrades:
    """Model for the sovereigntyUpgrades.jsonl SDE file."""

    fuel: SovereigntyUpgrades_Fuel | None = None
    mutually_exclusive_group: str
    power_allocation: int | None = None
    power_production: int | None = None
    workforce_allocation: int | None = None
    workforce_production: int | None = None


# @dataclass(slots=True, kw_only=True)
# class StationOperations_StationType:
#     """Nested model for the stationOperations.jsonl SDE file."""

#     key: int = Field(..., alias="_key")
#     value: int = Field(..., alias="_value")

#     model_config = ConfigDict(serialize_by_alias=True)


@dataclass(slots=True, kw_only=True)
class StationOperations:
    """Model for the stationOperations.jsonl SDE file."""

    activityID: int
    border: float
    corridor: float
    description: LocalizedString | None = None
    fringe: float
    hub: float
    manufacturingFactor: float
    operationName: LocalizedString
    ratio: float
    researchFactor: float
    services: list[int]
    stationTypes: dict[int, int] | None = None


@dataclass(slots=True, kw_only=True)
class StationServices:
    """Model for the stationServices.jsonl SDE file."""

    serviceName: LocalizedString
    description: LocalizedString | None = None


@dataclass(slots=True, kw_only=True)
class TranslationLanguages:
    """Model for the translationLanguages.jsonl SDE file."""

    name: str


@dataclass(slots=True, kw_only=True)
class TypeBonus_RoleBonus:
    """Nested model for the typeBonus.jsonl SDE file."""

    bonus: int | float | None = None
    bonusText: LocalizedString
    importance: int
    unitID: int | None = None


@dataclass(slots=True, kw_only=True)
class TypeBonus_Types_Bonus:
    """Nested model for the typeBonus.jsonl SDE file."""

    bonus: int | float | None = None
    bonusText: LocalizedString
    importance: int
    unitID: int | None = None


# @dataclass(slots=True, kw_only=True)
# class TypeBonus_Types:
#     """Nested model for the typeBonus.jsonl SDE file."""

#     # key: int = Field(..., alias="_key")
#     value: list[TypeBonus_Types_Bonus] = Field(..., alias="_value")


@dataclass(slots=True, kw_only=True)
class TypeBonus_MiscBonus:
    """Nested model for the typeBonus.jsonl SDE file."""

    bonus: int | float | None = None
    bonusText: LocalizedString
    importance: int
    isPositive: bool | None = None
    unitID: int | None = None


@dataclass(slots=True, kw_only=True)
class TypeBonus:
    """Model for the typeBonus.jsonl SDE file."""

    roleBonuses: list[TypeBonus_RoleBonus] | None = None
    types: dict[int, list[TypeBonus_Types_Bonus]] | None = None
    iconID: int | None = None
    miscBonuses: list[TypeBonus_MiscBonus] | None = None


@dataclass(slots=True, kw_only=True)
class TypeDogma_Attributes:
    """Nested model for the typeDogma.jsonl SDE file."""

    attributeID: int
    value: float


@dataclass(slots=True, kw_only=True)
class TypeDogma_Effects:
    """Nested model for the typeDogma.jsonl SDE file."""

    effectID: int
    isDefault: bool


@dataclass(slots=True, kw_only=True)
class TypeDogma:
    """Model for the typeDogma.jsonl SDE file."""

    dogmaAttributes: list[TypeDogma_Attributes]
    dogmaEffects: list[TypeDogma_Effects] | None = None


@dataclass(slots=True, kw_only=True)
class TypeMaterials_Material:
    """Nested model for the typeMaterials.jsonl SDE file."""

    materialTypeID: int
    quantity: int


@dataclass(slots=True, kw_only=True)
class TypeMaterials_RandomizedMaterial:
    """Nested model for the typeMaterials.jsonl SDE file."""

    materialTypeID: int
    quantityMax: int
    quantityMin: int


@dataclass(slots=True, kw_only=True)
class TypeMaterials:
    """Model for the typeMaterials.jsonl SDE file."""

    materials: list[TypeMaterials_Material] | None = None
    randomizedMaterials: list[TypeMaterials_RandomizedMaterial] | None = None


@dataclass(slots=True, kw_only=True)
class EveTypes:
    """Model for the types.jsonl SDE file."""

    groupID: int
    mass: float | None = None
    name: LocalizedString
    portionSize: int
    published: bool
    volume: float | None = None
    radius: float | None = None
    description: LocalizedString | None = None
    graphicID: int | None = None
    soundID: int | None = None
    iconID: int | None = None
    raceID: int | None = None
    basePrice: float | None = None
    marketGroupID: int | None = None
    capacity: float | None = None
    metaGroupID: int | None = None
    variationParentTypeID: int | None = None
    factionID: int | None = None


AgentsInSpaceRoot = RootModel[dict[int, AgentsInSpace]]
AgentTypesRoot = RootModel[dict[int, AgentTypes]]
AncestriesRoot = RootModel[dict[int, Ancestries]]
BloodlinesRoot = RootModel[dict[int, Bloodlines]]
BlueprintsRoot = RootModel[dict[int, Blueprints]]
CategoriesRoot = RootModel[dict[int, Categories]]
CertificatesRoot = RootModel[dict[int, Certificates]]
CharacterAttributesRoot = RootModel[dict[int, CharacterAttributes]]
CloneGradesRoot = RootModel[dict[int, CloneGrades]]
CompressibleTypesRoot = RootModel[dict[int, CompressibleTypes]]
ContrabandTypesRoot = RootModel[dict[int, ContrabandTypes]]
ControlTowerResourcesRoot = RootModel[dict[int, ControlTowerResources]]
CorporationActivitiesRoot = RootModel[dict[int, CorporationActivities]]
DebuffCollectionsRoot = RootModel[dict[int, DebuffCollections]]
DogmaAttributeCategoriesRoot = RootModel[dict[int, DogmaAttributeCategories]]
DogmaAttributesRoot = RootModel[dict[int, DogmaAttributes]]
DogmaEffectsRoot = RootModel[dict[int, DogmaEffects]]
DogmaUnitsRoot = RootModel[dict[int, DogmaUnits]]
DynamicItemAttributesRoot = RootModel[dict[int, DynamicItemAttributes]]
FactionsRoot = RootModel[dict[int, Factions]]
FreelanceJobSchemasRoot = RootModel[dict[int, dict[str, Any]]]
GraphicsRoot = RootModel[dict[int, Graphics]]
GroupsRoot = RootModel[dict[int, Groups]]
IconsRoot = RootModel[dict[int, Icons]]
LandmarksRoot = RootModel[dict[int, Landmarks]]
MapAsteroidBeltsRoot = RootModel[dict[int, MapAsteroidBelts]]
MapConstellationsRoot = RootModel[dict[int, MapConstellations]]
MapMoonsRoot = RootModel[dict[int, MapMoons]]
MapPlanetsRoot = RootModel[dict[int, MapPlanets]]
MapRegionsRoot = RootModel[dict[int, MapRegions]]
MapSecondarySunsRoot = RootModel[dict[int, MapSecondarySuns]]
MapSolarSystemsRoot = RootModel[dict[int, MapSolarSystems]]
MapStargatesRoot = RootModel[dict[int, MapStargates]]
MapStarsRoot = RootModel[dict[int, MapStars]]
MarketGroupsRoot = RootModel[dict[int, MarketGroups]]
MasteriesRoot = RootModel[dict[int, dict[int, list[int]]]]
MetaGroupsRoot = RootModel[dict[int, MetaGroups]]
MercenaryTacticalOperationsRoot = RootModel[dict[int, MercenaryTacticalOperations]]
NpcCharactersRoot = RootModel[dict[int, NpcCharacters]]
NpcCorporationDivisionsRoot = RootModel[dict[int, NpcCorporationDivisions]]
NpcCorporationsRoot = RootModel[dict[int, NpcCorporations]]
NpcStationsRoot = RootModel[dict[int, NpcStations]]
PlanetResourcesRoot = RootModel[dict[int, PlanetResources]]
PlanetSchematicsRoot = RootModel[dict[int, PlanetSchematics]]
RacesRoot = RootModel[dict[int, Races]]
SdeInfoRoot = RootModel[dict[str, SdeInfo]]
SkinLicensesRoot = RootModel[dict[int, SkinLicenses]]
SkinMaterialsRoot = RootModel[dict[int, SkinMaterials]]
SkinsRoot = RootModel[dict[int, Skins]]
SovereigntyUpgradesRoot = RootModel[dict[int, SovereigntyUpgrades]]
StationOperationsRoot = RootModel[dict[int, StationOperations]]
StationServicesRoot = RootModel[dict[int, StationServices]]
TranslationLanguagesRoot = RootModel[dict[str, TranslationLanguages]]
TypeBonusRoot = RootModel[dict[int, TypeBonus]]
TypeDogmaRoot = RootModel[dict[int, TypeDogma]]
TypeMaterialsRoot = RootModel[dict[int, TypeMaterials]]
EveTypesRoot = RootModel[dict[int, EveTypes]]
