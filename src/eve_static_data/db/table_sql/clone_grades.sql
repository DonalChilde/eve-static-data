-- Table definitions for records from the clone_grades.jsonl file.

CREATE TABLE IF NOT EXISTS clone_grades (
    clone_grades_id INTEGER PRIMARY KEY, -- This is the `_key` or `key` field from the imported record.
    name            TEXT,
    
CREATE TABLE IF NOT EXISTS clone_grades_skills (
    clone_grades_skills_id INTEGER PRIMARY KEY AUTOINCREMENT,
    clone_grades_id        INTEGER NOT NULL REFERENCES clone_grades(clone_grades_id) ON DELETE CASCADE,
    typeID                 INTEGER NOT NULL,
    skill_level            INTEGER NOT NULL -- From the `level` field in the `skills` array of the imported record.
);
