# pylint: disable=redefined-outer-name
import pytest

from flask_app.src import main as flask_app


@pytest.fixture
def app():
    yield flask_app


@pytest.fixture
def client(app):
    return app.test_client()
