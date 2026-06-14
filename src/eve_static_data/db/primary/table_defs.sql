-- Table definitions for the sde export to sqlite db.


CREATE TABLE IF NOT EXISTS DatasetEntriesInt (
    id            INTEGER PRIMARY KEY,
    record_key    INTEGER NOT NULL, -- This is the dict key from the imported record.
    dataset_name  TEXT    NOT NULL, -- The name of the dataset this record belongs to.
    record_json   BLOB    NOT NULL, -- The entire record as JSON bytes.
    UNIQUE(record_key, dataset_name)
) STRICT;

CREATE TABLE IF NOT EXISTS DatasetEntriesStr (
    id            INTEGER PRIMARY KEY,
    record_key    TEXT    NOT NULL, -- This is the dict key from the imported record.
    dataset_name  TEXT    NOT NULL, -- The name of the dataset this record belongs to.
    record_json   BLOB    NOT NULL, -- The entire record as JSON bytes.
    UNIQUE(record_key, dataset_name)
) STRICT;