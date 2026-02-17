"""Pydantic model definitions for EVE SDE Datasets.

This module contains Pydantic model definitions for EVE SDE datasets.
These models are used to validate and parse the data from the SDE files,
ensuring that the data conforms to the expected structure and types.

Field names match those in the original SDE files, with the exception of `_key`, which
is renamed to `key` due to a conflict with pydantic.

Note that many fields in the SDE files are optional, and as such that field may be
missing in a given record. In the TypedDict schema, this is represented as NotRequired.
In the pydantic models, the field is defined as optional and will be set to `None`
if it is missing in the data.
"""

from typing import Any

from pydantic import BaseModel, Field

# ------------------------------------------------------------------------------
# Common Pydantic model definitions.
# ------------------------------------------------------------------------------


class LocalizedString(BaseModel):
    """Type definition for LocalizedString.

    Source info: SDE file: translationLanguages.jsonl
    """

    en: str
    de: str
    fr: str
    ja: str
    zh: str
    ru: str
    ko: str
    es: str


class Materials(BaseModel):
    typeID: int
    quantity: int


class Skills(BaseModel):
    typeID: int
    level: int


class Color(BaseModel):
    b: float
    g: float
    r: float


class Position(BaseModel):
    x: float
    y: float
    z: float


class Position2D(BaseModel):
    x: float
    y: float


# ------------------------------------------------------------------------------
# File level Pydantic model definitions.
# ------------------------------------------------------------------------------


class AgentsInSpace(BaseModel):
    """Model for the agentsInSpace.jsonl SDE file."""

    key: int = Field(..., alias="_key")
    dungeonID: int
    solarSystemID: int
    spawnPointID: int
    typeID: int


class AgentTypes(BaseModel):
    """Model for the agentTypes.jsonl SDE file."""

    key: int = Field(..., alias="_key")
    name: str


class Ancestries(BaseModel):
    """Model for the ancestries.jsonl SDE file."""

    key: int = Field(..., alias="_key")
    bloodlineID: int
    charisma: int
    description: LocalizedString
    iconID: int | None = None
    intelligence: int
    memory: int
    name: LocalizedString
    perception: int
    shortDescription: int | None = None
    willpower: int


class Bloodlines(BaseModel):
    """Model for the bloodlines.jsonl SDE file."""

    key: int = Field(..., alias="_key")
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


class Blueprints_Products(BaseModel):
    typeID: int
    quantity: int
    probability: float | None = None


class Blueprints_Activity(BaseModel):
    materials: list[Materials] | None = None
    skills: list[Skills] | None = None
    time: int
    products: list[Blueprints_Products] | None = None


class Blueprints_Activities(BaseModel):
    copying: Blueprints_Activity | None = None
    invention: Blueprints_Activity | None = None
    manufacturing: Blueprints_Activity | None = None
    reaction: Blueprints_Activity | None = None
    research_material: Blueprints_Activity | None = None
    research_time: Blueprints_Activity | None = None


class Blueprints(BaseModel):
    """Model for the blueprints.jsonl SDE file."""

    key: int = Field(..., alias="_key")
    activities: Blueprints_Activities
    blueprintTypeID: int
    maxProductionLimit: int


class Categories(BaseModel):
    """Model for the categories.jsonl SDE file."""

    key: int = Field(..., alias="_key")
    name: LocalizedString
    published: bool
    iconID: int | None = None


class Certificates_SkillType(BaseModel):
    key: int = Field(..., alias="_key")
    basic: int
    standard: int
    improved: int
    advanced: int
    elite: int


class Certificates(BaseModel):
    """Model for the certificates.jsonl SDE file."""

    key: int = Field(..., alias="_key")
    description: LocalizedString
    groupID: int
    name: LocalizedString
    recommendedFor: list[int] | None = None
    skillTypes: list[Certificates_SkillType]


class CharacterAttributes(BaseModel):
    """Model for the characterAttributes.jsonl SDE file."""

    key: int = Field(..., alias="_key")
    description: str
    iconID: int
    name: LocalizedString
    notes: str
    shortDescription: str


class CompressibleTypes(BaseModel):
    """Model for the compressibleTypes.jsonl SDE file."""

    key: int = Field(..., alias="_key")
    compressedTypeID: int


class ContrabandTypes_Faction(BaseModel):
    key: int = Field(..., alias="_key")
    attackMinSec: float
    confiscateMinSec: float
    fineByValue: float
    standingLoss: float


