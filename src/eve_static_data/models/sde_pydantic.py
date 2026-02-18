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

from typing import Any, Self

from pydantic import BaseModel, ConfigDict, Field

from eve_static_data.models import sde_typeddict as TDM

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
    """Model used in multiple datasets for materials, e.g. in blueprints and typeMaterials."""

    typeID: int
    quantity: int


class Skills(BaseModel):
    """Model used in multiple datasets for skills, e.g. in blueprints and npcCharacters."""

    typeID: int
    level: int


class Color(BaseModel):
    """Model used in multiple datasets for color, e.g. in metaGroups."""

    b: float
    g: float
    r: float


class Position(BaseModel):
    """Model used in multiple datasets for position, e.g. in celestialObjects and npcCharacters."""

    x: float
    y: float
    z: float


class Position2D(BaseModel):
    """Model used in multiple datasets for 2D position, e.g. in mapSolarSystems."""

    x: float
    y: float


# ------------------------------------------------------------------------------
# File level Pydantic model definitions.
# ------------------------------------------------------------------------------


class SdeDataset(BaseModel):
    """Base model for all SDE datasets."""

    model_config = ConfigDict(serialize_by_alias=True)


class AgentsInSpace(SdeDataset):
    """Model for the agentsInSpace.jsonl SDE file."""

    key: int = Field(..., alias="_key")
    dungeonID: int
    solarSystemID: int
    spawnPointID: int
    typeID: int

    @classmethod
    def from_sde(cls, record: TDM.AgentsInSpace) -> Self:
        """Create an AgentsInSpace instance from a SDE record."""
        return cls.model_validate(record)


class AgentTypes(SdeDataset):
    """Model for the agentTypes.jsonl SDE file."""

    key: int = Field(..., alias="_key")
    name: str

    @classmethod
    def from_sde(cls, record: TDM.AgentTypes) -> Self:
        """Create an AgentTypes instance from a SDE record."""
        return cls.model_validate(record)


class Ancestries(SdeDataset):
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
    shortDescription: str | None = None
    willpower: int

    @classmethod
    def from_sde(cls, record: TDM.Ancestries) -> Self:
        """Create an Ancestries instance from a SDE record."""
        return cls.model_validate(record)


class Bloodlines(SdeDataset):
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

    @classmethod
    def from_sde(cls, record: TDM.Bloodlines) -> Self:
        """Create a Bloodlines instance from a SDE record."""
        return cls.model_validate(record)


class Blueprints_Products(BaseModel):
    """Nested model for the blueprints.jsonl SDE file."""

    typeID: int
    quantity: int
    probability: float | None = None


class Blueprints_Activity(BaseModel):
    """Nested model for the blueprints.jsonl SDE file."""

    materials: list[Materials] | None = None
    skills: list[Skills] | None = None
    time: int
    products: list[Blueprints_Products] | None = None


class Blueprints_Activities(BaseModel):
    """Nested model for the blueprints.jsonl SDE file."""

    copying: Blueprints_Activity | None = None
    invention: Blueprints_Activity | None = None
    manufacturing: Blueprints_Activity | None = None
    reaction: Blueprints_Activity | None = None
    research_material: Blueprints_Activity | None = None
    research_time: Blueprints_Activity | None = None


class Blueprints(SdeDataset):
    """Model for the blueprints.jsonl SDE file."""

    key: int = Field(..., alias="_key")
    activities: Blueprints_Activities
    blueprintTypeID: int
    maxProductionLimit: int

    @classmethod
    def from_sde(cls, record: TDM.Blueprints) -> Self:
        """Create a Blueprints instance from a SDE record."""
        return cls.model_validate(record)


class Categories(SdeDataset):
    """Model for the categories.jsonl SDE file."""

    key: int = Field(..., alias="_key")
    name: LocalizedString
    published: bool
    iconID: int | None = None

    @classmethod
    def from_sde(cls, record: TDM.Categories) -> Self:
        """Create a Categories instance from a SDE record."""
        return cls.model_validate(record)


