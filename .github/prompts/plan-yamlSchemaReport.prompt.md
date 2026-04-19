## Plan: YAML Schema Report V1 Minimal Scope

Deliver the fastest path to a useful YAML schema report: scan input YAML, aggregate recursive field paths and observed types with counts, and write a readable Markdown report. Defer baseline comparison, CLI wiring, and advanced diagnostics to v2.

**Steps**

1. Phase 1: Define V1 Report Contract
1. Confirm supported input shape: top-level mapping where each value is a record object.
1. Define recursive path notation for nested mappings and lists:
   - Dict traversal: path.key (standard dot notation)
   - List traversal: when a list is encountered, include it in the path (e.g., activities.manufacturing.materials)
   - List item fields: when list items are dicts, traverse their fields as separate paths (e.g., activities.manufacturing.materials.typeID, activities.manufacturing.materials.quantity)
1. Define type buckets and count semantics:
   - presence_count per path (count of records where path appears)
   - observed_types with counts per path (including null/None as a type bucket)
   - required/optional signal: path is required if presence_count == total_records, otherwise optional
   - For list paths, track the list container and item types; empty lists still reported with warning if applicable
   - For list item fields, presence_count is total items containing that field across all list occurrences

1. Phase 2: Implement Core Scanner Only
1. Add a helper module under src/eve_static_data/helpers for V1 scanning and report generation.
1. Implement single-file scan first to keep scope small and testable.
1. Implement optional directory scan as a thin loop over the single-file scanner.
1. Ensure deterministic output ordering for stable report diffs.

1. Phase 3: Markdown Report Output (Primary Goal)
1. Generate one Markdown report containing:

- global summary (total files scanned, total records, total unique paths discovered)
- **per-dataset section** for each YAML file scanned:
  - section heading: dataset filename
  - record count for that dataset
  - unified field table (path, presence with required/optional signal, observed types) that includes:
    - scalar paths (e.g., blueprintTypeID, name.en) with required/optional indicator
    - list paths (e.g., activities.manufacturing.materials) with required/optional indicator
    - list item field paths (e.g., activities.manufacturing.materials.typeID) with required/optional indicator

2. Include a warnings section for:
   - Malformed YAML or non-dict top-level values
   - Lists containing mixed types (dict vs scalar)
   - Schema inconsistencies (e.g., field never appears across dataset)

3. Phase 4: Essential Tests Only
4. Add focused unit tests for:

- recursive nested dict paths
- list item type counting
- mixed types represented as union with counts
- required/optional signal correctness
- null/None type tracking
- deterministic ordering
- malformed YAML and edge case handling

2. Add one golden-style snapshot test for Markdown output stability.

3. Phase 5: Define API Entry Points

```python
def scan_yaml_file(path: Path) -> YamlSchemaReport:
    """Scan a single YAML file and return schema report."""

def scan_yaml_directory(pattern: str | Path) -> YamlSchemaReport:
    """Scan multiple YAML files matching pattern and aggregate into single report."""
```

6. Phase 6: Validate V1 Outcome
1. Run tests for the new helper module.
1. Run scanner against at least one real dataset fixture to confirm report usefulness for TypedDict/dataclass planning.

**Relevant files**

- [scripts/jsonl_type_inspector.py](scripts/jsonl_type_inspector.py) — reuse recursive counting and deterministic shaping patterns
- [src/eve_static_data/helpers](src/eve_static_data/helpers) — add minimal V1 scanner/report helper
- [tests/eve_static_data](tests/eve_static_data) — add focused V1 tests aligned with existing layout
- [tests/resources/sde_data/yaml](tests/resources/sde_data/yaml) — use representative YAML-like fixture data where applicable

**Verification**

1. Targeted pytest run for the new scanner test module.
2. Manual check of generated Markdown report for readability and field coverage.
3. Confirm output includes nested paths and list item schemas needed for first-pass TypedDict/dataclass drafting.

**Decisions**

- Included in v1: scanner core plus Markdown report output.
- Excluded from v1: baseline diff comparison, CLI command integration, fail-on-change automation, historical snapshots.
- Primary success criterion: you can generate and inspect one schema report that is immediately useful for model design.

**Further Considerations**

1. V2 can add baseline comparison once report structure stabilizes.
2. V2 can add CLI wiring after helper API shape is validated by real data usage.

## Example v1 Report Format

```
## Summary
- files_scanned: 1
- total_records: 3
- total_paths_discovered: 11

## blueprints.yaml
Records: 3

| Path | Presence | Required | Types |
|------|----------|----------|-------|
| blueprintTypeID | 3/3 | yes | int:3 |
| maxProductionLimit | 3/3 | yes | int:3 |
| activities.manufacturing.time | 3/3 | yes | int:3 |
| activities.manufacturing.materials | 3/3 | yes | list:3 |
| activities.manufacturing.materials.quantity | 6/6 | yes | int:6 |
| activities.manufacturing.materials.typeID | 6/6 | yes | int:6 |
| activities.invention.time | 1/3 | no | int:1 |
| activities.invention.products | 1/3 | no | list:1 |
| activities.invention.products.probability | 1/1 | no | float:1 |
| activities.invention.products.quantity | 1/1 | no | int:1 |
| activities.invention.products.typeID | 1/1 | no | int:1 |
| deprecated_field | 0/3 | no | str:0 |

## Warnings
- deprecated_field: never appears in any records
- activities.invention.products: list appears in 1/3 records (optional)
```

Path notation rules:

- Dict keys use dot notation: `path.key`
- Lists are included in path: `path.to.list` (presence shows count of records containing that list)
- List item fields become separate paths: `path.to.list.fieldName`
- Required: yes if present in 100% of records, no otherwise
- Types include: int, float, str, bool, null, dict, list (with counts per type)
