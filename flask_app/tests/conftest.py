# pylint: disable=redefined-outer-name
import pytest, sys
sys.path.append( '/flask_app/src/' )
from flask_app.src.app import app as flask_app


@pytest.fixture
def app():
    yield flask_app


@pytest.fixture
def client(app):
    return app.test_client()

