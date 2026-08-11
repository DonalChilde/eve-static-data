"""Regression tests for schema report generation."""

from pathlib import Path

from pfmsoft.eve_sd.helpers.sde_metadata import (
    SdeMetadata,
    SdeVariant,
    SourceMedia,
)
from pfmsoft.eve_sd.schema_inspection import (
    DatasetInput,
    build_schema_report,
    generate_markdown_report,
    inspect_dataset_data,
)
from pfmsoft.eve_sd.schema_inspection.report_from_files import get_jsonl_schema_report


def test_inspect_dataset_data_returns_expected_structure() -> None:
    """Inspecting a sample dataset should produce the report structure used by the CLI."""
    metadata = SdeMetadata(
        buildNumber=123,
        releaseDate="2024-01-01",
        variant=SdeVariant.YAML,
        source_media=SourceMedia.YAML,
    )
    report = inspect_dataset_data(
        dataset_name="sample",
        dataset_data={
            "1": {"name": "Alice", "skills": [{"name": "Mining"}]},
            "2": {"name": "Bob", "skills": []},
        },
        sde_metadata=metadata,
    )

    assert report.dataset_name == "sample"
    assert report.total_records == 2
    assert report.valid_record_count == 2
    assert report.skipped_record_count == 0
    assert "name" in report.fields
    assert "skills" in report.fields
    assert report.fields["skills"].required is True
    assert report.fields["name"].required is True


def test_build_schema_report_aggregates_datasets_and_paths() -> None:
    """The aggregate report should summarize all inspected datasets."""
    metadata = SdeMetadata(
        buildNumber=123,
        releaseDate="2024-01-01",
        variant=SdeVariant.YAML,
        source_media=SourceMedia.YAML,
    )
    report = build_schema_report(
        datasets=[
            DatasetInput(
                dataset_name="alpha",
                dataset_data={"1": {"name": "Alice"}},
                sde_metadata=metadata,
            ),
            DatasetInput(
                dataset_name="beta",
                dataset_data={"1": {"name": "Bob"}},
                sde_metadata=metadata,
            ),
        ],
        sde_metadata=metadata,
        dataset_source="/tmp/sde",
    )

    assert report.file_count == 2
    assert report.total_records == 2
    assert set(report.datasets) == {"alpha", "beta"}


def test_generate_markdown_report_contains_expected_sections() -> None:
    """Markdown rendering should preserve the summary and warning sections."""
    metadata = SdeMetadata(
        buildNumber=123,
        releaseDate="2024-01-01",
        variant=SdeVariant.YAML,
        source_media=SourceMedia.YAML,
    )
    report = build_schema_report(
        datasets=[
            DatasetInput(
                dataset_name="alpha",
                dataset_data={"1": {"name": "Alice"}},
                sde_metadata=metadata,
            )
        ],
        sde_metadata=metadata,
        dataset_source="/tmp/sde",
    )

    markdown = generate_markdown_report(report)

    assert "# Schema Report v2" in markdown
    assert "## Summary" in markdown
    assert "## alpha" in markdown
    assert "### Warnings" in markdown


def test_get_jsonl_schema_report_reads_fixture_data(sde_jsonl_dir: Path) -> None:
    """The file-based report builder should read the JSONL fixture directory."""
    report = get_jsonl_schema_report(Path(sde_jsonl_dir))

    assert report.source_path == str(sde_jsonl_dir)
    assert report.file_count > 0
    assert report.datasets
