from find_a_friend.controllers.interfaces.pet_deleter_controller import (
    PetDeleterControllerInterface,
)
from find_a_friend.models.sqlite.interfaces.pets_repository import (
    PetsRepositoryInterface,
)


class PetDeleterController(PetDeleterControllerInterface):
    def __init__(self, pet_repository: PetsRepositoryInterface) -> None:
        self.__pet_repository = pet_repository

    def delete(self, name: str) -> None:
        self.__pet_repository.delete_pets(name)
