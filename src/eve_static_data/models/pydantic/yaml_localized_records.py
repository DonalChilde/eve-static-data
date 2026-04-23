"""Dataclass models for localized SDE records.

Represents localized records from the SDE, in the YAML format datamodel.

Because the localized records are formed from loaded records, the `model_id` field does not need
to be optional, as it is guaranteed to be present in the loaded records.
"""

from dataclasses import dataclass, field

from eve_static_data.models.pydantic import yaml_records


@dataclass(slots=True, kw_only=True)
class AncestriesLocalized:
    """Model for the ancestries.yaml SDE file with localized fields."""

    ancestries_id: int | None = None
    bloodlineID: int
    charisma: int
    description: str
    iconID: int | None = None
    intelligence: int
    memory: int
    name: str
    perception: int
    shortDescription: str | None = None
    willpower: int


@dataclass(slots=True, kw_only=True)
class BloodlinesLocalized:
    """Model for the bloodlines.yaml SDE file with localized fields."""

    bloodlines_id: int | None = None
    charisma: int
    corporationID: int
    description: str
    iconID: int | None = None
    intelligence: int
    memory: int
    name: str
    perception: int
    raceID: int
    willpower: int


@dataclass(slots=True, kw_only=True)
class CategoriesLocalized:
    """Model for the categories.yaml SDE file with localized fields."""

    categories_id: int | None = None
    name: str
    published: bool
    iconID: int | None = None


@dataclass(slots=True, kw_only=True)
class CertificatesLocalized:
    """Model for the certificates.jsonl SDE file with localized fields."""

    certificates_id: int | None = None
    description: str
    groupID: int
    name: str
    recommendedFor: list[int] | None = None
    skillTypes: dict[int, yaml_records.Certificates_SkillType]


@dataclass(slots=True, kw_only=True)
class CharacterAttributesLocalized:
    """Model for the characterAttributes.yaml SDE file with localized fields."""

    character_attributes_id: int | None = None
    description: str
    iconID: int
    name: str
    notes: str
    shortDescription: str


@dataclass(slots=True, kw_only=True)
class CorporationActivitiesLocalized:
    """Model for the corporationActivities.yaml SDE file with localized fields."""

    corporation_activities_id: int | None = None
    name: str


@dataclass(slots=True, kw_only=True)
class DebuffCollectionsLocalized:
    """Model for the debuffCollections.jsonl SDE file with localized fields."""

    debuff_collections_id: int | None = None
    aggregateMode: str
    developerDescription: str
    itemModifiers: list[yaml_records.DebuffCollections_ItemModifier] | None = None
    locationGroupModifiers: (
        list[yaml_records.DebuffCollections_LocationGroupModifier] | None
    ) = None
    locationModifiers: list[yaml_records.DebuffCollections_LocationModifier] | None = (
        None
    )
    locationRequiredSkillModifiers: (
        list[yaml_records.DebuffCollections_LocationRequiredSkillModifier] | None
    ) = None
    operationName: str
    showOutputValueInUI: str
    displayName: str | None = None


@dataclass(slots=True, kw_only=True)
class DogmaAttributesLocalized:
    """Model for the dogmaAttributes.jsonl SDE file with localized fields."""

    dogma_attributes_id: int | None = None
    attributeCategoryID: int | None = None
    dataType: int
    defaultValue: float
    description: str | None = None
    displayWhenZero: bool
    highIsGood: bool
    name: str
    published: bool
    stackable: bool
    displayName: str | None = None
    iconID: int | None = None
    tooltipDescription: str | None = None
    tooltipTitle: str | None = None
    unitID: int | None = None
    chargeRechargeTimeID: int | None = None
    maxAttributeID: int | None = None
    minAttributeID: int | None = None


@dataclass(slots=True, kw_only=True)
class DogmaEffectsLocalized:
    """Model for the dogmaEffects.jsonl SDE file with localized fields."""

    dogma_effects_id: int | None = None
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
    description: str | None = None
    displayName: str | None = None
    iconID: int | None = None
    modifierInfo: list[yaml_records.DogmaEffects_ModifierInfo] | None = None
    npcUsageChanceAttributeID: int | None = None
    npcActivationChanceAttributeID: int | None = None
    fittingUsageChanceAttributeID: int | None = None
    resistanceAttributeID: int | None = None


@dataclass(slots=True, kw_only=True)
class DogmaUnitsLocalized:
    """Model for the dogmaUnits.jsonl SDE file with localized fields."""

    dogma_units_id: int | None = None
    description: str | None = None
    displayName: str | None = None
    name: str


@dataclass(slots=True, kw_only=True)
class FactionsLocalized:
    """Model for the factions.jsonl SDE file with localized fields."""

    factions_id: int | None = None
    corporationID: int | None = None
    description: str
    flatLogo: str | None = None
    flatLogoWithName: str | None = None
    iconID: int
    memberRaces: list[int]
    militiaCorporationID: int | None = None
    name: str
    shortDescription: str | None = None
    sizeFactor: float
    solarSystemID: int
    uniqueName: bool


