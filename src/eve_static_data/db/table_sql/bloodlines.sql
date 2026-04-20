-- Table definitions for records from the bloodlines.jsonl file.

CREATE TABLE IF NOT EXISTS bloodlines (
    bloodlines_id  INTEGER PRIMARY KEY, -- This is the `dict key from the imported record.
    charisma      INTEGER,
    corporationID INTEGER,
    iconID        INTEGER,
    intelligence  INTEGER,
    memory        INTEGER,
    perception    INTEGER,
    raceID        INTEGER,
    willpower     INTEGER);

CREATE TABLE IF NOT EXISTS bloodlines_localized (
    bloodlines_localized_id INTEGER PRIMARY KEY AUTOINCREMENT,
    parent_id               INTEGER NOT NULL REFERENCES bloodlines(bloodlines_id) ON DELETE CASCADE,
    lang                    TEXT,
    localized_name          TEXT,
    localized_description   TEXT);
