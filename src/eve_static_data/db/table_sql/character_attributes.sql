-- Table definitions for records from the character_attributes.jsonl file.

CREATE TABLE IF NOT EXISTS character_attributes (
    character_attributes_id INTEGER PRIMARY KEY, -- This is the `_key` or `key` field from the imported record.
    iconID                  INTEGER,
    notes                   TEXT,
    shortDescription        TEXT,
);

CREATE TABLE IF NOT EXISTS character_attributes_localized (
    character_attributes_localized_id INTEGER PRIMARY KEY AUTOINCREMENT,
    character_attributes_id           INTEGER NOT NULL REFERENCES character_attributes(character_attributes_id) ON DELETE CASCADE,
    lang                              TEXT,
    localized_name                    TEXT,
    localized_description             TEXT);
