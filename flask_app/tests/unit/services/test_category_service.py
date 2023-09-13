from unittest.mock import patch
import pytest
from services.category import get_all_categories
from models.type import Type


@pytest.fixture
def mock_typelist() -> list:
    return [Type(name="lesson"),
            Type(name="interview"),
            Type(name="presentation")]


def test_get_all_categories(mock_typelist):
    # Test with a list of composers
    with patch('models.type.Type.get_all',
               return_value=mock_typelist):
        categories_list = get_all_categories()
        assert categories_list == ({'categories': mock_typelist}, 200)


def test_get_all_composers_empty():
    # Test with an empty list of speakers
    with patch('models.type.Type.get_all', return_value=[]):
        categories_list = get_all_categories()
        assert categories_list == ({'categories': []}, 200)
