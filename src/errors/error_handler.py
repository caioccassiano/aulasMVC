from src.views.http_types.http_response import HttpResponse
from src.errors.errors_type.http_badrequest_error import BadRequestError
from src.errors.errors_type.http_notfound_error import NotFoundError
from src.errors.errors_type.http_unprocessable_entity_error import UnprocessableEntityError


def error_handler(error: Exception) -> HttpResponse:
  if isinstance(error, (BadRequestError,NotFoundError, UnprocessableEntityError)):
    return HttpResponse(
      status_code = error.status_code,
      body={
        "errors": [{
          "title": error.name,
          "detail": error.message
        }]
      }
    )
  return HttpResponse(
    status_code=500,
    body={
      "errors": [{
        "title": "Server Error",
        "detail": str(error)

      }]
    }
  )