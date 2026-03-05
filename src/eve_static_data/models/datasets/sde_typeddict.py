"""Models for EVE Static Data Export (SDE) datasets as typeddicts.

Honestly not sure if this is needed.

"""

# from typing import Any, TypedDict

# from eve_static_data.models.records import sde_typeddict as STD


# class SdeDataset(TypedDict):
#     """Base TypedDict for SDE datasets.

#     All SDE dataset TypedDicts should inherit from this.
#     """

#     buildNumber: int
#     releaseDate: str
#     dataset: str
#     data: list[dict[str, Any]]


# class AgentsInSpaceDataset(SdeDataset):
#     """Model for the agentsInSpace.jsonl SDE file."""

#     records: list[STD.AgentsInSpace]
