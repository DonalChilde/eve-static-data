"""TypedDict definitions for EVE SDE Datasets."""

from typing import Any, NotRequired, TypedDict

# ------------------------------------------------------------------------------
# Common TypedDict definitions.
# ------------------------------------------------------------------------------


class LocalizedString(TypedDict):
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


class Materials(TypedDict):
    typeID: int
    quantity: int


class Skills(TypedDict):
    typeID: int
    level: int


class Color(TypedDict):
    b: float
    g: float
    r: float


class Position(TypedDict):
    x: float
    y: float
    z: float


class Position2D(TypedDict):
    x: float
    y: float


# ------------------------------------------------------------------------------
# File level TypedDict definitions.
# ------------------------------------------------------------------------------


class AgentsInSpace(TypedDict):
    _key: int
    dungeonID: int
    solarSystemID: int
    spawnPointID: int
    typeID: int


class AgentTypes(TypedDict):
    _key: int
    name: str


class Ancestries(TypedDict):
    _key: int
    bloodlineID: int
    charisma: int
    description: LocalizedString
    iconID: NotRequired[int]
    intelligence: int
    memory: int
    name: LocalizedString
    perception: int
    shortDescription: NotRequired[str]
    willpower: int


class Bloodlines(TypedDict):
    _key: int
    charisma: int
    corporationID: int
    description: LocalizedString
    iconID: NotRequired[int]
    intelligence: int
    memory: int
    name: LocalizedString
    perception: int
    raceID: int
    willpower: int


class Blueprints_Products(TypedDict):
    typeID: int
    quantity: int
    probability: NotRequired[float]


class Blueprints_Activity(TypedDict):
    materials: NotRequired[list[Materials]]
    skills: NotRequired[list[Skills]]
    time: int
    products: NotRequired[list[Blueprints_Products]]


class Blueprints_Activities(TypedDict):
    copying: NotRequired[Blueprints_Activity]
    invention: NotRequired[Blueprints_Activity]
    manufacturing: NotRequired[Blueprints_Activity]
    reaction: NotRequired[Blueprints_Activity]
    research_material: NotRequired[Blueprints_Activity]
    research_time: NotRequired[Blueprints_Activity]


class Blueprints(TypedDict):
    _key: int
    activities: Blueprints_Activities
    blueprintTypeID: int
    maxProductionLimit: int


class Categories(TypedDict):
    _key: int
    name: LocalizedString
    published: bool
    iconID: NotRequired[int]


class Certificates_SkillType(TypedDict):
    _key: int
    basic: int
    standard: int
    improved: int
    advanced: int
    elite: int


class Certificates(TypedDict):
    _key: int
    description: LocalizedString
    groupID: int
    name: LocalizedString
    recommendedFor: NotRequired[list[int]]
    skillTypes: list[Certificates_SkillType]


class CharacterAttributes(TypedDict):
    _key: int
    description: str
    iconID: int
    name: LocalizedString
    notes: str
    shortDescription: str


class CompressibleTypes(TypedDict):
    _key: int
    compressedTypeID: int


class ContrabandTypes_Faction(TypedDict):
    _key: int
    attackMinSec: float
    confiscateMinSec: float
    fineByValue: float
    standingLoss: float


class ContrabandTypes(TypedDict):
    _key: int
    factions: list[ContrabandTypes_Faction]


class ControlTowerResources_Resource(TypedDict):
    factionID: NotRequired[int]
    minSecurityLevel: NotRequired[float]
    purpose: int
    quantity: int
    resourceTypeID: int


class ControlTowerResources(TypedDict):
    _key: int
    resources: list[ControlTowerResources_Resource]


class CorporationActivities(TypedDict):
    _key: int
    name: LocalizedString


class DebuffCollections_LocationGroupModifier(TypedDict):
    dogmaAttributeID: int
    groupID: int


class DebuffCollections_LocationModifier(TypedDict):
    dogmaAttributeID: int


class DebuffCollections_LocationRequiredSkillModifier(TypedDict):
    dogmaAttributeID: int
    skillID: int


class DebuffCollections_ItemModifier(TypedDict):
    dogmaAttributeID: int


