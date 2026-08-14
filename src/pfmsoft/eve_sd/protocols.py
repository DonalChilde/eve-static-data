"""Protocols and type definitions for the Eve SD package."""

from collections.abc import Iterable
from typing import TYPE_CHECKING, Any, Protocol

if TYPE_CHECKING:
    from pfmsoft.eve_sd.db.models import SerializationFormat
    from pfmsoft.eve_sd.helpers.sde_metadata import SdeMetadata

type Record = dict[str | int, Any]
"""Type alias for a record from an EVE SDE dataset."""
type IntKeyedRecord = tuple[int, Record]
"""Type alias for a record from an EVE SDE dataset with an integer key."""
type StrKeyedRecord = tuple[str, Record]
"""Type alias for a record from an EVE SDE dataset with a string key."""
type KeyedRecord = IntKeyedRecord | StrKeyedRecord
"""Type alias for a record from an EVE SDE dataset with either an integer or string key."""
type Dataset = dict[str | int, Record]
"""Type alias for an EVE SDE dataset, which is a mapping of keys to records."""


class DatasetDbQueryProtocol(Protocol):
    """Protocol for the public read interface of an SDE database query."""

    @property
    def dataset_key_types(self) -> dict[str, str]:
        """Return key-type metadata for all datasets."""
        raise NotImplementedError

    @property
    def serialization_format(self) -> SerializationFormat:
        """Return the database serialization format."""
        raise NotImplementedError

    @property
    def sde_metadata(self) -> SdeMetadata:
        """Return the latest stored SDE metadata row."""
        raise NotImplementedError

    @property
    def dataset_record_counts(self) -> dict[str, int]:
        """Return record counts for all datasets."""
        raise NotImplementedError

    def dataset_record_count(self, dataset_name: str) -> int:
        """Return the record count for one dataset."""
        raise NotImplementedError

    def get_records(
        self, dataset_name: str, record_keys: set[str | int] | None = None
    ) -> Iterable[KeyedRecord]:
        """Yield records for a dataset, regardless of key type."""
        raise NotImplementedError

    def get_int_records(
        self, dataset_name: str, record_keys: set[int] | None = None
    ) -> Iterable[IntKeyedRecord]:
        """Yield records for an integer-keyed dataset."""
        raise NotImplementedError

    def get_int_keys(self, dataset_name: str) -> set[int]:
        """Return the set of integer keys for a dataset."""
        raise NotImplementedError

    def get_str_records(
        self, dataset_name: str, record_keys: set[str] | None = None
    ) -> Iterable[StrKeyedRecord]:
        """Yield records for a string-keyed dataset."""
        raise NotImplementedError

    def get_str_keys(self, dataset_name: str) -> set[str]:
        """Return the set of string keys for a dataset."""
        raise NotImplementedError

    def get_int_records_page(
        self, dataset_name: str, *, limit: int, offset: int
    ) -> Iterable[IntKeyedRecord]:
        """Yield a page of records for an integer-keyed dataset."""
        raise NotImplementedError

    def get_str_records_page(
        self, dataset_name: str, *, limit: int, offset: int
    ) -> Iterable[StrKeyedRecord]:
        """Yield a page of records for a string-keyed dataset."""
        raise NotImplementedError
