# Plan: Textual TUI (`esd-tui`)

**TL;DR** — Build a full-featured Textual TUI in `src/eve_static_data/tui/` with 6 feature screens. `textual[syntax]` is already in `pyproject.toml`. Only change needed to existing files is adding the `esd-tui` entry point. All existing async `SDETools` methods are called directly via Textual Workers — no rewrapping needed.

---

## Decisions

- Entry point: `esd-tui` (separate binary, not `esd tui` subcommand)
- Code location: `src/eve_static_data/tui/` (alongside `cli/`)
- Dataset browser: one format per directory; raw line mode OR parsed record mode; dynamic JSONL→pretty-JSON per line
- Async: Textual Workers wrapping existing `SDETools` async methods directly (no `asyncio.run`)
- JSONL validate/schema are **stubs** (JSONL models incomplete)
- `EsdTuiApp` will be importable with no module-level side effects (future TUI-in-TUI)
- Metadata save to `metadata/` folder is out of scope (future refactor)

---

## Phase 1: Foundation

1. Add `esd-tui = "eve_static_data.tui.main:run"` to `pyproject.toml` `[project.scripts]`
2. Create `src/eve_static_data/tui/__init__.py`
3. Create `src/eve_static_data/tui/main.py` — `EsdTuiApp(App)` with basic screen routing + `run()` entry function
4. Create `src/eve_static_data/tui/screens/__init__.py`
5. Create `src/eve_static_data/tui/widgets/__init__.py`
6. Verify: `esd-tui` launches and exits cleanly

## Phase 2: Home / Navigation

7. `screens/home.py` — main menu screen with 6 feature buttons
8. Keyboard shortcuts: `n`=network, `u`=unpack, `b`=browse, `v`=validate, `e`=export, `s`=schema, `q`=quit

## Phase 3: Network Screen

9. `screens/network.py`

   **Build number selection** — three sources, selectable in the UI:
   - _Latest_: fetched from the latest SDE API (`sde_tools.fetch_latest_sde_info()`)
   - _User input_: typed directly
   - _From directory_: user selects an unpacked SDE directory; metadata loaded via `load_sde_info_from_detected_file()`

   **Metadata source for directory mode**:
   - `SdeDatasetsInfo` provides `buildNumber`, `releaseDate`, `file_format`, and `data_format`
   - Use `buildNumber` for changelog queries and show `releaseDate` in the UI context panel

   **Operations** (all via Worker, all use the resolved build number):
   - View latest SDE version info (latest source only)
   - View schema changelog — calls `sde_tools.fetch_schema_changelog(build_number)`
   - View data changelog — calls `sde_tools.fetch_data_changes(build_number)`
   - Download SDE: select variant, shows progress — calls `sde_tools.download()`

   **Save options**:
   - Save any fetched text to an arbitrary file
   - When build number came from a directory source: option to save changelogs to a `metadata/` subdirectory of that SDE directory

## Phase 4: Unpack Screen

10. `screens/unpack.py`
    - File picker for downloaded zip
    - Output directory input
    - Toggle: use build number in output folder name
    - Unpack via Worker calling `helpers.sde_unpack.unpack()`
    - Show unpacked SDE metadata (`buildNumber`, `releaseDate`, `file_format`, `data_format`) from returned `SdeDatasetsInfo`

## Phase 5: Dataset Browser _(most complex)_

11. `screens/browser.py`
12. `widgets/dataset_list.py` — directory-aware file list
13. `widgets/record_viewer.py` — paged record display

    **Directory input**: user provides an unpacked SDE directory path.

    **SDE directory detection**: validate by checking for a `_sde.*` file using `detect_sde_info_file`.

    **Format detection**: resolve metadata with `load_sde_info_from_detected_file()` and use `SdeDatasetsInfo`:
    - `file_format` indicates the on-disk file format (`YAML`, `JSONL`, `JSON`)
    - `data_format` indicates the underlying dataset model (`YAML` or `JSONL`)
    - `buildNumber`/`releaseDate` shown in browser header/status

    **File listing**: enumerate all files of the detected format extension in the directory, matching each stem against `SdeDatasetFiles` enum values:
    - Known files: display by filename stem (e.g. `types`, `marketGroups`) — nearly identical to enum value and immediately recognizable
    - Unknown files: display by filename stem with a visual flag (e.g. different color or `[unknown]` badge) — likely new datasets not yet added to `SdeDatasetFiles`; fall back to raw line/basic display
    - `SDE_INFO` (`_sde.*`) displayed separately as directory metadata, not in the main dataset list

    **Mode selector** (per-file): Raw lines | Parsed records
    - Raw line mode: reads file line-by-line (no parsing); optional pretty-JSON rendering for JSONL/JSON lines
    - Parsed record mode: known datasets load via `SdeYamlDatasetLoader` or `jsonl_reader`; unknown datasets fall back to raw line mode with pretty-print
    - Page size: configurable (default ~50)

