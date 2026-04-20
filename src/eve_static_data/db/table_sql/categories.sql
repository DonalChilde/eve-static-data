-- Table definitions for records from the categories.yaml file.

CREATE TABLE IF NOT EXISTS categories (
    categories_id INTEGER PRIMARY KEY, -- This is the dict key from the imported record.
    iconID        INTEGER,
    published     BOOLEAN);

CREATE TABLE IF NOT EXISTS categories_localized (
    categories_localized_id INTEGER PRIMARY KEY AUTOINCREMENT,
    categories_id           INTEGER NOT NULL REFERENCES categories(categories_id) ON DELETE CASCADE,
    lang                    TEXT,
    localized_name          TEXT);
