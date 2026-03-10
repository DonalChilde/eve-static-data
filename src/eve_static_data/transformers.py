import logging
from dataclasses import dataclass

from pydantic import BaseModel, ValidationError

from eve_static_data.helpers.pydantic.jsonl_record import (
    BASE_MODELS,
    JsonlRecord,
    TransformBaseModel,
    TransformJsonDict,
)

logger = logging.getLogger(__name__)


@dataclass(slots=True)
class ValidationErrorRecord:
    line_number: int
    data: str
    error_message: str


class ValidModels(TransformBaseModel):
    def transform(
        self, value: tuple[int, str], model: type[BASE_MODELS]
    ) -> BASE_MODELS | None:
        index, text = value
        try:
            return model.model_validate_json(text)
        except ValidationError as e:
            logger.exception(
                "Validation error parsing line %d: %s in class %s",
                index,
                e,
                model.__name__,
            )
            return None
