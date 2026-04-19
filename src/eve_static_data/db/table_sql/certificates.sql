-- Table definitions for records from the certificates.jsonl file.

CREATE TABLE IF NOT EXISTS certificates (
    certificates_id INTEGER PRIMARY KEY, -- This is the `_key` or `key` field from the imported record.
    iconID          INTEGER,
    groupID         INTEGER,
    published       BOOLEAN);

CREATE TABLE IF NOT EXISTS certificates_recommended_for (
    certificates_recommended_for_id INTEGER PRIMARY KEY AUTOINCREMENT,
    certificate_id                  INTEGER NOT NULL REFERENCES certificates(certificates_id) ON DELETE CASCADE,
    value_id                        INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS certificates_skill_type (
    row_id                     INTEGER PRIMARY KEY AUTOINCREMENT,
    certificates_skill_type_id INTEGER,
    certificate_id             INTEGER NOT NULL REFERENCES certificates(certificates_id) ON DELETE CASCADE,
    basic_lvl                  INTEGER NOT NULL,
    standard_lvl               INTEGER NOT NULL,
    improved_lvl               INTEGER NOT NULL,
    advanced_lvl               INTEGER NOT NULL,
    elite_lvl                  INTEGER NOT NULL,
    UNIQUE(certificate_id, certificates_skill_type_id)
);

CREATE TABLE IF NOT EXISTS certificates_localized (
    certificates_localized_id INTEGER PRIMARY KEY AUTOINCREMENT,
    parent_id                 INTEGER NOT NULL REFERENCES certificates(certificates_id) ON DELETE CASCADE,
    lang                      TEXT,
    localized_name            TEXT,
    localized_description     TEXT);
