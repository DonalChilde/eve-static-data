# from typing import Self

# from eve_static_data.models.pydantic.datasets import SdeDataset, TypeDogmaDataset
# from eve_static_data.models.pydantic.localized_datasets import EveTypesLocalizedDataset


# class TypesMetaLevelsDataset(SdeDataset):
#     """A dataset of type_ids to meta level."""

#     records: dict[int, int]

#     @classmethod
#     def from_datasets(
#         cls,
#         type_dogma_dataset: TypeDogmaDataset,
#         eve_types_dataset: EveTypesLocalizedDataset,
#     ) -> Self:
#         """Create a PublishedBlueprints instance from localized datasets."""
#         result = cls(
#             build_number=eve_types_dataset.build_number,
#             release_date=eve_types_dataset.release_date,
#             records={},
#         )
#         for eve_type in eve_types_dataset.records.values():
#             if eve_type.published:
#                 type_dogma = type_dogma_dataset.records.get(eve_type.key)
#                 if type_dogma is not None:
#                     for dogma_attr in type_dogma.dogmaAttributes:
#                         # Dogma Attribute 633 is the meta level
#                         if dogma_attr.attributeID == 633:
#                             result.records[eve_type.key] = int(dogma_attr.value)
#                             break
#         return result
