from unittest.mock import patch
import pytest
from services.language import get_all_languages
from models.language import Language


@pytest.fixture
def mock_language():
    return Language(
        name="French",
        code="FR"
    )


@pytest.fixture
def mock_language_list(mock_language) -> list:
    return [mock_language, mock_language]


def test_get_all_languages(mock_language_list):
    # Test with a list of languages
    with patch('models.language.Language.get_all',
               return_value=mock_language_list):
        language_list = get_all_languages()
        assert language_list == ({'languages': mock_language_list}, 200)

    # Test with an empty list of languages
    with patch('models.language.Language.get_all', return_value=[]):
        language_list = get_all_languages()
        assert language_list == ({'languages': []}, 200)
