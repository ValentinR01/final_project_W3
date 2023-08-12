from flask_app.src.app import app as flask_app
import pytest
import sys
sys.path.append('/flask_app/src/')


@pytest.fixture
def app():
    yield flask_app


@pytest.fixture
def client(app):
    return app.test_client()
