# TODO for completion
# TODO needs factory function for loading from reader, and saving to disk.

from typing import TypedDict

from eve_static_data.models.records import sde_typeddict as STD


class SdeDataset(TypedDict):
    """Base TypedDict for SDE datasets.

    All SDE dataset TypedDicts should inherit from this.
    """

    buildNumber: int
    releaseDate: str


class AgentsInSpaceDataset(SdeDataset):
    """Model for the agentsInSpace.jsonl SDE file."""

    records: list[STD.AgentsInSpace]
