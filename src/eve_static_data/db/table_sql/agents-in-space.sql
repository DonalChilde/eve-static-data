-- Table definitions for records from the agentsInSpace.yaml file.

CREATE TABLE IF NOT EXISTS agents_in_space (
    agents_in_space_id INTEGER PRIMARY KEY, -- This is the dict key from the imported record.
    dungeonID          INTEGER,
    solarSystemID      INTEGER,
    spawnPointID       INTEGER,
    typeID             INTEGER
    );