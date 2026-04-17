# Plan: SQLite Database Schema for EVE Online SDE

## Decisions Made
- **Localization**: Dataset-specific localization tables with only relevant fields (e.g., types_localized may have name+description, while others only name)
- **Nested Structures**: Junction tables for arrays; JSON columns for deeply nested optional structures
- **Scope**: Complete coverage - all 103 dataclass models
- **Organization**: Alphabetical by table name, following naming convention: `dataset_name` for main table, `dataset_name_child` for nested structures
- **Total Tables Needed**: ~90-100 tables including main + localization + junction tables
- **Dataset Independence**: NO cross-dataset foreign keys. Each dataset is self-contained. IDs stored as integers without FK constraints to other datasets.
- **Primary Key Strategy**: Every table uses surrogate `id INTEGER PRIMARY KEY AUTOINCREMENT`; source dataclass `key` is stored separately as `source_key` (not unique).

## Plan: SQLite Database Schema for EVE Online SDE

### TL;DR
Convert all 103 dataclass models from [records.py](src/eve_static_data/models/records.py) into normalized SQLite tables using three patterns: (1) simple tables + localization tables for LocalizedString fields, (2) junction tables for arrays/nested lists, (3) JSON columns for complex nested objects. Each dataset is **independent** with no cross-dataset foreign keys—all ID references are stored as integers. Organize ~90-100 total tables alphabetically following naming convention `dataset` and `dataset_child`. Generate SQL statements to create all tables with surrogate autoincrement primary keys, `source_key` columns for original dataclass keys, within-dataset FKs only, and indexes.

### Design Patterns (with examples)

#### Pattern 1: Simple Table + Localization Table
**When to use**: Any model with `LocalizedString` fields.

**Example - Types.jsonl**:
```
Table: eve_types (primary data)
  - id (INTEGER PRIMARY KEY AUTOINCREMENT)
  - source_key (INT)  [original dataclass `key`, not unique]
  - group_id (INT)  [no FK - user manages cross-dataset references]
  - name_id (INT FK → eve_types_localized.id)  [FK only within dataset]
  - description_id (INT FK → eve_types_localized.id)
  - mass, volume, radius, etc. (nullable floats)
  - icon_id (INT nullable)  [no FK - just an ID value]
  - ... other fields

Table: eve_types_localized (language variants)
  - id (INTEGER PRIMARY KEY AUTOINCREMENT)
  - source_key (INT NULL)  [optional source key if present in source structure]
  - eve_type_id (INT FK → eve_types.id)  [FK within dataset]
  - language (VARCHAR(2): 'en', 'de', 'fr', 'ja', 'zh', 'ru', 'ko', 'es')
  - name (TEXT)
  - description (TEXT nullable)
```

**Example - Icons.jsonl** (independent dataset):
```
Table: icons
  - id (INT PK)
  - icon_file (TEXT NOT NULL)
```
*Note: eve_types stores icon_id as an INT, but there's no FK constraint to icons table. The user manages joining datasets as needed.*

#### Pattern 2: Junction Tables for Arrays/Lists (within-dataset only)
**When to use**: Arrays of primitive objects (Materials, Skills) in nested structures **within the same dataset**.

**Example - Blueprints.jsonl** (self-contained):
```
Table: blueprints (main)
  - id (INTEGER PRIMARY KEY AUTOINCREMENT)
  - source_key (INT)  [original dataclass `key`, not unique]
  - blueprint_type_id (INT)  [just an ID, not FK'd elsewhere]
  - max_production_limit (INT)

Table: blueprints_activities (nested under Blueprints_Activities)
  - id (INT PK)
  - blueprint_id (INT FK → blueprints.id)  [FK within dataset]
  - activity_type (VARCHAR: 'copying', 'invention', 'manufacturing', etc.)
  - time (INT)

Table: blueprints_activities_materials (nested under Blueprints_Activity → materials list)
  - id (INT PK)
  - blueprint_activity_id (INT FK → blueprints_activities.id)  [FK within dataset]
  - type_id (INT)  [just an ID, not FK'd to eve_types]
  - quantity (INT)

Table: blueprints_activities_skills (nested under Blueprints_Activity → skills list)
  - id (INT PK)
  - blueprint_activity_id (INT FK → blueprints_activities.id)
  - type_id (INT)  [just an ID]
  - level (INT)

Table: blueprints_activities_products (nested under Blueprints_Activity → products list)
  - id (INT PK)
  - blueprint_activity_id (INT FK → blueprints_activities.id)
  - type_id (INT)  [just an ID]
  - quantity (INT)
  - probability (FLOAT nullable)
```

#### Pattern 3: JSON Column for Complex Nested Objects
**When to use**: Deeply nested structures with optional varying fields where normalization adds excessive complexity.

