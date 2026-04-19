-- Table definitions for records from the contraband_types.jsonl file.

CREATE TABLE IF NOT EXISTS contraband_types (
    contraband_types_id INTEGER PRIMARY KEY, -- This is the `_key` or `key` field from the imported record.
    
);

CREATE TABLE IF NOT EXISTS contraband_types_faction (
    row_id                      INTEGER PRIMARY KEY AUTOINCREMENT,
    contraband_types_faction_id INTEGER  -- This is the `_key` or `key` field from the imported record.
    contraband_types_id         INTEGER NOT NULL REFERENCES contraband_types(contraband_types_id) ON DELETE CASCADE,
    attackMinSec                REAL NOT NULL,
    confiscateMinSec            REAL NOT NULL,
    fineByValue                 REAL NOT NULL,
    standingLoss                REAL NOT NULL,
);