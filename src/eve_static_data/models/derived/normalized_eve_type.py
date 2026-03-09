"""Models for normalized Eve types, which combine data from multiple localized datasets into a single structure."""

from typing import Self

from eve_static_data.models.pydantic import localized_datasets as LDS
from eve_static_data.models.pydantic import localized_records as PML


class NormalizedEveType(PML.EveTypesLocalized):
    """A normalized version of a localized Eve type, with related data from other datasets included.

    This is useful for spreadsheet exports and other use cases where having all related
    data in one place is convenient.
    """

    group: str | None
    categoryID: int | None
    category: str | None
    market_group: str | None
    meta_group: str | None
    # faction: str | None


class NormalizedEveTypesDataset(LDS.SdeDatasetLocalized):
    records: dict[int, NormalizedEveType]

    @classmethod
    def from_datasets(
        cls,
        eve_types_dataset: LDS.EveTypesLocalizedDataset,
        groups_dataset: LDS.GroupsLocalizedDataset,
        categories_dataset: LDS.CategoriesLocalizedDataset,
        market_groups_dataset: LDS.MarketGroupsLocalizedDataset,
        meta_groups_dataset: LDS.MetaGroupsLocalizedDataset,
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
                eve_type,
                groups_dataset.records,
                categories_dataset.records,
                market_groups_dataset.records,
                meta_groups_dataset.records,
            )
            result.records[normalized_type.key] = normalized_type
        return result


def normalize_eve_type(
    eve_type: PML.EveTypesLocalized,
    groups: dict[int, PML.GroupsLocalized],
    categories: dict[int, PML.CategoriesLocalized],
    market_groups: dict[int, PML.MarketGroupsLocalized],
    meta_groups: dict[int, PML.MetaGroupsLocalized],
) -> NormalizedEveType:
    """Normalize an Eve type using related datasets."""
    group = groups.get(eve_type.groupID) if eve_type.groupID else None
    category = categories.get(group.categoryID) if group else None
    market_group = (
        market_groups.get(eve_type.marketGroupID) if eve_type.marketGroupID else None
    )
    meta_group = meta_groups.get(eve_type.metaGroupID) if eve_type.metaGroupID else None

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