class Certificates_SkillType(BaseModel):
    """Nested model for the certificates.jsonl SDE file."""

    key: int = Field(..., alias="_key")
    basic: int
    standard: int
    improved: int
    advanced: int
    elite: int

    model_config = ConfigDict(serialize_by_alias=True)


class Certificates(SdeDataset):
    """Model for the certificates.jsonl SDE file."""

    key: int = Field(..., alias="_key")
    description: LocalizedString
    groupID: int
    name: LocalizedString
    recommendedFor: list[int] | None = None
    skillTypes: list[Certificates_SkillType]

    @classmethod
    def from_sde(cls, record: TDM.Certificates) -> Self:
        """Create a Certificates instance from a SDE record."""
        return cls.model_validate(record)


class CharacterAttributes(SdeDataset):
    """Model for the characterAttributes.jsonl SDE file."""

    key: int = Field(..., alias="_key")
    description: str
    iconID: int
    name: LocalizedString
    notes: str
    shortDescription: str

    @classmethod
    def from_sde(cls, record: TDM.CharacterAttributes) -> Self:
        """Create a CharacterAttributes instance from a SDE record."""
        return cls.model_validate(record)


class CloneGrades(SdeDataset):
    """Model for the cloneGrades.jsonl SDE file."""

    key: int = Field(..., alias="_key")
    name: str
    skills: list[Skills]

    @classmethod
    def from_sde(cls, record: TDM.CloneGrades) -> Self:
        """Create a CloneGrades instance from a SDE record."""
        return cls.model_validate(record)


class CompressibleTypes(SdeDataset):
    """Model for the compressibleTypes.jsonl SDE file."""

    key: int = Field(..., alias="_key")
    compressedTypeID: int

    @classmethod
    def from_sde(cls, record: TDM.CompressibleTypes) -> Self:
        """Create a CompressibleTypes instance from a SDE record."""
        return cls.model_validate(record)


class ContrabandTypes_Faction(SdeDataset):
    """Nested model for the contrabandTypes.jsonl SDE file."""

    key: int = Field(..., alias="_key")
    attackMinSec: float
    confiscateMinSec: float
    fineByValue: float
    standingLoss: float

    @classmethod
    def from_sde(cls, record: TDM.ContrabandTypes_Faction) -> Self:
        """Create a ContrabandTypes_Faction instance from a SDE record."""
        return cls.model_validate(record)


class ContrabandTypes(SdeDataset):
    """Model for the contrabandTypes.jsonl SDE file."""

    key: int = Field(..., alias="_key")
    factions: list[ContrabandTypes_Faction]

    @classmethod
    def from_sde(cls, record: TDM.ContrabandTypes) -> Self:
        """Create a ContrabandTypes instance from a SDE record."""
        return cls.model_validate(record)


class ControlTowerResources_Resource(BaseModel):
    """Nested model for the controlTowerResources.jsonl SDE file."""

    factionID: int | None = None
    minSecurityLevel: float | None = None
    purpose: int
    quantity: int
    resourceTypeID: int


class ControlTowerResources(SdeDataset):
    """Model for the controlTowerResources.jsonl SDE file."""

    key: int = Field(..., alias="_key")
    resources: list[ControlTowerResources_Resource]

    @classmethod
    def from_sde(cls, record: TDM.ControlTowerResources) -> Self:
        """Create a ControlTowerResources instance from a SDE record."""
        return cls.model_validate(record)


class CorporationActivities(SdeDataset):
    """Model for the corporationActivities.jsonl SDE file."""

    key: int = Field(..., alias="_key")
    name: LocalizedString

    @classmethod
    def from_sde(cls, record: TDM.CorporationActivities) -> Self:
        """Create a CorporationActivities instance from a SDE record."""
        return cls.model_validate(record)


class DebuffCollections_LocationGroupModifier(BaseModel):
    """Nested model for the debuffCollections.jsonl SDE file."""

    dogmaAttributeID: int
    groupID: int


class DebuffCollections_LocationModifier(BaseModel):
    """Nested model for the debuffCollections.jsonl SDE file."""

    dogmaAttributeID: int


class DebuffCollections_LocationRequiredSkillModifier(BaseModel):
    """Nested model for the debuffCollections.jsonl SDE file."""

    dogmaAttributeID: int
    skillID: int


