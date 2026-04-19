-- Table definitions for records from the ancestries.jsonl file.

CREATE TABLE IF NOT EXISTS ancestries (
    ancestries_id    INTEGER PRIMARY KEY, -- This is the `_key` or `key` field from the imported record.
    bloodlineID      INTEGER,
    charisma         INTEGER,
    iconID           INTEGER,
    intelligence     INTEGER,
    memory           INTEGER,
    perception       INTEGER,
    shortDescription TEXT,
    willpower        INTEGER);
CREATE TABLE IF NOT EXISTS ancestries_localized (
    ancestries_localized_id INTEGER PRIMARY KEY AUTOINCREMENT,
    parent_id               INTEGER NOT NULL REFERENCES ancestries(ancestries_id) ON DELETE CASCADE,
    lang                    TEXT,
    localized_name          TEXT,
    localized_description   TEXT);