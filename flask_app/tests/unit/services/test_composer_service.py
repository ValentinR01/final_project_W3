from unittest.mock import patch
import pytest
from services.composer import create_composer, get_composer_by_id, \
    get_all_composers, update_composer
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


def test_create_composer(mock_composer):
    data = {'fullname': 'Robert Schumann'}

    # Test creation of a new composer
    with patch('models.composer.Composer.get_by', return_value=False):
        with patch('models.composer.Composer.create', return_value=True):
            response = create_composer(data)
            assert response == ({'message':
                                'The composer has been successfully created'},
                                200)

    # Test creation of an existing composer
    with patch('models.composer.Composer.get_by', return_value=mock_composer):
        response = create_composer(data)
        assert response == ({'message': 'composer already exists'}, 409)


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


def test_update_composer(mock_composer):
    data = {'fullname': 'Alexandre'}

    # Test with empty data
    response = update_composer(data={}, composer_id=1)
    assert response == ({'message': 'Missing parameters'}, 400)

    # Test with non-existing speaker
    with patch('models.composer.Composer.get_by', return_value=False):
        response = update_composer(data=data, composer_id=99999)
        assert response == ({'message': 'Entity not found'}, 404)

    # Test with an existing speaker
    with patch('models.composer.Composer.get_by', return_value=mock_composer):
        with patch('models.composer.Composer.update', return_value=True):
            response = update_composer(data=data, composer_id=1)
            assert response == ({'message':
                                'The composer has been successfully updated'},
                                200)