class ContrabandTypes(BaseModel):
    """Model for the contrabandTypes.jsonl SDE file."""

    key: int = Field(..., alias="_key")
    factions: list[ContrabandTypes_Faction]


class ControlTowerResources_Resource(BaseModel):
    factionID: int | None = None
    minSecurityLevel: float | None = None
    purpose: int
    quantity: int
    resourceTypeID: int


class ControlTowerResources(BaseModel):
    """Model for the controlTowerResources.jsonl SDE file."""

    key: int = Field(..., alias="_key")
    resources: list[ControlTowerResources_Resource]


class CorporationActivities(BaseModel):
    """Model for the corporationActivities.jsonl SDE file."""

    key: int = Field(..., alias="_key")
    name: LocalizedString


class DebuffCollections_LocationGroupModifier(BaseModel):
    dogmaAttributeID: int
    groupID: int


class DebuffCollections_LocationModifier(BaseModel):
    dogmaAttributeID: int


class DebuffCollections_LocationRequiredSkillModifier(BaseModel):
    dogmaAttributeID: int
    skillID: int


class DebuffCollections_ItemModifier(BaseModel):
    dogmaAttributeID: int


class DebuffCollections(BaseModel):
    """Model for the debuffCollections.jsonl SDE file."""

    key: int = Field(..., alias="_key")
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


class DogmaAttributeCategories(BaseModel):
    """Model for the dogmaAttributeCategories.jsonl SDE file."""

    key: int = Field(..., alias="_key")
    description: str | None = None
    name: str


class DogmaAttributes(BaseModel):
    """Model for the dogmaAttributes.jsonl SDE file."""

    key: int = Field(..., alias="_key")
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


class DogmaEffects_ModifierInfo(BaseModel):
    domain: str
    effectID: int | None = None
    func: str
    groupID: int | None = None
    modifiedAttributeID: int | None = None
    modifyingAttributeID: int | None = None
    operation: int | None = None
    skillTypeID: int | None = None


class DogmaEffects(BaseModel):
    """Model for the dogmaEffects.jsonl SDE file."""

    key: int = Field(..., alias="_key")
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


class DogmaUnits(BaseModel):
    """Model for the dogmaUnits.jsonl SDE file."""

    key: int = Field(..., alias="_key")
    description: LocalizedString | None = None
    displayName: LocalizedString | None = None
    name: str


class DynamicItemAttributes_AttributeID(BaseModel):
    key: int = Field(..., alias="_key")
    highIsGood: bool | None = None
    max: float
    min: float


class DynamicItemAttributes_InputOutputMapping(BaseModel):
    applicableTypes: list[int]
    resultingType: int


class DynamicItemAttributes(BaseModel):
    """Model for the dynamicItemAttributes.jsonl SDE file."""

    key: int = Field(..., alias="_key")
    attributeIDs: list[DynamicItemAttributes_AttributeID]
    inputOutputMapping: list[DynamicItemAttributes_InputOutputMapping]


class Factions(BaseModel):
    """Model for the factions.jsonl SDE file."""

    key: int = Field(..., alias="_key")
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


class FreelanceJobSchemas(BaseModel):
    """Model for the freelanceJobSchemas.jsonl SDE file."""

    key: int = Field(..., alias="_key")
    value: dict[str, Any] = Field(..., alias="_value")


class Graphics(BaseModel):
    """Model for the graphics.jsonl SDE file."""

    key: int = Field(..., alias="_key")
    graphicFile: str | None = None
    iconFolder: str | None = None
    sofFactionName: str | None = None
    sofHullName: str | None = None
    sofRaceName: str | None = None
    sofMaterialSetID: int | None = None
    sofLayout: list[str] | None = None


class Groups(BaseModel):
    """Model for the groups.jsonl SDE file."""

    key: int = Field(..., alias="_key")
    anchorable: bool
    anchored: bool
    categoryID: int
    fittableNonSingleton: bool
    name: LocalizedString
    published: bool
    useBasePrice: bool
    iconID: int | None = None


# TODO The below classes need the following refactors, using the previous classes as an example:
# - Change the inherited model from TypedDict to BaseModel.
# - Rename _key to key and add alias in the pydantic model definition.
# - Add optional fields with default value of None for any fields that are not always present in the SDE data.
# - Add a class docstring for each class, describing the source SDE file


