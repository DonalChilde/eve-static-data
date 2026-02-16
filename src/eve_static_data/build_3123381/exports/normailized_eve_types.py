from pydantic import BaseModel

from ..access.pydantic_lazy_loader import LocalizedLazyLoader
from ..access.raw_json_td import RawJsonFileAccess


class NormalizedEveType(BaseModel):
    typeID: int
    name: str
    groupID: int | None
    group: str | None
    categoryID: int | None
    category: str | None
    marketGroupID: int | None
    market_group: str | None
    metaGroupID: int | None
    meta_group: str | None
    factionID: int | None
    # faction: str | None
    variationParentTypeID: int | None
    volume: float | None
    radius: float | None
    mass: float | None
    portion_size: int
    published: bool
    description: str | None
    base_price: float | None
    capacity: float | None


def get_normalized_eve_types(
    access: LocalizedLazyLoader,
) -> dict[int, NormalizedEveType]:
    normalized_types: dict[int, NormalizedEveType] = {}
    eve_types = access.eve_types
    groups = access.groups
    categories = access.categories
    market_groups = access.market_groups
    meta_groups = access.meta_groups

    for eve_type in eve_types.data.values():
        group = groups.data.get(eve_type.groupID) if eve_type.groupID else None
        category = categories.data.get(group.categoryID) if group else None
        market_group = (
            market_groups.data.get(eve_type.marketGroupID)
            if eve_type.marketGroupID
            else None
        )
        meta_group = (
            meta_groups.data.get(eve_type.metaGroupID) if eve_type.metaGroupID else None
        )

        normalized_type = NormalizedEveType(
            typeID=eve_type.key,
            name=eve_type.name,
            groupID=group.key if group else None,
            group=group.name if group else None,
            categoryID=category.key if category else None,
            category=category.name if category else None,
            marketGroupID=market_group.key if market_group else None,
            market_group=market_group.name if market_group else None,
            metaGroupID=meta_group.key if meta_group else None,
            meta_group=meta_group.name if meta_group else None,
            factionID=eve_type.factionID,
            # faction=eve_type.faction_name,
            variationParentTypeID=eve_type.variationParentTypeID,
            volume=eve_type.volume,
            radius=eve_type.radius,
            mass=eve_type.mass,
            portion_size=eve_type.portionSize,
            published=eve_type.published,
            description=eve_type.description,
            base_price=eve_type.basePrice,
            capacity=eve_type.capacity,
        )
        normalized_types[eve_type.key] = normalized_type

    return normalized_types
