"""An incomplete set of models for exported SDE data.

More models to be added as needed for use.

Each dataset is exported as a json file with sde build number and release date metadata,
and a data field that contains the actual data records as a dictionary.
"""

from typing import Self

from eve_static_data.access.sde_reader import SdeReader
from eve_static_data.models import sde_pydantic as PM
from eve_static_data.models.sde_dataset_base import SdeDataset
from eve_static_data.models.sde_dataset_files import SdeDatasetFiles


class BlueprintsDataset(SdeDataset):
    data: dict[int, PM.Blueprints]

    @classmethod
    def from_sde(cls, reader: SdeReader, file_name: str | None = None) -> Self:
        """Create a BlueprintsDataset instance from SDE records."""
        if reader.build_number is None or reader.release_date is None:
            raise ValueError("SDE Reader must have build number and release date.")
        result = cls(
            build_number=reader.build_number,
            release_date=reader.release_date,
            data={},
        )
        for record, metadata in reader.records(
            SdeDatasetFiles.BLUEPRINTS, file_name=file_name
        ):
            item = PM.Blueprints.from_sde(record, metadata=metadata)
            result.data[item.key] = item
        return result


class TypeMaterialsDataset(SdeDataset):
    data: dict[int, PM.TypeMaterials]

    @classmethod
    def from_sde(cls, reader: SdeReader, file_name: str | None = None) -> Self:
        """Create a TypeMaterialsDataset instance from SDE records."""
        if reader.build_number is None or reader.release_date is None:
            raise ValueError("SDE Reader must have build number and release date.")
        result = cls(
            build_number=reader.build_number,
            release_date=reader.release_date,
            data={},
        )
        for record, metadata in reader.records(
            SdeDatasetFiles.TYPE_MATERIALS, file_name=file_name
        ):
            item = PM.TypeMaterials.from_sde(record, metadata=metadata)
            result.data[item.key] = item
        return result