class Icons(TypedDict):
    _key: int
    iconFile: str


class Landmarks(TypedDict):
    _key: int
    description: LocalizedString
    name: LocalizedString
    position: Position
    iconID: NotRequired[int]
    locationID: NotRequired[int]


class MapAsteroidBelts_Statistics(TypedDict):
    density: float
    eccentricity: float
    escapeVelocity: float
    locked: bool
    massDust: float
    massGas: NotRequired[float]
    orbitPeriod: float
    orbitRadius: float
    rotationRate: float
    spectralClass: str
    surfaceGravity: float
    temperature: float


class MapAsteroidBelts(TypedDict):
    _key: int
    celestialIndex: int
    orbitID: int
    orbitIndex: int
    position: Position
    radius: NotRequired[float]
    solarSystemID: int
    statistics: NotRequired[MapAsteroidBelts_Statistics]
    typeID: int
    uniqueName: NotRequired[LocalizedString]


class MapConstellations(TypedDict):
    _key: int
    factionID: NotRequired[int]
    name: LocalizedString
    position: Position
    regionID: int
    solarSystemIDs: list[int]
    wormholeClassID: NotRequired[int]


class MapMoons_Attributes(TypedDict):
    heightMap1: int
    heightMap2: int
    shaderPreset: int


class MapMoons_Statistics(TypedDict):
    density: float
    eccentricity: float
    escapeVelocity: float
    locked: bool
    massDust: float
    massGas: NotRequired[float]
    orbitPeriod: float
    orbitRadius: float
    pressure: float
    rotationRate: float
    spectralClass: str
    surfaceGravity: float
    temperature: float


class MapMoons(TypedDict):
    _key: int
    attributes: MapMoons_Attributes
    celestialIndex: int
    orbitID: int
    orbitIndex: int
    position: Position
    radius: float
    solarSystemID: int
    statistics: NotRequired[MapMoons_Statistics]
    typeID: int
    npcStationIDs: NotRequired[list[int]]
    uniqueName: NotRequired[LocalizedString]


class MapPlanets_Attributes(TypedDict):
    heightMap1: int
    heightMap2: int
    population: bool
    shaderPreset: int


class MapPlanets_Statistics(TypedDict):
    density: float
    eccentricity: float
    escapeVelocity: float
    locked: bool
    massDust: float
    massGas: NotRequired[float]
    orbitPeriod: NotRequired[float]
    orbitRadius: NotRequired[float]
    pressure: float
    rotationRate: float
    spectralClass: str
    surfaceGravity: NotRequired[float]
    temperature: float


class MapPlanets(TypedDict):
    _key: int
    asteroidBeltIDs: NotRequired[list[int]]
    attributes: MapPlanets_Attributes
    celestialIndex: int
    moonIDs: NotRequired[list[int]]
    orbitID: int
    position: Position
    radius: int
    solarSystemID: int
    statistics: NotRequired[MapPlanets_Statistics]
    typeID: int
    npcStationIDs: NotRequired[list[int]]
    uniqueName: NotRequired[LocalizedString]


class MapRegions(TypedDict):
    _key: int
    constellationIDs: list[int]
    description: NotRequired[LocalizedString]
    factionID: NotRequired[int]
    name: LocalizedString
    nebulaID: int
    position: Position
    wormholeClassID: NotRequired[int]


class MapSolarSystems(TypedDict):
    _key: int
    border: NotRequired[bool]
    constellationID: int
    corridor: NotRequired[bool]
    disallowedAnchorCategories: NotRequired[list[int]]
    disallowedAnchorGroups: NotRequired[list[int]]
    factionID: NotRequired[int]
    fringe: NotRequired[bool]
    hub: NotRequired[bool]
    international: NotRequired[bool]
    luminosity: NotRequired[float]
    name: LocalizedString
    planetIDs: NotRequired[list[int]]
    position: Position
    position2D: NotRequired[Position2D]
    radius: float
    regionID: int
    regional: NotRequired[bool]
    securityClass: NotRequired[str]
    securityStatus: float
    starID: NotRequired[int]
    stargateIDs: NotRequired[list[int]]
    visualEffect: NotRequired[str]
    wormholeClassID: NotRequired[int]


class MapStargates_Destination(TypedDict):
    solarSystemID: int
    stargateID: int


class MapStargates(TypedDict):
    _key: int
    destination: MapStargates_Destination
    position: Position
    solarSystemID: int
    typeID: int


