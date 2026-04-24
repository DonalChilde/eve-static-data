"""Unit tests for request_records helper functions."""

from typing import Any

import pytest

from eve_static_data.db.request_records import (
    _build_localized_fields_for_record,  # type: ignore
)
from eve_static_data.models.common import LocalizedString


class TestBuildLocalizedFieldsForRecord:
    """Tests for _build_localized_fields_for_record."""

    def test_single_language_single_field(self) -> None:
        """Single row with one localized field returns (id, None, LocalizedString)."""
        rows = [(1, "en", "Hello")]
        result = _build_localized_fields_for_record(rows)
        assert result == (1, None, LocalizedString(en="Hello"))

    def test_multiple_languages_single_field(self) -> None:
        """Multiple language rows are aggregated into one LocalizedString."""
        rows = [(5, "en", "Hello"), (5, "de", "Hallo"), (5, "fr", "Bonjour")]
        result = _build_localized_fields_for_record(rows)
        assert result == (
            5,
            None,
            LocalizedString(en="Hello", de="Hallo", fr="Bonjour"),
        )

    def test_multiple_languages_two_fields(self) -> None:
        """Two localized fields are assembled into separate LocalizedStrings."""
        rows = [
            (3, "en", "Name EN", "Desc EN"),
            (3, "de", "Name DE", "Desc DE"),
        ]
        result = _build_localized_fields_for_record(rows)
        assert result == (
            3,
            None,
            LocalizedString(en="Name EN", de="Name DE"),
            LocalizedString(en="Desc EN", de="Desc DE"),
        )

    def test_all_none_field_returns_none(self) -> None:
        """A localized field that is None for all languages returns None."""
        rows = [(7, "en", None), (7, "de", None)]
        result = _build_localized_fields_for_record(rows)
        assert result == (7, None, None)

    def test_all_none_among_multiple_fields(self) -> None:
        """One field all-None, another with values: None and LocalizedString returned."""
        rows = [(2, "en", "Name EN", None), (2, "de", "Name DE", None)]
        result = _build_localized_fields_for_record(rows)
        assert result == (2, None, LocalizedString(en="Name EN", de="Name DE"), None)

    def test_empty_rows_raises(self) -> None:
        """Empty input raises ValueError."""
        with pytest.raises(ValueError, match="No localized rows provided"):
            _build_localized_fields_for_record([])

    def test_mismatched_ids_raises(self) -> None:
        """Rows with different ids raise ValueError."""
        rows = [(1, "en", "Hello"), (2, "de", "Hallo")]
        with pytest.raises(ValueError, match="same id"):
            _build_localized_fields_for_record(rows)

    def test_mismatched_field_count_raises(self) -> None:
        """Rows with different numbers of localized fields raise ValueError."""
        rows: list[tuple[Any, ...]] = [(1, "en", "Name"), (1, "de", "Name DE", "Extra")]
        with pytest.raises(ValueError, match="same number of localized fields"):
            _build_localized_fields_for_record(rows)

    def test_partial_none_raises(self) -> None:
        """A field that is None for some but not all languages raises ValueError."""
        rows: list[tuple[Any, ...]] = [(4, "en", "Hello"), (4, "de", None)]
        with pytest.raises(
            ValueError, match="Some but not all localized fields are None"
        ):
            _build_localized_fields_for_record(rows)

    def test_id_is_preserved(self) -> None:
        """The record id is the first element of the result."""
        rows: list[tuple[Any, ...]] = [(42, "en", "Val")]
        result = _build_localized_fields_for_record(rows)
        assert result[0] == 42

    def test_second_element_is_none(self) -> None:
        """The second element of the result is always None (lang placeholder)."""
        rows: list[tuple[Any, ...]] = [(1, "en", "Val")]
        result = _build_localized_fields_for_record(rows)
        assert result[1] is None
