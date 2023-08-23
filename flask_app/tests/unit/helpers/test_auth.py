import pytest
import jwt
from datetime import datetime, timedelta
from unittest.mock import patch
from werkzeug.security import generate_password_hash

from helpers.auth import AuthHandler
from models.user import User
from models.role import Role
from models.domain import Domain
from conf import TOKEN_SECRET


@pytest.fixture
def user():
    return User(
        email="john@example.com",
        fullname="John Doe",
        password=generate_password_hash("password"),
        domain_id=1,
        role_id=1
    )


@pytest.fixture
def role():
    return Role(name="admin")


@pytest.fixture
def domain():
    return Domain(name="example.com")


def test_authenticate_with_valid_credentials(user):
    with patch('models.user.User.get_by', return_value=user):
        with patch('werkzeug.security.check_password_hash', return_value=True):
            result = AuthHandler.authenticate(user.email, "password")
            assert result == user


def test_authenticate_with_invalid_credentials(user):
    with patch('models.user.User.get_by', return_value=user):
        with patch('werkzeug.security.check_password_hash',
                   return_value=False):
            result = AuthHandler.authenticate(user.email, "wrong_password")
            assert result is None


def test_generate_token(user, role, domain):
    with patch('models.role.Role.get_by', return_value=role):
        with patch('models.domain.Domain.get_by', return_value=domain):
            token = AuthHandler.generate_token(user)
            assert isinstance(token, str)


def test_decode_token_with_valid_token(user):
    payload = {
        "id": user.id,
        "fullname": user.fullname,
        "email": user.email,
        "role": "admin",
        "domain": "example.com",
        "exp": 1752179546,
        "iat": 1688984385
    }
    token = jwt.encode(payload, key=TOKEN_SECRET, algorithm='HS256')

    result = AuthHandler.decode_token(token)

    assert result == payload


@patch('helpers.auth.abort')
def test_decode_token_with_expired_token(mock_abort, user):
    current_time = datetime.utcnow()
    expired_time = current_time - timedelta(hours=1)
    payload = {
        "id": user.id,
        "fullname": user.fullname,
        "email": user.email,
        "role": "admin",
        "domain": "example.com",
        "exp": int(expired_time.timestamp()),
        "iat": int(current_time.timestamp())
    }
    token = jwt.encode(payload, key=TOKEN_SECRET, algorithm='HS256')

    AuthHandler.decode_token(token)

    mock_abort.assert_called_with(401, "Token has expired.")


@patch('helpers.auth.abort')
def test_decode_token_with_invalid_token(mock_abort):
    invalid_token = "invalid_token"

    AuthHandler.decode_token(invalid_token)

    mock_abort.assert_called_with(401, "Invalid token.")
