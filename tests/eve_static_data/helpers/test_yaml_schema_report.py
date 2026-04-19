"""Tests for YAML schema report generation."""

from pathlib import Path
from textwrap import dedent

from eve_static_data.helpers.yaml_schema_report import (
    YamlSchemaReport,
    generate_markdown_report,
    scan_yaml_directory,
    scan_yaml_file,
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


def _dataset(report: YamlSchemaReport, file_name: str) -> dict:
    """Return one dataset block from a schema report.

    Args:
        report: Schema report to inspect.
        file_name: Dataset file name to fetch.

    Returns:
        Dataset inspection mapping.
    """
    return report["datasets"][file_name]


def test_scan_yaml_file_tracks_nested_paths_and_required_flags(tmp_path: Path) -> None:
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

    report = scan_yaml_file(file_path)
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


def test_scan_yaml_file_tracks_union_types_and_nulls(tmp_path: Path) -> None:
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

    report = scan_yaml_file(file_path)
    foo = _dataset(report, "types.yaml")["paths"]["foo"]

    assert foo["required"] is True
    assert foo["presence_count"] == 3
    assert foo["container_count"] == 3
    assert foo["value_type_counts"] == {"int": 1, "null": 1, "str": 1}


def test_scan_yaml_file_warns_for_skipped_records_and_list_edge_cases(
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

    report = scan_yaml_file(file_path)
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


def test_scan_yaml_directory_sorts_datasets_and_aggregates_summary(
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

    report = scan_yaml_directory(tmp_path)

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

    markdown = generate_markdown_report(scan_yaml_file(file_path))

    assert "# YAML Schema Report" in markdown
    assert "## sample.yaml" in markdown
    assert "- Records: 2" in markdown
    assert "- Top-level key types: int:2" in markdown
    assert "- Valid dict records: 2" in markdown
    assert "| Path | Presence | Required | Types |" in markdown
    assert "| foo | 2/2 | yes | str:0 |" not in markdown
    assert "| foo | 2/2 | yes | int:1, null:1 |" in markdown
    assert "| bar.baz | 1/1 | no | bool:1 |" in markdown
    assert "### Warnings" in markdown


def test_scan_yaml_file_smoke_on_real_fixture() -> None:
    """A real YAML dataset fixture should produce expected key paths."""
    fixture_path = (
        Path(__file__).resolve().parents[3]
        / "tests"
        / "resources"
        / "sde_data"
        / "yaml"
        / "blueprints.yaml"
    )

    report = scan_yaml_file(fixture_path)
    dataset = _dataset(report, "blueprints.yaml")

    assert dataset["valid_record_count"] == 3
    assert "activities.manufacturing.materials" in dataset["paths"]
    assert "activities.manufacturing.materials.typeID" in dataset["paths"]
    assert "blueprintTypeID" in dataset["paths"]
