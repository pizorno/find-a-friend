from find_a_friend.controllers.pet_lister_controller import PetListerController
from find_a_friend.models.sqlite.entities.pets import PetsTable


class MockPetsRepository:
    def list_pets(self):
        return [
            PetsTable(name='Fluffy', type='cat', id=4),
            PetsTable(name='Buddy', type='dog', id=47),
        ]


def test_list_pets():
    controller = PetListerController(MockPetsRepository())
    response = controller.find()
    expected_response = {
        'data': {
            'type': 'Pets',
            'count': 2,
            'attributes': [
                {'name': 'Fluffy', 'id': 4},
                {'name': 'Buddy', 'id': 47},
            ],
        }
    }

    assert response == expected_response
