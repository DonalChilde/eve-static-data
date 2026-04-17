"""Static SQLite DDL statements for EVE SDE tables."""

AGENT_TYPES_TABLE: tuple[str, ...] = (
    """CREATE TABLE IF NOT EXISTS agent_types (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    source_key INTEGER,
    name TEXT);
""",
)
AGENTS_IN_SPACE_TABLE: tuple[str, ...] = (
    """CREATE TABLE IF NOT EXISTS agents_in_space (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    source_key INTEGER,
    dungeon_id INTEGER,
    solar_system_id INTEGER,
    spawn_point_id INTEGER,
    type_id INTEGER
);""",
)


CREATE_TABLE_STATEMENTS: tuple[str, ...] = (
    """CREATE TABLE IF NOT EXISTS agent_types (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    source_key INTEGER,
    name TEXT
);""",
    """CREATE TABLE IF NOT EXISTS agents_in_space (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    source_key INTEGER,
    dungeon_id INTEGER,
    solar_system_id INTEGER,
    spawn_point_id INTEGER,
    type_id INTEGER
);""",
    """CREATE TABLE IF NOT EXISTS ancestries (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    source_key INTEGER,
    bloodline_id INTEGER,
    charisma INTEGER,
    icon_id INTEGER,
    intelligence INTEGER,
    memory INTEGER,
    perception INTEGER,
    short_description TEXT,
    willpower INTEGER
);""",
    """CREATE TABLE IF NOT EXISTS ancestries_description_localized (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    parent_id INTEGER NOT NULL,
    source_key INTEGER,
    en TEXT,
    de TEXT,
    fr TEXT,
    ja TEXT,
    zh TEXT,
    ru TEXT,
    ko TEXT,
    es TEXT
);""",
    """CREATE TABLE IF NOT EXISTS ancestries_name_localized (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    parent_id INTEGER NOT NULL,
    source_key INTEGER,
    en TEXT,
    de TEXT,
    fr TEXT,
    ja TEXT,
    zh TEXT,
    ru TEXT,
    ko TEXT,
    es TEXT
);""",
    """CREATE TABLE IF NOT EXISTS bloodlines (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    source_key INTEGER,
    charisma INTEGER,
    corporation_id INTEGER,
    icon_id INTEGER,
    intelligence INTEGER,
    memory INTEGER,
    perception INTEGER,
    race_id INTEGER,
    willpower INTEGER
);""",
    """CREATE TABLE IF NOT EXISTS bloodlines_description_localized (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    parent_id INTEGER NOT NULL,
    source_key INTEGER,
    en TEXT,
    de TEXT,
    fr TEXT,
    ja TEXT,
    zh TEXT,
    ru TEXT,
    ko TEXT,
    es TEXT
);""",
    """CREATE TABLE IF NOT EXISTS bloodlines_name_localized (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    parent_id INTEGER NOT NULL,
    source_key INTEGER,
    en TEXT,
    de TEXT,
    fr TEXT,
    ja TEXT,
    zh TEXT,
    ru TEXT,
    ko TEXT,
    es TEXT
);""",
    """CREATE TABLE IF NOT EXISTS blueprints (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    source_key INTEGER,
    activities JSON,
    blueprint_type_id INTEGER,
    max_production_limit INTEGER
);""",
    """CREATE TABLE IF NOT EXISTS blueprints_activities (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    copying JSON,
    invention JSON,
    manufacturing JSON,
    reaction JSON,
    research_material JSON,
    research_time JSON
);""",
    """CREATE TABLE IF NOT EXISTS blueprints_activity (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    time INTEGER
);""",
    """CREATE TABLE IF NOT EXISTS blueprints_activity_materials (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    parent_id INTEGER NOT NULL,
    item_index INTEGER NOT NULL,
    item_json JSON
);""",
    """CREATE TABLE IF NOT EXISTS blueprints_activity_products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    parent_id INTEGER NOT NULL,
    item_index INTEGER NOT NULL,
    item_json JSON
);""",
    """CREATE TABLE IF NOT EXISTS blueprints_activity_skills (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    parent_id INTEGER NOT NULL,
    item_index INTEGER NOT NULL,
    item_json JSON
);""",
    """CREATE TABLE IF NOT EXISTS blueprints_products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    type_id INTEGER,
    quantity INTEGER,
    probability REAL
);""",
    """CREATE TABLE IF NOT EXISTS categories (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    source_key INTEGER,
    published INTEGER,
    icon_id INTEGER
);""",
    """CREATE TABLE IF NOT EXISTS categories_name_localized (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    parent_id INTEGER NOT NULL,
    source_key INTEGER,
    en TEXT,
    de TEXT,
    fr TEXT,
    ja TEXT,
    zh TEXT,
    ru TEXT,
    ko TEXT,
    es TEXT
);""",
    """CREATE TABLE IF NOT EXISTS certificates (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    source_key INTEGER,
    group_id INTEGER
);""",
    """CREATE TABLE IF NOT EXISTS certificates_description_localized (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    parent_id INTEGER NOT NULL,
    source_key INTEGER,
    en TEXT,
    de TEXT,
    fr TEXT,
    ja TEXT,
    zh TEXT,
    ru TEXT,
    ko TEXT,
    es TEXT
);""",
    """CREATE TABLE IF NOT EXISTS certificates_name_localized (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    parent_id INTEGER NOT NULL,
    source_key INTEGER,
    en TEXT,
    de TEXT,
    fr TEXT,
    ja TEXT,
    zh TEXT,
    ru TEXT,
    ko TEXT,
    es TEXT
);""",
    """CREATE TABLE IF NOT EXISTS certificates_recommended_for (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    parent_id INTEGER NOT NULL,
    item_index INTEGER NOT NULL,
    item_json JSON
);""",
    """CREATE TABLE IF NOT EXISTS certificates_skill_type (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    source_key INTEGER,
    basic INTEGER,
    standard INTEGER,
    improved INTEGER,
    advanced INTEGER,
    elite INTEGER
);""",
    """CREATE TABLE IF NOT EXISTS certificates_skill_types (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    parent_id INTEGER NOT NULL,
    item_index INTEGER NOT NULL,
    item_json JSON
);""",
    """CREATE TABLE IF NOT EXISTS character_attributes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    source_key INTEGER,
    description TEXT,
    icon_id INTEGER,
    notes TEXT,
    short_description TEXT
);""",
    """CREATE TABLE IF NOT EXISTS character_attributes_name_localized (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    parent_id INTEGER NOT NULL,
    source_key INTEGER,
    en TEXT,
    de TEXT,
    fr TEXT,
    ja TEXT,
    zh TEXT,
    ru TEXT,
    ko TEXT,
    es TEXT
);""",
    """CREATE TABLE IF NOT EXISTS clone_grades (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    source_key INTEGER,
    name TEXT
);""",
    """CREATE TABLE IF NOT EXISTS clone_grades_skills (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    parent_id INTEGER NOT NULL,
    item_index INTEGER NOT NULL,
    item_json JSON
);""",
    """CREATE TABLE IF NOT EXISTS color (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    b REAL,
    g REAL,
    r REAL
);""",
    """CREATE TABLE IF NOT EXISTS compressible_types (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    source_key INTEGER,
    compressed_type_id INTEGER
);""",
    """CREATE TABLE IF NOT EXISTS contraband_types (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    source_key INTEGER
);""",
    """CREATE TABLE IF NOT EXISTS contraband_types_faction (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    source_key INTEGER,
    attack_min_sec REAL,
    confiscate_min_sec REAL,
    fine_by_value REAL,
    standing_loss REAL
);""",
    """CREATE TABLE IF NOT EXISTS contraband_types_factions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    parent_id INTEGER NOT NULL,
    item_index INTEGER NOT NULL,
    item_json JSON
);""",
    """CREATE TABLE IF NOT EXISTS control_tower_resources (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    source_key INTEGER
);""",
    """CREATE TABLE IF NOT EXISTS control_tower_resources_resource (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    faction_id INTEGER,
    min_security_level REAL,
    purpose INTEGER,
    quantity INTEGER,
    resource_type_id INTEGER
);""",
    """CREATE TABLE IF NOT EXISTS control_tower_resources_resources (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    parent_id INTEGER NOT NULL,
    item_index INTEGER NOT NULL,
    item_json JSON
);""",
    """CREATE TABLE IF NOT EXISTS corporation_activities (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    source_key INTEGER
);""",
    """CREATE TABLE IF NOT EXISTS corporation_activities_name_localized (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    parent_id INTEGER NOT NULL,
    source_key INTEGER,
    en TEXT,
    de TEXT,
    fr TEXT,
    ja TEXT,
    zh TEXT,
    ru TEXT,
    ko TEXT,
    es TEXT
);""",
    """CREATE TABLE IF NOT EXISTS debuff_collections (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    source_key INTEGER,
    aggregate_mode TEXT,
    developer_description TEXT,
    operation_name TEXT,
    show_output_value_in_ui TEXT
);""",
    """CREATE TABLE IF NOT EXISTS debuff_collections_display_name_localized (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    parent_id INTEGER NOT NULL,
    source_key INTEGER,
    en TEXT,
    de TEXT,
    fr TEXT,
    ja TEXT,
    zh TEXT,
    ru TEXT,
    ko TEXT,
    es TEXT
);""",
    """CREATE TABLE IF NOT EXISTS debuff_collections_item_modifier (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    dogma_attribute_id INTEGER
);""",
    """CREATE TABLE IF NOT EXISTS debuff_collections_item_modifiers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    parent_id INTEGER NOT NULL,
    item_index INTEGER NOT NULL,
    item_json JSON
);""",
    """CREATE TABLE IF NOT EXISTS debuff_collections_location_group_modifier (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    dogma_attribute_id INTEGER,
    group_id INTEGER
);""",
    """CREATE TABLE IF NOT EXISTS debuff_collections_location_group_modifiers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    parent_id INTEGER NOT NULL,
    item_index INTEGER NOT NULL,
    item_json JSON
);""",
    """CREATE TABLE IF NOT EXISTS debuff_collections_location_modifier (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    dogma_attribute_id INTEGER
);""",
    """CREATE TABLE IF NOT EXISTS debuff_collections_location_modifiers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    parent_id INTEGER NOT NULL,
    item_index INTEGER NOT NULL,
    item_json JSON
);""",
    """CREATE TABLE IF NOT EXISTS debuff_collections_location_required_skill_modifier (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    dogma_attribute_id INTEGER,
    skill_id INTEGER
);""",
    """CREATE TABLE IF NOT EXISTS debuff_collections_location_required_skill_modifiers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    parent_id INTEGER NOT NULL,
    item_index INTEGER NOT NULL,
    item_json JSON
);""",
    """CREATE TABLE IF NOT EXISTS dogma_attribute_categories (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    source_key INTEGER,
    description TEXT,
    name TEXT
);""",
    """CREATE TABLE IF NOT EXISTS dogma_attributes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    source_key INTEGER,
    attribute_category_id INTEGER,
    data_type INTEGER,
    default_value REAL,
    description TEXT,
    display_when_zero INTEGER,
    high_is_good INTEGER,
    name TEXT,
    published INTEGER,
    stackable INTEGER,
    icon_id INTEGER,
    unit_id INTEGER,
    charge_recharge_time_id INTEGER,
    max_attribute_id INTEGER,
    min_attribute_id INTEGER
);""",
    """CREATE TABLE IF NOT EXISTS dogma_attributes_display_name_localized (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    parent_id INTEGER NOT NULL,
    source_key INTEGER,
    en TEXT,
    de TEXT,
    fr TEXT,
    ja TEXT,
    zh TEXT,
    ru TEXT,
    ko TEXT,
    es TEXT
);""",
    """CREATE TABLE IF NOT EXISTS dogma_attributes_tooltip_description_localized (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    parent_id INTEGER NOT NULL,
    source_key INTEGER,
    en TEXT,
    de TEXT,
    fr TEXT,
    ja TEXT,
    zh TEXT,
    ru TEXT,
    ko TEXT,
    es TEXT
);""",
    """CREATE TABLE IF NOT EXISTS dogma_attributes_tooltip_title_localized (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    parent_id INTEGER NOT NULL,
    source_key INTEGER,
    en TEXT,
    de TEXT,
    fr TEXT,
    ja TEXT,
    zh TEXT,
    ru TEXT,
    ko TEXT,
    es TEXT
);""",
    """CREATE TABLE IF NOT EXISTS dogma_effects (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    source_key INTEGER,
    disallow_auto_repeat INTEGER,
    discharge_attribute_id INTEGER,
    duration_attribute_id INTEGER,
    effect_category_id INTEGER,
    electronic_chance INTEGER,
    guid TEXT,
    is_assistance INTEGER,
    is_offensive INTEGER,
    is_warp_safe INTEGER,
    name TEXT,
    propulsion_chance INTEGER,
    published INTEGER,
    range_chance INTEGER,
    distribution INTEGER,
    falloff_attribute_id INTEGER,
    range_attribute_id INTEGER,
    tracking_speed_attribute_id INTEGER,
    icon_id INTEGER,
    npc_usage_chance_attribute_id INTEGER,
    npc_activation_chance_attribute_id INTEGER,
    fitting_usage_chance_attribute_id INTEGER,
    resistance_attribute_id INTEGER
);""",
    """CREATE TABLE IF NOT EXISTS dogma_effects_description_localized (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    parent_id INTEGER NOT NULL,
    source_key INTEGER,
    en TEXT,
    de TEXT,
    fr TEXT,
    ja TEXT,
    zh TEXT,
    ru TEXT,
    ko TEXT,
    es TEXT
);""",
    """CREATE TABLE IF NOT EXISTS dogma_effects_display_name_localized (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    parent_id INTEGER NOT NULL,
    source_key INTEGER,
    en TEXT,
    de TEXT,
    fr TEXT,
    ja TEXT,
    zh TEXT,
    ru TEXT,
    ko TEXT,
    es TEXT
);""",
    """CREATE TABLE IF NOT EXISTS dogma_effects_modifier_info (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    parent_id INTEGER NOT NULL,
    item_index INTEGER NOT NULL,
    item_json JSON
);""",
    """CREATE TABLE IF NOT EXISTS dogma_effects_modifier_info (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    domain TEXT,
    effect_id INTEGER,
    func TEXT,
    group_id INTEGER,
    modified_attribute_id INTEGER,
    modifying_attribute_id INTEGER,
    operation INTEGER,
    skill_type_id INTEGER
);""",
    """CREATE TABLE IF NOT EXISTS dogma_units (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    source_key INTEGER,
    name TEXT
);""",
    """CREATE TABLE IF NOT EXISTS dogma_units_description_localized (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    parent_id INTEGER NOT NULL,
    source_key INTEGER,
    en TEXT,
    de TEXT,
    fr TEXT,
    ja TEXT,
    zh TEXT,
    ru TEXT,
    ko TEXT,
    es TEXT
);""",
    """CREATE TABLE IF NOT EXISTS dogma_units_display_name_localized (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    parent_id INTEGER NOT NULL,
    source_key INTEGER,
    en TEXT,
    de TEXT,
    fr TEXT,
    ja TEXT,
    zh TEXT,
    ru TEXT,
    ko TEXT,
    es TEXT
);""",
    """CREATE TABLE IF NOT EXISTS dynamic_item_attributes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    source_key INTEGER
);""",
    """CREATE TABLE IF NOT EXISTS dynamic_item_attributes_attribute_i_ds (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    parent_id INTEGER NOT NULL,
    item_index INTEGER NOT NULL,
    item_json JSON
);""",
    """CREATE TABLE IF NOT EXISTS dynamic_item_attributes_attribute_id (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    source_key INTEGER,
    high_is_good INTEGER,
    max REAL,
    min REAL
);""",
    """CREATE TABLE IF NOT EXISTS dynamic_item_attributes_input_output_mapping (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    parent_id INTEGER NOT NULL,
    item_index INTEGER NOT NULL,
    item_json JSON
);""",
    """CREATE TABLE IF NOT EXISTS dynamic_item_attributes_input_output_mapping (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    resulting_type INTEGER
);""",
    """CREATE TABLE IF NOT EXISTS dynamic_item_attributes_input_output_mapping_applicable_types (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    parent_id INTEGER NOT NULL,
    item_index INTEGER NOT NULL,
    item_json JSON
);""",
    """CREATE TABLE IF NOT EXISTS eve_types (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    source_key INTEGER,
    group_id INTEGER,
    mass REAL,
    portion_size INTEGER,
    published INTEGER,
    volume REAL,
    radius REAL,
    graphic_id INTEGER,
    sound_id INTEGER,
    icon_id INTEGER,
    race_id INTEGER,
    base_price REAL,
    market_group_id INTEGER,
    capacity REAL,
    meta_group_id INTEGER,
    variation_parent_type_id INTEGER,
    faction_id INTEGER
);""",
    """CREATE TABLE IF NOT EXISTS eve_types_description_localized (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    parent_id INTEGER NOT NULL,
    source_key INTEGER,
    en TEXT,
    de TEXT,
    fr TEXT,
    ja TEXT,
    zh TEXT,
    ru TEXT,
    ko TEXT,
    es TEXT
);""",
    """CREATE TABLE IF NOT EXISTS eve_types_name_localized (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    parent_id INTEGER NOT NULL,
    source_key INTEGER,
    en TEXT,
    de TEXT,
    fr TEXT,
    ja TEXT,
    zh TEXT,
    ru TEXT,
    ko TEXT,
    es TEXT
);""",
    """CREATE TABLE IF NOT EXISTS factions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    source_key INTEGER,
    corporation_id INTEGER,
    flat_logo TEXT,
    flat_logo_with_name TEXT,
    icon_id INTEGER,
    militia_corporation_id INTEGER,
    size_factor REAL,
    solar_system_id INTEGER,
    unique_name INTEGER
);""",
    """CREATE TABLE IF NOT EXISTS factions_description_localized (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    parent_id INTEGER NOT NULL,
    source_key INTEGER,
    en TEXT,
    de TEXT,
    fr TEXT,
    ja TEXT,
    zh TEXT,
    ru TEXT,
    ko TEXT,
    es TEXT
);""",
    """CREATE TABLE IF NOT EXISTS factions_member_races (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    parent_id INTEGER NOT NULL,
    item_index INTEGER NOT NULL,
    item_json JSON
);""",
    """CREATE TABLE IF NOT EXISTS factions_name_localized (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    parent_id INTEGER NOT NULL,
    source_key INTEGER,
    en TEXT,
    de TEXT,
    fr TEXT,
    ja TEXT,
    zh TEXT,
    ru TEXT,
    ko TEXT,
    es TEXT
);""",
    """CREATE TABLE IF NOT EXISTS factions_short_description_localized (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    parent_id INTEGER NOT NULL,
    source_key INTEGER,
    en TEXT,
    de TEXT,
    fr TEXT,
    ja TEXT,
    zh TEXT,
    ru TEXT,
    ko TEXT,
    es TEXT
);""",
    """CREATE TABLE IF NOT EXISTS freelance_job_schemas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    source_key INTEGER
);""",
    """CREATE TABLE IF NOT EXISTS freelance_job_schemas_value (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    parent_id INTEGER NOT NULL,
    item_index INTEGER NOT NULL,
    item_json JSON
);""",
    """CREATE TABLE IF NOT EXISTS graphics (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    source_key INTEGER,
    graphic_file TEXT,
    icon_folder TEXT,
    sof_faction_name TEXT,
    sof_hull_name TEXT,
    sof_race_name TEXT,
    sof_material_set_id INTEGER
);""",
    """CREATE TABLE IF NOT EXISTS graphics_sof_layout (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    parent_id INTEGER NOT NULL,
    item_index INTEGER NOT NULL,
    item_json JSON
);""",
    """CREATE TABLE IF NOT EXISTS groups (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    source_key INTEGER,
    anchorable INTEGER,
    anchored INTEGER,
    category_id INTEGER,
    fittable_non_singleton INTEGER,
    published INTEGER,
    use_base_price INTEGER,
    icon_id INTEGER
);""",
    """CREATE TABLE IF NOT EXISTS groups_name_localized (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    parent_id INTEGER NOT NULL,
    source_key INTEGER,
    en TEXT,
    de TEXT,
    fr TEXT,
    ja TEXT,
    zh TEXT,
    ru TEXT,
    ko TEXT,
    es TEXT
);""",
    """CREATE TABLE IF NOT EXISTS icons (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    source_key INTEGER,
    icon_file TEXT
);""",
    """CREATE TABLE IF NOT EXISTS landmarks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    source_key INTEGER,
    position JSON,
    icon_id INTEGER,
    location_id INTEGER
);""",
    """CREATE TABLE IF NOT EXISTS landmarks_description_localized (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    parent_id INTEGER NOT NULL,
    source_key INTEGER,
    en TEXT,
    de TEXT,
    fr TEXT,
    ja TEXT,
    zh TEXT,
    ru TEXT,
    ko TEXT,
    es TEXT
);""",
    """CREATE TABLE IF NOT EXISTS landmarks_name_localized (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    parent_id INTEGER NOT NULL,
    source_key INTEGER,
    en TEXT,
    de TEXT,
    fr TEXT,
    ja TEXT,
    zh TEXT,
    ru TEXT,
    ko TEXT,
    es TEXT
);""",
    """CREATE TABLE IF NOT EXISTS localized_string (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    en TEXT,
    de TEXT,
    fr TEXT,
    ja TEXT,
    zh TEXT,
    ru TEXT,
    ko TEXT,
    es TEXT
);""",
    """CREATE TABLE IF NOT EXISTS map_asteroid_belts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    source_key INTEGER,
    celestial_index INTEGER,
    orbit_id INTEGER,
    orbit_index INTEGER,
    position JSON,
    radius REAL,
    solar_system_id INTEGER,
    statistics JSON,
    type_id INTEGER
);""",
    """CREATE TABLE IF NOT EXISTS map_asteroid_belts_statistics (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    density REAL,
    eccentricity REAL,
    escape_velocity REAL,
    locked INTEGER,
    mass_dust REAL,
    mass_gas REAL,
    orbit_period REAL,
    orbit_radius REAL,
    rotation_rate REAL,
    spectral_class TEXT,
    surface_gravity REAL,
    temperature REAL
);""",
    """CREATE TABLE IF NOT EXISTS map_asteroid_belts_unique_name_localized (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    parent_id INTEGER NOT NULL,
    source_key INTEGER,
    en TEXT,
    de TEXT,
    fr TEXT,
    ja TEXT,
    zh TEXT,
    ru TEXT,
    ko TEXT,
    es TEXT
);""",
    """CREATE TABLE IF NOT EXISTS map_constellations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    source_key INTEGER,
    faction_id INTEGER,
    position JSON,
    region_id INTEGER,
    wormhole_class_id INTEGER
);""",
    """CREATE TABLE IF NOT EXISTS map_constellations_name_localized (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    parent_id INTEGER NOT NULL,
    source_key INTEGER,
    en TEXT,
    de TEXT,
    fr TEXT,
    ja TEXT,
    zh TEXT,
    ru TEXT,
    ko TEXT,
    es TEXT
);""",
    """CREATE TABLE IF NOT EXISTS map_constellations_solar_system_i_ds (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    parent_id INTEGER NOT NULL,
    item_index INTEGER NOT NULL,
    item_json JSON
);""",
    """CREATE TABLE IF NOT EXISTS map_moons (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    source_key INTEGER,
    attributes JSON,
    celestial_index INTEGER,
    orbit_id INTEGER,
    orbit_index INTEGER,
    position JSON,
    radius REAL,
    solar_system_id INTEGER,
    statistics JSON,
    type_id INTEGER
);""",
    """CREATE TABLE IF NOT EXISTS map_moons_attributes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    height_map1 INTEGER,
    height_map2 INTEGER,
    shader_preset INTEGER
);""",
    """CREATE TABLE IF NOT EXISTS map_moons_npc_station_i_ds (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    parent_id INTEGER NOT NULL,
    item_index INTEGER NOT NULL,
    item_json JSON
);""",
    """CREATE TABLE IF NOT EXISTS map_moons_statistics (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    density REAL,
    eccentricity REAL,
    escape_velocity REAL,
    locked INTEGER,
    mass_dust REAL,
    mass_gas REAL,
    orbit_period REAL,
    orbit_radius REAL,
    pressure REAL,
    rotation_rate REAL,
    spectral_class TEXT,
    surface_gravity REAL,
    temperature REAL
);""",
    """CREATE TABLE IF NOT EXISTS map_moons_unique_name_localized (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    parent_id INTEGER NOT NULL,
    source_key INTEGER,
    en TEXT,
    de TEXT,
    fr TEXT,
    ja TEXT,
    zh TEXT,
    ru TEXT,
    ko TEXT,
    es TEXT
);""",
    """CREATE TABLE IF NOT EXISTS map_planets (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    source_key INTEGER,
    attributes JSON,
    celestial_index INTEGER,
    orbit_id INTEGER,
    position JSON,
    radius INTEGER,
    solar_system_id INTEGER,
    statistics JSON,
    type_id INTEGER
);""",
    """CREATE TABLE IF NOT EXISTS map_planets_asteroid_belt_i_ds (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    parent_id INTEGER NOT NULL,
    item_index INTEGER NOT NULL,
    item_json JSON
);""",
    """CREATE TABLE IF NOT EXISTS map_planets_attributes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    height_map1 INTEGER,
    height_map2 INTEGER,
    population INTEGER,
    shader_preset INTEGER
);""",
    """CREATE TABLE IF NOT EXISTS map_planets_moon_i_ds (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    parent_id INTEGER NOT NULL,
    item_index INTEGER NOT NULL,
    item_json JSON
);""",
    """CREATE TABLE IF NOT EXISTS map_planets_npc_station_i_ds (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    parent_id INTEGER NOT NULL,
    item_index INTEGER NOT NULL,
    item_json JSON
);""",
    """CREATE TABLE IF NOT EXISTS map_planets_statistics (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    density REAL,
    eccentricity REAL,
    escape_velocity REAL,
    locked INTEGER,
    mass_dust REAL,
    mass_gas REAL,
    orbit_period REAL,
    orbit_radius REAL,
    pressure REAL,
    rotation_rate REAL,
    spectral_class TEXT,
    surface_gravity REAL,
    temperature REAL
);""",
    """CREATE TABLE IF NOT EXISTS map_planets_unique_name_localized (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    parent_id INTEGER NOT NULL,
    source_key INTEGER,
    en TEXT,
    de TEXT,
    fr TEXT,
    ja TEXT,
    zh TEXT,
    ru TEXT,
    ko TEXT,
    es TEXT
);""",
    """CREATE TABLE IF NOT EXISTS map_regions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    source_key INTEGER,
    faction_id INTEGER,
    nebula_id INTEGER,
    position JSON,
    wormhole_class_id INTEGER
);""",
    """CREATE TABLE IF NOT EXISTS map_regions_constellation_i_ds (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    parent_id INTEGER NOT NULL,
    item_index INTEGER NOT NULL,
    item_json JSON
);""",
    """CREATE TABLE IF NOT EXISTS map_regions_description_localized (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    parent_id INTEGER NOT NULL,
    source_key INTEGER,
    en TEXT,
    de TEXT,
    fr TEXT,
    ja TEXT,
    zh TEXT,
    ru TEXT,
    ko TEXT,
    es TEXT
);""",
    """CREATE TABLE IF NOT EXISTS map_regions_name_localized (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    parent_id INTEGER NOT NULL,
    source_key INTEGER,
    en TEXT,
    de TEXT,
    fr TEXT,
    ja TEXT,
    zh TEXT,
    ru TEXT,
    ko TEXT,
    es TEXT
);""",
    """CREATE TABLE IF NOT EXISTS map_secondary_suns (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    source_key INTEGER,
    effect_beacon_type_id INTEGER,
    position JSON,
    solar_system_id INTEGER,
    type_id INTEGER
);""",
    """CREATE TABLE IF NOT EXISTS map_solar_systems (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    source_key INTEGER,
    border INTEGER,
    constellation_id INTEGER,
    corridor INTEGER,
    faction_id INTEGER,
    fringe INTEGER,
    hub INTEGER,
    international INTEGER,
    luminosity REAL,
    position JSON,
    position2_d JSON,
    radius REAL,
    region_id INTEGER,
    regional INTEGER,
    security_class TEXT,
    security_status REAL,
    star_id INTEGER,
    visual_effect TEXT,
    wormhole_class_id INTEGER
);""",
    """CREATE TABLE IF NOT EXISTS map_solar_systems_disallowed_anchor_categories (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    parent_id INTEGER NOT NULL,
    item_index INTEGER NOT NULL,
    item_json JSON
);""",
    """CREATE TABLE IF NOT EXISTS map_solar_systems_disallowed_anchor_groups (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    parent_id INTEGER NOT NULL,
    item_index INTEGER NOT NULL,
    item_json JSON
);""",
    """CREATE TABLE IF NOT EXISTS map_solar_systems_name_localized (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    parent_id INTEGER NOT NULL,
    source_key INTEGER,
    en TEXT,
    de TEXT,
    fr TEXT,
    ja TEXT,
    zh TEXT,
    ru TEXT,
    ko TEXT,
    es TEXT
);""",
    """CREATE TABLE IF NOT EXISTS map_solar_systems_planet_i_ds (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    parent_id INTEGER NOT NULL,
    item_index INTEGER NOT NULL,
    item_json JSON
);""",
    """CREATE TABLE IF NOT EXISTS map_solar_systems_stargate_i_ds (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    parent_id INTEGER NOT NULL,
    item_index INTEGER NOT NULL,
    item_json JSON
);""",
    """CREATE TABLE IF NOT EXISTS map_stargates (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    source_key INTEGER,
    destination JSON,
    position JSON,
    solar_system_id INTEGER,
    type_id INTEGER
);""",
    """CREATE TABLE IF NOT EXISTS map_stargates_destination (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    solar_system_id INTEGER,
    stargate_id INTEGER
);""",
    """CREATE TABLE IF NOT EXISTS map_stars (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    source_key INTEGER,
    radius INTEGER,
    solar_system_id INTEGER,
    statistics JSON,
    type_id INTEGER
);""",
    """CREATE TABLE IF NOT EXISTS map_stars_statistics (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    age REAL,
    life REAL,
    luminosity REAL,
    spectral_class TEXT,
    temperature REAL
);""",
    """CREATE TABLE IF NOT EXISTS market_groups (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    source_key INTEGER,
    has_types INTEGER,
    icon_id INTEGER,
    parent_group_id INTEGER
);""",
    """CREATE TABLE IF NOT EXISTS market_groups_description_localized (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    parent_id INTEGER NOT NULL,
    source_key INTEGER,
    en TEXT,
    de TEXT,
    fr TEXT,
    ja TEXT,
    zh TEXT,
    ru TEXT,
    ko TEXT,
    es TEXT
);""",
    """CREATE TABLE IF NOT EXISTS market_groups_name_localized (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    parent_id INTEGER NOT NULL,
    source_key INTEGER,
    en TEXT,
    de TEXT,
    fr TEXT,
    ja TEXT,
    zh TEXT,
    ru TEXT,
    ko TEXT,
    es TEXT
);""",
    """CREATE TABLE IF NOT EXISTS masteries (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    source_key INTEGER
);""",
    """CREATE TABLE IF NOT EXISTS masteries_value (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    parent_id INTEGER NOT NULL,
    item_index INTEGER NOT NULL,
    item_json JSON
);""",
    """CREATE TABLE IF NOT EXISTS masteries_value (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    source_key INTEGER
);""",
    """CREATE TABLE IF NOT EXISTS masteries_value_value (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    parent_id INTEGER NOT NULL,
    item_index INTEGER NOT NULL,
    item_json JSON
);""",
    """CREATE TABLE IF NOT EXISTS materials (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    type_id INTEGER,
    quantity INTEGER
);""",
    """CREATE TABLE IF NOT EXISTS mercenary_tactical_operations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    source_key INTEGER,
    anarchy_impact INTEGER,
    development_impact INTEGER,
    infomorph_bonus INTEGER
);""",
    """CREATE TABLE IF NOT EXISTS mercenary_tactical_operations_description_localized (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    parent_id INTEGER NOT NULL,
    source_key INTEGER,
    en TEXT,
    de TEXT,
    fr TEXT,
    ja TEXT,
    zh TEXT,
    ru TEXT,
    ko TEXT,
    es TEXT
);""",
    """CREATE TABLE IF NOT EXISTS mercenary_tactical_operations_name_localized (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    parent_id INTEGER NOT NULL,
    source_key INTEGER,
    en TEXT,
    de TEXT,
    fr TEXT,
    ja TEXT,
    zh TEXT,
    ru TEXT,
    ko TEXT,
    es TEXT
);""",
    """CREATE TABLE IF NOT EXISTS meta_groups (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    source_key INTEGER,
    color JSON,
    icon_id INTEGER,
    icon_suffix TEXT
);""",
    """CREATE TABLE IF NOT EXISTS meta_groups_description_localized (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    parent_id INTEGER NOT NULL,
    source_key INTEGER,
    en TEXT,
    de TEXT,
    fr TEXT,
    ja TEXT,
    zh TEXT,
    ru TEXT,
    ko TEXT,
    es TEXT
);""",
    """CREATE TABLE IF NOT EXISTS meta_groups_name_localized (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    parent_id INTEGER NOT NULL,
    source_key INTEGER,
    en TEXT,
    de TEXT,
    fr TEXT,
    ja TEXT,
    zh TEXT,
    ru TEXT,
    ko TEXT,
    es TEXT
);""",
    """CREATE TABLE IF NOT EXISTS npc_characters (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    source_key INTEGER,
    bloodline_id INTEGER,
    ceo INTEGER,
    corporation_id INTEGER,
    gender INTEGER,
    location_id INTEGER,
    race_id INTEGER,
    start_date TEXT,
    unique_name INTEGER,
    ancestry_id INTEGER,
    career_id INTEGER,
    school_id INTEGER,
    speciality_id INTEGER,
    agent JSON,
    description TEXT
);""",
    """CREATE TABLE IF NOT EXISTS npc_characters_agent (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    agent_type_id INTEGER,
    division_id INTEGER,
    is_locator INTEGER,
    level INTEGER
);""",
    """CREATE TABLE IF NOT EXISTS npc_characters_name_localized (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    parent_id INTEGER NOT NULL,
    source_key INTEGER,
    en TEXT,
    de TEXT,
    fr TEXT,
    ja TEXT,
    zh TEXT,
    ru TEXT,
    ko TEXT,
    es TEXT
);""",
    """CREATE TABLE IF NOT EXISTS npc_characters_skill (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    type_id INTEGER
);""",
    """CREATE TABLE IF NOT EXISTS npc_characters_skills (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    parent_id INTEGER NOT NULL,
    item_index INTEGER NOT NULL,
    item_json JSON
);""",
    """CREATE TABLE IF NOT EXISTS npc_corporation_divisions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    source_key INTEGER,
    display_name TEXT,
    internal_name TEXT
);""",
    """CREATE TABLE IF NOT EXISTS npc_corporation_divisions_description_localized (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    parent_id INTEGER NOT NULL,
    source_key INTEGER,
    en TEXT,
    de TEXT,
    fr TEXT,
    ja TEXT,
    zh TEXT,
    ru TEXT,
    ko TEXT,
    es TEXT
);""",
    """CREATE TABLE IF NOT EXISTS npc_corporation_divisions_leader_type_name_localized (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    parent_id INTEGER NOT NULL,
    source_key INTEGER,
    en TEXT,
    de TEXT,
    fr TEXT,
    ja TEXT,
    zh TEXT,
    ru TEXT,
    ko TEXT,
    es TEXT
);""",
    """CREATE TABLE IF NOT EXISTS npc_corporation_divisions_name_localized (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    parent_id INTEGER NOT NULL,
    source_key INTEGER,
    en TEXT,
    de TEXT,
    fr TEXT,
    ja TEXT,
    zh TEXT,
    ru TEXT,
    ko TEXT,
    es TEXT
);""",
    """CREATE TABLE IF NOT EXISTS npc_corporations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    source_key INTEGER,
    ceo_id INTEGER,
    deleted INTEGER,
    extent TEXT,
    has_player_personnel_manager INTEGER,
    initial_price INTEGER,
    member_limit INTEGER,
    min_security REAL,
    minimum_join_standing INTEGER,
    send_char_termination_message INTEGER,
    shares INTEGER,
    size TEXT,
    station_id INTEGER,
    tax_rate REAL,
    ticker_name TEXT,
    unique_name INTEGER,
    enemy_id INTEGER,
    faction_id INTEGER,
    friend_id INTEGER,
    icon_id INTEGER,
    main_activity_id INTEGER,
    race_id INTEGER,
    size_factor REAL,
    solar_system_id INTEGER,
    secondary_activity_id INTEGER
);""",
    """CREATE TABLE IF NOT EXISTS npc_corporations_allowed_member_races (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    parent_id INTEGER NOT NULL,
    item_index INTEGER NOT NULL,
    item_json JSON
);""",
    """CREATE TABLE IF NOT EXISTS npc_corporations_corporation_trades (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    parent_id INTEGER NOT NULL,
    item_index INTEGER NOT NULL,
    item_json JSON
);""",
    """CREATE TABLE IF NOT EXISTS npc_corporations_description_localized (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    parent_id INTEGER NOT NULL,
    source_key INTEGER,
    en TEXT,
    de TEXT,
    fr TEXT,
    ja TEXT,
    zh TEXT,
    ru TEXT,
    ko TEXT,
    es TEXT
);""",
    """CREATE TABLE IF NOT EXISTS npc_corporations_divisions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    parent_id INTEGER NOT NULL,
    item_index INTEGER NOT NULL,
    item_json JSON
);""",
    """CREATE TABLE IF NOT EXISTS npc_corporations_divisions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    source_key INTEGER,
    division_number INTEGER,
    leader_id INTEGER,
    size INTEGER
);""",
    """CREATE TABLE IF NOT EXISTS npc_corporations_exchange_rates (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    parent_id INTEGER NOT NULL,
    item_index INTEGER NOT NULL,
    item_json JSON
);""",
    """CREATE TABLE IF NOT EXISTS npc_corporations_exchange_rates (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    source_key INTEGER,
    value REAL
);""",
    """CREATE TABLE IF NOT EXISTS npc_corporations_investors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    parent_id INTEGER NOT NULL,
    item_index INTEGER NOT NULL,
    item_json JSON
);""",
    """CREATE TABLE IF NOT EXISTS npc_corporations_investors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    source_key INTEGER,
    value INTEGER
);""",
    """CREATE TABLE IF NOT EXISTS npc_corporations_lp_offer_tables (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    parent_id INTEGER NOT NULL,
    item_index INTEGER NOT NULL,
    item_json JSON
);""",
    """CREATE TABLE IF NOT EXISTS npc_corporations_name_localized (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    parent_id INTEGER NOT NULL,
    source_key INTEGER,
    en TEXT,
    de TEXT,
    fr TEXT,
    ja TEXT,
    zh TEXT,
    ru TEXT,
    ko TEXT,
    es TEXT
);""",
    """CREATE TABLE IF NOT EXISTS npc_corporations_trade (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    source_key INTEGER,
    value INTEGER
);""",
    """CREATE TABLE IF NOT EXISTS npc_stations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    source_key INTEGER,
    celestial_index INTEGER,
    operation_id INTEGER,
    orbit_id INTEGER,
    orbit_index INTEGER,
    owner_id INTEGER,
    position JSON,
    reprocessing_efficiency REAL,
    reprocessing_hangar_flag INTEGER,
    reprocessing_stations_take REAL,
    solar_system_id INTEGER,
    type_id INTEGER,
    use_operation_name INTEGER
);""",
    """CREATE TABLE IF NOT EXISTS planet_resources (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    source_key INTEGER,
    power INTEGER,
    workforce INTEGER,
    reagent JSON
);""",
    """CREATE TABLE IF NOT EXISTS planet_resources_reagent (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    amount_per_cycle INTEGER,
    cycle_period INTEGER,
    secured_capacity INTEGER,
    type_id INTEGER,
    unsecured_capacity INTEGER
);""",
    """CREATE TABLE IF NOT EXISTS planet_schematics (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    source_key INTEGER,
    cycle_time INTEGER
);""",
    """CREATE TABLE IF NOT EXISTS planet_schematics_name_localized (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    parent_id INTEGER NOT NULL,
    source_key INTEGER,
    en TEXT,
    de TEXT,
    fr TEXT,
    ja TEXT,
    zh TEXT,
    ru TEXT,
    ko TEXT,
    es TEXT
);""",
    """CREATE TABLE IF NOT EXISTS planet_schematics_pins (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    parent_id INTEGER NOT NULL,
    item_index INTEGER NOT NULL,
    item_json JSON
);""",
    """CREATE TABLE IF NOT EXISTS planet_schematics_types (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    parent_id INTEGER NOT NULL,
    item_index INTEGER NOT NULL,
    item_json JSON
);""",
    """CREATE TABLE IF NOT EXISTS planet_schematics_types (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    source_key INTEGER,
    is_input INTEGER,
    quantity INTEGER
);""",
    """CREATE TABLE IF NOT EXISTS position (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    x REAL,
    y REAL,
    z REAL
);""",
    """CREATE TABLE IF NOT EXISTS position2_d (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    x REAL,
    y REAL
);""",
    """CREATE TABLE IF NOT EXISTS races (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    source_key INTEGER,
    icon_id INTEGER,
    ship_type_id INTEGER
);""",
    """CREATE TABLE IF NOT EXISTS races_description_localized (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    parent_id INTEGER NOT NULL,
    source_key INTEGER,
    en TEXT,
    de TEXT,
    fr TEXT,
    ja TEXT,
    zh TEXT,
    ru TEXT,
    ko TEXT,
    es TEXT
);""",
    """CREATE TABLE IF NOT EXISTS races_name_localized (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    parent_id INTEGER NOT NULL,
    source_key INTEGER,
    en TEXT,
    de TEXT,
    fr TEXT,
    ja TEXT,
    zh TEXT,
    ru TEXT,
    ko TEXT,
    es TEXT
);""",
    """CREATE TABLE IF NOT EXISTS races_skill (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    source_key INTEGER,
    value INTEGER
);""",
    """CREATE TABLE IF NOT EXISTS races_skills (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    parent_id INTEGER NOT NULL,
    item_index INTEGER NOT NULL,
    item_json JSON
);""",
    """CREATE TABLE IF NOT EXISTS sde_info (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    source_key INTEGER,
    build_number INTEGER,
    release_date TEXT
);""",
    """CREATE TABLE IF NOT EXISTS skills (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    type_id INTEGER,
    level INTEGER
);""",
    """CREATE TABLE IF NOT EXISTS skin_licenses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    source_key INTEGER,
    duration INTEGER,
    license_type_id INTEGER,
    skin_id INTEGER,
    is_single_use INTEGER
);""",
    """CREATE TABLE IF NOT EXISTS skin_materials (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    source_key INTEGER,
    material_set_id INTEGER
);""",
    """CREATE TABLE IF NOT EXISTS skin_materials_display_name_localized (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    parent_id INTEGER NOT NULL,
    source_key INTEGER,
    en TEXT,
    de TEXT,
    fr TEXT,
    ja TEXT,
    zh TEXT,
    ru TEXT,
    ko TEXT,
    es TEXT
);""",
    """CREATE TABLE IF NOT EXISTS skins (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    source_key INTEGER,
    allow_ccp_devs INTEGER,
    internal_name TEXT,
    skin_material_id INTEGER,
    visible_serenity INTEGER,
    visible_tranquility INTEGER,
    is_structure_skin INTEGER
);""",
    """CREATE TABLE IF NOT EXISTS skins_skin_description_localized (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    parent_id INTEGER NOT NULL,
    source_key INTEGER,
    en TEXT,
    de TEXT,
    fr TEXT,
    ja TEXT,
    zh TEXT,
    ru TEXT,
    ko TEXT,
    es TEXT
);""",
    """CREATE TABLE IF NOT EXISTS skins_types (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    parent_id INTEGER NOT NULL,
    item_index INTEGER NOT NULL,
    item_json JSON
);""",
    """CREATE TABLE IF NOT EXISTS sovereignty_upgrades (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    source_key INTEGER,
    fuel JSON,
    mutually_exclusive_group TEXT,
    power_allocation INTEGER,
    power_production INTEGER,
    workforce_allocation INTEGER,
    workforce_production INTEGER
);""",
    """CREATE TABLE IF NOT EXISTS sovereignty_upgrades_fuel (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    hourly_upkeep INTEGER,
    startup_cost INTEGER,
    type_id INTEGER
);""",
    """CREATE TABLE IF NOT EXISTS station_operations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    source_key INTEGER,
    activity_id INTEGER,
    border REAL,
    corridor REAL,
    fringe REAL,
    hub REAL,
    manufacturing_factor REAL,
    ratio REAL,
    research_factor REAL
);""",
    """CREATE TABLE IF NOT EXISTS station_operations_description_localized (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    parent_id INTEGER NOT NULL,
    source_key INTEGER,
    en TEXT,
    de TEXT,
    fr TEXT,
    ja TEXT,
    zh TEXT,
    ru TEXT,
    ko TEXT,
    es TEXT
);""",
    """CREATE TABLE IF NOT EXISTS station_operations_operation_name_localized (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    parent_id INTEGER NOT NULL,
    source_key INTEGER,
    en TEXT,
    de TEXT,
    fr TEXT,
    ja TEXT,
    zh TEXT,
    ru TEXT,
    ko TEXT,
    es TEXT
);""",
    """CREATE TABLE IF NOT EXISTS station_operations_services (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    parent_id INTEGER NOT NULL,
    item_index INTEGER NOT NULL,
    item_json JSON
);""",
    """CREATE TABLE IF NOT EXISTS station_operations_station_type (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    source_key INTEGER,
    value INTEGER
);""",
    """CREATE TABLE IF NOT EXISTS station_operations_station_types (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    parent_id INTEGER NOT NULL,
    item_index INTEGER NOT NULL,
    item_json JSON
);""",
    """CREATE TABLE IF NOT EXISTS station_services (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    source_key INTEGER
);""",
    """CREATE TABLE IF NOT EXISTS station_services_description_localized (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    parent_id INTEGER NOT NULL,
    source_key INTEGER,
    en TEXT,
    de TEXT,
    fr TEXT,
    ja TEXT,
    zh TEXT,
    ru TEXT,
    ko TEXT,
    es TEXT
);""",
    """CREATE TABLE IF NOT EXISTS station_services_service_name_localized (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    parent_id INTEGER NOT NULL,
    source_key INTEGER,
    en TEXT,
    de TEXT,
    fr TEXT,
    ja TEXT,
    zh TEXT,
    ru TEXT,
    ko TEXT,
    es TEXT
);""",
    """CREATE TABLE IF NOT EXISTS translation_languages (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    source_key INTEGER,
    name TEXT
);""",
    """CREATE TABLE IF NOT EXISTS type_bonus (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    source_key INTEGER,
    icon_id INTEGER
);""",
    """CREATE TABLE IF NOT EXISTS type_bonus_misc_bonus (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    bonus JSON,
    importance INTEGER,
    is_positive INTEGER,
    unit_id INTEGER
);""",
    """CREATE TABLE IF NOT EXISTS type_bonus_misc_bonus_bonus_text_localized (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    parent_id INTEGER NOT NULL,
    source_key INTEGER,
    en TEXT,
    de TEXT,
    fr TEXT,
    ja TEXT,
    zh TEXT,
    ru TEXT,
    ko TEXT,
    es TEXT
);""",
    """CREATE TABLE IF NOT EXISTS type_bonus_misc_bonuses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    parent_id INTEGER NOT NULL,
    item_index INTEGER NOT NULL,
    item_json JSON
);""",
    """CREATE TABLE IF NOT EXISTS type_bonus_role_bonus (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    bonus JSON,
    importance INTEGER,
    unit_id INTEGER
);""",
    """CREATE TABLE IF NOT EXISTS type_bonus_role_bonus_bonus_text_localized (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    parent_id INTEGER NOT NULL,
    source_key INTEGER,
    en TEXT,
    de TEXT,
    fr TEXT,
    ja TEXT,
    zh TEXT,
    ru TEXT,
    ko TEXT,
    es TEXT
);""",
    """CREATE TABLE IF NOT EXISTS type_bonus_role_bonuses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    parent_id INTEGER NOT NULL,
    item_index INTEGER NOT NULL,
    item_json JSON
);""",
    """CREATE TABLE IF NOT EXISTS type_bonus_types (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    parent_id INTEGER NOT NULL,
    item_index INTEGER NOT NULL,
    item_json JSON
);""",
    """CREATE TABLE IF NOT EXISTS type_bonus_types (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    source_key INTEGER
);""",
    """CREATE TABLE IF NOT EXISTS type_bonus_types_bonus (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    bonus JSON,
    importance INTEGER,
    unit_id INTEGER
);""",
    """CREATE TABLE IF NOT EXISTS type_bonus_types_bonus_bonus_text_localized (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    parent_id INTEGER NOT NULL,
    source_key INTEGER,
    en TEXT,
    de TEXT,
    fr TEXT,
    ja TEXT,
    zh TEXT,
    ru TEXT,
    ko TEXT,
    es TEXT
);""",
    """CREATE TABLE IF NOT EXISTS type_bonus_types_value (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    parent_id INTEGER NOT NULL,
    item_index INTEGER NOT NULL,
    item_json JSON
);""",
    """CREATE TABLE IF NOT EXISTS type_dogma (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    source_key INTEGER
);""",
    """CREATE TABLE IF NOT EXISTS type_dogma_attributes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    attribute_id INTEGER,
    value REAL
);""",
    """CREATE TABLE IF NOT EXISTS type_dogma_dogma_attributes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    parent_id INTEGER NOT NULL,
    item_index INTEGER NOT NULL,
    item_json JSON
);""",
    """CREATE TABLE IF NOT EXISTS type_dogma_dogma_effects (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    parent_id INTEGER NOT NULL,
    item_index INTEGER NOT NULL,
    item_json JSON
);""",
    """CREATE TABLE IF NOT EXISTS type_dogma_effects (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    effect_id INTEGER,
    is_default INTEGER
);""",
    """CREATE TABLE IF NOT EXISTS type_materials (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    source_key INTEGER
);""",
    """CREATE TABLE IF NOT EXISTS type_materials_material (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    material_type_id INTEGER,
    quantity INTEGER
);""",
    """CREATE TABLE IF NOT EXISTS type_materials_materials (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    parent_id INTEGER NOT NULL,
    item_index INTEGER NOT NULL,
    item_json JSON
);""",
    """CREATE TABLE IF NOT EXISTS type_materials_randomized_material (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    material_type_id INTEGER,
    quantity_max INTEGER,
    quantity_min INTEGER
);""",
    """CREATE TABLE IF NOT EXISTS type_materials_randomized_materials (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    parent_id INTEGER NOT NULL,
    item_index INTEGER NOT NULL,
    item_json JSON
);""",
)

