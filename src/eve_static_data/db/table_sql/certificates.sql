-- Table definitions for records from the certificates.jsonl file.

CREATE TABLE IF NOT EXISTS certificates (
    certificates_id INTEGER PRIMARY KEY, -- This is the dict key from the imported record.
    groupID         INTEGER
);

CREATE TABLE IF NOT EXISTS certificates_recommended_for (
    certificates_recommended_for_id INTEGER PRIMARY KEY AUTOINCREMENT,
    certificates_id                 INTEGER NOT NULL REFERENCES certificates(certificates_id) ON DELETE CASCADE,
    value_int                       INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS certificates_skill_type (
    row_id                     INTEGER PRIMARY KEY AUTOINCREMENT,
    certificates_skill_type_id INTEGER NOT NULL, -- This is the dict key from the imported record.
    certificates_id            INTEGER NOT NULL REFERENCES certificates(certificates_id) ON DELETE CASCADE,
    basic_lvl                  INTEGER NOT NULL,
    standard_lvl               INTEGER NOT NULL,
    improved_lvl               INTEGER NOT NULL,
    advanced_lvl               INTEGER NOT NULL,
    elite_lvl                  INTEGER NOT NULL,
    UNIQUE(certificates_id, certificates_skill_type_id)
);

CREATE TABLE IF NOT EXISTS certificates_localized (
    certificates_localized_id INTEGER PRIMARY KEY AUTOINCREMENT,
    certificates_id           INTEGER NOT NULL REFERENCES certificates(certificates_id) ON DELETE CASCADE,
    lang                      TEXT,
    localized_name            TEXT,
    localized_description     TEXT);
