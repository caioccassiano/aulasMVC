from src.models.sqlite.interfaces.pets_repository import PetsRepositoryInterface
from .interfaces.pet_deleter_controller_interface import PetDeleterControllerInterface


class PetDeleterController(PetDeleterControllerInterface):
  def __init__(self, pets_repository: PetsRepositoryInterface):
    self.__pets_repository = pets_repository

  def delete_pets(self, name: str)-> None:
    self.__pets_repository.delete_pets(name)

