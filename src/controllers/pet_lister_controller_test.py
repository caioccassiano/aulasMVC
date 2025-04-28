from .pet_lister_controller import PetsLister
from src.models.sqlite.entities.pets import PetsTable

class MockPetsRepository:
  def list_pets(self):
    return [
      PetsTable(name="Fluffy",id=4),
      PetsTable(name="Mike", id=41),
    ]
  
def test_list_pets():
  controller = PetsLister(MockPetsRepository())
  response = controller.lister()
  
  expected_response = {
    "data": {
      "type": "Pets",
      "count": 2,
      "attributes": [
        {"name": "Fluffy","id": 4},
        {"name": "Mike","id": 41},
      ]
    }
  }

  assert response == expected_response

