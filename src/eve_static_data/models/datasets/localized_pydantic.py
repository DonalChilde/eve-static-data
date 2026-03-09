# """An incomplete set of models for localized SDE datasets.

# More models to be added as needed for use.
# """

# from typing import Self

# from eve_static_data.access.sde_reader import SdeReader
# from eve_static_data.models.datasets.sde_dataset_base import LocalizedSdeDataset
# from eve_static_data.models.datasets.sde_dataset_files import SdeDatasetFiles
# from eve_static_data.models.records import sde_pydantic_localized as PML


# class AncestriesLocalizedDataset(LocalizedSdeDataset):
#     data: dict[int, PML.AncestriesLocalized]

#     @classmethod
#     def from_sde(
#         cls, reader: SdeReader, file_name: str | None = None, localized: str = "en"
#     ) -> Self:
#         """Create an AncestriesLocalizedDataset instance from SDE records."""
#         if reader.build_number is None or reader.release_date is None:
#             raise ValueError("SDE Reader must have build number and release date.")
#         result = cls(
#             localized=localized,
#             build_number=reader.build_number,
#             release_date=reader.release_date,
#             data={},
#         )
#         for record, metadata in reader.records(
#             SdeDatasetFiles.ANCESTRIES, file_name=file_name
#         ):
#             item = PML.AncestriesLocalized.from_sde(
#                 record, metadata=metadata, localized=localized
#             )
#             result.data[item.key] = item
#         return result


# class CategoriesLocalizedDataset(LocalizedSdeDataset):
#     data: dict[int, PML.CategoriesLocalized]

#     @classmethod
#     def from_sde(
#         cls, reader: SdeReader, file_name: str | None = None, localized: str = "en"
#     ) -> Self:
#         """Create a CategoriesLocalizedDataset instance from SDE records."""
#         if reader.build_number is None or reader.release_date is None:
#             raise ValueError("SDE Reader must have build number and release date.")
#         result = cls(
#             localized=localized,
#             build_number=reader.build_number,
#             release_date=reader.release_date,
#             data={},
#         )
#         for record, metadata in reader.records(
#             SdeDatasetFiles.CATEGORIES, file_name=file_name
#         ):
#             item = PML.CategoriesLocalized.from_sde(
#                 record, metadata=metadata, localized=localized
#             )
#             result.data[item.key] = item
#         return result


# class GroupsLocalizedDataset(LocalizedSdeDataset):
#     data: dict[int, PML.GroupsLocalized]

#     @classmethod
#     def from_sde(
#         cls, reader: SdeReader, file_name: str | None = None, localized: str = "en"
#     ) -> Self:
#         """Create a GroupsLocalizedDataset instance from SDE records."""
#         if reader.build_number is None or reader.release_date is None:
#             raise ValueError("SDE Reader must have build number and release date.")
#         result = cls(
#             localized=localized,
#             build_number=reader.build_number,
#             release_date=reader.release_date,
#             data={},
#         )
#         for record, metadata in reader.records(
#             SdeDatasetFiles.GROUPS, file_name=file_name
#         ):
#             item = PML.GroupsLocalized.from_sde(
#                 record, metadata=metadata, localized=localized
#             )
#             result.data[item.key] = item
#         return result


# class MapRegionsLocalizedDataset(LocalizedSdeDataset):
#     data: dict[int, PML.MapRegionsLocalized]

#     @classmethod
#     def from_sde(
#         cls, reader: SdeReader, file_name: str | None = None, localized: str = "en"
#     ) -> Self:
#         """Create a MapRegionsLocalizedDataset instance from SDE records."""
#         if reader.build_number is None or reader.release_date is None:
#             raise ValueError("SDE Reader must have build number and release date.")
#         result = cls(
#             localized=localized,
#             build_number=reader.build_number,
#             release_date=reader.release_date,
#             data={},
#         )
#         for record, metadata in reader.records(
#             SdeDatasetFiles.MAP_REGIONS, file_name=file_name
#         ):
#             item = PML.MapRegionsLocalized.from_sde(
#                 record, metadata=metadata, localized=localized
#             )
#             result.data[item.key] = item
#         return result