class MapStars_Statistics(TypedDict):
    age: float
    life: float
    luminosity: float
    spectralClass: str
    temperature: float


class MapStars(TypedDict):
    _key: int
    radius: int
    solarSystemID: int
    statistics: MapStars_Statistics
    typeID: int


class MarketGroups(TypedDict):
    _key: int
    description: NotRequired[LocalizedString]
    hasTypes: bool
    iconID: NotRequired[int]
    name: LocalizedString
    parentGroupID: NotRequired[int]


class Masteries_Value(TypedDict):
    _key: int
    _value: list[int]


class Masteries(TypedDict):
    _key: int
    _value: list[Masteries_Value]


class MetaGroups(TypedDict):
    _key: int
    color: NotRequired[Color]
    name: LocalizedString
    iconID: NotRequired[int]
    iconSuffix: NotRequired[str]
    description: NotRequired[LocalizedString]


class NpcCharacters_Skill(TypedDict):
    typeID: int


class NpcCharacters_Agent(TypedDict):
    agentTypeID: int
    divisionID: int
    isLocator: bool
    level: int


class NpcCharacters(TypedDict):
    _key: int
    bloodlineID: int
    ceo: bool
    corporationID: int
    gender: bool
    locationID: NotRequired[int]
    name: LocalizedString
    raceID: int
    startDate: NotRequired[str]
    uniqueName: bool
    skills: NotRequired[list[NpcCharacters_Skill]]
    ancestryID: NotRequired[int]
    careerID: NotRequired[int]
    schoolID: NotRequired[int]
    specialityID: NotRequired[int]
    agent: NotRequired[NpcCharacters_Agent]
    description: NotRequired[str]


class NpcCorporationDivisions(TypedDict):
    _key: int
    displayName: NotRequired[str]
    internalName: str
    leaderTypeName: LocalizedString
    name: LocalizedString
    description: NotRequired[LocalizedString]


class NpcCorporations_Trade(TypedDict):
    _key: int
    _value: float


class NpcCorporations_Divisions(TypedDict):
    _key: int
    divisionNumber: int
    leaderID: int
    size: int


class NpcCorporations_Investors(TypedDict):
    _key: int
    _value: int


class NpcCorporations_ExchangeRates(TypedDict):
    _key: int
    _value: float


class NpcCorporations(TypedDict):
    _key: int
    ceoID: NotRequired[int]
    deleted: bool
    description: NotRequired[LocalizedString]
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
    stationID: NotRequired[int]
    taxRate: float
    tickerName: str
    uniqueName: bool
    allowedMemberRaces: NotRequired[list[int]]
    corporationTrades: NotRequired[list[NpcCorporations_Trade]]
    divisions: NotRequired[list[NpcCorporations_Divisions]]
    enemyID: NotRequired[int]
    factionID: NotRequired[int]
    friendID: NotRequired[int]
    iconID: NotRequired[int]
    investors: NotRequired[list[NpcCorporations_Investors]]
    lpOfferTables: NotRequired[list[int]]
    mainActivityID: NotRequired[int]
    raceID: NotRequired[int]
    sizeFactor: NotRequired[float]
    solarSystemID: NotRequired[int]
    secondaryActivityID: NotRequired[int]
    exchangeRates: NotRequired[list[NpcCorporations_ExchangeRates]]


class NpcStations(TypedDict):
    _key: int
    celestialIndex: NotRequired[int]
    operationID: int
    orbitID: int
    orbitIndex: NotRequired[int]
    ownerID: int
    position: Position
    reprocessingEfficiency: float
    reprocessingHangarFlag: int
    reprocessingStationsTake: float
    solarSystemID: int
    typeID: int
    useOperationName: bool


class PlanetResources(TypedDict):
    _key: int
    power: NotRequired[int]
    workforce: NotRequired[int]
    cycle_minutes: NotRequired[int]
    harvest_silo_max: NotRequired[int]
    maturation_cycle_minutes: NotRequired[int]
    maturation_percent: NotRequired[int]
    mature_silo_max: NotRequired[int]
    reagent_harvest_amount: NotRequired[int]
    reagent_type_id: NotRequired[int]


class PlanetSchematics_Types(TypedDict):
    _key: int
    isInput: bool
    quantity: int


