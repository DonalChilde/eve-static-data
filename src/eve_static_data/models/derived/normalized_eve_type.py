"""Models for normalized Eve types, which combine data from multiple localized datasets into a single structure."""

from typing import Self

from eve_static_data.models.pydantic.datasets import TypeDogmaDataset
from eve_static_data.models.pydantic.localized_datasets import (
    CategoriesLocalizedDataset,
    EveTypesLocalizedDataset,
    GroupsLocalizedDataset,
    MarketGroupsLocalizedDataset,
    MetaGroupsLocalizedDataset,
    SdeDatasetLocalized,
)
from eve_static_data.models.pydantic.localized_records import (
    CategoriesLocalized,
    EveTypesLocalized,
    GroupsLocalized,
    MarketGroupsLocalized,
    MetaGroupsLocalized,
)
from eve_static_data.models.pydantic.records import TypeDogma


class NormalizedEveType(EveTypesLocalized):
    """A normalized version of a localized Eve type, with related data from other datasets included.

    This is useful for spreadsheet exports and other use cases where having all related
    data in one place is convenient.
    """

    group: str | None
    categoryID: int | None
    category: str | None
    market_group: str | None
    meta_group: str | None
    meta_level: float | None
    """Dogma Attribute 633, which indicates the meta level of the item. This is not always present, so it is optional."""
    # faction: str | None


class NormalizedEveTypesDataset(SdeDatasetLocalized):
    records: dict[int, NormalizedEveType]

    @classmethod
    def from_datasets(
        cls,
        eve_types_dataset: EveTypesLocalizedDataset,
        groups_dataset: GroupsLocalizedDataset,
        categories_dataset: CategoriesLocalizedDataset,
        market_groups_dataset: MarketGroupsLocalizedDataset,
        meta_groups_dataset: MetaGroupsLocalizedDataset,
        type_dogma_dataset: TypeDogmaDataset,
    ) -> Self:
        """Create a NormalizedEveTypesDataset instance from localized datasets."""
        result = cls(
            lang=eve_types_dataset.lang,
            build_number=eve_types_dataset.build_number,
            release_date=eve_types_dataset.release_date,
            records={},
        )
        for eve_type in eve_types_dataset.records.values():
            normalized_type = normalize_eve_type(
                eve_type=eve_type,
                groups=groups_dataset.records,
                categories=categories_dataset.records,
                market_groups=market_groups_dataset.records,
                meta_groups=meta_groups_dataset.records,
                type_dogmas=type_dogma_dataset.records,
            )
            result.records[normalized_type.key] = normalized_type
        return result


def normalize_eve_type(
    eve_type: EveTypesLocalized,
    groups: dict[int, GroupsLocalized],
    categories: dict[int, CategoriesLocalized],
    market_groups: dict[int, MarketGroupsLocalized],
    meta_groups: dict[int, MetaGroupsLocalized],
    type_dogmas: dict[int, TypeDogma],
) -> NormalizedEveType:
    """Normalize an Eve type using related datasets."""
    group = groups.get(eve_type.groupID) if eve_type.groupID else None
    category = categories.get(group.categoryID) if group else None
    market_group = (
        market_groups.get(eve_type.marketGroupID) if eve_type.marketGroupID else None
    )
    meta_group = meta_groups.get(eve_type.metaGroupID) if eve_type.metaGroupID else None
    meta_level: float | None = None
    type_dogma = type_dogmas.get(eve_type.key)
    if type_dogma is not None:
        for dogma_attr in type_dogma.dogmaAttributes:
            if dogma_attr.attributeID == 633:  # Dogma Attribute 633 is the meta level
                meta_level = dogma_attr.value
                break

    return NormalizedEveType(
        _key=eve_type.key,
        name=eve_type.name,
        groupID=eve_type.groupID,
        group=group.name if group else None,
        categoryID=group.categoryID if group else None,
        category=category.name if category else None,
        marketGroupID=eve_type.marketGroupID,
        market_group=market_group.name if market_group else None,
        metaGroupID=eve_type.metaGroupID,
        meta_group=meta_group.name if meta_group else None,
        meta_level=meta_level,
        factionID=eve_type.factionID,
        variationParentTypeID=eve_type.variationParentTypeID,
        volume=eve_type.volume,
        radius=eve_type.radius,
        mass=eve_type.mass,
        portionSize=eve_type.portionSize,
        published=eve_type.published,
        description=eve_type.description,
        basePrice=eve_type.basePrice,
        capacity=eve_type.capacity,
    )
