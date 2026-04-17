"""Testing the various possibilities with the dataclass type adaptor."""

import json
from collections.abc import Iterator
from dataclasses import dataclass
from pathlib import Path

from pydantic import BaseModel, ConfigDict, Field, TypeAdapter
from pydantic.dataclasses import dataclass as pydantic_dataclass

test_data = [
    '{"_key": 3018347, "dungeonID": 416, "solarSystemID": 30000165, "spawnPointID": 4239, "typeID": 20536}',
    '{"_key": 3018350, "dungeonID": 423, "solarSystemID": 30000166, "spawnPointID": 4280, "typeID": 20643}',
    '{"_key": 3018351, "dungeonID": 423, "solarSystemID": 30000166, "spawnPointID": 4280, "typeID": 20644}',
    '{"_key": 3018352, "dungeonID": 423, "solarSystemID": 30000166, "spawnPointID": 4280, "typeID": 20645}',
]

model_config = ConfigDict(serialize_by_alias=True)


@dataclass(slots=True, kw_only=True)
class AgentsInSpace_2:
    """Model for the agentsInSpace.jsonl SDE file."""

    key: int
    dungeonID: int
    solarSystemID: int
    spawnPointID: int
    typeID: int


@pydantic_dataclass(kw_only=True, config=model_config)
class AgentsInSpace(AgentsInSpace_2):
    """Model for the agentsInSpace.jsonl SDE file."""

    key: int = Field(..., alias="_key")


@dataclass(slots=True, kw_only=True)
class AgentsInSpace_3:
    """Model for the agentsInSpace.jsonl SDE file."""

    _key: int
    dungeonID: int
    solarSystemID: int
    spawnPointID: int
    typeID: int


class AgentsInSpace_4(BaseModel):
    """Model for the agentsInSpace.jsonl SDE file."""

    _key: int
    dungeonID: int
    solarSystemID: int
    spawnPointID: int
    typeID: int


def test_dataclass_type_adaptor():
    """Test that the dataclass type adaptor can convert JSONL lines into dataclass instances."""
    adapter = TypeAdapter(AgentsInSpace)
    for line in test_data:
        index = test_data.index(line)
        _ = index
        result = adapter.validate_json(line)
        json_result = json.loads(line)
        assert isinstance(result, AgentsInSpace)
        assert result.key == json_result["_key"]

        dumped_result = adapter.dump_json(result)
        jsoned_dumped_result = json.loads(dumped_result)
        assert jsoned_dumped_result == json_result


def read_records_from_file[T](
    file_path: Path, model: type[T]
) -> Iterator[tuple[int, T]]:
    """Read records from a JSONL file and convert them to dataclass instances."""
    adapter = TypeAdapter(model)

    with file_path.open() as f:
        for index, line in enumerate(f):
            result: T = adapter.validate_json(line)
            if result is not None:
                yield index, result


def test_read_from_file(test_output_dir: Path):
    """Test that the dataclass type adaptor can read from a file."""
    test_file = test_output_dir / "agents_in_space.jsonl"
    with test_file.open("w") as f:
        for line in test_data:
            f.write(line + "\n")

    records = list(read_records_from_file(test_file, AgentsInSpace))
    assert len(records) == len(test_data)
    for index, record in records:
        assert isinstance(record, AgentsInSpace)
        assert isinstance(record, AgentsInSpace_2)
        json_result = json.loads(test_data[index])
        assert record.key == json_result["_key"]


def test_roundtrip_with_underscore_key():
    """Test that the dataclass type adaptor can round-trip with an underscore key."""
    adapter = TypeAdapter(AgentsInSpace_3)
    for line in test_data:
        index = test_data.index(line)
        _ = index
        result = adapter.validate_json(line)
        assert isinstance(result, AgentsInSpace_3)

        dumped_result = adapter.dump_json(result)
        jsoned_dumped_result = json.loads(dumped_result)
        json_result = json.loads(line)
        assert jsoned_dumped_result == json_result


# def test_base_model_with_underscore_key():
#     """Test that the dataclass type adaptor can handle a BaseModel with an underscore key."""

#     for line in test_data:
#         index = test_data.index(line)
#         result = AgentsInSpace_4.model_validate_json(line)
#         assert isinstance(result, AgentsInSpace_4)

#         dumped_result = AgentsInSpace_4.model_dump_json(result)
#         jsoned_dumped_result = json.loads(dumped_result)
#         json_result = json.loads(line)
#         assert jsoned_dumped_result == json_result
