import pytest
from db import db
from models.base import Base
from unittest.mock import MagicMock, patch
from services.base import \
    create_entity, get_all_entities, search_entities, get_entity_by_id, \
    delete_entity


class MockEntity(Base):
    __tablename__ = 'mockentity'
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(80), nullable=False, unique=True)

    def __init__(self, data=None):
        self.data = data


@pytest.fixture
def mock_session():
    session = MagicMock()
    with patch('models.base.Base.create', session):
        yield session


@pytest.fixture
def mock_entity():
    return MockEntity(data="value")


def test_create_entity_missing_parameters():
    with patch('models.base.Base.get_by', return_value=None):
        response, status_code = create_entity(MockEntity, {})
        assert status_code == 400
        assert response == {'message': 'Missing parameters'}


def test_create_entity_already_exists(mock_entity):
    with patch('models.base.Base.get_by', return_value=mock_entity):
        response, status_code = create_entity(MockEntity, {"data": "value"})
        assert status_code == 409
        assert response == {'message':
                            f'{mock_entity.__tablename__} already exists'}


def test_create_entity_success(mock_session):
    with patch('models.base.Base.get_by', return_value=None):
        response, status_code = create_entity(
            MockEntity, {"data": "value"}
        )
        assert \
            response == {'message':
                         'The mockentity has been successfully created'}


def test_get_all_entities_no_entity_found():
    with patch('models.base.Base.get_all_by', return_value=[]):
        response, status_code = get_all_entities(MockEntity)
        assert response == {'message': "No entities found"}
        assert status_code == 404


def test_get_all_entities_success():
    mock_entity = MagicMock()
    mock_entity.__dict__ = {"data": "entity1"}
    mock_data = [mock_entity]

    with patch('models.base.Base.get_all_by', return_value=mock_data):
        response, status_code = get_all_entities(MockEntity)
        assert response == {'all_mockentity': [{'data': 'entity1'}]}
        assert status_code == 200


def test_search_entities_no_entity_found():
    with patch(
            'models.base.Base.get_entities_by_search_values',
            return_value=None):
        response, status_code = search_entities(
            MockEntity, "search_val", "col1"
        )
        assert status_code == 404
        assert response == {'message': "No entities found"}


def test_search_entities_success():
    with patch(
            'models.base.Base.get_entities_by_search_values',
            return_value=["entity1", "entity2"]):
        response, status_code = search_entities(
            MockEntity, "search_val", "col1"
        )
        assert status_code == 200
        assert response == {'all_mockentity': ["entity1", "entity2"]}


def test_get_entity_by_id_no_entity_found():
    with patch('models.base.Base.get_entity_with_joins', return_value=None):
        response, status_code = get_entity_by_id(MockEntity, 1)
        assert status_code == 404
        assert response == {'message': 'Entity not found'}


def test_get_entity_by_id_success():
    with patch(
            'models.base.Base.get_entity_with_joins',
            return_value="entity_data"):
        response, status_code = get_entity_by_id(MockEntity, 1)
        assert status_code == 200
        assert response == {'mockentity': 'entity_data'}


def test_delete_entity(mock_entity):
    # Test on entity found
    with patch('models.base.Base.get_by', return_value=mock_entity):
        with patch('models.base.Base.delete', return_value=True):
            response, status_code = delete_entity(mock_entity, 1)
            assert status_code == 200
            assert response == {'message':
                                'The mockentity has been successfully deleted'}


def test_delete_entity_not_found(mock_entity):
    # Test on entity not found
    with patch('models.base.Base.get_by', return_value=None):
        response, status_code = delete_entity(mock_entity, 999)
        assert status_code == 404
        assert response == {'message': 'Entity not found'}
