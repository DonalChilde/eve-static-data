"""Tests for SDE schema report generation."""

import json
from pathlib import Path
from textwrap import dedent

from eve_static_data.helpers.schema_report import (
    SchemaReport,
    generate_markdown_report,
    scan_directory,
    scan_file,
)


def _write_yaml(tmp_path: Path, file_name: str, content: str) -> Path:
    """Write YAML test content to disk.

    Args:
        tmp_path: Temporary test directory.
        file_name: Output file name.
        content: YAML content to write.

    Returns:
        Path to the written YAML file.
    """
    path = tmp_path / file_name
    path.write_text(dedent(content).strip() + "\n", encoding="utf-8")
    return path


def _write_json(tmp_path: Path, file_name: str, data: object) -> Path:
    """Write JSON test content to disk.

    Args:
        tmp_path: Temporary test directory.
        file_name: Output file name.
        data: Data to serialise as JSON.

    Returns:
        Path to the written JSON file.
    """
    path = tmp_path / file_name
    path.write_text(json.dumps(data), encoding="utf-8")
    return path


def _dataset(report: SchemaReport, file_name: str) -> dict:
    """Return one dataset block from a schema report.

    Args:
        report: Schema report to inspect.
        file_name: Dataset file name to fetch.

    Returns:
        Dataset inspection mapping.
    """
    return report["datasets"][file_name]


# ---------------------------------------------------------------------------
# yaml-model tests (dict top-level)
# ---------------------------------------------------------------------------


def test_scan_file_yaml_model_tracks_nested_paths_and_required_flags(
    tmp_path: Path,
) -> None:
    """Nested dict and list-of-dict paths should be flattened correctly."""
    file_path = _write_yaml(
        tmp_path,
        "blueprints.yaml",
        """
        681:
          activities:
            manufacturing:
              materials:
                - quantity: 86
                  typeID: 38
              time: 600
          blueprintTypeID: 681
          maxProductionLimit: 300
        682:
          activities:
            manufacturing:
              materials:
                - quantity: 133
                  typeID: 38
              time: 600
            invention:
              products:
                - probability: 0.3
                  quantity: 1
                  typeID: 39581
              time: 63900
          blueprintTypeID: 682
          maxProductionLimit: 30
        """,
    )

    report = scan_file(file_path, sde_format="yaml-model")
    dataset = _dataset(report, "blueprints.yaml")
    paths = dataset["paths"]

    assert dataset["total_records"] == 2
    assert dataset["top_level_key_type_counts"] == {"int": 2}
    assert paths["activities.manufacturing.materials"]["value_type_counts"] == {
        "list": 2,
    }
    assert paths["activities.manufacturing.materials.quantity"]["presence_count"] == 2
    assert paths["activities.manufacturing.materials.quantity"]["container_count"] == 2
    assert paths["activities.manufacturing.materials.quantity"]["required"] is True
    assert paths["activities.invention.time"]["presence_count"] == 1
    assert paths["activities.invention.time"]["container_count"] == 1
    assert paths["activities.invention.time"]["required"] is False
    assert paths["activities.invention.products.probability"]["presence_count"] == 1
    assert paths["activities.invention.products.probability"]["container_count"] == 1
    assert paths["activities.invention.products.probability"]["required"] is False


def test_scan_file_yaml_model_tracks_union_types_and_nulls(tmp_path: Path) -> None:
    """Scalar union counts and null values should be preserved."""
    file_path = _write_yaml(
        tmp_path,
        "types.yaml",
        """
        1:
          foo: 10
        2:
          foo: null
        3:
          foo: text
        """,
    )

    report = scan_file(file_path, sde_format="yaml-model")
    foo = _dataset(report, "types.yaml")["paths"]["foo"]

    assert foo["required"] is True
    assert foo["presence_count"] == 3
    assert foo["container_count"] == 3
    assert foo["value_type_counts"] == {"int": 1, "null": 1, "str": 1}


def test_scan_file_yaml_model_warns_for_skipped_records_and_list_edge_cases(
    tmp_path: Path,
) -> None:
    """Warnings should capture skipped top-level values and mixed or empty lists."""
    file_path = _write_yaml(
        tmp_path,
        "edge_cases.yaml",
        """
        1:
          values:
            - 1
            - key: value
        2:
          values: []
        3: skipped
        """,
    )

    report = scan_file(file_path, sde_format="yaml-model")
    dataset = _dataset(report, "edge_cases.yaml")

    assert dataset["skipped_record_count"] == 1
    assert dataset["paths"]["values"]["presence_count"] == 2
    assert any(
        "non-dict value str; skipped" in warning for warning in dataset["warnings"]
    )
    assert any(
        "values: list contains mixed item types" in warning
        for warning in dataset["warnings"]
    )
    assert any(
        "values: encountered 1 empty list" in warning for warning in dataset["warnings"]
    )


