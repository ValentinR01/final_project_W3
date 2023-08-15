import pytest
from db import db
from flask import Flask
from models.asset import Asset
from unittest.mock import patch
from conf import POSTGRESQL_DATABASE_URI
from services.asset import create_asset, get_asset, search_asset

mock_data = {
    "title": "NassLaMenass",
    "music_title": "Music Title",
    "created_by_id": 1,
    "updated_by_id": 1,
    "status_by_domain_id": 1,
    "step_lifecycle_id": 1
}


def create_app():
    app = Flask(__name__)
    app.config['RESTPLUS_MASK_SWAGGER'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = POSTGRESQL_DATABASE_URI
    db.init_app(app)
    return app


@pytest.fixture
def mock_asset():
    return Asset(**mock_data)


@pytest.fixture
def mock_asset_list(mock_asset) -> list:
    return [mock_asset]


def test_create_asset(mock_asset):
    with patch('models.asset.Asset.get_by', return_value=None):
        with patch('models.asset.Asset.create'):
            response = mock_asset.create()

            response = create_asset(mock_data)

            print(response)
            # assert response == \
            #        ({'message': 'The asset created successfully'}, 200)

    # with patch('models.asset.Asset.get_by', return_value=mock_asset):
    #     response = create_asset(mock_data)
    #     assert response == \
    #            ({'message': 'Entity already exists'}, 409)


# def test_get_all_assets(mock_asset_list):
#     app = create_app()
#     with app.app_context():
#         with patch('models.asset.Asset.get_all', return_value=mock_asset_list):
#             assets = get_asset()
#             print(assets)
#             assert len(assets[0].get("all_asset")) > 0
#             assert assets[0].get("all_asset")[1].get("title") == "NassLaMenass"


# def test_get_asset_by_id(mock_asset):
#     with patch('models.asset.Asset.get_by', return_value=mock_asset):
#         print(mock_asset)
#         fetched_asset = get_asset(id=mock_asset.id)
#         print(fetched_asset)


# def test_search_asset(mock_asset):
#     with patch('models.asset.Asset.search', return_value=[mock_asset]):
#         results = search_asset(search="NassLaMenass")
#         assert len(results) == 1
#         assert results[0].title == "NassLaMenass"