@dataclass(slots=True, kw_only=True)
class GroupsLocalized:
    """Model for the groups.jsonl SDE file with localized fields."""

    groups_id: int | None = None
    anchorable: bool
    anchored: bool
    categoryID: int
    fittableNonSingleton: bool
    name: str
    published: bool
    useBasePrice: bool
    iconID: int | None = None


@dataclass(slots=True, kw_only=True)
class LandmarksLocalized:
    """Model for the landmarks.jsonl SDE file with localized fields."""

    landmarks_id: int | None = None
    description: str
    name: str
    position: yaml_records.Position
    iconID: int | None = None
    locationID: int | None = None


@dataclass(slots=True, kw_only=True)
class MapAsteroidBeltsLocalized:
    """Model for the mapAsteroidBelts.jsonl SDE file with localized fields."""

    map_asteroid_belts_id: int | None = None
    celestialIndex: int
    orbitID: int
    orbitIndex: int
    position: yaml_records.Position
    radius: float | None = None
    solarSystemID: int
    statistics: yaml_records.MapAsteroidBelts_Statistics | None = None
    typeID: int
    uniqueName: str | None = None


@dataclass(slots=True, kw_only=True)
class MapConstellationsLocalized:
    """Model for the mapConstellations.jsonl SDE file with localized fields."""

    map_constellations_id: int | None = None
    factionID: int | None = None
    name: str
    position: yaml_records.Position
    regionID: int
    solarSystemIDs: list[int]
    wormholeClassID: int | None = None


@dataclass(slots=True, kw_only=True)
class MapMoonsLocalized:
    """Model for the mapMoons.jsonl SDE file with localized fields."""

    map_moons_id: int | None = None
    attributes: yaml_records.MapMoons_Attributes
    celestialIndex: int
    orbitID: int
    orbitIndex: int
    position: yaml_records.Position
    radius: float
    solarSystemID: int
    statistics: yaml_records.MapMoons_Statistics | None = None
    typeID: int
    npcStationIDs: list[int] | None = None
    uniqueName: str | None = None


@dataclass(slots=True, kw_only=True)
class MapPlanetsLocalized:
    """Model for the mapPlanets.jsonl SDE file with localized fields."""

    map_planets_id: int | None = None
    asteroidBeltIDs: list[int] | None = None
    attributes: yaml_records.MapPlanets_Attributes
    celestialIndex: int
    moonIDs: list[int] | None = None
    orbitID: int
    position: yaml_records.Position
    radius: int
    solarSystemID: int
    statistics: yaml_records.MapPlanets_Statistics | None = None
    typeID: int
    npcStationIDs: list[int] | None = None
    uniqueName: str | None = None


@dataclass(slots=True, kw_only=True)
class MapRegionsLocalized:
    """Model for the mapRegions.jsonl SDE file with localized fields."""

    map_regions_id: int | None = None
    constellationIDs: list[int]
    description: str | None = None
    factionID: int | None = None
    name: str
    nebulaID: int
    position: yaml_records.Position
    wormholeClassID: int | None = None


@dataclass(slots=True, kw_only=True)
class MapSolarSystemsLocalized:
    """Model for the mapSolarSystems.jsonl SDE file with localized fields."""

    map_solar_systems_id: int | None = None
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
    name: str
    planetIDs: list[int] | None = None
    position: yaml_records.Position
    position2D: yaml_records.Position2D | None = None
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
class MarketGroupsLocalized:
    """Model for the marketGroups.jsonl SDE file with localized fields."""

    market_groups_id: int | None = None
    description: str | None = None
    hasTypes: bool
    iconID: int | None = None
    name: str
    parentGroupID: int | None = None


@dataclass(slots=True, kw_only=True)
class MetaGroupsLocalized:
    """Model for the metaGroups.jsonl SDE file with localized fields."""

    meta_groups_id: int | None = None
    color: yaml_records.Color | None = None
    name: str
    iconID: int | None = None
    iconSuffix: str | None = None
    description: str | None = None


@dataclass(slots=True, kw_only=True)
class MercenaryTacticalOperationsLocalized:
    """Model for the mercenaryTacticalOperations.jsonl SDE file with localized fields."""

    mercenary_tactical_operations_id: int | None = None
    anarchy_impact: int
    development_impact: int
    infomorph_bonus: int
    name: str
    description: str | None = None


@dataclass(slots=True, kw_only=True)
class NpcCharactersLocalized:
    """Model for the npcCharacters.jsonl SDE file with localized fields."""

    npc_characters_id: int | None = None
    bloodlineID: int
    ceo: bool
    corporationID: int
    gender: bool
    locationID: int | None = None
    name: str
    raceID: int
    startDate: str | None = None
    uniqueName: bool
    skills: list[yaml_records.NpcCharacters_Skill] | None = None
    ancestryID: int | None = None
    careerID: int | None = None
    schoolID: int | None = None
    specialityID: int | None = None
    agent: yaml_records.NpcCharacters_Agent | None = None
    description: str | None = None


