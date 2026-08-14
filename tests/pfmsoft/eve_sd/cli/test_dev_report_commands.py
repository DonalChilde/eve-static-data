"""Tests for dev performance report commands."""

from pathlib import Path

from typer.testing import CliRunner

from pfmsoft.eve_sd.cli import main_typer
from pfmsoft.eve_sd.cli.dev import performance_reports
from pfmsoft.eve_sd.helpers.sde_metadata import SdeMetadata, SdeVariant, SourceMedia
from pfmsoft.eve_sd.performance.models import DatasetTiming, SourceReport

runner = CliRunner()


def _make_report(source_type: str, *, build_number: int = 3464040) -> SourceReport:
    """Create minimal report data for CLI tests without real datasets."""
    return SourceReport(
        source_type=source_type,
        source_path=f"/tmp/{source_type}",
        generated_at="2024-01-01T00:00:00+00:00",
        startup_seconds=0.25,
        total_seconds=1.5,
        dataset_count=1,
        sde_metadata=SdeMetadata(
            buildNumber=build_number,
            releaseDate="2024-01-01",
            variant=SdeVariant.YAML,
            source_media=SourceMedia.YAML,
        ),
        datasets=[
            DatasetTiming(
                dataset_name="agents",
                record_count=10,
                total_seconds=0.5,
                source_type=source_type,
                key_type="str",
                file_size_bytes=1024,
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

    def test_render_report_command_is_available(self) -> None:
        """The dev group exposes a markdown render command."""
        result = runner.invoke(main_typer.app, ["dev", "render-report", "--help"])

        assert result.exit_code == 0
        assert "markdown" in result.stdout.lower()
        assert "--from" in result.stdout

    def test_report_json_round_trips_and_renders_markdown(
        self, tmp_path: Path, monkeypatch
    ) -> None:
        """A report can be serialized, deserialized, and rendered to markdown."""
        report = _make_report("files")
        report_path = tmp_path / "report.json"
        report_path.write_text(report.serialize(indent=2), encoding="utf-8")

        monkeypatch.setattr(
            performance_reports,
            "render_report_markdown",
            lambda report_obj: (
                "# SDE performance report\n\n### agents\n\n- record_count: 10"
            ),
        )

        result = runner.invoke(
            main_typer.app,
            ["dev", "render-report", "--from", str(report_path), "--to", "-"],
        )

        assert result.exit_code == 0
        assert "# SDE performance report" in result.stdout
        assert "agents" in result.stdout
        assert "record_count: 10" in result.stdout

        restored = SourceReport.deserialize(report.serialize())
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
            lambda source_dir: _make_report("files", build_number=3464040),
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
            lambda source_db: _make_report("db", build_number=3464040),
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
