"""Factory methods for creating localized Pydantic models from SDE records."""

import logging
from collections.abc import Iterable

from eve_static_data.access.sde_reader import SdeReader
from eve_static_data.models import sde_pydantic_localized as PML
from eve_static_data.models import sde_typeddict as TDM
from eve_static_data.models.sde_dataset_files import SdeDatasetFiles

logger = logging.getLogger(__name__)


# TODO split out to helper module
def localize_string_dict(
    string_dict: TDM.LocalizedString | None, localized: str = "en"
) -> str:
    """Extract the localized string from a LocalizedString.

    Args:
        string_dict: The LocalizedString to extract from.
        localized: The language code to extract (default is "en" for English).

    Returns:
        The localized string or an empty string if the language code is not found or if the input is None.
    """
    if string_dict is None:
        return ""
    if localized not in string_dict:
        logger.warning(
            f"Localized string for '{localized}' not found. Available languages: {list(string_dict.keys())}"
        )
        return ""
    return string_dict.get(localized, "")


# TODO decide wether to split out object translation from class method or not.


# if split, then needs dataset factory module as well.
def ancestries(
    reader: SdeReader, file_name: str | None = None, localized: str = "en"
) -> Iterable[PML.AncestriesLocalized]:
    """Yield AncestriesLocalized instances from SDE records."""
    for record, metadata in reader.records(
        SdeDatasetFiles.ANCESTRIES, file_name=file_name
    ):
        record["name"] = localize_string_dict(record.get("name"), localized)
        record["description"] = localize_string_dict(
            record.get("description"), localized
        )
        yield PML.AncestriesLocalized.from_sde(
            record, metadata=metadata, localized=localized
        )
