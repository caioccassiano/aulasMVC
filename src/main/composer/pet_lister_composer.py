from src.models.sqlite.settings.connection import db_connection_handler
from src.models.sqlite.repositories.pets_repositoy import PetsRepository
from src.controllers.pet_lister_controller import PetsLister
from src.views.pet_lister_view import PetsListerView

def pet_lister_composer():
  model = PetsRepository(db_connection=db_connection_handler)
  controller = PetsLister(pets_repository=model)
  view = PetsListerView(controller=controller)

  return view


