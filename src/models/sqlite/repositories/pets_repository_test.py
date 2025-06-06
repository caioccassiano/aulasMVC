from unittest import mock
from mock_alchemy.mocking import UnifiedAlchemyMagicMock
from src.models.sqlite.entities.pets import PetsTable
from .pets_repositoy import PetsRepository

class MockConnection:
  def __init__(self):
    self.session = UnifiedAlchemyMagicMock(
      data = [
        (
          [mock.call.query(PetsTable)],
          [
            PetsTable(name="dog", type="dog"),
            PetsTable(name="cat", type = "cat")
          ]
        )
      ]
    )

  def __enter__(self): return self
  def __exit__(self, exc_type, exc_val, exc_tb): pass




def test_list_pets():
  mock_connection = MockConnection()
  repo = PetsRepository(mock_connection)
  response = repo.list_pets()

  mock_connection.session.query.assert_called_once_with(PetsTable)

  assert response[0].name == "dog"


def test_delete_pet():
  mock_connection = MockConnection()
  repo = PetsRepository(mock_connection)
  repo.delete_pets("petName")

  mock_connection.session.query.assert_called_once_with(PetsTable)
  mock_connection.session.filter.assert_called_once_with(PetsTable.name == "petName")
  mock_connection.session.delete.assert_called_once()

   