CREATE_INDEX_STATEMENTS: tuple[str, ...] = (
    """CREATE INDEX IF NOT EXISTS idx_agent_types_source_key ON agent_types (source_key);""",
    """CREATE INDEX IF NOT EXISTS idx_agents_in_space_source_key ON agents_in_space (source_key);""",
    """CREATE INDEX IF NOT EXISTS idx_ancestries_description_localized_parent_id ON ancestries_description_localized (parent_id);""",
    """CREATE INDEX IF NOT EXISTS idx_ancestries_description_localized_source_key ON ancestries_description_localized (source_key);""",
    """CREATE INDEX IF NOT EXISTS idx_ancestries_name_localized_parent_id ON ancestries_name_localized (parent_id);""",
    """CREATE INDEX IF NOT EXISTS idx_ancestries_name_localized_source_key ON ancestries_name_localized (source_key);""",
    """CREATE INDEX IF NOT EXISTS idx_ancestries_source_key ON ancestries (source_key);""",
    """CREATE INDEX IF NOT EXISTS idx_bloodlines_description_localized_parent_id ON bloodlines_description_localized (parent_id);""",
    """CREATE INDEX IF NOT EXISTS idx_bloodlines_description_localized_source_key ON bloodlines_description_localized (source_key);""",
    """CREATE INDEX IF NOT EXISTS idx_bloodlines_name_localized_parent_id ON bloodlines_name_localized (parent_id);""",
    """CREATE INDEX IF NOT EXISTS idx_bloodlines_name_localized_source_key ON bloodlines_name_localized (source_key);""",
    """CREATE INDEX IF NOT EXISTS idx_bloodlines_source_key ON bloodlines (source_key);""",
    """CREATE INDEX IF NOT EXISTS idx_blueprints_activity_materials_item_index ON blueprints_activity_materials (item_index);""",
    """CREATE INDEX IF NOT EXISTS idx_blueprints_activity_materials_parent_id ON blueprints_activity_materials (parent_id);""",
    """CREATE INDEX IF NOT EXISTS idx_blueprints_activity_products_item_index ON blueprints_activity_products (item_index);""",
    """CREATE INDEX IF NOT EXISTS idx_blueprints_activity_products_parent_id ON blueprints_activity_products (parent_id);""",
    """CREATE INDEX IF NOT EXISTS idx_blueprints_activity_skills_item_index ON blueprints_activity_skills (item_index);""",
    """CREATE INDEX IF NOT EXISTS idx_blueprints_activity_skills_parent_id ON blueprints_activity_skills (parent_id);""",
    """CREATE INDEX IF NOT EXISTS idx_blueprints_source_key ON blueprints (source_key);""",
    """CREATE INDEX IF NOT EXISTS idx_categories_name_localized_parent_id ON categories_name_localized (parent_id);""",
    """CREATE INDEX IF NOT EXISTS idx_categories_name_localized_source_key ON categories_name_localized (source_key);""",
    """CREATE INDEX IF NOT EXISTS idx_categories_source_key ON categories (source_key);""",
    """CREATE INDEX IF NOT EXISTS idx_certificates_description_localized_parent_id ON certificates_description_localized (parent_id);""",
    """CREATE INDEX IF NOT EXISTS idx_certificates_description_localized_source_key ON certificates_description_localized (source_key);""",
    """CREATE INDEX IF NOT EXISTS idx_certificates_name_localized_parent_id ON certificates_name_localized (parent_id);""",
    """CREATE INDEX IF NOT EXISTS idx_certificates_name_localized_source_key ON certificates_name_localized (source_key);""",
    """CREATE INDEX IF NOT EXISTS idx_certificates_recommended_for_item_index ON certificates_recommended_for (item_index);""",
    """CREATE INDEX IF NOT EXISTS idx_certificates_recommended_for_parent_id ON certificates_recommended_for (parent_id);""",
    """CREATE INDEX IF NOT EXISTS idx_certificates_skill_type_source_key ON certificates_skill_type (source_key);""",
    """CREATE INDEX IF NOT EXISTS idx_certificates_skill_types_item_index ON certificates_skill_types (item_index);""",
    """CREATE INDEX IF NOT EXISTS idx_certificates_skill_types_parent_id ON certificates_skill_types (parent_id);""",
    """CREATE INDEX IF NOT EXISTS idx_certificates_source_key ON certificates (source_key);""",
    """CREATE INDEX IF NOT EXISTS idx_character_attributes_name_localized_parent_id ON character_attributes_name_localized (parent_id);""",
    """CREATE INDEX IF NOT EXISTS idx_character_attributes_name_localized_source_key ON character_attributes_name_localized (source_key);""",
    """CREATE INDEX IF NOT EXISTS idx_character_attributes_source_key ON character_attributes (source_key);""",
    """CREATE INDEX IF NOT EXISTS idx_clone_grades_skills_item_index ON clone_grades_skills (item_index);""",
    """CREATE INDEX IF NOT EXISTS idx_clone_grades_skills_parent_id ON clone_grades_skills (parent_id);""",
    """CREATE INDEX IF NOT EXISTS idx_clone_grades_source_key ON clone_grades (source_key);""",
    """CREATE INDEX IF NOT EXISTS idx_compressible_types_source_key ON compressible_types (source_key);""",
    """CREATE INDEX IF NOT EXISTS idx_contraband_types_faction_source_key ON contraband_types_faction (source_key);""",
    """CREATE INDEX IF NOT EXISTS idx_contraband_types_factions_item_index ON contraband_types_factions (item_index);""",
    """CREATE INDEX IF NOT EXISTS idx_contraband_types_factions_parent_id ON contraband_types_factions (parent_id);""",
    """CREATE INDEX IF NOT EXISTS idx_contraband_types_source_key ON contraband_types (source_key);""",
    """CREATE INDEX IF NOT EXISTS idx_control_tower_resources_resources_item_index ON control_tower_resources_resources (item_index);""",
    """CREATE INDEX IF NOT EXISTS idx_control_tower_resources_resources_parent_id ON control_tower_resources_resources (parent_id);""",
    """CREATE INDEX IF NOT EXISTS idx_control_tower_resources_source_key ON control_tower_resources (source_key);""",
    """CREATE INDEX IF NOT EXISTS idx_corporation_activities_name_localized_parent_id ON corporation_activities_name_localized (parent_id);""",
    """CREATE INDEX IF NOT EXISTS idx_corporation_activities_name_localized_source_key ON corporation_activities_name_localized (source_key);""",
    """CREATE INDEX IF NOT EXISTS idx_corporation_activities_source_key ON corporation_activities (source_key);""",
    """CREATE INDEX IF NOT EXISTS idx_debuff_collections_display_name_localized_parent_id ON debuff_collections_display_name_localized (parent_id);""",
    """CREATE INDEX IF NOT EXISTS idx_debuff_collections_display_name_localized_source_key ON debuff_collections_display_name_localized (source_key);""",
    """CREATE INDEX IF NOT EXISTS idx_debuff_collections_item_modifiers_item_index ON debuff_collections_item_modifiers (item_index);""",
    """CREATE INDEX IF NOT EXISTS idx_debuff_collections_item_modifiers_parent_id ON debuff_collections_item_modifiers (parent_id);""",
    """CREATE INDEX IF NOT EXISTS idx_debuff_collections_location_group_modifiers_item_index ON debuff_collections_location_group_modifiers (item_index);""",
    """CREATE INDEX IF NOT EXISTS idx_debuff_collections_location_group_modifiers_parent_id ON debuff_collections_location_group_modifiers (parent_id);""",
    """CREATE INDEX IF NOT EXISTS idx_debuff_collections_location_modifiers_item_index ON debuff_collections_location_modifiers (item_index);""",
    """CREATE INDEX IF NOT EXISTS idx_debuff_collections_location_modifiers_parent_id ON debuff_collections_location_modifiers (parent_id);""",
    """CREATE INDEX IF NOT EXISTS idx_debuff_collections_location_required_skill_modifiers_item_index ON debuff_collections_location_required_skill_modifiers (item_index);""",
    """CREATE INDEX IF NOT EXISTS idx_debuff_collections_location_required_skill_modifiers_parent_id ON debuff_collections_location_required_skill_modifiers (parent_id);""",
    """CREATE INDEX IF NOT EXISTS idx_debuff_collections_source_key ON debuff_collections (source_key);""",
    """CREATE INDEX IF NOT EXISTS idx_dogma_attribute_categories_source_key ON dogma_attribute_categories (source_key);""",
    """CREATE INDEX IF NOT EXISTS idx_dogma_attributes_display_name_localized_parent_id ON dogma_attributes_display_name_localized (parent_id);""",
    """CREATE INDEX IF NOT EXISTS idx_dogma_attributes_display_name_localized_source_key ON dogma_attributes_display_name_localized (source_key);""",
    """CREATE INDEX IF NOT EXISTS idx_dogma_attributes_source_key ON dogma_attributes (source_key);""",
    """CREATE INDEX IF NOT EXISTS idx_dogma_attributes_tooltip_description_localized_parent_id ON dogma_attributes_tooltip_description_localized (parent_id);""",
    """CREATE INDEX IF NOT EXISTS idx_dogma_attributes_tooltip_description_localized_source_key ON dogma_attributes_tooltip_description_localized (source_key);""",
    """CREATE INDEX IF NOT EXISTS idx_dogma_attributes_tooltip_title_localized_parent_id ON dogma_attributes_tooltip_title_localized (parent_id);""",
    """CREATE INDEX IF NOT EXISTS idx_dogma_attributes_tooltip_title_localized_source_key ON dogma_attributes_tooltip_title_localized (source_key);""",
    """CREATE INDEX IF NOT EXISTS idx_dogma_effects_description_localized_parent_id ON dogma_effects_description_localized (parent_id);""",
    """CREATE INDEX IF NOT EXISTS idx_dogma_effects_description_localized_source_key ON dogma_effects_description_localized (source_key);""",
    """CREATE INDEX IF NOT EXISTS idx_dogma_effects_display_name_localized_parent_id ON dogma_effects_display_name_localized (parent_id);""",
    """CREATE INDEX IF NOT EXISTS idx_dogma_effects_display_name_localized_source_key ON dogma_effects_display_name_localized (source_key);""",
    """CREATE INDEX IF NOT EXISTS idx_dogma_effects_modifier_info_item_index ON dogma_effects_modifier_info (item_index);""",
    """CREATE INDEX IF NOT EXISTS idx_dogma_effects_modifier_info_parent_id ON dogma_effects_modifier_info (parent_id);""",
    """CREATE INDEX IF NOT EXISTS idx_dogma_effects_source_key ON dogma_effects (source_key);""",
    """CREATE INDEX IF NOT EXISTS idx_dogma_units_description_localized_parent_id ON dogma_units_description_localized (parent_id);""",
    """CREATE INDEX IF NOT EXISTS idx_dogma_units_description_localized_source_key ON dogma_units_description_localized (source_key);""",
    """CREATE INDEX IF NOT EXISTS idx_dogma_units_display_name_localized_parent_id ON dogma_units_display_name_localized (parent_id);""",
    """CREATE INDEX IF NOT EXISTS idx_dogma_units_display_name_localized_source_key ON dogma_units_display_name_localized (source_key);""",
    """CREATE INDEX IF NOT EXISTS idx_dogma_units_source_key ON dogma_units (source_key);""",
    """CREATE INDEX IF NOT EXISTS idx_dynamic_item_attributes_attribute_i_ds_item_index ON dynamic_item_attributes_attribute_i_ds (item_index);""",
    """CREATE INDEX IF NOT EXISTS idx_dynamic_item_attributes_attribute_i_ds_parent_id ON dynamic_item_attributes_attribute_i_ds (parent_id);""",
    """CREATE INDEX IF NOT EXISTS idx_dynamic_item_attributes_attribute_id_source_key ON dynamic_item_attributes_attribute_id (source_key);""",
    """CREATE INDEX IF NOT EXISTS idx_dynamic_item_attributes_input_output_mapping_applicable_types_item_index ON dynamic_item_attributes_input_output_mapping_applicable_types (item_index);""",
    """CREATE INDEX IF NOT EXISTS idx_dynamic_item_attributes_input_output_mapping_applicable_types_parent_id ON dynamic_item_attributes_input_output_mapping_applicable_types (parent_id);""",
    """CREATE INDEX IF NOT EXISTS idx_dynamic_item_attributes_input_output_mapping_item_index ON dynamic_item_attributes_input_output_mapping (item_index);""",
    """CREATE INDEX IF NOT EXISTS idx_dynamic_item_attributes_input_output_mapping_parent_id ON dynamic_item_attributes_input_output_mapping (parent_id);""",
    """CREATE INDEX IF NOT EXISTS idx_dynamic_item_attributes_source_key ON dynamic_item_attributes (source_key);""",
    """CREATE INDEX IF NOT EXISTS idx_eve_types_description_localized_parent_id ON eve_types_description_localized (parent_id);""",
    """CREATE INDEX IF NOT EXISTS idx_eve_types_description_localized_source_key ON eve_types_description_localized (source_key);""",
    """CREATE INDEX IF NOT EXISTS idx_eve_types_name_localized_parent_id ON eve_types_name_localized (parent_id);""",
    """CREATE INDEX IF NOT EXISTS idx_eve_types_name_localized_source_key ON eve_types_name_localized (source_key);""",
    """CREATE INDEX IF NOT EXISTS idx_eve_types_source_key ON eve_types (source_key);""",
    """CREATE INDEX IF NOT EXISTS idx_factions_description_localized_parent_id ON factions_description_localized (parent_id);""",
    """CREATE INDEX IF NOT EXISTS idx_factions_description_localized_source_key ON factions_description_localized (source_key);""",
    """CREATE INDEX IF NOT EXISTS idx_factions_member_races_item_index ON factions_member_races (item_index);""",
    """CREATE INDEX IF NOT EXISTS idx_factions_member_races_parent_id ON factions_member_races (parent_id);""",
    """CREATE INDEX IF NOT EXISTS idx_factions_name_localized_parent_id ON factions_name_localized (parent_id);""",
    """CREATE INDEX IF NOT EXISTS idx_factions_name_localized_source_key ON factions_name_localized (source_key);""",
    """CREATE INDEX IF NOT EXISTS idx_factions_short_description_localized_parent_id ON factions_short_description_localized (parent_id);""",
    """CREATE INDEX IF NOT EXISTS idx_factions_short_description_localized_source_key ON factions_short_description_localized (source_key);""",
    """CREATE INDEX IF NOT EXISTS idx_factions_source_key ON factions (source_key);""",
    """CREATE INDEX IF NOT EXISTS idx_freelance_job_schemas_source_key ON freelance_job_schemas (source_key);""",
    """CREATE INDEX IF NOT EXISTS idx_freelance_job_schemas_value_item_index ON freelance_job_schemas_value (item_index);""",
    """CREATE INDEX IF NOT EXISTS idx_freelance_job_schemas_value_parent_id ON freelance_job_schemas_value (parent_id);""",
    """CREATE INDEX IF NOT EXISTS idx_graphics_sof_layout_item_index ON graphics_sof_layout (item_index);""",
    """CREATE INDEX IF NOT EXISTS idx_graphics_sof_layout_parent_id ON graphics_sof_layout (parent_id);""",
    """CREATE INDEX IF NOT EXISTS idx_graphics_source_key ON graphics (source_key);""",
    """CREATE INDEX IF NOT EXISTS idx_groups_name_localized_parent_id ON groups_name_localized (parent_id);""",
    """CREATE INDEX IF NOT EXISTS idx_groups_name_localized_source_key ON groups_name_localized (source_key);""",
    """CREATE INDEX IF NOT EXISTS idx_groups_source_key ON groups (source_key);""",
    """CREATE INDEX IF NOT EXISTS idx_icons_source_key ON icons (source_key);""",
    """CREATE INDEX IF NOT EXISTS idx_landmarks_description_localized_parent_id ON landmarks_description_localized (parent_id);""",
    """CREATE INDEX IF NOT EXISTS idx_landmarks_description_localized_source_key ON landmarks_description_localized (source_key);""",
    """CREATE INDEX IF NOT EXISTS idx_landmarks_name_localized_parent_id ON landmarks_name_localized (parent_id);""",
    """CREATE INDEX IF NOT EXISTS idx_landmarks_name_localized_source_key ON landmarks_name_localized (source_key);""",
    """CREATE INDEX IF NOT EXISTS idx_landmarks_source_key ON landmarks (source_key);""",
    """CREATE INDEX IF NOT EXISTS idx_map_asteroid_belts_source_key ON map_asteroid_belts (source_key);""",
    """CREATE INDEX IF NOT EXISTS idx_map_asteroid_belts_unique_name_localized_parent_id ON map_asteroid_belts_unique_name_localized (parent_id);""",
    """CREATE INDEX IF NOT EXISTS idx_map_asteroid_belts_unique_name_localized_source_key ON map_asteroid_belts_unique_name_localized (source_key);""",
    """CREATE INDEX IF NOT EXISTS idx_map_constellations_name_localized_parent_id ON map_constellations_name_localized (parent_id);""",
    """CREATE INDEX IF NOT EXISTS idx_map_constellations_name_localized_source_key ON map_constellations_name_localized (source_key);""",
    """CREATE INDEX IF NOT EXISTS idx_map_constellations_solar_system_i_ds_item_index ON map_constellations_solar_system_i_ds (item_index);""",
    """CREATE INDEX IF NOT EXISTS idx_map_constellations_solar_system_i_ds_parent_id ON map_constellations_solar_system_i_ds (parent_id);""",
    """CREATE INDEX IF NOT EXISTS idx_map_constellations_source_key ON map_constellations (source_key);""",
    """CREATE INDEX IF NOT EXISTS idx_map_moons_npc_station_i_ds_item_index ON map_moons_npc_station_i_ds (item_index);""",
    """CREATE INDEX IF NOT EXISTS idx_map_moons_npc_station_i_ds_parent_id ON map_moons_npc_station_i_ds (parent_id);""",
    """CREATE INDEX IF NOT EXISTS idx_map_moons_source_key ON map_moons (source_key);""",
    """CREATE INDEX IF NOT EXISTS idx_map_moons_unique_name_localized_parent_id ON map_moons_unique_name_localized (parent_id);""",
    """CREATE INDEX IF NOT EXISTS idx_map_moons_unique_name_localized_source_key ON map_moons_unique_name_localized (source_key);""",
    """CREATE INDEX IF NOT EXISTS idx_map_planets_asteroid_belt_i_ds_item_index ON map_planets_asteroid_belt_i_ds (item_index);""",
    """CREATE INDEX IF NOT EXISTS idx_map_planets_asteroid_belt_i_ds_parent_id ON map_planets_asteroid_belt_i_ds (parent_id);""",
    """CREATE INDEX IF NOT EXISTS idx_map_planets_moon_i_ds_item_index ON map_planets_moon_i_ds (item_index);""",
    """CREATE INDEX IF NOT EXISTS idx_map_planets_moon_i_ds_parent_id ON map_planets_moon_i_ds (parent_id);""",
    """CREATE INDEX IF NOT EXISTS idx_map_planets_npc_station_i_ds_item_index ON map_planets_npc_station_i_ds (item_index);""",
    """CREATE INDEX IF NOT EXISTS idx_map_planets_npc_station_i_ds_parent_id ON map_planets_npc_station_i_ds (parent_id);""",
    """CREATE INDEX IF NOT EXISTS idx_map_planets_source_key ON map_planets (source_key);""",
    """CREATE INDEX IF NOT EXISTS idx_map_planets_unique_name_localized_parent_id ON map_planets_unique_name_localized (parent_id);""",
    """CREATE INDEX IF NOT EXISTS idx_map_planets_unique_name_localized_source_key ON map_planets_unique_name_localized (source_key);""",
    """CREATE INDEX IF NOT EXISTS idx_map_regions_constellation_i_ds_item_index ON map_regions_constellation_i_ds (item_index);""",
    """CREATE INDEX IF NOT EXISTS idx_map_regions_constellation_i_ds_parent_id ON map_regions_constellation_i_ds (parent_id);""",
    """CREATE INDEX IF NOT EXISTS idx_map_regions_description_localized_parent_id ON map_regions_description_localized (parent_id);""",
    """CREATE INDEX IF NOT EXISTS idx_map_regions_description_localized_source_key ON map_regions_description_localized (source_key);""",
    """CREATE INDEX IF NOT EXISTS idx_map_regions_name_localized_parent_id ON map_regions_name_localized (parent_id);""",
    """CREATE INDEX IF NOT EXISTS idx_map_regions_name_localized_source_key ON map_regions_name_localized (source_key);""",
    """CREATE INDEX IF NOT EXISTS idx_map_regions_source_key ON map_regions (source_key);""",
    """CREATE INDEX IF NOT EXISTS idx_map_secondary_suns_source_key ON map_secondary_suns (source_key);""",
    """CREATE INDEX IF NOT EXISTS idx_map_solar_systems_disallowed_anchor_categories_item_index ON map_solar_systems_disallowed_anchor_categories (item_index);""",
    """CREATE INDEX IF NOT EXISTS idx_map_solar_systems_disallowed_anchor_categories_parent_id ON map_solar_systems_disallowed_anchor_categories (parent_id);""",
    """CREATE INDEX IF NOT EXISTS idx_map_solar_systems_disallowed_anchor_groups_item_index ON map_solar_systems_disallowed_anchor_groups (item_index);""",
    """CREATE INDEX IF NOT EXISTS idx_map_solar_systems_disallowed_anchor_groups_parent_id ON map_solar_systems_disallowed_anchor_groups (parent_id);""",
    """CREATE INDEX IF NOT EXISTS idx_map_solar_systems_name_localized_parent_id ON map_solar_systems_name_localized (parent_id);""",
    """CREATE INDEX IF NOT EXISTS idx_map_solar_systems_name_localized_source_key ON map_solar_systems_name_localized (source_key);""",
    """CREATE INDEX IF NOT EXISTS idx_map_solar_systems_planet_i_ds_item_index ON map_solar_systems_planet_i_ds (item_index);""",
    """CREATE INDEX IF NOT EXISTS idx_map_solar_systems_planet_i_ds_parent_id ON map_solar_systems_planet_i_ds (parent_id);""",
    """CREATE INDEX IF NOT EXISTS idx_map_solar_systems_source_key ON map_solar_systems (source_key);""",
    """CREATE INDEX IF NOT EXISTS idx_map_solar_systems_stargate_i_ds_item_index ON map_solar_systems_stargate_i_ds (item_index);""",
    """CREATE INDEX IF NOT EXISTS idx_map_solar_systems_stargate_i_ds_parent_id ON map_solar_systems_stargate_i_ds (parent_id);""",
    """CREATE INDEX IF NOT EXISTS idx_map_stargates_source_key ON map_stargates (source_key);""",
    """CREATE INDEX IF NOT EXISTS idx_map_stars_source_key ON map_stars (source_key);""",
    """CREATE INDEX IF NOT EXISTS idx_market_groups_description_localized_parent_id ON market_groups_description_localized (parent_id);""",
    """CREATE INDEX IF NOT EXISTS idx_market_groups_description_localized_source_key ON market_groups_description_localized (source_key);""",
    """CREATE INDEX IF NOT EXISTS idx_market_groups_name_localized_parent_id ON market_groups_name_localized (parent_id);""",
    """CREATE INDEX IF NOT EXISTS idx_market_groups_name_localized_source_key ON market_groups_name_localized (source_key);""",
    """CREATE INDEX IF NOT EXISTS idx_market_groups_source_key ON market_groups (source_key);""",
    """CREATE INDEX IF NOT EXISTS idx_masteries_source_key ON masteries (source_key);""",
    """CREATE INDEX IF NOT EXISTS idx_masteries_value_item_index ON masteries_value (item_index);""",
    """CREATE INDEX IF NOT EXISTS idx_masteries_value_parent_id ON masteries_value (parent_id);""",
    """CREATE INDEX IF NOT EXISTS idx_masteries_value_source_key ON masteries_value (source_key);""",
    """CREATE INDEX IF NOT EXISTS idx_masteries_value_value_item_index ON masteries_value_value (item_index);""",
    """CREATE INDEX IF NOT EXISTS idx_masteries_value_value_parent_id ON masteries_value_value (parent_id);""",
    """CREATE INDEX IF NOT EXISTS idx_mercenary_tactical_operations_description_localized_parent_id ON mercenary_tactical_operations_description_localized (parent_id);""",
    """CREATE INDEX IF NOT EXISTS idx_mercenary_tactical_operations_description_localized_source_key ON mercenary_tactical_operations_description_localized (source_key);""",
    """CREATE INDEX IF NOT EXISTS idx_mercenary_tactical_operations_name_localized_parent_id ON mercenary_tactical_operations_name_localized (parent_id);""",
    """CREATE INDEX IF NOT EXISTS idx_mercenary_tactical_operations_name_localized_source_key ON mercenary_tactical_operations_name_localized (source_key);""",
    """CREATE INDEX IF NOT EXISTS idx_mercenary_tactical_operations_source_key ON mercenary_tactical_operations (source_key);""",
    """CREATE INDEX IF NOT EXISTS idx_meta_groups_description_localized_parent_id ON meta_groups_description_localized (parent_id);""",
    """CREATE INDEX IF NOT EXISTS idx_meta_groups_description_localized_source_key ON meta_groups_description_localized (source_key);""",
    """CREATE INDEX IF NOT EXISTS idx_meta_groups_name_localized_parent_id ON meta_groups_name_localized (parent_id);""",
    """CREATE INDEX IF NOT EXISTS idx_meta_groups_name_localized_source_key ON meta_groups_name_localized (source_key);""",
    """CREATE INDEX IF NOT EXISTS idx_meta_groups_source_key ON meta_groups (source_key);""",
    """CREATE INDEX IF NOT EXISTS idx_npc_characters_name_localized_parent_id ON npc_characters_name_localized (parent_id);""",
    """CREATE INDEX IF NOT EXISTS idx_npc_characters_name_localized_source_key ON npc_characters_name_localized (source_key);""",
    """CREATE INDEX IF NOT EXISTS idx_npc_characters_skills_item_index ON npc_characters_skills (item_index);""",
    """CREATE INDEX IF NOT EXISTS idx_npc_characters_skills_parent_id ON npc_characters_skills (parent_id);""",
    """CREATE INDEX IF NOT EXISTS idx_npc_characters_source_key ON npc_characters (source_key);""",
    """CREATE INDEX IF NOT EXISTS idx_npc_corporation_divisions_description_localized_parent_id ON npc_corporation_divisions_description_localized (parent_id);""",
    """CREATE INDEX IF NOT EXISTS idx_npc_corporation_divisions_description_localized_source_key ON npc_corporation_divisions_description_localized (source_key);""",
    """CREATE INDEX IF NOT EXISTS idx_npc_corporation_divisions_leader_type_name_localized_parent_id ON npc_corporation_divisions_leader_type_name_localized (parent_id);""",
    """CREATE INDEX IF NOT EXISTS idx_npc_corporation_divisions_leader_type_name_localized_source_key ON npc_corporation_divisions_leader_type_name_localized (source_key);""",
    """CREATE INDEX IF NOT EXISTS idx_npc_corporation_divisions_name_localized_parent_id ON npc_corporation_divisions_name_localized (parent_id);""",
    """CREATE INDEX IF NOT EXISTS idx_npc_corporation_divisions_name_localized_source_key ON npc_corporation_divisions_name_localized (source_key);""",
    """CREATE INDEX IF NOT EXISTS idx_npc_corporation_divisions_source_key ON npc_corporation_divisions (source_key);""",
    """CREATE INDEX IF NOT EXISTS idx_npc_corporations_allowed_member_races_item_index ON npc_corporations_allowed_member_races (item_index);""",
    """CREATE INDEX IF NOT EXISTS idx_npc_corporations_allowed_member_races_parent_id ON npc_corporations_allowed_member_races (parent_id);""",
    """CREATE INDEX IF NOT EXISTS idx_npc_corporations_corporation_trades_item_index ON npc_corporations_corporation_trades (item_index);""",
    """CREATE INDEX IF NOT EXISTS idx_npc_corporations_corporation_trades_parent_id ON npc_corporations_corporation_trades (parent_id);""",
    """CREATE INDEX IF NOT EXISTS idx_npc_corporations_description_localized_parent_id ON npc_corporations_description_localized (parent_id);""",
    """CREATE INDEX IF NOT EXISTS idx_npc_corporations_description_localized_source_key ON npc_corporations_description_localized (source_key);""",
    """CREATE INDEX IF NOT EXISTS idx_npc_corporations_divisions_item_index ON npc_corporations_divisions (item_index);""",
    """CREATE INDEX IF NOT EXISTS idx_npc_corporations_divisions_parent_id ON npc_corporations_divisions (parent_id);""",
    """CREATE INDEX IF NOT EXISTS idx_npc_corporations_divisions_source_key ON npc_corporations_divisions (source_key);""",
    """CREATE INDEX IF NOT EXISTS idx_npc_corporations_exchange_rates_item_index ON npc_corporations_exchange_rates (item_index);""",
    """CREATE INDEX IF NOT EXISTS idx_npc_corporations_exchange_rates_parent_id ON npc_corporations_exchange_rates (parent_id);""",
    """CREATE INDEX IF NOT EXISTS idx_npc_corporations_exchange_rates_source_key ON npc_corporations_exchange_rates (source_key);""",
    """CREATE INDEX IF NOT EXISTS idx_npc_corporations_investors_item_index ON npc_corporations_investors (item_index);""",
    """CREATE INDEX IF NOT EXISTS idx_npc_corporations_investors_parent_id ON npc_corporations_investors (parent_id);""",
    """CREATE INDEX IF NOT EXISTS idx_npc_corporations_investors_source_key ON npc_corporations_investors (source_key);""",
    """CREATE INDEX IF NOT EXISTS idx_npc_corporations_lp_offer_tables_item_index ON npc_corporations_lp_offer_tables (item_index);""",
    """CREATE INDEX IF NOT EXISTS idx_npc_corporations_lp_offer_tables_parent_id ON npc_corporations_lp_offer_tables (parent_id);""",
    """CREATE INDEX IF NOT EXISTS idx_npc_corporations_name_localized_parent_id ON npc_corporations_name_localized (parent_id);""",
    """CREATE INDEX IF NOT EXISTS idx_npc_corporations_name_localized_source_key ON npc_corporations_name_localized (source_key);""",
    """CREATE INDEX IF NOT EXISTS idx_npc_corporations_source_key ON npc_corporations (source_key);""",
    """CREATE INDEX IF NOT EXISTS idx_npc_corporations_trade_source_key ON npc_corporations_trade (source_key);""",
    """CREATE INDEX IF NOT EXISTS idx_npc_stations_source_key ON npc_stations (source_key);""",
    """CREATE INDEX IF NOT EXISTS idx_planet_resources_source_key ON planet_resources (source_key);""",
    """CREATE INDEX IF NOT EXISTS idx_planet_schematics_name_localized_parent_id ON planet_schematics_name_localized (parent_id);""",
    """CREATE INDEX IF NOT EXISTS idx_planet_schematics_name_localized_source_key ON planet_schematics_name_localized (source_key);""",
    """CREATE INDEX IF NOT EXISTS idx_planet_schematics_pins_item_index ON planet_schematics_pins (item_index);""",
    """CREATE INDEX IF NOT EXISTS idx_planet_schematics_pins_parent_id ON planet_schematics_pins (parent_id);""",
    """CREATE INDEX IF NOT EXISTS idx_planet_schematics_source_key ON planet_schematics (source_key);""",
    """CREATE INDEX IF NOT EXISTS idx_planet_schematics_types_item_index ON planet_schematics_types (item_index);""",
    """CREATE INDEX IF NOT EXISTS idx_planet_schematics_types_parent_id ON planet_schematics_types (parent_id);""",
    """CREATE INDEX IF NOT EXISTS idx_planet_schematics_types_source_key ON planet_schematics_types (source_key);""",
    """CREATE INDEX IF NOT EXISTS idx_races_description_localized_parent_id ON races_description_localized (parent_id);""",
    """CREATE INDEX IF NOT EXISTS idx_races_description_localized_source_key ON races_description_localized (source_key);""",
    """CREATE INDEX IF NOT EXISTS idx_races_name_localized_parent_id ON races_name_localized (parent_id);""",
    """CREATE INDEX IF NOT EXISTS idx_races_name_localized_source_key ON races_name_localized (source_key);""",
    """CREATE INDEX IF NOT EXISTS idx_races_skill_source_key ON races_skill (source_key);""",
    """CREATE INDEX IF NOT EXISTS idx_races_skills_item_index ON races_skills (item_index);""",
    """CREATE INDEX IF NOT EXISTS idx_races_skills_parent_id ON races_skills (parent_id);""",
    """CREATE INDEX IF NOT EXISTS idx_races_source_key ON races (source_key);""",
    """CREATE INDEX IF NOT EXISTS idx_sde_info_source_key ON sde_info (source_key);""",
    """CREATE INDEX IF NOT EXISTS idx_skin_licenses_source_key ON skin_licenses (source_key);""",
    """CREATE INDEX IF NOT EXISTS idx_skin_materials_display_name_localized_parent_id ON skin_materials_display_name_localized (parent_id);""",
    """CREATE INDEX IF NOT EXISTS idx_skin_materials_display_name_localized_source_key ON skin_materials_display_name_localized (source_key);""",
    """CREATE INDEX IF NOT EXISTS idx_skin_materials_source_key ON skin_materials (source_key);""",
    """CREATE INDEX IF NOT EXISTS idx_skins_skin_description_localized_parent_id ON skins_skin_description_localized (parent_id);""",
    """CREATE INDEX IF NOT EXISTS idx_skins_skin_description_localized_source_key ON skins_skin_description_localized (source_key);""",
    """CREATE INDEX IF NOT EXISTS idx_skins_source_key ON skins (source_key);""",
    """CREATE INDEX IF NOT EXISTS idx_skins_types_item_index ON skins_types (item_index);""",
    """CREATE INDEX IF NOT EXISTS idx_skins_types_parent_id ON skins_types (parent_id);""",
    """CREATE INDEX IF NOT EXISTS idx_sovereignty_upgrades_source_key ON sovereignty_upgrades (source_key);""",
    """CREATE INDEX IF NOT EXISTS idx_station_operations_description_localized_parent_id ON station_operations_description_localized (parent_id);""",
    """CREATE INDEX IF NOT EXISTS idx_station_operations_description_localized_source_key ON station_operations_description_localized (source_key);""",
    """CREATE INDEX IF NOT EXISTS idx_station_operations_operation_name_localized_parent_id ON station_operations_operation_name_localized (parent_id);""",
    """CREATE INDEX IF NOT EXISTS idx_station_operations_operation_name_localized_source_key ON station_operations_operation_name_localized (source_key);""",
    """CREATE INDEX IF NOT EXISTS idx_station_operations_services_item_index ON station_operations_services (item_index);""",
    """CREATE INDEX IF NOT EXISTS idx_station_operations_services_parent_id ON station_operations_services (parent_id);""",
    """CREATE INDEX IF NOT EXISTS idx_station_operations_source_key ON station_operations (source_key);""",
    """CREATE INDEX IF NOT EXISTS idx_station_operations_station_type_source_key ON station_operations_station_type (source_key);""",
    """CREATE INDEX IF NOT EXISTS idx_station_operations_station_types_item_index ON station_operations_station_types (item_index);""",
    """CREATE INDEX IF NOT EXISTS idx_station_operations_station_types_parent_id ON station_operations_station_types (parent_id);""",
    """CREATE INDEX IF NOT EXISTS idx_station_services_description_localized_parent_id ON station_services_description_localized (parent_id);""",
    """CREATE INDEX IF NOT EXISTS idx_station_services_description_localized_source_key ON station_services_description_localized (source_key);""",
    """CREATE INDEX IF NOT EXISTS idx_station_services_service_name_localized_parent_id ON station_services_service_name_localized (parent_id);""",
    """CREATE INDEX IF NOT EXISTS idx_station_services_service_name_localized_source_key ON station_services_service_name_localized (source_key);""",
    """CREATE INDEX IF NOT EXISTS idx_station_services_source_key ON station_services (source_key);""",
    """CREATE INDEX IF NOT EXISTS idx_translation_languages_source_key ON translation_languages (source_key);""",
    """CREATE INDEX IF NOT EXISTS idx_type_bonus_misc_bonus_bonus_text_localized_parent_id ON type_bonus_misc_bonus_bonus_text_localized (parent_id);""",
    """CREATE INDEX IF NOT EXISTS idx_type_bonus_misc_bonus_bonus_text_localized_source_key ON type_bonus_misc_bonus_bonus_text_localized (source_key);""",
    """CREATE INDEX IF NOT EXISTS idx_type_bonus_misc_bonuses_item_index ON type_bonus_misc_bonuses (item_index);""",
    """CREATE INDEX IF NOT EXISTS idx_type_bonus_misc_bonuses_parent_id ON type_bonus_misc_bonuses (parent_id);""",
    """CREATE INDEX IF NOT EXISTS idx_type_bonus_role_bonus_bonus_text_localized_parent_id ON type_bonus_role_bonus_bonus_text_localized (parent_id);""",
    """CREATE INDEX IF NOT EXISTS idx_type_bonus_role_bonus_bonus_text_localized_source_key ON type_bonus_role_bonus_bonus_text_localized (source_key);""",
    """CREATE INDEX IF NOT EXISTS idx_type_bonus_role_bonuses_item_index ON type_bonus_role_bonuses (item_index);""",
    """CREATE INDEX IF NOT EXISTS idx_type_bonus_role_bonuses_parent_id ON type_bonus_role_bonuses (parent_id);""",
    """CREATE INDEX IF NOT EXISTS idx_type_bonus_source_key ON type_bonus (source_key);""",
    """CREATE INDEX IF NOT EXISTS idx_type_bonus_types_bonus_bonus_text_localized_parent_id ON type_bonus_types_bonus_bonus_text_localized (parent_id);""",
    """CREATE INDEX IF NOT EXISTS idx_type_bonus_types_bonus_bonus_text_localized_source_key ON type_bonus_types_bonus_bonus_text_localized (source_key);""",
    """CREATE INDEX IF NOT EXISTS idx_type_bonus_types_item_index ON type_bonus_types (item_index);""",
    """CREATE INDEX IF NOT EXISTS idx_type_bonus_types_parent_id ON type_bonus_types (parent_id);""",
    """CREATE INDEX IF NOT EXISTS idx_type_bonus_types_source_key ON type_bonus_types (source_key);""",
    """CREATE INDEX IF NOT EXISTS idx_type_bonus_types_value_item_index ON type_bonus_types_value (item_index);""",
    """CREATE INDEX IF NOT EXISTS idx_type_bonus_types_value_parent_id ON type_bonus_types_value (parent_id);""",
    """CREATE INDEX IF NOT EXISTS idx_type_dogma_dogma_attributes_item_index ON type_dogma_dogma_attributes (item_index);""",
    """CREATE INDEX IF NOT EXISTS idx_type_dogma_dogma_attributes_parent_id ON type_dogma_dogma_attributes (parent_id);""",
    """CREATE INDEX IF NOT EXISTS idx_type_dogma_dogma_effects_item_index ON type_dogma_dogma_effects (item_index);""",
    """CREATE INDEX IF NOT EXISTS idx_type_dogma_dogma_effects_parent_id ON type_dogma_dogma_effects (parent_id);""",
    """CREATE INDEX IF NOT EXISTS idx_type_dogma_source_key ON type_dogma (source_key);""",
    """CREATE INDEX IF NOT EXISTS idx_type_materials_materials_item_index ON type_materials_materials (item_index);""",
    """CREATE INDEX IF NOT EXISTS idx_type_materials_materials_parent_id ON type_materials_materials (parent_id);""",
    """CREATE INDEX IF NOT EXISTS idx_type_materials_randomized_materials_item_index ON type_materials_randomized_materials (item_index);""",
    """CREATE INDEX IF NOT EXISTS idx_type_materials_randomized_materials_parent_id ON type_materials_randomized_materials (parent_id);""",
    """CREATE INDEX IF NOT EXISTS idx_type_materials_source_key ON type_materials (source_key);""",
)

CREATE_SCHEMA_STATEMENTS: tuple[str, ...] = (
    *CREATE_TABLE_STATEMENTS,
    *CREATE_INDEX_STATEMENTS,
)
