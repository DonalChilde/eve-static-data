"""Tests to prove behavior of pydantic validation of TypedDicts."""

# ruff: noqa: D103
from typing import Any, NotRequired, TypedDict

import pytest
from pydantic import TypeAdapter, ValidationError


class AgentsInSpace(TypedDict):
    _key: int
    dungeonID: int
    solarSystemID: int
    spawnPointID: int
    typeID: int


class Blueprints_Products(TypedDict):
    typeID: int
    quantity: int
    probability: NotRequired[float]


def test_dash_key():
    adapter = TypeAdapter(AgentsInSpace)
    sample_data: dict[str, Any] = {
        "_key": 1,
        "dungeonID": 100,
        "solarSystemID": 200,
        "spawnPointID": 300,
        "typeID": 400,
    }
    validated_data = adapter.validate_python(sample_data)
    assert validated_data["_key"] == 1
    assert validated_data["dungeonID"] == 100
    assert validated_data["solarSystemID"] == 200
    assert validated_data["spawnPointID"] == 300
    assert validated_data["typeID"] == 400


def test_wrong_type():
    adapter = TypeAdapter(AgentsInSpace)
    sample_data: dict[str, Any] = {
        "_key": list(),  # wrong type
        "dungeonID": 100,
        "solarSystemID": 200,
        "spawnPointID": 300,
        "typeID": 400,
    }
    with pytest.raises(ValidationError):
        validated_data = adapter.validate_python(sample_data)
        _ = validated_data


def test_extra_key():
    adapter = TypeAdapter(AgentsInSpace)
    sample_data: dict[str, Any] = {
        "_key": 1,
        "dungeonID": 100,
        "solarSystemID": 200,
        "spawnPointID": 300,
        "typeID": 400,
        "fooo": "bar",  # extra key
    }
    with pytest.raises(ValidationError):
        validated_data = adapter.validate_python(sample_data, extra="forbid")
        _ = validated_data


def test_not_required_present():
    adapter = TypeAdapter(Blueprints_Products)
    sample_data: dict[str, Any] = {
        "typeID": 500,
        "quantity": 10,
        "probability": 0.75,
    }
    validated_data = adapter.validate_python(sample_data)
    assert validated_data["typeID"] == 500
    assert validated_data["quantity"] == 10
    assert validated_data["probability"] == 0.75  # pyright: ignore[reportTypedDictNotRequiredAccess]


def test_not_required_missing():
    adapter = TypeAdapter(Blueprints_Products)
    sample_data: dict[str, Any] = {
        "typeID": 500,
        "quantity": 10,
        # "probability" is missing
    }
    validated_data = adapter.validate_python(sample_data)
    assert validated_data["typeID"] == 500
    assert validated_data["quantity"] == 10
    assert "probability" not in validated_data