class DebuffCollections_ItemModifier(BaseModel):
    """Nested model for the debuffCollections.jsonl SDE file."""

    dogmaAttributeID: int


class DebuffCollections(SdeDataset):
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

    @classmethod
    def from_sde(cls, record: TDM.DebuffCollections) -> Self:
        """Create a DebuffCollections instance from a SDE record."""
        return cls.model_validate(record)


class DogmaAttributeCategories(SdeDataset):
    """Model for the dogmaAttributeCategories.jsonl SDE file."""

    key: int = Field(..., alias="_key")
    description: str | None = None
    name: str

    @classmethod
    def from_sde(cls, record: TDM.DogmaAttributeCategories) -> Self:
        """Create a DogmaAttributeCategories instance from a SDE record."""
        return cls.model_validate(record)


class DogmaAttributes(SdeDataset):
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

    @classmethod
    def from_sde(cls, record: TDM.DogmaAttributes) -> Self:
        """Create a DogmaAttributes instance from a SDE record."""
        return cls.model_validate(record)


class DogmaEffects_ModifierInfo(BaseModel):
    """Nested model for the dogmaEffects.jsonl SDE file."""

    domain: str
    effectID: int | None = None
    func: str
    groupID: int | None = None
    modifiedAttributeID: int | None = None
    modifyingAttributeID: int | None = None
    operation: int | None = None
    skillTypeID: int | None = None


class DogmaEffects(SdeDataset):
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

    @classmethod
    def from_sde(cls, record: TDM.DogmaEffects) -> Self:
        """Create a DogmaEffects instance from a SDE record."""
        return cls.model_validate(record)


class DogmaUnits(SdeDataset):
    """Model for the dogmaUnits.jsonl SDE file."""

    key: int = Field(..., alias="_key")
    description: LocalizedString | None = None
    displayName: LocalizedString | None = None
    name: str

    @classmethod
    def from_sde(cls, record: TDM.DogmaUnits) -> Self:
        """Create a DogmaUnits instance from a SDE record."""
        return cls.model_validate(record)


class DynamicItemAttributes_AttributeID(SdeDataset):
    """Nested model for the dynamicItemAttributes.jsonl SDE file."""

    key: int = Field(..., alias="_key")
    highIsGood: bool | None = None
    max: float
    min: float

    @classmethod
    def from_sde(cls, record: TDM.DynamicItemAttributes_AttributeID) -> Self:
        """Create a DynamicItemAttributes_AttributeID instance from a SDE record."""
        return cls.model_validate(record)


class DynamicItemAttributes_InputOutputMapping(BaseModel):
    """Nested model for the dynamicItemAttributes.jsonl SDE file."""

    applicableTypes: list[int]
    resultingType: int


class DynamicItemAttributes(SdeDataset):
    """Model for the dynamicItemAttributes.jsonl SDE file."""

    key: int = Field(..., alias="_key")
    attributeIDs: list[DynamicItemAttributes_AttributeID]
    inputOutputMapping: list[DynamicItemAttributes_InputOutputMapping]

    @classmethod
    def from_sde(cls, record: TDM.DynamicItemAttributes) -> Self:
        """Create a DynamicItemAttributes instance from a SDE record."""
        return cls.model_validate(record)


class Factions(SdeDataset):
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

    @classmethod
    def from_sde(cls, record: TDM.Factions) -> Self:
        """Create a Factions instance from a SDE record."""
        return cls.model_validate(record)


class FreelanceJobSchemas(SdeDataset):
    """Model for the freelanceJobSchemas.jsonl SDE file."""

    key: int = Field(..., alias="_key")
    value: list[dict[str, Any]] = Field(..., alias="_value")

    @classmethod
    def from_sde(cls, record: TDM.FreelanceJobSchemas) -> Self:
        """Create a FreelanceJobSchemas instance from a SDE record."""
        return cls.model_validate(record)


