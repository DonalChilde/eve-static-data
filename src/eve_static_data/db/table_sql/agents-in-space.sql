-- Table definitions for records from the agentsInSpace.jsonl file.

CREATE TABLE IF NOT EXISTS agents_in_space (
    agents_in_space_id INTEGER PRIMARY KEY, -- This is the `_key` or `key` field from the imported record.
    dungeonID          INTEGER,
    solarSystemID      INTEGER,
    spawnPointID       INTEGER,
    typeID             INTEGER);