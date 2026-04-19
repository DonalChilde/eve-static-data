-- Table definitions for records from the agentTypes.yaml file.

CREATE TABLE IF NOT EXISTS agent_types (
    agent_types_id INTEGER PRIMARY KEY, -- This is the dict key from the imported record.
    agent_name TEXT -- From the `name` field of the imported record.
    ); 