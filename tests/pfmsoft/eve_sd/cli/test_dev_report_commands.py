"""Tests for dev performance report commands."""

from pathlib import Path

from typer.testing import CliRunner

from pfmsoft.eve_sd.cli import main_typer
from pfmsoft.eve_sd.cli.dev import performance_reports
from pfmsoft.eve_sd.helpers.sde_metadata import SdeMetadata, SdeVariant, SourceMedia
from pfmsoft.eve_sd.performance.models import (
    DbDatasetTiming,
    DbSourceReport,
    FileDatasetTiming,
    FileSourceReport,
)
from pfmsoft.eve_sd.performance.renderers import (
    render_db_report_markdown,
    render_files_report_markdown,
)

runner = CliRunner()


def _make_file_report(*, build_number: int = 3464040) -> FileSourceReport:
    """Create a mocked file-backed report without real dataset loading."""
    return FileSourceReport(
        source_path="/tmp/files",
        generated_at="2024-01-01T00:00:00+00:00",
        startup_seconds=0.25,
        total_seconds=1.5,
        dataset_count=1,
        deserialization_method="jsonl/json/yaml raw loaders",
        sde_metadata=SdeMetadata(
            buildNumber=build_number,
            releaseDate="2024-01-01",
            variant=SdeVariant.YAML,
            source_media=SourceMedia.YAML,
        ),
        file_size_bytes=2048,
        datasets=[
            FileDatasetTiming(
                dataset_name="agents",
                record_count=10,
                total_seconds=0.5,
                key_type="str",
                file_size_bytes=1024,
                notes="loaded via mocked report generator",
            )
        ],
    )


def _make_db_report(*, build_number: int = 3464040) -> DbSourceReport:
    """Create a mocked DB-backed report without a real SQLite database."""
    return DbSourceReport(
        source_path="/tmp/db.sqlite",
        generated_at="2024-01-01T00:00:00+00:00",
        startup_seconds=0.25,
        total_seconds=1.5,
        dataset_count=1,
        serialization_format="sqlite-json",
        sde_metadata=SdeMetadata(
            buildNumber=build_number,
            releaseDate="2024-01-01",
            variant=SdeVariant.YAML,
            source_media=SourceMedia.DB,
        ),
        datasets=[
            DbDatasetTiming(
                dataset_name="agents",
                record_count=10,
                total_seconds=0.5,
                dataset_load_seconds=0.5,
                all_dataset_keys_seconds=0.2,
                random_record_access_seconds=0.1,
                random_record_access_sample_size=5,
                key_type="str",
                notes="loaded via mocked report generator",
            )
        ],
    )


