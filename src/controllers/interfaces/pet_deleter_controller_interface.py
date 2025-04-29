from abc import ABC, abstractmethod

class PetDeleterControllerInterface(ABC):

  @abstractmethod
  def delete_pets(self, name: str)-> None:
   pass