class DebuffCollections(TypedDict):
    _key: int
    aggregateMode: str
    developerDescription: str
    itemModifiers: NotRequired[list[DebuffCollections_ItemModifier]]
    locationGroupModifiers: NotRequired[list[DebuffCollections_LocationGroupModifier]]
    locationModifiers: NotRequired[list[DebuffCollections_LocationModifier]]
    locationRequiredSkillModifiers: NotRequired[
        list[DebuffCollections_LocationRequiredSkillModifier]
    ]
    operationName: str
    showOutputValueInUI: str
    displayName: NotRequired[LocalizedString]


class DogmaAttributeCategories(TypedDict):
    _key: int
    description: NotRequired[str]
    name: str


class DogmaAttributes(TypedDict):
    _key: int
    attributeCategoryID: NotRequired[int]
    dataType: int
    defaultValue: float
    description: NotRequired[str]
    displayWhenZero: bool
    highIsGood: bool
    name: str
    published: bool
    stackable: bool
    displayName: NotRequired[LocalizedString]
    iconID: NotRequired[int]
    tooltipDescription: NotRequired[LocalizedString]
    tooltipTitle: NotRequired[LocalizedString]
    unitID: NotRequired[int]
    chargeRechargeTimeID: NotRequired[int]
    maxAttributeID: NotRequired[int]
    minAttributeID: NotRequired[int]


class DogmaEffects_ModifierInfo(TypedDict):
    domain: str
    effectID: NotRequired[int]
    func: str
    groupID: NotRequired[int]
    modifiedAttributeID: NotRequired[int]
    modifyingAttributeID: NotRequired[int]
    operation: NotRequired[int]
    skillTypeID: NotRequired[int]


class DogmaEffects(TypedDict):
    _key: int
    disallowAutoRepeat: bool
    dischargeAttributeID: NotRequired[int]
    durationAttributeID: NotRequired[int]
    effectCategoryID: int
    electronicChance: bool
    guid: NotRequired[str]
    isAssistance: bool
    isOffensive: bool
    isWarpSafe: bool
    name: str
    propulsionChance: bool
    published: bool
    rangeChance: bool
    distribution: NotRequired[int]
    falloffAttributeID: NotRequired[int]
    rangeAttributeID: NotRequired[int]
    trackingSpeedAttributeID: NotRequired[int]
    description: NotRequired[LocalizedString]
    displayName: NotRequired[LocalizedString]
    iconID: NotRequired[int]
    modifierInfo: NotRequired[list[DogmaEffects_ModifierInfo]]
    npcUsageChanceAttributeID: NotRequired[int]
    npcActivationChanceAttributeID: NotRequired[int]
    fittingUsageChanceAttributeID: NotRequired[int]
    resistanceAttributeID: NotRequired[int]


class DogmaUnits(TypedDict):
    _key: int
    description: NotRequired[LocalizedString]
    displayName: NotRequired[LocalizedString]
    name: str


class DynamicItemAttributes_AttributeID(TypedDict):
    _key: int
    highIsGood: NotRequired[bool]
    max: float
    min: float


class DynamicItemAttributes_InputOutputMapping(TypedDict):
    applicableTypes: list[int]
    resultingType: int


class DynamicItemAttributes(TypedDict):
    _key: int
    attributeIDs: list[DynamicItemAttributes_AttributeID]
    inputOutputMapping: list[DynamicItemAttributes_InputOutputMapping]


class Factions(TypedDict):
    _key: int
    corporationID: NotRequired[int]
    description: LocalizedString
    flatLogo: NotRequired[str]
    flatLogoWithName: NotRequired[str]
    iconID: int
    memberRaces: list[int]
    militiaCorporationID: NotRequired[int]
    name: LocalizedString
    shortDescription: NotRequired[LocalizedString]
    sizeFactor: float
    solarSystemID: int
    uniqueName: bool


type FreelanceJobSchemas = dict[str, Any]


class Graphics(TypedDict):
    _key: int
    graphicFile: NotRequired[str]
    iconFolder: NotRequired[str]
    sofFactionName: NotRequired[str]
    sofHullName: NotRequired[str]
    sofRaceName: NotRequired[str]
    sofMaterialSetID: NotRequired[int]
    sofLayout: NotRequired[list[str]]


class Groups(TypedDict):
    _key: int
    anchorable: bool
    anchored: bool
    categoryID: int
    fittableNonSingleton: bool
    name: LocalizedString
    published: bool
    useBasePrice: bool
    iconID: NotRequired[int]


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
