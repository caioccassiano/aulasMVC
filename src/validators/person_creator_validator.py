from pydantic import BaseModel, constr, ValidationError
from src.views.http_types.http_request import HttpRequest
from src.errors.errors_type.http_unprocessable_entity_error import UnprocessableEntityError


def person_creator_validator(http_request: HttpRequest) -> None:

  class BodyData(BaseModel):
    first_name: constr(min_length=1)  # type: ignore
    last_name: constr(min_length=1)  # type: ignore
    age: int
    pet_id: int

  try:
    BodyData(**http_request.body)
  except ValidationError as e:
    raise UnprocessableEntityError(e.errors()) from e
  