def test_scan_directory_yaml_model_sorts_datasets_and_aggregates_summary(
    tmp_path: Path,
) -> None:
    """Directory scans should produce sorted dataset sections and aggregate counts."""
    _write_yaml(
        tmp_path,
        "b.yaml",
        """
        1:
          second: 2
        """,
    )
    _write_yaml(
        tmp_path,
        "a.yaml",
        """
        1:
          first: 1
        """,
    )

    report = scan_directory(tmp_path, sde_format="yaml-model")

    assert list(report["datasets"]) == ["a.yaml", "b.yaml"]
    assert report["file_count"] == 2
    assert report["total_records"] == 2
    assert report["total_unique_paths"] == 2
    assert report["datasets"]["a.yaml"]["top_level_key_type_counts"] == {"int": 1}


def test_generate_markdown_report_includes_dataset_sections_and_table(
    tmp_path: Path,
) -> None:
    """Rendered markdown should include the summary and per-dataset field table."""
    file_path = _write_yaml(
        tmp_path,
        "sample.yaml",
        """
        1:
          foo: 1
          bar:
            baz: true
        2:
          foo: null
        """,
    )

    markdown = generate_markdown_report(scan_file(file_path, sde_format="yaml-model"))

    assert "# Schema Report" in markdown
    assert "## sample.yaml" in markdown
    assert "- Records: 2" in markdown
    assert "- Top-level key types: int:2" in markdown
    assert "- Valid dict records: 2" in markdown
    assert "| Path | Presence | Required | Types |" in markdown
    assert "| foo | 2/2 | yes | str:0 |" not in markdown
    assert "| foo | 2/2 | yes | int:1, null:1 |" in markdown
    assert "| bar.baz | 1/1 | no | bool:1 |" in markdown
    assert "### Warnings" in markdown


def test_scan_file_yaml_model_smoke_on_real_fixture() -> None:
    """A real YAML dataset fixture should produce expected key paths."""
    fixture_path = (
        Path(__file__).resolve().parents[3]
        / "tests"
        / "resources"
        / "sde_data"
        / "yaml"
        / "blueprints.yaml"
    )

    report = scan_file(fixture_path, sde_format="yaml-model")
    dataset = _dataset(report, "blueprints.yaml")

    assert dataset["valid_record_count"] == 3
    assert "activities.manufacturing.materials" in dataset["paths"]
    assert "activities.manufacturing.materials.typeID" in dataset["paths"]
    assert "blueprintTypeID" in dataset["paths"]


# ---------------------------------------------------------------------------
# yaml-model JSON input (yaml-converted-to-json dicts)
# ---------------------------------------------------------------------------


def test_scan_file_yaml_model_json_dict_input_matches_yaml_report(
    tmp_path: Path,
) -> None:
    """A JSON dict file with yaml-model format should produce the same shape as YAML."""
    yaml_path = _write_yaml(
        tmp_path,
        "types.yaml",
        """
        1:
          name: Alpha
          group: 5
        2:
          name: Beta
          group: 7
        """,
    )
    # Equivalent yaml-converted-to-json: string keys, same structure.
    json_path = _write_json(
        tmp_path,
        "types.json",
        {"1": {"name": "Alpha", "group": 5}, "2": {"name": "Beta", "group": 7}},
    )

    yaml_report = scan_file(yaml_path, sde_format="yaml-model")
    json_report = scan_file(json_path, sde_format="yaml-model")

    yaml_paths = _dataset(yaml_report, "types.yaml")["paths"]
    json_paths = _dataset(json_report, "types.json")["paths"]

    assert set(yaml_paths) == set(json_paths)
    assert yaml_paths["name"]["presence_count"] == json_paths["name"]["presence_count"]
    assert yaml_paths["group"]["required"] == json_paths["group"]["required"]


# ---------------------------------------------------------------------------
# yaml-model integer key normalization
# ---------------------------------------------------------------------------


def test_scan_file_yaml_model_normalizes_nested_int_keys_to_integer_key(
    tmp_path: Path,
) -> None:
    """Nested int-keyed dicts should collapse to INTEGER_KEY paths."""
    file_path = _write_yaml(
        tmp_path,
        "skills.yaml",
        """
        1:
          requiredSkills:
            3380: 5
            3388: 4
        2:
          requiredSkills:
            3380: 3
        """,
    )

    report = scan_file(file_path, sde_format="yaml-model")
    paths = _dataset(report, "skills.yaml")["paths"]

    # Paths named after specific int keys must not appear.
    assert "requiredSkills.3380" not in paths
    assert "requiredSkills.3388" not in paths

    # All int keys should be merged under INTEGER_KEY.
    assert "requiredSkills.INTEGER_KEY" in paths
    int_key_path = paths["requiredSkills.INTEGER_KEY"]
    # Record 1 contributes 2 keys, record 2 contributes 1 → 3 total presences.
    assert int_key_path["presence_count"] == 3


