from src.models.sqlite.interfaces.pets_repository import PetsRepositoryInterface
from src.models.sqlite.entities.pets import PetsTable
from .interfaces.pet_lister_controller_interface import PetsListerInterface

class PetsLister(PetsListerInterface):
  def __init__(self, pets_repository: PetsRepositoryInterface)-> None:
    self.__pets_repository = pets_repository
  

  def lister(self)-> dict:
     pets = self.__find_pets_in_db()
     response = self.__format_response(pets)
     return response

     
  

  def __find_pets_in_db(self) -> list[PetsTable]:
    pets = self.__pets_repository.list_pets()
    return pets
  
  def __format_response(self, pets:list[PetsTable]) -> dict:
    formated_list = []
    for pet in pets:
      formated_list.append({ "name": pet.name, "id": pet.id})

    return {
        "data": {
          "type": "Pets",
          "count": len(formated_list),
          "attributes":formated_list
        }
      }

