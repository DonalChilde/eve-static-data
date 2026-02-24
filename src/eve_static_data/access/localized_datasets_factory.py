"""Factory methods for creating localized Dataset models from SDE records.

Each model corresponds to a dataset in the SDE, and the factory methods handle the
loading and localization of the data.
"""

from eve_static_data.access import localized_pydantic_factory as LPF
from eve_static_data.access.sde_reader import SdeReader
from eve_static_data.models import exported_localized_datasets as LDS
from eve_static_data.models import sde_pydantic_localized as PML


def ancestries_dataset(
    reader: SdeReader, file_name: str | None = None
) -> LDS.AncestriesDataset:
    """Create a localized AncestriesDataset instance from SDE records."""
    if reader.build_number is None or reader.release_date is None:
        raise ValueError("SDE Reader must have build number and release date.")
    result = LDS.AncestriesDataset(
        build_number=reader.build_number,
        release_date=reader.release_date,
        data={},
    )
    for record in LPF.ancestries(reader, file_name):
        result.data[record.key] = record
    return result
