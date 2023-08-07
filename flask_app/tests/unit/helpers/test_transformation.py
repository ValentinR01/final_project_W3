import pytest
from datetime import datetime
from helpers.etl import transformation


class MockObject:
    def __init__(self, a, b, c=None):
        self.a = a
        self.b = b


@pytest.fixture
def mock_obj():
    return MockObject("test", datetime.now())


def test_transformation_with_plain_object(mock_obj):
    transformed = transformation(mock_obj)
    assert transformed == [
        {"a": "test", "b": mock_obj.b.strftime('%Y-%m-%d %H:%M:%S')}
    ]
