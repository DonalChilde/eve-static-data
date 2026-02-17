"""Lookup for pydantic models corresponding to SDE datasets."""

from typing import TypedDict

from pydantic import BaseModel

import eve_static_data.models.raw_pydantic as PM
import eve_static_data.models.raw_td as TDM
from eve_static_data.models.sde_datasets import SdeDatasets

DatasetPydanticModels: dict[SdeDatasets, type[BaseModel]] = {
    SdeDatasets.AGENTS_IN_SPACE: PM.AgentsInSpace,
    SdeDatasets.AGENT_TYPES: PM.AgentTypes,
    SdeDatasets.ANCESTRIES: PM.Ancestries,
    SdeDatasets.BLOODLINES: PM.Bloodlines,
    # Add more mappings here for other datasets.
}
DatasetTDModels: dict[SdeDatasets, type[TypedDict]] = {
    SdeDatasets.AGENTS_IN_SPACE: TDM.AgentsInSpace,
    SdeDatasets.AGENT_TYPES: TDM.AgentTypes,
    SdeDatasets.ANCESTRIES: TDM.Ancestries,
    SdeDatasets.BLOODLINES: TDM.Bloodlines,
    SdeDatasets.CATEGORIES: TDM.Categories,
    # TODO complete this mapping for all datasets
}


def dataset_pydantic_model_lookup(dataset: SdeDatasets) -> type[BaseModel]:
    """Lookup the pydantic model for a given dataset."""
    if dataset not in DatasetPydanticModels:
        raise ValueError(f"No pydantic model found for dataset: {dataset}")
    return DatasetPydanticModels[dataset]


def dataset_td_model_lookup(dataset: SdeDatasets) -> type[TypedDict]:
    """Lookup the TypedDict model for a given dataset."""
    # TODO see if this code actually works, re the use with TypeAdaptor for validation
    if dataset not in DatasetTDModels:
        raise ValueError(f"No TypedDict model found for dataset: {dataset}")
    return DatasetTDModels[dataset]
