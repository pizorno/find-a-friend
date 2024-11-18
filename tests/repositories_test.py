from find_a_friend.models.sqlite.repositories.pets_repository import (
    PetsRepository,
)
from find_a_friend.models.sqlite.settings.connection import (
    db_connection_handler,
)

db_connection_handler.connect_to_db()


def test_list_pets():
    repo = PetsRepository(db_connection_handler)
    response = repo.list_pets()
    print(response)