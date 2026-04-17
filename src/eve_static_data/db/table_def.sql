-- The Table definitions for the SDE

-- agent_types
CREATE TABLE IF NOT EXISTS agent_types (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    source_key INTEGER,
    name TEXT);

-- agents_in_space
CREATE TABLE IF NOT EXISTS agents_in_space (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    source_key INTEGER,
    dungeon_id INTEGER,
    solar_system_id INTEGER,
    spawn_point_id INTEGER,
    type_id INTEGER);

-- ancestries
CREATE TABLE IF NOT EXISTS ancestries (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    source_key INTEGER,
    bloodline_id INTEGER,
    charisma INTEGER,
    icon_id INTEGER,
    intelligence INTEGER,
    memory INTEGER,
    perception INTEGER,
    short_description TEXT,
    willpower INTEGER);
CREATE TABLE IF NOT EXISTS ancestries_localized (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    parent_id INTEGER NOT NULL,
    source_key INTEGER,
    language TEXT,
    name TEXT,
    description TEXT);