class Graphics(SdeDataset):
    """Model for the graphics.jsonl SDE file."""

    key: int = Field(..., alias="_key")
    graphicFile: str | None = None
    iconFolder: str | None = None
    sofFactionName: str | None = None
    sofHullName: str | None = None
    sofRaceName: str | None = None
    sofMaterialSetID: int | None = None
    sofLayout: list[str] | None = None

    @classmethod
    def from_sde(cls, record: TDM.Graphics) -> Self:
        """Create a Graphics instance from a SDE record."""
        return cls.model_validate(record)


class Groups(SdeDataset):
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

    @classmethod
    def from_sde(cls, record: TDM.Groups) -> Self:
        """Create a Groups instance from a SDE record."""
        return cls.model_validate(record)


class Icons(SdeDataset):
    """Model for the icons.jsonl SDE file."""

    key: int = Field(..., alias="_key")
    iconFile: str

    @classmethod
    def from_sde(cls, record: TDM.Icons) -> Self:
        """Create an Icons instance from a SDE record."""
        return cls.model_validate(record)


class Landmarks(SdeDataset):
    """Model for the landmarks.jsonl SDE file."""

    key: int = Field(..., alias="_key")
    description: LocalizedString
    name: LocalizedString
    position: Position
    iconID: int | None = None
    locationID: int | None = None

    @classmethod
    def from_sde(cls, record: TDM.Landmarks) -> Self:
        """Create a Landmarks instance from a SDE record."""
        return cls.model_validate(record)


class MapAsteroidBelts_Statistics(BaseModel):
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


class MapAsteroidBelts(SdeDataset):
    """Model for the mapAsteroidBelts.jsonl SDE file."""

    key: int = Field(..., alias="_key")
    celestialIndex: int
    orbitID: int
    orbitIndex: int
    position: Position
    radius: float | None = None
    solarSystemID: int
    statistics: MapAsteroidBelts_Statistics | None = None
    typeID: int
    uniqueName: LocalizedString | None = None

    @classmethod
    def from_sde(cls, record: TDM.MapAsteroidBelts) -> Self:
        """Create a MapAsteroidBelts instance from a SDE record."""
        return cls.model_validate(record)


class MapConstellations(SdeDataset):
    """Model for the mapConstellations.jsonl SDE file."""

    key: int = Field(..., alias="_key")
    factionID: int | None = None
    name: LocalizedString
    position: Position
    regionID: int
    solarSystemIDs: list[int]
    wormholeClassID: int | None = None

    @classmethod
    def from_sde(cls, record: TDM.MapConstellations) -> Self:
        """Create a MapConstellations instance from a SDE record."""
        return cls.model_validate(record)


class MapMoons_Attributes(BaseModel):
    """Nested model for the mapMoons.jsonl SDE file."""

    heightMap1: int
    heightMap2: int
    shaderPreset: int


class MapMoons_Statistics(BaseModel):
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


class MapMoons(SdeDataset):
    """Model for the mapMoons.jsonl SDE file."""

    key: int = Field(..., alias="_key")
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

    @classmethod
    def from_sde(cls, record: TDM.MapMoons) -> Self:
        """Create a MapMoons instance from a SDE record."""
        return cls.model_validate(record)


class MapPlanets_Attributes(BaseModel):
    """Nested model for the mapPlanets.jsonl SDE file."""

    heightMap1: int
    heightMap2: int
    population: bool
    shaderPreset: int


class MapPlanets_Statistics(BaseModel):
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


class MapPlanets(SdeDataset):
    """Model for the mapPlanets.jsonl SDE file."""

    key: int = Field(..., alias="_key")
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

    @classmethod
    def from_sde(cls, record: TDM.MapPlanets) -> Self:
        """Create a MapPlanets instance from a SDE record."""
        return cls.model_validate(record)


class MapRegions(SdeDataset):
    """Model for the mapRegions.jsonl SDE file."""

    key: int = Field(..., alias="_key")
    constellationIDs: list[int]
    description: LocalizedString | None = None
    factionID: int | None = None
    name: LocalizedString
    nebulaID: int
    position: Position
    wormholeClassID: int | None = None

    @classmethod
    def from_sde(cls, record: TDM.MapRegions) -> Self:
        """Create a MapRegions instance from a SDE record."""
        return cls.model_validate(record)


