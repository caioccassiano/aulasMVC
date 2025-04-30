from src.controllers.interfaces.pet_lister_controller_interface import PetsListerInterface
from .interfaces.view_interface import ViewInterface
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse

class PetsListerView(ViewInterface):
  def __init__(self, controller: PetsListerInterface)-> None:
    self.__controller = controller
    
  def handle(self, http_request: HttpRequest)-> HttpResponse:
    body_response = self.__controller.lister()
    return HttpResponse(status_code=200, body=body_response)
  

