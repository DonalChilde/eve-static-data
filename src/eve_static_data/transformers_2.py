import json
import logging
from dataclasses import dataclass
from typing import Any

from pydantic import ValidationError

from eve_static_data.helpers.jsonl_reader import BASE_MODELS, PydanticTransformer
from eve_static_data.models.type_defs import Lang, LocalizedString

logger = logging.getLogger(__name__)


@dataclass(slots=True)
class ModelValidationErrorRecord:
    model: str
    line_number: int
    data: str
    error_messages: list[str]


def is_published_false(text: str) -> bool:
    """Check if the text contains "published": false.

    This is used to identify records that are not published.
    Unpublished records fail validation more often.
    """
    return '"published": false' in text


class ValidModels(PydanticTransformer[BASE_MODELS]):
    """A transformer that validates the models and records any validation errors.

    This transformer checks if the record is not published and records that information.
    It also catches any validation errors and records them in a dictionary.
    """

    def __init__(self, model: type[BASE_MODELS], only_published: bool = True):
        """Initialize the class."""
        super().__init__(model)
        self.validation_errors: dict[int, ModelValidationErrorRecord] = {}
        self.line_record_not_published: set[int] = set()
        self.only_published = only_published

    def __call__(self, value: tuple[int, str]) -> tuple[int, BASE_MODELS | None]:
        """Transform an indexed string into a pydantic BaseModel instance, and record any validation errors."""
        return super().__call__(value)

    def _inspect_string(self, index: int, text: str) -> str:
        """Inspect the string before model creation.

        Check if the record is not published and record that information.
        """
        if is_published_false(text):
            self.line_record_not_published.add(index)
        return text

    def _text_to_model(self, index: int, text: str) -> BASE_MODELS | None:
        """Convert the text to a model instance."""
        if self.only_published and index in self.line_record_not_published:
            return None
        try:
            return self.model.model_validate_json(text)
        except ValidationError as e:
            self.validation_errors[index] = ModelValidationErrorRecord(
                model=self.model.__name__,
                line_number=index,
                data=text,
                error_messages=[err["msg"] for err in e.errors()],
            )
            return None


def localize_string_dict(string_dict: LocalizedString | None, lang: Lang = "en") -> str:
    """Extract the localized string from a LocalizedString.

    Args:
        string_dict: The LocalizedString to extract from.
        lang: The language code to extract (default is "en" for English).

    Returns:
        The localized string for the specified language, OR:
        - "TRANSLATIONS_NOT_PRESENT" if the input string_dict is None (indicating that the translations are not present in the dataset).
        - "NOT_TRANSLATED" if the specified language is not found in the string_dict (indicating that the translation for that language is not provided).
    """
    if string_dict is None:
        logger.warning(
            "Localized string dictionary is None, indicating that translations are not present in the dataset."
        )
        return "TRANSLATIONS_NOT_PRESENT"
    if lang not in string_dict:
        logger.warning(
            f"Localized string for '{lang=}' not found. Available languages: {list(string_dict.keys())}"
        )
        return "NOT_TRANSLATED"
    return string_dict[lang]


class LocalizationTransformer(PydanticTransformer[BASE_MODELS]):
    def __init__(
        self,
        model: type[BASE_MODELS],
        localized_fields: list[str],
        only_published: bool = True,
        lang: Lang = "en",
    ):
        """A transformer that localizes the string fields in the model before validation.

        Does not support nested localization (i.e. localized fields that are themselves
        dictionaries containing localized strings).

        Args:
            model: The Pydantic model class to use for validation.
            localized_fields: A list of field names in the model that should be localized.
            lang: The language code to use for localization (default is "en" for English).
            only_published: Whether to only include published records (default is True).
        """
        super().__init__(model)
        self.localized_fields = localized_fields
        self.lang: Lang = lang
        self.only_published = only_published
        self.validation_errors: dict[int, ModelValidationErrorRecord] = {}
        self.line_record_not_published: set[int] = set()

    def _inspect_string(self, index: int, text: str) -> str:
        """Inspect the string before model creation.

        Check if the record is not published and record that information.
        """
        if is_published_false(text):
            self.line_record_not_published.add(index)
        return text

    def _text_to_model(self, index: int, text: str) -> BASE_MODELS | None:
        """Convert the text to a model instance, after localizing any specified fields."""
        if self.only_published and index in self.line_record_not_published:
            return None
        json_dict = self._transform_dict(index, text)
        return self.model.model_validate(json_dict)

    def _transform_dict(self, index: int, text: str) -> dict[str, Any]:
        """Convert the text to a dictionary, after localizing any specified fields."""
        json_dict = json.loads(text)
        for field in self.localized_fields:
            field_dict = json_dict.get(field)
            localized_field = localize_string_dict(field_dict, self.lang)
            json_dict[field] = localized_field
        return json_dict
