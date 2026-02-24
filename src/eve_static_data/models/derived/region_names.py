from typing import Self

from eve_static_data.models.datasets import localized_pydantic as LDS
from eve_static_data.models.datasets.sde_dataset_base import LocalizedSdeDataset


class RegionNames(LocalizedSdeDataset):
    data: dict[int, str]

    @classmethod
    def from_datasets(cls, map_regions_dataset: LDS.MapRegionsLocalizedDataset) -> Self:
        """Create a RegionNames instance from the MapRegionsLocalizedDataset."""
        return cls(
            localized=map_regions_dataset.localized,
            build_number=map_regions_dataset.build_number,
            release_date=map_regions_dataset.release_date,
            data={
                region.key: region.name for region in map_regions_dataset.data.values()
            },
        )