class MapSolarSystems(SdeDataset):
    """Model for the mapSolarSystems.jsonl SDE file."""

    key: int = Field(..., alias="_key")
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

    @classmethod
    def from_sde(cls, record: TDM.MapSolarSystems) -> Self:
        """Create a MapSolarSystems instance from a SDE record."""
        return cls.model_validate(record)


class MapStargates_Destination(BaseModel):
    """Nested model for the mapStargates.jsonl SDE file."""

    solarSystemID: int
    stargateID: int


class MapStargates(SdeDataset):
    """Model for the mapStargates.jsonl SDE file."""

    key: int = Field(..., alias="_key")
    destination: MapStargates_Destination
    position: Position
    solarSystemID: int
    typeID: int

    @classmethod
    def from_sde(cls, record: TDM.MapStargates) -> Self:
        """Create a MapStargates instance from a SDE record."""
        return cls.model_validate(record)


class MapStars_Statistics(BaseModel):
    """Nested model for the mapStars.jsonl SDE file."""

    age: float
    life: float
    luminosity: float
    spectralClass: str
    temperature: float


class MapStars(SdeDataset):
    """Model for the mapStars.jsonl SDE file."""

    key: int = Field(..., alias="_key")
    radius: int
    solarSystemID: int
    statistics: MapStars_Statistics
    typeID: int

    @classmethod
    def from_sde(cls, record: TDM.MapStars) -> Self:
        """Create a MapStars instance from a SDE record."""
        return cls.model_validate(record)


class MarketGroups(SdeDataset):
    """Model for the marketGroups.jsonl SDE file."""

    key: int = Field(..., alias="_key")
    description: LocalizedString | None = None
    hasTypes: bool
    iconID: int | None = None
    name: LocalizedString
    parentGroupID: int | None = None

    @classmethod
    def from_sde(cls, record: TDM.MarketGroups) -> Self:
        """Create a MarketGroups instance from a SDE record."""
        return cls.model_validate(record)


class Masteries_Value(SdeDataset):
    """Nested model for the masteries.jsonl SDE file."""

    key: int = Field(..., alias="_key")
    value: list[int] = Field(..., alias="_value")

    @classmethod
    def from_sde(cls, record: TDM.Masteries_Value) -> Self:
        """Create a Masteries_Value instance from a SDE record."""
        return cls.model_validate(record)


class Masteries(SdeDataset):
    """Model for the masteries.jsonl SDE file."""

    key: int = Field(..., alias="_key")
    value: list[Masteries_Value] = Field(..., alias="_value")

    @classmethod
    def from_sde(cls, record: TDM.Masteries) -> Self:
        """Create a Masteries instance from a SDE record."""
        return cls.model_validate(record)


class MetaGroups(SdeDataset):
    """Model for the metaGroups.jsonl SDE file."""

    key: int = Field(..., alias="_key")
    color: Color | None = None
    name: LocalizedString
    iconID: int | None = None
    iconSuffix: str | None = None
    description: LocalizedString | None = None

    @classmethod
    def from_sde(cls, record: TDM.MetaGroups) -> Self:
        """Create a MetaGroups instance from a SDE record."""
        return cls.model_validate(record)


class NpcCharacters_Skill(BaseModel):
    """Nested model for the npcCharacters.jsonl SDE file."""

    typeID: int


class NpcCharacters_Agent(BaseModel):
    """Nested model for the npcCharacters.jsonl SDE file."""

    agentTypeID: int
    divisionID: int
    isLocator: bool
    level: int


class NpcCharacters(SdeDataset):
    """Model for the npcCharacters.jsonl SDE file."""

    key: int = Field(..., alias="_key")
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

    @classmethod
    def from_sde(cls, record: TDM.NpcCharacters) -> Self:
        """Create a NpcCharacters instance from a SDE record."""
        return cls.model_validate(record)


class NpcCorporationDivisions(SdeDataset):
    """Model for the npcCorporationDivisions.jsonl SDE file."""

    key: int = Field(..., alias="_key")
    displayName: str | None = None
    internalName: str
    leaderTypeName: LocalizedString
    name: LocalizedString
    description: LocalizedString | None = None

    @classmethod
    def from_sde(cls, record: TDM.NpcCorporationDivisions) -> Self:
        """Create a NpcCorporationDivisions instance from a SDE record."""
        return cls.model_validate(record)


