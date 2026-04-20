-- Table definitions for records from the ancestries.yaml file.

CREATE TABLE IF NOT EXISTS ancestries (
    ancestries_id    INTEGER PRIMARY KEY, -- This is the dict key from the imported record.
    bloodlineID      INTEGER,
    charisma         INTEGER,
    iconID           INTEGER,
    intelligence     INTEGER,
    memory           INTEGER,
    perception       INTEGER,
    shortDescription TEXT,
    willpower        INTEGER
    );
CREATE TABLE IF NOT EXISTS ancestries_localized (
    ancestries_localized_id INTEGER PRIMARY KEY AUTOINCREMENT,
    ancestries_id           INTEGER NOT NULL REFERENCES ancestries(ancestries_id) ON DELETE CASCADE,
    lang                    TEXT,
    localized_name          TEXT,
    localized_description   TEXT,
    UNIQUE(ancestries_id, lang)
    );