def test_scan_file_yaml_model_normalizes_string_digit_keys_from_json(
    tmp_path: Path,
) -> None:
    """String digit keys in JSON (yaml-converted-to-json) should normalise to INTEGER_KEY."""
    # JSON always uses string keys; yaml-to-json conversion turns int keys to strings.
    file_path = _write_json(
        tmp_path,
        "skills.json",
        {
            "1": {"requiredSkills": {"3380": 5, "3388": 4}},
            "2": {"requiredSkills": {"3380": 3}},
        },
    )

    report = scan_file(file_path, sde_format="yaml-model")
    paths = _dataset(report, "skills.json")["paths"]

    assert "requiredSkills.3380" not in paths
    assert "requiredSkills.INTEGER_KEY" in paths
    assert paths["requiredSkills.INTEGER_KEY"]["presence_count"] == 3


# ---------------------------------------------------------------------------
# jsonl-model tests (list-of-dicts top-level)
# ---------------------------------------------------------------------------


def test_scan_file_jsonl_model_treats_list_items_as_records(tmp_path: Path) -> None:
    """JSONL-model input should iterate list items as records with _key as a normal field."""
    file_path = _write_json(
        tmp_path,
        "agentTypes.json",
        [
            {"_key": 1, "name": "NonAgent"},
            {"_key": 2, "name": "BasicAgent"},
            {"_key": 3, "name": "TutorialAgent"},
        ],
    )

    report = scan_file(file_path, sde_format="jsonl-model")
    dataset = _dataset(report, "agentTypes.json")

    assert dataset["total_records"] == 3
    assert dataset["valid_record_count"] == 3
    assert dataset["skipped_record_count"] == 0
    assert "_key" in dataset["paths"]
    assert "name" in dataset["paths"]
    assert dataset["paths"]["_key"]["presence_count"] == 3
    assert dataset["paths"]["_key"]["required"] is True
    assert dataset["paths"]["name"]["presence_count"] == 3
    assert dataset["paths"]["name"]["required"] is True


def test_scan_file_jsonl_model_skips_non_dict_list_items(tmp_path: Path) -> None:
    """Non-dict items in a jsonl-model list should be counted as skipped."""
    file_path = _write_json(
        tmp_path,
        "mixed.json",
        [
            {"_key": 1, "name": "Alpha"},
            "not a dict",
        ],
    )

    report = scan_file(file_path, sde_format="jsonl-model")
    dataset = _dataset(report, "mixed.json")

    assert dataset["total_records"] == 2
    assert dataset["valid_record_count"] == 1
    assert dataset["skipped_record_count"] == 1


def test_scan_file_jsonl_model_does_not_normalize_int_like_keys(
    tmp_path: Path,
) -> None:
    """Integer normalization does not apply to jsonl-model field names."""
    file_path = _write_json(
        tmp_path,
        "items.json",
        [{"_key": 1, "nested": {"3380": 5}}],
    )

    report = scan_file(file_path, sde_format="jsonl-model")
    paths = _dataset(report, "items.json")["paths"]

    # The string key "3380" should NOT be normalized for jsonl-model.
    assert "nested.3380" in paths
    assert "nested.INTEGER_KEY" not in paths


def test_scan_file_jsonl_model_errors_on_non_list_input(tmp_path: Path) -> None:
    """A jsonl-model file whose top-level value is not a list should emit a warning."""
    file_path = _write_json(
        tmp_path,
        "bad.json",
        {"1": {"name": "foo"}},
    )

    report = scan_file(file_path, sde_format="jsonl-model")
    dataset = _dataset(report, "bad.json")

    assert dataset["total_records"] == 0
    assert len(dataset["warnings"]) > 0
    assert any("list" in w for w in dataset["warnings"])


def test_report_includes_sde_format_in_dataset_header(tmp_path: Path) -> None:
    """Markdown report should include the sde_format in the dataset header section."""
    file_path = _write_yaml(
        tmp_path,
        "sample.yaml",
        """
        1:
          x: 1
        """,
    )
    markdown = generate_markdown_report(scan_file(file_path, sde_format="yaml-model"))
    assert "yaml-model" in markdown