class NpcCorporations_Trade(SdeDataset):
    """Nested model for the npcCorporations.jsonl SDE file."""

    key: int = Field(..., alias="_key")
    value: float = Field(..., alias="_value")

    @classmethod
    def from_sde(cls, record: TDM.NpcCorporations_Trade) -> Self:
        """Create a NpcCorporations_Trade instance from a SDE record."""
        return cls.model_validate(record)


class NpcCorporations_Divisions(SdeDataset):
    """Nested model for the npcCorporations.jsonl SDE file."""

    key: int = Field(..., alias="_key")
    divisionNumber: int
    leaderID: int
    size: int

    @classmethod
    def from_sde(cls, record: TDM.NpcCorporations_Divisions) -> Self:
        """Create a NpcCorporations_Divisions instance from a SDE record."""
        return cls.model_validate(record)


class NpcCorporations_Investors(SdeDataset):
    """Nested model for the npcCorporations.jsonl SDE file."""

    key: int = Field(..., alias="_key")
    value: int = Field(..., alias="_value")

    @classmethod
    def from_sde(cls, record: TDM.NpcCorporations_Investors) -> Self:
        """Create a NpcCorporations_Investors instance from a SDE record."""
        return cls.model_validate(record)


class NpcCorporations_ExchangeRates(SdeDataset):
    """Nested model for the npcCorporations.jsonl SDE file."""

    key: int = Field(..., alias="_key")
    value: float = Field(..., alias="_value")

    @classmethod
    def from_sde(cls, record: TDM.NpcCorporations_ExchangeRates) -> Self:
        """Create a NpcCorporations_ExchangeRates instance from a SDE record."""
        return cls.model_validate(record)


class NpcCorporations(SdeDataset):
    """Model for the npcCorporations.jsonl SDE file."""

    key: int = Field(..., alias="_key")
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
    corporationTrades: list[NpcCorporations_Trade] | None = None
    divisions: list[NpcCorporations_Divisions] | None = None
    enemyID: int | None = None
    factionID: int | None = None
    friendID: int | None = None
    iconID: int | None = None
    investors: list[NpcCorporations_Investors] | None = None
    lpOfferTables: list[int] | None = None
    mainActivityID: int | None = None
    raceID: int | None = None
    sizeFactor: float | None = None
    solarSystemID: int | None = None
    secondaryActivityID: int | None = None
    exchangeRates: list[NpcCorporations_ExchangeRates] | None = None

    @classmethod
    def from_sde(cls, record: TDM.NpcCorporations) -> Self:
        """Create a NpcCorporations instance from a SDE record."""
        return cls.model_validate(record)


class NpcStations(SdeDataset):
    """Model for the npcStations.jsonl SDE file."""

    key: int = Field(..., alias="_key")
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

    @classmethod
    def from_sde(cls, record: TDM.NpcStations) -> Self:
        """Create a NpcStations instance from a SDE record."""
        return cls.model_validate(record)


class PlanetResources_Reagent(BaseModel):
    """Nested model for the planetResources.jsonl SDE file."""

    amount_per_cycle: int
    cycle_period: int
    secured_capacity: int
    type_id: int
    unsecured_capacity: int


class PlanetResources(SdeDataset):
    """Model for the planetResources.jsonl SDE file."""

    key: int = Field(..., alias="_key")
    power: int | None = None
    workforce: int | None = None
    reagent: PlanetResources_Reagent | None = None

    @classmethod
    def from_sde(cls, record: TDM.PlanetResources) -> Self:
        """Create a PlanetResources instance from a SDE record."""
        return cls.model_validate(record)


class PlanetSchematics_Types(BaseModel):
    """Nested model for the planetSchematics.jsonl SDE file."""

    key: int = Field(..., alias="_key")
    isInput: bool
    quantity: int

    model_config = ConfigDict(serialize_by_alias=True)


