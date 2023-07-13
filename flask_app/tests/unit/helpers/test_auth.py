import pytest
import jwt

from datetime import datetime, timedelta
from werkzeug.security import generate_password_hash
from unittest.mock import patch
from models.user import User
from models.role import Role
from models.domain import Domain
from helpers.auth import AuthHandler
from conf import TOKEN_SECRET


@pytest.fixture
def user():
    password_hash = generate_password_hash('password')
    role = Role(name='worker')
    domain = Domain(name='redaction')
    user = User(
        email='john@saline.com',
        fullname='John Doe',
        password=password_hash,
        role_id=role,
        domain_id=domain
    )
    return user


@patch('helpers.auth.User.get_by')
def test_authenticate_valid_user(mock_get_by, user):
    # Mock the User.get_by method to return the user
    mock_get_by.return_value = user

    # Call the authenticate method with valid credentials
    authenticated_user = AuthHandler.authenticate('john@saline.com', 'password')

    # Assertions
    assert authenticated_user == user


@patch('helpers.auth.User.get_by')
def test_authenticate_invalid_user(mock_get_by, user):
    # Mock the User.get_by method to return None
    mock_get_by.return_value = None

    # Call the authenticate method with invalid credentials
    authenticated_user = AuthHandler.authenticate('john@saline.com',
                                                  'wrong_password')

    # Assertions
    assert authenticated_user is None


def test_generate_token(user):
    with patch('models.role.Role.get_by', return_value=user.role_id):
        with patch('models.domain.Domain.get_by', return_value=user.domain_id):
            token = AuthHandler.generate_token(user)
            assert isinstance(token, str)


def test_decode_token_valid_token():
    # Generate a valid token
    role = Role(name='worker')
    domain = Domain(name='redaction')
    user = User(
        email='john@saline.com',
        fullname='John Doe',
        password='password',
        role_id=role,
        domain_id=domain
    )
    payload = {
        'id': user.id,
        'fullname': user.fullname,
        'email': user.email,
        'role': role.name,
        'domain': domain.name,
        'exp': 1720777536,
        'iat': 1689241536
    }
    token = jwt.encode(payload, key=TOKEN_SECRET, algorithm='HS256')

    # Call the decode_token method
    decoded_payload = AuthHandler.decode_token(token)

    # Assertions
    assert decoded_payload == payload


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
