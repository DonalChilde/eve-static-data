-- Table definitions for records from the compressible_types.jsonl file.

CREATE TABLE IF NOT EXISTS compressible_types (
    compressible_types_id          INTEGER PRIMARY KEY, -- This is the `_key` or `key` field from the imported record.
    compressedTypeID               INTEGER NOT NULL
);
