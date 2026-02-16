"""Lookup for pydantic models corresponding to SDE datasets."""

from pydantic import BaseModel

import eve_static_data.models.raw_pydantic as PM
from eve_static_data.models.sde_datasets import SdeDatasets

DatasetPydanticModels: dict[SdeDatasets, type[BaseModel]] = {
    SdeDatasets.AGENTS_IN_SPACE: PM.AgentsInSpace,
    SdeDatasets.AGENT_TYPES: PM.AgentTypes,
    SdeDatasets.ANCESTRIES: PM.Ancestries,
    SdeDatasets.BLOODLINES: PM.Bloodlines,
    # Add more mappings here for other datasets.
}


def dataset_pydantic_model_lookup(dataset: SdeDatasets) -> type[BaseModel]:
    """Lookup the pydantic model for a given dataset."""
    if dataset not in DatasetPydanticModels:
        raise ValueError(f"No pydantic model found for dataset: {dataset}")
    return DatasetPydanticModels[dataset]
