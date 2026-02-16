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