# class MapSolarSystemsLocalizedDataset(LocalizedSdeDataset):
#     data: dict[int, PML.MapSolarSystemsLocalized]

#     @classmethod
#     def from_sde(
#         cls, reader: SdeReader, file_name: str | None = None, localized: str = "en"
#     ) -> Self:
#         """Create a MapSolarSystemsLocalizedDataset instance from SDE records."""
#         if reader.build_number is None or reader.release_date is None:
#             raise ValueError("SDE Reader must have build number and release date.")
#         result = cls(
#             localized=localized,
#             build_number=reader.build_number,
#             release_date=reader.release_date,
#             data={},
#         )
#         for record, metadata in reader.records(
#             SdeDatasetFiles.MAP_SOLAR_SYSTEMS, file_name=file_name
#         ):
#             item = PML.MapSolarSystemsLocalized.from_sde(
#                 record, metadata=metadata, localized=localized
#             )
#             result.data[item.key] = item
#         return result


# class MarketGroupsLocalizedDataset(LocalizedSdeDataset):
#     data: dict[int, PML.MarketGroupsLocalized]

#     @classmethod
#     def from_sde(
#         cls, reader: SdeReader, file_name: str | None = None, localized: str = "en"
#     ) -> Self:
#         """Create a MarketGroupsLocalizedDataset instance from SDE records."""
#         if reader.build_number is None or reader.release_date is None:
#             raise ValueError("SDE Reader must have build number and release date.")
#         result = cls(
#             localized=localized,
#             build_number=reader.build_number,
#             release_date=reader.release_date,
#             data={},
#         )
#         for record, metadata in reader.records(
#             SdeDatasetFiles.MARKET_GROUPS, file_name=file_name
#         ):
#             item = PML.MarketGroupsLocalized.from_sde(
#                 record, metadata=metadata, localized=localized
#             )
#             result.data[item.key] = item
#         return result


# class MetaGroupsLocalizedDataset(LocalizedSdeDataset):
#     data: dict[int, PML.MetaGroupsLocalized]

#     @classmethod
#     def from_sde(
#         cls, reader: SdeReader, file_name: str | None = None, localized: str = "en"
#     ) -> Self:
#         """Create a MetaGroupsLocalizedDataset instance from SDE records."""
#         if reader.build_number is None or reader.release_date is None:
#             raise ValueError("SDE Reader must have build number and release date.")
#         result = cls(
#             localized=localized,
#             build_number=reader.build_number,
#             release_date=reader.release_date,
#             data={},
#         )
#         for record, metadata in reader.records(
#             SdeDatasetFiles.META_GROUPS, file_name=file_name
#         ):
#             item = PML.MetaGroupsLocalized.from_sde(
#                 record, metadata=metadata, localized=localized
#             )
#             result.data[item.key] = item
#         return result


# class EveTypesLocalizedDataset(LocalizedSdeDataset):
#     data: dict[int, PML.EveTypesLocalized]

#     @classmethod
#     def from_sde(
#         cls, reader: SdeReader, file_name: str | None = None, localized: str = "en"
#     ) -> Self:
#         """Create an EveTypesLocalizedDataset instance from SDE records."""
#         if reader.build_number is None or reader.release_date is None:
#             raise ValueError("SDE Reader must have build number and release date.")
#         result = cls(
#             localized=localized,
#             build_number=reader.build_number,
#             release_date=reader.release_date,
#             data={},
#         )
#         for record, metadata in reader.records(
#             SdeDatasetFiles.TYPES, file_name=file_name
#         ):
#             item = PML.EveTypesLocalized.from_sde(
#                 record, metadata=metadata, localized=localized
#             )
#             result.data[item.key] = item
#         return result
