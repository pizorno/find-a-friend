from abc import ABC, abstractmethod

from find_a_friend.models.sqlite.entities.pets import PetsTable


class PetsRepositoryInterface(ABC):
    @abstractmethod
    def list_pets(self) -> list[PetsTable]:
        pass

    @abstractmethod
    def delete_pets(self, name: str) -> None:
        pass
