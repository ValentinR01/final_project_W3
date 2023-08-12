import pytest
from db import db
from models.base import Base
from unittest.mock import Mock
from flask_app.src.app import app
from services.base import create_entity


class MockEntity(Base):
    __tablename__ = 'mockentity'

    id = db.Column(db.Integer, primary_key=True)

    @classmethod
    def get_by(cls, **kwargs):
        return super().get_by(**kwargs)


@pytest.fixture
def mock_entity():
    with app.app_context():
        mock_instance = MockEntity(id=None)
        mock_instance.get_by = Mock(return_value=True)
        return mock_instance


def test_create_entity_missing_parameters():
    response, status_code = create_entity(MockEntity, {})
    assert status_code == 400
    assert response == {'message': 'Missing parameters'}


# def test_create_entity_already_exists(mock_entity):
#     mock_entity.get_by.return_value = True
#     response, status_code = create_entity(
#         MockEntity, {"data": "value"},
#         some_key="some_value"
#     )
#     assert status_code == 409
#     assert response == {'message': 'Entity already exists'}


# def test_create_entity_success(mock_entity):
#     mock_entity.get_by.return_value = False
#     response, status_code = create_entity(MockEntity, {"data": "value"})
#     assert status_code == 200
#     assert response == {'message': 'The mockentity created successfully'}
#
#
# # Tests for get_all_entities
#
# def test_get_all_entities_no_entity_found(mock_entity):
#     mock_entity.get_all_by.return_value = None
#     response, status_code = get_all_entities(MockEntity)
#     assert status_code == 404
#     assert response == {'message': "No entities found or it's empty"}
#
#
# def test_get_all_entities_success(mock_entity):
#     mock_entity.get_all_by.return_value = ["entity1", "entity2"]
#     response, status_code = get_all_entities(MockEntity)
#     assert status_code == 200
#     assert response == {'all_mockentity': ["entity1", "entity2"]}
#
#
# # Tests for search_entities
#
# def test_search_entities_no_entity_found(mock_entity):
#     mock_entity.get_entities_by_search_values.return_value = None
#     response, status_code = search_entities(MockEntity, "search_val", "col1")
#     assert status_code == 404
#     assert response == {'message': "No entities found or it's empty"}
#
#
# def test_search_entities_success(mock_entity):
#     mock_entity.get_entities_by_search_values.return_value = ["entity1", "entity2"]
#     response, status_code = search_entities(MockEntity, "search_val", "col1")
#     assert status_code == 200
#     assert response == {'all_mockentity': ["entity1", "entity2"]}
#
#
# # Tests for get_entity_by_id
#
# def test_get_entity_by_id_no_entity_found(mock_entity):
#     mock_entity.get_entity_with_joins.return_value = None
#     response, status_code = get_entity_by_id(MockEntity, 1)
#     assert status_code == 404
#     assert response == {'message': 'Entity not found'}
#
#
# def test_get_entity_by_id_success(mock_entity):
#     mock_entity.get_entity_with_joins.return_value = "entity_data"
#     response, status_code = get_entity_by_id(MockEntity, 1)
#     assert status_code == 200
#     assert response == {'mockentity': 'entity_data'}
