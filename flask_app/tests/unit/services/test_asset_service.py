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


def test_create_asset(mock_asset):
    with patch('models.asset.Asset.get_by', return_value=None):
        with patch('models.asset.Asset.create'):
            response = create_asset(mock_data)
            assert response == \
                   ({'message': 'The asset created successfully'}, 200)

    with patch('models.asset.Asset.get_by', return_value=mock_asset):
        response = create_asset(mock_data)
        assert response == \
               ({'message': 'Entity already exists'}, 409)


def test_get_all_assets():
    app = create_app()
    with app.app_context():
        with patch('models.asset.Asset.get_all'):
            assets = get_asset()
            assert len(assets[0].get("all_asset")) > 0
            assert assets[0].get("all_asset")[0].get("title") == "Title"


def test_get_asset_by_id():
    app = create_app()
    with app.app_context():
        with patch('models.asset.Asset.get_by'):
            fetched_asset = get_asset(id=1)
            obj = fetched_asset[0].get("asset")[0]
            assert fetched_asset[0].get("asset") is not None
            assert len(fetched_asset[0].get("asset")) == 1
            assert obj.get("title") == "Title"
            assert obj.get("id") == 1
            if isinstance(obj, dict):
                if any(isinstance(key, dict) for key in obj.values()):
                    assert True


def test_search_asset():
    with patch('models.asset.Asset.get_entities_by_search_values',
               return_value=[mock_data]):
        results = search_asset(search="NassLaMenass")
        assert len(results[0]) == 1
        assert results[0].get("all_asset")[0].get("title") == "NassLaMenass"
