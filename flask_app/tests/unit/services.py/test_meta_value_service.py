import pytest
from unittest.mock import Mock, patch

from services.meta_value import get_all_meta_values


@pytest.fixture
def meta_value_mock():
    return [
        {'id': 1, 'value': 'Value 1'},
        {'id': 2, 'value': 'Value 2'}
    ]


@pytest.fixture
def meta_key_id_mock():
    return 123


@pytest.fixture
def meta_value_get_all_mock(meta_value_mock):
    with patch('models.meta_value.MetaValue.get_all') as mock:
        mock.return_value = meta_value_mock
        yield mock


@pytest.fixture
def meta_key_get_by_mock(meta_key_id_mock):
    with patch('models.meta_key.MetaKey.get_by') as mock:
        mock.return_value = meta_key_id_mock
        yield mock


@pytest.fixture
def meta_value_get_all_by_mock(meta_value_mock):
    def get_all_by(meta_key_id):
        if meta_key_id == 123:  # Assuming 123 is the valid meta_key_id
            return []
        return meta_value_mock

    with patch('models.meta_value.MetaValue.get_all_by',
               side_effect=get_all_by) as mock:
        yield mock


def test_get_all_meta_values_without_key(meta_value_get_all_mock):
    response, _ = get_all_meta_values()
    assert response == {'meta_values': [{'id': 1, 'value': 'Value 1'},
                                        {'id': 2, 'value': 'Value 2'}]}


def test_get_all_meta_values_with_invalid_key(meta_key_get_by_mock):
    meta_key_get_by_mock.return_value = None
    logging_mock = Mock()
    with patch('logging.error', logging_mock):
        response, _ = get_all_meta_values(meta_key='invalid_key')
        assert response == {'meta_values': []}


def test_get_all_meta_values_with_valid_key(meta_key_get_by_mock,
                                            meta_value_get_all_by_mock):
    meta_key_object_mock = Mock(id=123)
    meta_key_get_by_mock.return_value = meta_key_object_mock
    response, _ = get_all_meta_values(meta_key='valid_key')
    assert response == {'meta_values': []}
