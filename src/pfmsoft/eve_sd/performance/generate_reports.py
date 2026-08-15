"""Generate JSON and markdown reports for SDE file and database access."""

from __future__ import annotations

import random
from collections.abc import Iterable
from datetime import UTC, datetime
from pathlib import Path
from time import perf_counter

from pfmsoft.eve_sd.eve_sd import EveSdDbQueryManager
from pfmsoft.eve_sd.helpers.load_raw_datasets import (
    load_json_as_dataset,
    load_jsonl_as_dataset,
    load_yaml_as_dataset,
)
from pfmsoft.eve_sd.helpers.sde_metadata import load_sde_metadata
from pfmsoft.eve_sd.performance.models import (
    DbDatasetTiming,
    DbSourceReport,
    FileDatasetTiming,
    FileSourceReport,
)
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


def generate_files_report(source_dir: Path) -> FileSourceReport:
    """Benchmark SDE datasets loaded from files and return a file report."""
    start = perf_counter()
    source_dir = source_dir.resolve()
    dataset_entries: list[FileDatasetTiming] = []
    collected_paths = _scan_dataset_files(source_dir)
    collect_paths_finished = perf_counter() - start

    for dataset_name, dataset_path in collected_paths:
        dataset_start = perf_counter()
        dataset = _load_file_dataset(dataset_path)
        dataset_elapsed = perf_counter() - dataset_start
        dataset_entries.append(
            FileDatasetTiming(
                dataset_name=dataset_name,
                record_count=len(dataset),
                total_seconds=dataset_elapsed,
                key_type="str"
                if all(isinstance(key, str) for key in dataset)
                else "int",
                file_size_bytes=dataset_path.stat().st_size,
                notes="loaded via raw filesystem dataset loader",
            )
        )

    total_seconds = perf_counter() - start
    sde_metadata = load_sde_metadata(source_dir)
    ordered_datasets = sorted(dataset_entries, key=lambda item: item.dataset_name)
    return FileSourceReport(
        source_path=str(source_dir),
        generated_at=_now_iso(),
        startup_seconds=collect_paths_finished,
        total_seconds=total_seconds,
        dataset_count=len(ordered_datasets),
        deserialization_method="jsonl/json/yaml raw loaders",
        sde_metadata=sde_metadata,
        datasets=ordered_datasets,
    )


def generate_db_report(source_db: Path) -> DbSourceReport:
    """Benchmark SDE datasets loaded from SQLite and return a db report."""
    start = perf_counter()
    with EveSdDbQueryManager(source_db) as conn:
        connection_established_seconds = perf_counter() - start
        dataset_entries: list[DbDatasetTiming] = []

        for dataset_name, key_type in conn.query.dataset_key_types.items():
            dataset_start = perf_counter()
            if key_type == "int":
                records = list(conn.query.get_int_records(dataset_name))
                dataset_elapsed = perf_counter() - dataset_start
                key_query_start = perf_counter()
                keys = conn.query.get_int_keys(dataset_name)
                all_dataset_keys_seconds = perf_counter() - key_query_start
                sample_size = min(max(1, len(keys) // 10), 100)
                sample_keys = (
                    set(random.sample(sorted(keys), sample_size))
                    if len(keys) > sample_size
                    else set(keys)
                )
                random_access_start = perf_counter()
                if sample_keys:
                    _ = list(
                        conn.query.get_int_records(
                            dataset_name, record_keys=sample_keys
                        )
                    )
                random_record_access_seconds = (
                    perf_counter() - random_access_start
                ) / max(len(sample_keys), 1)
            elif key_type == "str":
                records = list(conn.query.get_str_records(dataset_name))
                dataset_elapsed = perf_counter() - dataset_start
                key_query_start = perf_counter()
                keys = conn.query.get_str_keys(dataset_name)
                all_dataset_keys_seconds = perf_counter() - key_query_start
                sample_size = min(max(1, len(keys) // 10), 100)
                sample_keys = (
                    set(random.sample(sorted(keys), sample_size))
                    if len(keys) > sample_size
                    else set(keys)
                )
                random_access_start = perf_counter()
                if sample_keys:
                    _ = list(
                        conn.query.get_str_records(
                            dataset_name, record_keys=sample_keys
                        )
                    )
                random_record_access_seconds = (
                    perf_counter() - random_access_start
                ) / max(len(sample_keys), 1)
            else:
                raise ValueError(f"Unknown dataset key type: {key_type}")
            dataset_total_seconds = perf_counter() - dataset_start
            dataset_entries.append(
                DbDatasetTiming(
                    dataset_name=dataset_name,
                    record_count=len(records),
                    total_seconds=dataset_total_seconds,
                    dataset_load_seconds=dataset_elapsed,
                    all_dataset_keys_seconds=all_dataset_keys_seconds,
                    random_record_access_seconds=random_record_access_seconds,
                    random_record_access_sample_size=len(sample_keys),
                    key_type=key_type,
                    notes="loaded via DatasetDbQuery",
                )
            )

        total_seconds = perf_counter() - start
        sde_metadata = conn.query.sde_metadata
        ordered_datasets = sorted(dataset_entries, key=lambda item: item.dataset_name)
        return DbSourceReport(
            source_path=str(source_db),
            generated_at=_now_iso(),
            startup_seconds=connection_established_seconds,
            total_seconds=total_seconds,
            dataset_count=len(ordered_datasets),
            dataset_names=[item.dataset_name for item in ordered_datasets],
            serialization_format=str(conn.query.serialization_format),
            sde_metadata=sde_metadata,
            datasets=ordered_datasets,
        )


__all__ = [
    "generate_db_report",
    "generate_files_report",
]