## Phase 6: Validate Screen

14. `screens/validate.py`
    - Directory picker for SDE folder
    - Resolve and display `SdeDatasetsInfo` metadata (`buildNumber`, `releaseDate`, `file_format`, `data_format`)
    - Run validation via Worker (reuse existing pydantic validation logic from `validation.py`)
    - Stream results to scrollable log
    - Option to save report; default save path is the `validation/` subdirectory of the selected SDE directory
    - JSONL validation: stub

## Phase 7: Export Screen

15. `screens/export.py`
    - YAML→JSON export (calls existing export logic)
    - Localization narrowing (select language, select datasets)
    - Resolve source directory metadata via `SdeDatasetsInfo` to gate export options by `data_format`
    - Both run via Workers with progress

## Phase 8: Schema Inspection Screen

16. `screens/schema_inspect.py`
    - Dataset selector
    - Resolve and show SDE metadata from `SdeDatasetsInfo`
    - Renders schema report (reuse `helpers/schema_report.py`)
    - Option to save; default save path is the `schema/` subdirectory of the selected SDE directory
    - JSONL schema: stub

## Phase 9: Shared Widgets & Polish

17. `widgets/text_viewer.py` — scrollable text/YAML/JSON viewer (uses `textual[syntax]` for highlighting)
18. `widgets/progress_log.py` — worker progress/log display
19. Error handling: catch Worker errors, show in modal
20. Help overlay (`?` key)

---

## Files to Create

- `src/eve_static_data/helpers/sde_directory.py` — new helper module with:
  - `is_sde_directory(path: Path) -> bool` (optional wrapper over `detect_sde_info_file(path) is not None`)
  - `load_sde_info(path: Path) -> SdeDatasetsInfo` (or reuse `load_sde_info_from_detected_file` directly)
- `src/eve_static_data/tui/__init__.py`
- `src/eve_static_data/tui/main.py`
- `src/eve_static_data/tui/screens/__init__.py`
- `src/eve_static_data/tui/screens/home.py`
- `src/eve_static_data/tui/screens/network.py`
- `src/eve_static_data/tui/screens/unpack.py`
- `src/eve_static_data/tui/screens/browser.py`
- `src/eve_static_data/tui/screens/validate.py`
- `src/eve_static_data/tui/screens/export.py`
- `src/eve_static_data/tui/screens/schema_inspect.py`
- `src/eve_static_data/tui/widgets/__init__.py`
- `src/eve_static_data/tui/widgets/dataset_list.py`
- `src/eve_static_data/tui/widgets/record_viewer.py`
- `src/eve_static_data/tui/widgets/text_viewer.py`
- `src/eve_static_data/tui/widgets/progress_log.py`

## Files to Modify

- `pyproject.toml` — add `esd-tui` entry point under `[project.scripts]`

## Key Files to Reuse (no changes expected)

- `src/eve_static_data/sde_tools.py` — `SDETools` async methods called directly by Workers
- `src/eve_static_data/settings.py` — `EveStaticDataSettings` / `EveStaticDataSettingsPydantic`
- `src/eve_static_data/access/yaml_datasets.py` — `SdeYamlDatasetLoader`
- `src/eve_static_data/models/dataset_filenames.py` — `SdeDatasetFiles` (54 datasets)
- `src/eve_static_data/helpers/sde_info.py` — source of `SdeDatasetsInfo` and `_sde.*` detection/loading
- `src/eve_static_data/helpers/sde_unpack.py`
- `src/eve_static_data/helpers/schema_report.py`
- `src/eve_static_data/helpers/jsonl_reader.py`
- `src/eve_static_data/validation.py`

---

## Verification

1. `pip install -e .` → `esd-tui` launches
2. Home screen navigation works, all 6 feature screens reachable
3. Network: latest + manual + directory-sourced build number flows work; changelogs fetch and save
4. Directory metadata panel correctly shows `buildNumber`, `releaseDate`, `file_format`, `data_format` from `SdeDatasetsInfo`
5. Unpack: unpack a real zip file
6. Browser: correct format detection from `SdeDatasetsInfo.file_format`; known/unknown file behavior works
7. Validate: run against a real SDE folder, view output, default save to `validation/`
8. Export: YAML→JSON and localization narrowing work end-to-end with format-gating by `data_format`
9. Schema: schema report displays for ≥3 datasets; default save to `schema/`
10. Workers: error cases handled (bad path, network failure) → error modal, not crash
11. `ruff check src/eve_static_data/tui/` passes
