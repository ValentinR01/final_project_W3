from unittest.mock import patch
import pytest
from services.composer import register_service, get_composer_by_id, \
    get_all_composers
from models.composer import Composer


@pytest.fixture
def mock_composer():
    return Composer(
        fullname="Robert Schumann",
        biography="",
        publishable=0,
        last_update=1689087134,
        composer_parent=None,
        language_id=None
    )


@pytest.fixture
def mock_composer_list(mock_composer) -> list:
    return [mock_composer, mock_composer]


def test_register_service(mock_composer):
    data = {'fullname': 'Robert Schumann'}

    # Test creation of a new composer
    with patch('models.composer.Composer.get_by', return_value=False):
        with patch('models.composer.Composer.create', return_value=True):
            response = register_service(data)
            assert response == ({'message': 'Composer well created'}, 201)

    # Test creation of an existing composer
    with patch('models.composer.Composer.get_by', return_value=mock_composer):
        response = register_service(data)
        assert response == ({'message': 'Composer already exists'}, 409)


def test_get_composer_by_id(mock_composer):
    with patch('models.composer.Composer.get_by', return_value=mock_composer):
        response = get_composer_by_id(1)
        assert response == (mock_composer, 200)

    #  Test with a not existing composer
    with patch('models.composer.Composer.get_by', return_value=None):
        response = get_composer_by_id(1000)
        assert response == ({'message': 'Composer not found'}, 404)


def test_get_all_composers(mock_composer_list):
    # Test with a list of composers
    with patch('models.composer.Composer.get_all',
               return_value=mock_composer_list):
        composer_list = get_all_composers()
        assert composer_list == ({'composers': mock_composer_list}, 200)

    # Test with an empty list of speakers
    with patch('models.composer.Composer.get_all', return_value=[]):
        composer_list = get_all_composers()
        assert composer_list == ({'composers': []}, 200)
