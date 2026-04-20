CREATE TABLE IF NOT EXISTS blueprints (
    blueprints_id      INTEGER PRIMARY KEY, -- This is the dict key from the imported record.
    blueprintTypeID    INTEGER NOT NULL,
    maxProductionLimit INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS blueprint_activities (
    blueprint_activity_id  INTEGER PRIMARY KEY AUTOINCREMENT,
    blueprint_id           INTEGER NOT NULL REFERENCES blueprints(blueprints_id) ON DELETE CASCADE,
    activity_type          TEXT NOT NULL,  -- 'manufacturing', 'copying', etc.
    activity_time          INTEGER NOT NULL,
    UNIQUE(blueprint_id, activity_type)
);

CREATE TABLE IF NOT EXISTS blueprint_activity_materials (
    activity_material_id   INTEGER PRIMARY KEY AUTOINCREMENT,
    blueprint_activity_id  INTEGER NOT NULL REFERENCES blueprint_activities(blueprint_activity_id) ON DELETE CASCADE,
    typeID                 INTEGER NOT NULL,
    quantity               INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS blueprint_activity_skills (
    activity_skill_id      INTEGER PRIMARY KEY AUTOINCREMENT,
    blueprint_activity_id  INTEGER NOT NULL REFERENCES blueprint_activities(blueprint_activity_id) ON DELETE CASCADE,
    typeID                 INTEGER NOT NULL,
    skill_level            INTEGER NOT NULL -- From the `level` field in the `skills` array of the imported record.
);

CREATE TABLE IF NOT EXISTS blueprint_activity_products (
    activity_product_id    INTEGER PRIMARY KEY AUTOINCREMENT,
    blueprint_activity_id  INTEGER NOT NULL REFERENCES blueprint_activities(blueprint_activity_id) ON DELETE CASCADE,
    typeID                 INTEGER NOT NULL,
    quantity               INTEGER NOT NULL,
    probability            REAL
);