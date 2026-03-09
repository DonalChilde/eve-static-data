"""Region names derived from the MapRegionsLocalizedDataset."""

from typing import Self

from eve_static_data.models.pydantic import localized_datasets as LDS


class RegionNames(LDS.SdeDatasetLocalized):
    records: dict[int, str]

    @classmethod
    def from_datasets(cls, map_regions_dataset: LDS.MapRegionsLocalizedDataset) -> Self:
        """Create a RegionNames instance from the MapRegionsLocalizedDataset."""
        return cls(
            lang=map_regions_dataset.lang,
            build_number=map_regions_dataset.build_number,
            release_date=map_regions_dataset.release_date,
            records={
                region.key: region.name
                for region in map_regions_dataset.records.values()
            },
        )
