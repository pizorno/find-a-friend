import pytest

from find_a_friend.models.sqlite.repositories.pets_repository import (
    PetsRepository,
)
from find_a_friend.models.sqlite.settings.connection import (
    db_connection_handler,
)

db_connection_handler.connect_to_db()


@pytest.mark.skip(reason='Interação com o banco')
def test_list_pets():
    repo = PetsRepository(db_connection_handler)
    response = repo.list_pets()
    print(response)


@pytest.mark.skip(reason='Interação com o banco')
def test_delete_pet():
    name = 'belinha'
    repo = PetsRepository(db_connection_handler)
    repo.delete_pets(name)