@dataclass(slots=True, kw_only=True)
class NpcCorporationDivisionsLocalized:
    """Model for the npcCorporationDivisions.jsonl SDE file with localized fields."""

    npc_corporation_divisions_id: int | None = None
    displayName: str | None = None
    internalName: str
    leaderTypeName: str
    name: str
    description: str | None = None


@dataclass(slots=True, kw_only=True)
class NpcCorporationsLocalized:
    """Model for the npcCorporations.jsonl SDE file with localized fields."""

    npc_corporations_id: int | None = None
    ceoID: int | None = None
    deleted: bool
    description: str | None = None
    extent: str
    hasPlayerPersonnelManager: bool
    initialPrice: int
    memberLimit: int
    minSecurity: float
    minimumJoinStanding: int
    name: str
    sendCharTerminationMessage: bool
    shares: int
    size: str
    stationID: int | None = None
    taxRate: float
    tickerName: str
    uniqueName: bool
    allowedMemberRaces: list[int] | None = None
    corporationTrades: dict[int, float] | None = None
    divisions: dict[int, yaml_records.NpcCorporations_Divisions] | None = None
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
class PlanetSchematicsLocalized:
    """Model for the planetSchematics.jsonl SDE file with localized fields."""

    planet_schematics_id: int | None = None
    cycleTime: int
    name: str
    pins: list[int]
    types: dict[int, yaml_records.PlanetSchematics_Types]


@dataclass(slots=True, kw_only=True)
class RacesLocalized:
    """Model for the races.jsonl SDE file with localized fields."""

    races_id: int | None = None
    description: str | None = None
    iconID: int | None = None
    name: str
    shipTypeID: int | None = None
    skills: dict[int, int] | None = None


@dataclass(slots=True, kw_only=True)
class SkinMaterialsLocalized:
    """Model for the skinMaterials.jsonl SDE file with localized fields."""

    skin_materials_id: int | None = None
    displayName: str | None = None
    materialSetID: int


@dataclass(slots=True, kw_only=True)
class SkinsLocalized:
    """Model for the skins.jsonl SDE file with localized fields."""

    skins_id: int | None = None
    allowCCPDevs: bool
    internalName: str
    skinMaterialID: int
    types: list[int]
    visibleSerenity: bool
    visibleTranquility: bool
    isStructureSkin: bool | None = None
    skinDescription: str | None = None


@dataclass(slots=True, kw_only=True)
class StationOperationsLocalized:
    """Model for the stationOperations.jsonl SDE file with localized fields."""

    station_operations_id: int | None = None
    activityID: int
    border: float
    corridor: float
    description: str | None = None
    fringe: float
    hub: float
    manufacturingFactor: float
    operationName: str
    ratio: float
    researchFactor: float
    services: list[int]
    stationTypes: dict[int, int] | None = None


@dataclass(slots=True, kw_only=True)
class StationServicesLocalized:
    """Model for the stationServices.jsonl SDE file with localized fields."""

    station_services_id: int | None = None
    serviceName: str
    description: str | None = None


@dataclass(slots=True, kw_only=True)
class TypeBonus_RoleBonusLocalized:
    """Nested model for the typeBonus.jsonl SDE file with localized fields."""

    bonus: int | float | None = None
    bonusText: str
    importance: int
    unitID: int | None = None


@dataclass(slots=True, kw_only=True)
class TypeBonus_Types_BonusLocalized:
    """Nested model for the typeBonus.jsonl SDE file with localized fields."""

    bonus: int | float | None = None
    bonusText: str
    importance: int
    unitID: int | None = None


@dataclass(slots=True, kw_only=True)
class TypeBonus_TypesLocalized:
    """Nested model for the typeBonus.jsonl SDE file with localized fields."""

    key: int
    value: list[TypeBonus_Types_BonusLocalized] = field(
        default_factory=list[TypeBonus_Types_BonusLocalized],
        metadata={"alias": "_value"},
    )


@dataclass(slots=True, kw_only=True)
class TypeBonus_MiscBonusLocalized:
    """Nested model for the typeBonus.jsonl SDE file with localized fields."""

    bonus: int | float | None = None
    bonusText: str
    importance: int
    isPositive: bool | None = None
    unitID: int | None = None


@dataclass(slots=True, kw_only=True)
class TypeBonusLocalized:
    """Model for the typeBonus.jsonl SDE file with localized fields."""

    type_bonus_id: int | None = None
    roleBonuses: list[yaml_records.TypeBonus_RoleBonus] | None = None
    types: dict[int, list[yaml_records.TypeBonus_Types_Bonus]] | None = None
    iconID: int | None = None
    miscBonuses: list[yaml_records.TypeBonus_MiscBonus] | None = None


@dataclass(slots=True, kw_only=True)
class EveTypesLocalized:
    """Model for the types.jsonl SDE file with localized fields."""

    type_id: int | None = None
    groupID: int
    mass: float | None = None
    name: str
    portionSize: int
    published: bool
    volume: float | None = None
    radius: float | None = None
    description: str | None = None
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
