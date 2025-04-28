from .person_creator_controller import PersonCreatorController
import pytest


class MockCreator:
  def insert_people(self, first_name:str, last_name:str, age:int, pet_id:int) -> None:
    pass


def test_create():
  person_info = {
    "first_name": "Caio",
    "last_name": "Cassiano",
    "age": 26,
    "pet_id": 231
  }

  controller = PersonCreatorController(MockCreator())
  response = controller.create(person_info=person_info)
  
  assert response["data"]["type"] == "Person"
  assert response["data"]["count"] == 1
  assert response["data"]["attributes"] == person_info



def test_creator_with_error():
  person_info = {
    "first_name": "Caio123",
    "last_name": "Cassiano",
    "age": 26,
    "pet_id": 231
  }

  controller = PersonCreatorController(MockCreator())

  with pytest.raises(Exception):
    controller.create(person_info=person_info)
  