class PlanetSchematics(SdeDataset):
    """Model for the planetSchematics.jsonl SDE file."""

    key: int = Field(..., alias="_key")
    cycleTime: int
    name: LocalizedString
    pins: list[int]
    types: list[PlanetSchematics_Types]

    @classmethod
    def from_sde(cls, record: TDM.PlanetSchematics) -> Self:
        """Create a PlanetSchematics instance from a SDE record."""
        return cls.model_validate(record)


class Races_Skill(BaseModel):
    """Nested model for the races.jsonl SDE file."""

    key: int = Field(..., alias="_key")
    value: int = Field(..., alias="_value")

    model_config = ConfigDict(serialize_by_alias=True)


class Races(SdeDataset):
    """Model for the races.jsonl SDE file."""

    key: int = Field(..., alias="_key")
    description: LocalizedString | None = None
    iconID: int | None = None
    name: LocalizedString
    shipTypeID: int | None = None
    skills: list[Races_Skill] | None = None

    @classmethod
    def from_sde(cls, record: TDM.Races) -> Self:
        """Create a Races instance from a SDE record."""
        return cls.model_validate(record)


class SdeInfo(SdeDataset):
    """Model for the sdeInfo.jsonl SDE file."""

    key: str = Field(..., alias="_key")
    buildNumber: int
    releaseDate: str

    @classmethod
    def from_sde(cls, record: TDM.SdeInfo) -> Self:
        """Create a SdeInfo instance from a SDE record."""
        return cls.model_validate(record)


class SkinLicenses(SdeDataset):
    """Model for the skinLicenses.jsonl SDE file."""

    key: int = Field(..., alias="_key")
    duration: int
    licenseTypeID: int
    skinID: int
    isSingleUse: bool | None = None

    @classmethod
    def from_sde(cls, record: TDM.SkinLicenses) -> Self:
        """Create a SkinLicenses instance from a SDE record."""
        return cls.model_validate(record)


class SkinMaterials(SdeDataset):
    """Model for the skinMaterials.jsonl SDE file."""

    key: int = Field(..., alias="_key")
    displayName: LocalizedString | None = None
    materialSetID: int

    @classmethod
    def from_sde(cls, record: TDM.SkinMaterials) -> Self:
        """Create a SkinMaterials instance from a SDE record."""
        return cls.model_validate(record)


class Skins(SdeDataset):
    """Model for the skins.jsonl SDE file."""

    key: int = Field(..., alias="_key")
    allowCCPDevs: bool
    internalName: str
    skinMaterialID: int
    types: list[int]
    visibleSerenity: bool
    visibleTranquility: bool
    isStructureSkin: bool | None = None
    skinDescription: LocalizedString | None = None

    @classmethod
    def from_sde(cls, record: TDM.Skins) -> Self:
        """Create a Skins instance from a SDE record."""
        return cls.model_validate(record)


class SovereigntyUpgrades_Fuel(BaseModel):
    """Nested model for the sovereigntyUpgrades.jsonl SDE file."""

    hourly_upkeep: int
    startup_cost: int
    type_id: int


class SovereigntyUpgrades(SdeDataset):
    """Model for the sovereigntyUpgrades.jsonl SDE file."""

    key: int = Field(..., alias="_key")
    fuel: SovereigntyUpgrades_Fuel | None = None
    mutually_exclusive_group: str
    power_allocation: int | None = None
    power_production: int | None = None
    workforce_allocation: int | None = None
    workforce_production: int | None = None

    @classmethod
    def from_sde(cls, record: TDM.SovereigntyUpgrades) -> Self:
        """Create a SovereigntyUpgrades instance from a SDE record."""
        return cls.model_validate(record)


class StationOperations_StationType(SdeDataset):
    """Nested model for the stationOperations.jsonl SDE file."""

    key: int = Field(..., alias="_key")
    value: int = Field(..., alias="_value")

    model_config = ConfigDict(serialize_by_alias=True)


class StationOperations(SdeDataset):
    """Model for the stationOperations.jsonl SDE file."""

    key: int = Field(..., alias="_key")
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
    stationTypes: list[StationOperations_StationType] | None = None

    @classmethod
    def from_sde(cls, record: TDM.StationOperations) -> Self:
        """Create a StationOperations instance from a SDE record."""
        return cls.model_validate(record)


