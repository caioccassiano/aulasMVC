from abc import ABC, abstractmethod

class PetsListerInterface(ABC):

  @abstractmethod
  def lister(self)-> dict:
    pass



