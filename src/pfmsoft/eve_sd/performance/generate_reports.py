"""Generate JSON and markdown reports for SDE file and database access."""

from __future__ import annotations

from collections.abc import Iterable
from dataclasses import asdict
from datetime import UTC, datetime
from pathlib import Path
from time import perf_counter
from typing import Any

from pfmsoft.eve_snippets.sqlite3.connection_helpers import db_connection_manager

from pfmsoft.eve_sd.db.query import DatasetDbQuery
from pfmsoft.eve_sd.helpers.load_raw_datasets import (
    load_json_as_dataset,
    load_jsonl_as_dataset,
    load_yaml_as_dataset,
)
from pfmsoft.eve_sd.helpers.sde_metadata import load_sde_metadata
from pfmsoft.eve_sd.performance.models import DatasetTiming, SourceReport
from pfmsoft.eve_sd.protocols import Dataset


def _now_iso() -> str:
    """Return an ISO 8601 UTC timestamp for report metadata."""
    return datetime.now(UTC).isoformat()


def _scan_dataset_files(dataset_dir: Path) -> Iterable[tuple[str, Path]]:
    """Yield dataset files from a source directory."""
    for file_path in sorted(dataset_dir.iterdir()):
        if file_path.is_file() and file_path.name not in {"_sde.yaml", "_sde.jsonl"}:
            yield file_path.stem, file_path


def _load_file_dataset(dataset_path: Path) -> Dataset:
    """Load a dataset from a filesystem path."""
    suffix = dataset_path.suffix.lower()
    if suffix == ".jsonl":
        return load_jsonl_as_dataset(dataset_path)
    if suffix == ".json":
        return load_json_as_dataset(dataset_path)
    if suffix in {".yaml", ".yml"}:
        return load_yaml_as_dataset(dataset_path)
    raise ValueError(f"Unsupported dataset file type: {dataset_path}")


def generate_files_report(source_dir: Path) -> SourceReport:
    """Benchmark SDE datasets loaded from files and return a report object."""
    start = perf_counter()
    source_dir = source_dir.resolve()
    dataset_entries: list[DatasetTiming] = []

    for dataset_name, dataset_path in _scan_dataset_files(source_dir):
        dataset_start = perf_counter()
        dataset = _load_file_dataset(dataset_path)
        dataset_elapsed = perf_counter() - dataset_start
        dataset_entries.append(
            DatasetTiming(
                dataset_name=dataset_name,
                record_count=len(dataset),
                total_seconds=dataset_elapsed,
                source_type="files",
                key_type="str"
                if all(isinstance(key, str) for key in dataset)
                else "int",
                file_size_bytes=dataset_path.stat().st_size,
                notes="loaded via raw filesystem dataset loader",
            )
        )

    total_seconds = perf_counter() - start
    sde_metadata = load_sde_metadata(source_dir)
    return SourceReport(
        source_type="files",
        source_path=str(source_dir),
        generated_at=_now_iso(),
        startup_seconds=total_seconds,
        total_seconds=total_seconds,
        dataset_count=len(dataset_entries),
        deserialization_method="jsonl/json/yaml raw loaders",
        sde_metadata=sde_metadata,
        datasets=dataset_entries,
    )


def generate_db_report(source_db: Path) -> SourceReport:
    """Benchmark SDE datasets loaded from a SQLite database and return a report."""
    start = perf_counter()
    with db_connection_manager(source_db) as connection:
        db_query = DatasetDbQuery(connection)
        dataset_entries: list[DatasetTiming] = []

        for dataset_name, key_type in db_query.dataset_key_types.items():
            dataset_start = perf_counter()
            if key_type == "int":
                records = list(db_query.get_int_records(dataset_name))
            elif key_type == "str":
                records = list(db_query.get_str_records(dataset_name))
            else:
                raise ValueError(f"Unknown dataset key type: {key_type}")
            dataset_elapsed = perf_counter() - dataset_start
            dataset_entries.append(
                DatasetTiming(
                    dataset_name=dataset_name,
                    record_count=len(records),
                    total_seconds=dataset_elapsed,
                    source_type="db",
                    key_type=key_type,
                    notes="loaded via DatasetDbQuery",
                )
            )

        total_seconds = perf_counter() - start
        sde_metadata = db_query.sde_metadata
        return SourceReport(
            source_type="db",
            source_path=str(source_db),
            generated_at=_now_iso(),
            startup_seconds=total_seconds,
            total_seconds=total_seconds,
            dataset_count=len(dataset_entries),
            serialization_format=str(db_query.serialization_format),
            sde_metadata=sde_metadata,
            datasets=dataset_entries,
        )


def render_report_markdown(report: SourceReport | dict[str, Any]) -> str:
    """Render a performance report object to markdown text."""
    report_data = asdict(report) if isinstance(report, SourceReport) else report
    markdown_lines = [
        "# SDE performance report",
        "",
        f"- source type: {report_data.get('source_type', 'unknown')}",
        f"- source path: {report_data.get('source_path', 'unknown')}",
        f"- generated at: {report_data.get('generated_at', 'unknown')}",
        f"- total seconds: {report_data.get('total_seconds', 'unknown')}",
        "",
        "## Datasets",
        "",
    ]

    for dataset in report_data.get("datasets", []):
        markdown_lines.append(f"### {dataset.get('dataset_name', 'unknown')}")
        markdown_lines.append("")
        markdown_lines.append(
            f"- record_count: {dataset.get('record_count', 'unknown')}"
        )
        markdown_lines.append(
            f"- total_seconds: {dataset.get('total_seconds', 'unknown')}"
        )
        markdown_lines.append(f"- key_type: {dataset.get('key_type', 'unknown')}")
        markdown_lines.append(
            f"- file_size_bytes: {dataset.get('file_size_bytes', 'unknown')}"
        )
        markdown_lines.append("")

    return "\n".join(markdown_lines)
