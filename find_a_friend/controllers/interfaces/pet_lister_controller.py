from abc import ABC, abstractmethod


class PetListerControllerInterface(ABC):
    @abstractmethod
    def find(self) -> dict:
        pass
