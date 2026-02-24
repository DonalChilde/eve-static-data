"""Models for localized dataset files, which define the expected filenames for each dataset when exported to disk."""

from enum import StrEnum


class DerivedLocalizedDatasetFiles(StrEnum):
    MARKET_PATHS = "market_paths.json"
    NORMALIZED_EVE_TYPES = "normalized_eve_types.json"
    NORMALIZED_EVE_TYPES_PUBLISHED = "normalized_eve_types_published.json"


class ExportedDatasetFiles(StrEnum):
    ANCESTRIES = "ancestries.json"
    BLUEPRINTS = "blueprints.json"
    CATEGORIES = "categories.json"
    GROUPS = "groups.json"
    MAP_REGIONS = "map_regions.json"
    MAP_SOLARSYSTEMS = "map_solarsystems.json"
    MARKET_GROUPS = "market_groups.json"
    META_GROUPS = "meta_groups.json"
    TYPE_MATERIALS = "type_materials.json"
    EVE_TYPES = "eve_types.json"


# TODO make this a template, add language code to filename.
class ExportedLocalizedDatasetFiles(StrEnum):
    ANCESTRIES = "ancestries-localized.json"
    CATEGORIES = "categories-localized.json"
    GROUPS = "groups-localized.json"
    MAP_REGIONS = "map_regions-localized.json"
    MAP_SOLARSYSTEMS = "map_solarsystems-localized.json"
    MARKET_GROUPS = "market_groups-localized.json"
    META_GROUPS = "meta_groups-localized.json"
    EVE_TYPES = "eve_types-localized.json"
