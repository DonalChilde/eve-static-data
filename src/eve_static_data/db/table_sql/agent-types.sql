-- Table definitions for records from the agentTypes.jsonl file.

CREATE TABLE IF NOT EXISTS agent_types (
    agent_types_id INTEGER PRIMARY KEY, -- This is the `_key` or `key` field from the imported record.
    agent_name TEXT); -- From the `name` field of the imported record.