class TestDevReportCommands:
    """Tests for dev performance-report command registration."""

    def test_report_files_command_is_available(self) -> None:
        """The dev group exposes a files-based performance report command."""
        result = runner.invoke(main_typer.app, ["dev", "report-files", "--help"])

        assert result.exit_code == 0
        assert "JSON performance report" in result.stdout
        assert "--from" in result.stdout

    def test_report_db_command_is_available(self) -> None:
        """The dev group exposes a DB-based performance report command."""
        result = runner.invoke(main_typer.app, ["dev", "report-db", "--help"])

        assert result.exit_code == 0
        assert "JSON performance report" in result.stdout
        assert "--from" in result.stdout

    def test_report_markdown_commands_are_available(self) -> None:
        """The dev group exposes source-specific markdown render commands."""
        files_result = runner.invoke(
            main_typer.app, ["dev", "report-files-markdown", "--help"]
        )
        db_result = runner.invoke(
            main_typer.app, ["dev", "report-db-markdown", "--help"]
        )

        assert files_result.exit_code == 0
        assert "markdown" in files_result.stdout.lower()
        assert "--from" in files_result.stdout
        assert db_result.exit_code == 0
        assert "markdown" in db_result.stdout.lower()
        assert "--from" in db_result.stdout

    def test_report_json_round_trips_and_renders_markdown(
        self, tmp_path: Path, monkeypatch
    ) -> None:
        """A file report can be serialized, deserialized, and rendered to markdown."""
        report = _make_file_report()
        report_path = tmp_path / "report.json"
        report_path.write_text(report.serialize(indent=2), encoding="utf-8")

        monkeypatch.setattr(
            performance_reports,
            "render_files_report_markdown",
            lambda report_obj: (
                "# SDE performance report\n\n### agents\n\n- record_count: 10"
            ),
        )

        result = runner.invoke(
            main_typer.app,
            [
                "dev",
                "report-files-markdown",
                "--from",
                str(report_path),
                "--to",
                "-",
            ],
        )

        assert result.exit_code == 0
        assert "# SDE performance report" in result.stdout
        assert "agents" in result.stdout
        assert "record_count: 10" in result.stdout

        restored = FileSourceReport.deserialize(report.serialize())
        assert restored.source_type == report.source_type
        assert restored.datasets[0].dataset_name == report.datasets[0].dataset_name

    def test_report_commands_write_named_files_to_output_directory(
        self, tmp_path: Path, monkeypatch
    ) -> None:
        """Directory output gets a build-numbered default filename per source type."""
        files_output_dir = tmp_path / "reports_files"
        files_input_dir = tmp_path / "fake-files"
        files_input_dir.mkdir()
        monkeypatch.setattr(
            performance_reports,
            "generate_files_report",
            lambda source_dir: _make_file_report(build_number=3464040),
        )
        result_files = runner.invoke(
            main_typer.app,
            [
                "dev",
                "report-files",
                "--from",
                str(files_input_dir),
                "--to",
                str(files_output_dir),
            ],
        )

        assert result_files.exit_code == 0
        files_output_files = list(files_output_dir.iterdir())
        assert len(files_output_files) == 1
        assert files_output_files[0].name.startswith(
            "performance_report_files_build_3464040"
        )
        assert files_output_files[0].suffix == ".json"

        db_output_dir = tmp_path / "reports_db"
        db_input_path = tmp_path / "fake-db.sqlite"
        db_input_path.write_text("not a real db", encoding="utf-8")
        monkeypatch.setattr(
            performance_reports,
            "generate_db_report",
            lambda source_db: _make_db_report(build_number=3464040),
        )
        result_db = runner.invoke(
            main_typer.app,
            [
                "dev",
                "report-db",
                "--from",
                str(db_input_path),
                "--to",
                str(db_output_dir),
            ],
        )

        assert result_db.exit_code == 0
        db_output_files = list(db_output_dir.iterdir())
        assert len(db_output_files) == 1
        assert db_output_files[0].name.startswith("performance_report_db_build_3464040")
        assert db_output_files[0].suffix == ".json"

    def test_file_and_db_reports_use_specific_report_types(self) -> None:
        """Each source type uses a dedicated report model and markdown formatter."""
        files_report = _make_file_report()
        db_report = _make_db_report()

        assert isinstance(
            FileSourceReport.deserialize(files_report.serialize()), FileSourceReport
        )
        assert isinstance(
            DbSourceReport.deserialize(db_report.serialize()), DbSourceReport
        )
        assert "file_size_bytes" in render_files_report_markdown(files_report)
        assert "serialization_format" in render_db_report_markdown(db_report)

    def test_rendered_times_use_decimal_not_scientific_notation(self) -> None:
        """Tiny time values should render as fixed-point decimals for readability."""
        report = _make_db_report()
        report.datasets[0].total_seconds = 0.000000000001
        report.datasets[0].dataset_load_seconds = 0.000000000001
        report.datasets[0].all_dataset_keys_seconds = 0.000000000002
        report.datasets[0].random_record_access_seconds = 0.000000000003

        rendered = render_db_report_markdown(report)

        assert "0.000000000001" in rendered
        assert "1e-12" not in rendered
        assert "2e-12" not in rendered
        assert "3e-12" not in rendered
