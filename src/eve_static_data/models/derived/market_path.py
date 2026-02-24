"""Module for handling market paths in EVE Online static data."""

from typing import Self

from pydantic import BaseModel

from eve_static_data.models.datasets.localized_pydantic import (
    MarketGroupsLocalizedDataset,
)
from eve_static_data.models.datasets.sde_dataset_base import LocalizedSdeDataset
from eve_static_data.models.records.sde_pydantic_localized import MarketGroupsLocalized


class MarketPath(BaseModel):
    """Represents the path of a market group in the market group hierarchy."""

    key: int
    int_path: list[int]
    str_path: list[str]

    def int_string_path(self, separator: str = "/") -> str:
        """Get the market path as a string of integers."""
        return separator.join(str(mg_id) for mg_id in self.int_path)

    def str_string_path(self, separator: str = "/") -> str:
        """Get the market path as a string of names."""
        return separator.join(self.str_path)


class MarketPathsDataset(LocalizedSdeDataset):
    data: dict[int, MarketPath]

    @classmethod
    def from_dataset(cls, market_groups_dataset: MarketGroupsLocalizedDataset) -> Self:
        """Create a MarketPathsDataset instance from a MarketGroupsLocalizedDataset."""
        result = cls(
            localized=market_groups_dataset.localized,
            build_number=market_groups_dataset.build_number,
            release_date=market_groups_dataset.release_date,
            data={},
        )
        for mg_id in market_groups_dataset.data.keys():
            market_path = get_market_path(mg_id, market_groups_dataset.data)
            result.data[mg_id] = market_path
        return result


def get_market_path(
    market_group_id: int, market_groups: dict[int, MarketGroupsLocalized]
) -> MarketPath:
    """Get the market path for a given market group ID."""
    int_path = get_market_path_int(market_group_id, market_groups)
    str_path = get_market_path_string(int_path, market_groups)
    return MarketPath(
        key=market_group_id,
        int_path=int_path,
        str_path=str_path.split("/"),
    )


def get_market_path_int(
    market_group_id: int, market_groups: dict[int, MarketGroupsLocalized]
) -> list[int]:
    """Get the market path as a list of integers for a given market group ID.

    Starting from the given market group ID, traverse up the parentGroupIDs
    to build the full path to the root market group. Path is returned as a list
    of integers representing market group IDs from root to the specified market group.
    """
    if market_group_id not in market_groups:
        raise ValueError(
            f"Market group ID {market_group_id} not found in market groups."
        )

    def get_path(market_group_id: int) -> list[int]:
        path: list[int] = []
        current = market_groups.get(market_group_id)
        while current:
            path.append(current.key)
            if current.parentGroupID is None:
                break
            current = market_groups.get(current.parentGroupID)
        return path

    path = get_path(market_group_id)
    if not path:
        raise ValueError(
            f"Market group ID {market_group_id} not found in market groups."
        )
    return list(reversed(path))


def get_market_path_string(
    market_path: list[int],
    market_groups: dict[int, MarketGroupsLocalized],
    separator: str = "/",
) -> str:
    """Get the market path as a string for a given market path list of integers."""
    names: list[str] = []
    for mg_id in market_path:
        market_group = market_groups.get(mg_id)
        if market_group is None:
            raise ValueError(f"Market group ID {mg_id} not found in market groups.")
        names.append(market_group.name)
    return separator.join(names)
