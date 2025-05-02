from .person_creator_validator import person_creator_validator

class MockBody:
  def __init__(self, body):
    self.body = body
  

def test_person_creator_validator():
  request = MockBody({
    "first_name": "Caio",
    "last_name": "Cassiano",
    "age": 26,
    "pet_id": 4
  })

  person_creator_validator(request)