**Example - FreelanceJobSchemas.jsonl**:
```
Table: freelance_job_schemas
  - id (INT PK)
  - schema_data (JSON)  [stores the list of objects as-is]
```

**Example - Masteries.jsonl** (nested list of lists):
```
Table: masteries
  - id (INT PK)
  - mastery_data (JSON)  [stores list of Masteries_Value objects]
```

### Implementation Steps

**All tables are independent. Create in alphabetical order with no ordering constraints.**

1. **Main tables**: One table per dataclass model (agent_types, ancestries, blueprints, ..., zones) with `id INTEGER PRIMARY KEY AUTOINCREMENT` and `source_key INT`
2. **Localization tables**: For each dataset with `LocalizedString` fields, create `{dataset}_localized` table with autoincrement `id`
3. **Junction tables**: For each nested array/list structure, create `{parent}_{child}` tables with autoincrement `id`
4. **JSON columns**: For deeply nested optional structures, use JSON column type
5. All foreign keys are **within-dataset only** (main → localized, parent → child within same dataset)
6. Cross-dataset ID references (group_id, icon_id, type_id) stored as INT with no FK constraint
7. Add non-unique index on `source_key` in each table for source lookup and dedupe workflows

### Table Organization (Alphabetical)

**Categories** (~90-100 total):
- agent_* (3 tables): agent_types, agents_in_space, etc.
- ancestries* (2): ancestries, ancestries_localized
- blueprints* (5-6): blueprints, blueprints_activities, blueprints_activities_materials, blueprints_activities_skills, blueprints_activities_products, blueprints_localized
- bloodlines* (2): bloodlines, bloodlines_localized
- ... continuing alphabetically through zones

**[Complete table list to be generated during implementation phase]**

### Critical Design Decisions

1. **Primary Keys**: All tables use surrogate `id INTEGER PRIMARY KEY AUTOINCREMENT`
2. **Source Key Handling**: Original dataclass `key` is stored as `source_key` (INT, non-unique by default)
3. **Foreign Keys**: Only enforce referential integrity **within each dataset** (main ↔ localized, parent ↔ child tables)
4. **Cross-dataset ID references**: Stored as INT columns with NO FK constraints (user manages joins at query time)
5. **Indexes**:
   - All within-dataset FK columns indexed for JOIN performance
   - `source_key` indexed (non-unique) for source-record lookup
   - ID columns indexed (frequently searched: id, parent_id)
   - Name/description columns indexed if frequently searched
6. **Nullable Columns**: Follow dataclass optional fields (`field | None`)
7. **Localization Table Structure**:
   - FK to parent table (within-dataset)
   - Language column (CHAR(2) with check constraint: 'en'|'de'|'fr'|'ja'|'zh'|'ru'|'ko'|'es')
   - Localized text columns for only the fields in that dataset
8. **Junction Tables**: Named `parent_child` following records.py convention, FK'd only within dataset

### Verification Steps

1. ✓ All 103 models have a corresponding primary table
2. ✓ Every table uses `id INTEGER PRIMARY KEY AUTOINCREMENT`
3. ✓ Original dataclass `key` values are mapped to `source_key` (non-unique)
4. ✓ All `LocalizedString` fields have localization tables
5. ✓ All arrays/nested lists have junction tables
6. ✓ All within-dataset foreign keys correctly reference parent tables
7. ✓ Cross-dataset ID columns are INT (no FK constraints)
8. ✓ Nullable columns follow original `field | None` pattern
9. ✓ Alphabetical organization by table name
10. ✓ Indexes include within-dataset FK columns and `source_key`

### Further Considerations

1. **Localization Strategy Clarification**: For datasets with only a `name` field (e.g., `Icons`), should we create a separate localization table or just store the ID + name in the main table?
   → **Recommend**: Icons and other non-localized datasets skip localization tables. Create localization tables only for datasets with `LocalizedString` fields.

2. **JSON vs. Junction Tables**: For complex nested structures like `Masteries` (nested list of lists), should we normalize to multiple junction tables or use JSON columns?
   → **Recommend**: Use JSON columns for rarely-joined nested structures. Use junction tables only for frequently-queried nested items (e.g., blueprint materials need easy filtering).

3. **Import Performance**: Should the implementation include batch import helpers or transaction/pragma optimizations?
   → **Recommend**: Document expected import patterns (iterate Pydantic records → insert per dataset), optimize after schema validation.

4. **Future Cross-Dataset Joins**: If users need to perform frequent joins (e.g., types with icons, types with groups), should we provide helper views or recommend indices?
   → **Recommend**: Plan as Phase 2 after initial schema validation and import testing.