class PlanetSchematics(TypedDict):
    _key: int
    cycleTime: int
    name: LocalizedString
    pins: list[int]
    types: list[PlanetSchematics_Types]


class Races_Skill(TypedDict):
    _key: int
    _value: int


class Races(TypedDict):
    _key: int
    description: NotRequired[LocalizedString]
    iconID: NotRequired[int]
    name: LocalizedString
    shipTypeID: NotRequired[int]
    skills: list[Races_Skill]


class SdeInfo(TypedDict):
    _key: str
    buildNumber: int
    releaseDate: str


class SkinLicenses(TypedDict):
    _key: int
    duration: int
    licenseTypeID: int
    skinID: int
    isSingleUse: NotRequired[bool]


class SkinMaterials(TypedDict):
    _key: int
    displayName: NotRequired[LocalizedString]
    materialSetID: int


class Skins(TypedDict):
    _key: int
    allowCCPDevs: bool
    internalName: str
    skinMaterialID: int
    types: list[int]
    visibleSerenity: bool
    visibleTranquility: bool
    isStructureSkin: NotRequired[bool]
    skinDescription: NotRequired[LocalizedString]


class SovereigntyUpgrades(TypedDict):
    _key: int
    fuel_hourly_upkeep: NotRequired[int]
    fuel_startup_cost: NotRequired[int]
    fuel_type_id: NotRequired[int]
    mutually_exclusive_group: str
    power_allocation: int
    workforce_allocation: int


class StationOperations_StationType(TypedDict):
    _key: int
    _value: int


class StationOperations(TypedDict):
    _key: int
    activityID: int
    border: float
    corridor: float
    description: NotRequired[LocalizedString]
    fringe: float
    hub: float
    manufacturingFactor: float
    operationName: LocalizedString
    ratio: float
    researchFactor: float
    services: list[int]
    stationTypes: list[StationOperations_StationType]


class StationServices(TypedDict):
    _key: int
    serviceName: LocalizedString
    description: NotRequired[LocalizedString]


class TranslationLanguages(TypedDict):
    _key: str
    name: str


class TypeBonus_RoleBonus(TypedDict):
    bonus: NotRequired[int | float]
    bonusText: LocalizedString
    importance: int
    unitID: NotRequired[int]


class TypeBonus_Types_Bonus(TypedDict):
    bonus: NotRequired[int | float]
    bonusText: LocalizedString
    importance: int
    unitID: NotRequired[int]


class TypeBonus_Types(TypedDict):
    _key: int
    _value: list[TypeBonus_Types_Bonus]


class TypeBonus_MiscBonus(TypedDict):
    bonus: NotRequired[int | float]
    bonusText: LocalizedString
    importance: int
    isPositive: NotRequired[bool]
    unitID: NotRequired[int]


class TypeBonus(TypedDict):
    _key: int
    roleBonuses: list[TypeBonus_RoleBonus]
    types: list[TypeBonus_Types]
    iconID: NotRequired[int]
    miscBonuses: NotRequired[list[TypeBonus_MiscBonus]]


class TypeDogma_Attributes(TypedDict):
    attributeID: int
    value: float


class TypeDogma_Effects(TypedDict):
    effectID: int
    isDefault: bool


class TypeDogma(TypedDict):
    _key: int
    dogmaAttributes: list[TypeDogma_Attributes]
    dogmaEffects: list[TypeDogma_Effects]


class TypeMaterials_Material(TypedDict):
    materialTypeID: int
    quantity: int


class TypeMaterials_RandomizedMaterial(TypedDict):
    materialTypeID: int
    quantityMax: int
    quantityMin: int


class TypeMaterials(TypedDict):
    _key: int
    materials: list[TypeMaterials_Material]
    randomizedMaterials: list[TypeMaterials_RandomizedMaterial]


class EveTypes(TypedDict):
    _key: int
    groupID: int
    mass: NotRequired[float]
    name: LocalizedString
    portionSize: int
    published: bool
    volume: NotRequired[float]
    radius: NotRequired[float]
    description: NotRequired[LocalizedString]
    graphicID: NotRequired[int]
    soundID: NotRequired[int]
    iconID: NotRequired[int]
    raceID: NotRequired[int]
    basePrice: NotRequired[float]
    marketGroupID: NotRequired[int]
    capacity: NotRequired[float]
    metaGroupID: NotRequired[int]
    variationParentTypeID: NotRequired[int]
    factionID: NotRequired[int]
