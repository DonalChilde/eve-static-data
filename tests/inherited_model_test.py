import json

from eve_static_data.models import sde_pydantic as PM
from eve_static_data.models import sde_pydantic_localized as LM

TestString = '{"_key": 20, "iconID": 0, "name": {"de": "Implantat", "en": "Implant", "es": "Implante", "fr": "Implant", "ja": "インプラント", "ko": "임플란트", "ru": "Имплантат", "zh": "植入体"}, "published": true}'


def test_localized_model():
    raw_dict = json.loads(TestString)
    parent_model = PM.Categories.model_validate(raw_dict)
    assert parent_model.key == 20
    localized_model = LM.CategoriesLocalized.from_sde(raw_dict)
    assert localized_model.key == 20
    assert localized_model.iconID == 0
    assert localized_model.name == "Implant"
    localized_model_dump = localized_model.model_dump(mode="json")
    assert localized_model_dump["_key"] == 20
    assert localized_model_dump["iconID"] == 0
    assert localized_model_dump["name"] == "Implant"
    localized_loaded = LM.CategoriesLocalized.model_validate(localized_model_dump)
    assert localized_loaded.key == 20
    assert localized_loaded.iconID == 0
    assert localized_loaded.name == "Implant"
    assert localized_loaded == localized_model
