import pytest
from models.asset import Asset
from unittest.mock import patch
from services.asset import create_asset, get_asset, search_asset
from helpers.etl import transformation

data_asset = {
    "title": "NassLaMenass",
    "music_title": "Music Title",
    "created_by_id": 1,
    "updated_by_id": 1,
    "status_by_domain_id": 1,
    "step_lifecycle_id": 1
}

data_all_assets = \
    {
        'art_description': None,
        'asset_description': None,
        'booking_id': None,
        'captation_id': None,
        'composer_id': None,
        'created_at': None,
        'created_by_id': 1,
        'current_assigned_user_id': None,
        'has_high_priority': False,
        'last_assignment_at': None,
        'link_partitions': None,
        'music_title': 'Music Title',
        'post_prod_id': None,
        'published': False,
        'published_at': None,
        'resumed': None,
        'speaker_id': None,
        'status_by_domain_id': 1,
        'step_lifecycle_id': 1,
        'student_fullname': None,
        'thumbnail': None,
        'title': 'NassLaMenass',
        'transformation_id': None,
        'updated_at': None,
        'updated_by_id': 1
    }


@pytest.fixture
def mock_asset():
    return Asset(**data_asset)


@pytest.fixture
def mock_all_assets():
    return Asset(**data_all_assets)


@pytest.fixture
def mock_assets_list(mock_all_assets) -> list:
    return [mock_all_assets, mock_all_assets]


def test_create_asset(mock_asset):
    # Test creation of a new asset
    with patch('models.asset.Asset.get_by', return_value=None):
        with patch('models.asset.Asset.create'):
            response = create_asset(data_asset)
            assert response == \
                   ({'message':
                    'The asset has been successfully created'}, 200)


def test_create_asset_already_exists(mock_asset):
    with patch('models.asset.Asset.get_by', return_value=data_asset):
        response = create_asset(data_asset)
        assert response == \
               ({'message': 'asset already exists'}, 409)


def test_get_all_assets(mock_assets_list):
    #  Test with assets
    with patch('models.asset.Asset.get_all_by', return_value=mock_assets_list):
        response = get_asset()
        print(response)
        assert response == ({'all_asset': transformation(mock_assets_list)},
                            200)


def test_get_all_assets_empty():
    # Test without assets
    with patch('models.asset.Asset.get_all_by', return_value=[]):
        response = get_asset()
        assert response == ({'message': 'No entities found'}, 404)


def test_get_asset_by_id(mock_assets_list):
    #  Test with assets
    with patch('models.asset.Asset.get_entity_with_joins',
               return_value=mock_assets_list):
        response = get_asset(id=1)
        assert response == ({'asset': mock_assets_list}, 200)


def test_get_asset_by_id_not_existing():
    # Test without assets
    with patch('models.asset.Asset.get_entity_with_joins', return_value=[]):
        response = get_asset(id=500)
        assert response == ({'message': 'Entity not found'}, 404)


def test_search_asset():
    with patch('models.asset.Asset.get_entities_by_search_values',
               return_value=[data_asset]):
        results = search_asset(search="NassLaMenass")
        assert len(results[0]) == 1
        assert results[0].get("all_asset")[0].get("title") == "NassLaMenass"
