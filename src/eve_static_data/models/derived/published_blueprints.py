# from typing import Self

# from eve_static_data.models.pydantic.datasets import BlueprintsDataset, SdeDataset
# from eve_static_data.models.pydantic.localized_datasets import EveTypesLocalizedDataset
# from eve_static_data.models.pydantic.records import Blueprints


# class PublishedBlueprintsDataset(SdeDataset):
#     """A dataset of blueprints that are published in the SDE."""

#     records: dict[int, Blueprints]

#     @classmethod
#     def from_datasets(
#         cls,
#         blueprints_dataset: BlueprintsDataset,
#         eve_types_dataset: EveTypesLocalizedDataset,
#     ) -> Self:
#         """Create a PublishedBlueprints instance from localized datasets."""
#         result = cls(
#             build_number=blueprints_dataset.build_number,
#             release_date=blueprints_dataset.release_date,
#             records={},
#         )
#         for blueprint in blueprints_dataset.records.values():
#             eve_type = eve_types_dataset.records.get(blueprint.blueprintTypeID)
#             if (
#                 eve_type is None
#             ):  # If the EveTypesLocalizedDataset was loaded only_published, some
#                 # blueprints may not have a corresponding eve type and should be skipped.
#                 continue
#             if not eve_type.published:
#                 continue
#             result.records[blueprint.key] = blueprint
#         return result
