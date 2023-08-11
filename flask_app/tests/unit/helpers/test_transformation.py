import pytest
from datetime import datetime
from helpers.etl import transformation


class MockObject:
    def __init__(self, a, b, c, password=None, _sa_instance=None):
        self.a = a
        self.b = b
        self.c = c
        self.password = password
        self._sa_Instance = _sa_instance


@pytest.fixture
def mock_obj():
    return MockObject(
        "test", datetime.now(),
        MockObject(1, "c.test", datetime.now(), "password"),
    )


def test_transformation_with_plain_object(mock_obj):
    transformed = transformation(mock_obj)
    assert isinstance(transformed, list)
    assert isinstance(transformed[0], dict)
    assert transformed != [mock_obj.__dict__.values()]
    assert transformed == [{
        "a": "test",
        "b": mock_obj.b.strftime('%Y-%m-%d %H:%M:%S'),
        "c": {
            "a": 1, "b": "c.test",
            "c": mock_obj.c.c.strftime('%Y-%m-%d %H:%M:%S')
        }
    }]
