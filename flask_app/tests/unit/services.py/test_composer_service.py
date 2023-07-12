from unittest.mock import patch
import pytest
from services.composer import register_service
from models.composer import Composer


@pytest.fixture
def composer():
    return Composer(
        fullname = "Robert Schumann",
        biography = "",
        publishable = 0,
        last_update = 1689087134,
        composer_parent = None,
        language_id = None
    )

def test_register_service(composer):
    data = {'fullname': 'Robert Schumann'}

    # Test creation of a new speaker
    with patch('models.composer.Composer.get_by', return_value=False):
        with patch('models.composer.Composer.create', return_value=True):
            response = register_service(data)
            assert response == ({'message': 'Composer well created'}, 201)

    # Test creation of an existing speaker
    with patch('models.composer.Composer.get_by', return_value=composer):
        response = register_service(data)
        assert response == ({'message': 'Composer already exists'}, 409)