class StationServices(SdeDataset):
    """Model for the stationServices.jsonl SDE file."""

    key: int = Field(..., alias="_key")
    serviceName: LocalizedString
    description: LocalizedString | None = None

    @classmethod
    def from_sde(cls, record: TDM.StationServices) -> Self:
        """Create a StationServices instance from a SDE record."""
        return cls.model_validate(record)


class TranslationLanguages(SdeDataset):
    """Model for the translationLanguages.jsonl SDE file."""

    key: str = Field(..., alias="_key")
    name: str

    @classmethod
    def from_sde(cls, record: TDM.TranslationLanguages) -> Self:
        """Create a TranslationLanguages instance from a SDE record."""
        return cls.model_validate(record)


class TypeBonus_RoleBonus(BaseModel):
    """Nested model for the typeBonus.jsonl SDE file."""

    bonus: int | float | None = None
    bonusText: LocalizedString
    importance: int
    unitID: int | None = None


class TypeBonus_Types_Bonus(BaseModel):
    """Nested model for the typeBonus.jsonl SDE file."""

    bonus: int | float | None = None
    bonusText: LocalizedString
    importance: int
    unitID: int | None = None


class TypeBonus_Types(BaseModel):
    """Nested model for the typeBonus.jsonl SDE file."""

    key: int = Field(..., alias="_key")
    value: list[TypeBonus_Types_Bonus] = Field(..., alias="_value")

    model_config = ConfigDict(serialize_by_alias=True)


class TypeBonus_MiscBonus(BaseModel):
    """Nested model for the typeBonus.jsonl SDE file."""

    bonus: int | float | None = None
    bonusText: LocalizedString
    importance: int
    isPositive: bool | None = None
    unitID: int | None = None


class TypeBonus(SdeDataset):
    """Model for the typeBonus.jsonl SDE file."""

    key: int = Field(..., alias="_key")
    roleBonuses: list[TypeBonus_RoleBonus] | None = None
    types: list[TypeBonus_Types] | None = None
    iconID: int | None = None
    miscBonuses: list[TypeBonus_MiscBonus] | None = None

    @classmethod
    def from_sde(cls, record: TDM.TypeBonus) -> Self:
        """Create a TypeBonus instance from a SDE record."""
        return cls.model_validate(record)


class TypeDogma_Attributes(BaseModel):
    """Nested model for the typeDogma.jsonl SDE file."""

    attributeID: int
    value: float


class TypeDogma_Effects(BaseModel):
    """Nested model for the typeDogma.jsonl SDE file."""

    effectID: int
    isDefault: bool


class TypeDogma(SdeDataset):
    """Model for the typeDogma.jsonl SDE file."""

    key: int = Field(..., alias="_key")
    dogmaAttributes: list[TypeDogma_Attributes]
    dogmaEffects: list[TypeDogma_Effects] | None = None

    @classmethod
    def from_sde(cls, record: TDM.TypeDogma) -> Self:
        """Create a TypeDogma instance from a SDE record."""
        return cls.model_validate(record)


class TypeMaterials_Material(BaseModel):
    """Nested model for the typeMaterials.jsonl SDE file."""

    materialTypeID: int
    quantity: int


class TypeMaterials_RandomizedMaterial(BaseModel):
    """Nested model for the typeMaterials.jsonl SDE file."""

    materialTypeID: int
    quantityMax: int
    quantityMin: int


class TypeMaterials(SdeDataset):
    """Model for the typeMaterials.jsonl SDE file."""

    key: int = Field(..., alias="_key")
    materials: list[TypeMaterials_Material] | None = None
    randomizedMaterials: list[TypeMaterials_RandomizedMaterial] | None = None

    @classmethod
    def from_sde(cls, record: TDM.TypeMaterials) -> Self:
        """Create a TypeMaterials instance from a SDE record."""
        return cls.model_validate(record)


class EveTypes(SdeDataset):
    """Model for the types.jsonl SDE file."""

    key: int = Field(..., alias="_key")
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

    @classmethod
    def from_sde(cls, record: TDM.EveTypes) -> Self:
        """Create an EveTypes instance from a SDE record."""
        return cls.model_validate(record)
