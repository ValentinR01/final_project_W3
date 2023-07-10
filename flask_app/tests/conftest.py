# pylint: disable=redefined-outer-name
import pytest
import sys
from flask_app.src.app import app as flask_app

sys.path.append('/flask_app/src/')


@pytest.fixture
def app():
    yield flask_app


@pytest.fixture
def client(app):
    return app.test_client()
