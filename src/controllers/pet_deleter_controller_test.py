from .pet_deleter_controller import PetDeleterController

def test_delete_pets(mocker):
  mock_repository = mocker.Mock()
  controller = PetDeleterController(mock_repository)
  controller.delete_pets("amiguinho")

  mock_repository.delete_pets.assert_called_once_with("amiguinho")
