import pytest

from find_a_friend.models.sqlite.repositories.people_repository import (
    PeopleRepository,
)
from find_a_friend.models.sqlite.repositories.pets_repository import (
    PetsRepository,
)
from find_a_friend.models.sqlite.settings.connection import (
    db_connection_handler,
)

## db_connection_handler.connect_to_db()


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


@pytest.mark.skip(reason='Interação com o banco')
def test_insert_person():
    first_name = 'Test name'
    last_name = 'test last'
    age = 77
    pet_id = 2
    repo = PeopleRepository(db_connection_handler)
    repo.insert_person(first_name, last_name, age, pet_id)


@pytest.mark.skip(reason='Interação com o banco')
def test_get_person():
    person_id = 1
    repo = PeopleRepository(db_connection_handler)
    response = repo.get_person(person_id)
    print()
    print(response)
