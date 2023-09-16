import pytest
from unittest.mock import patch
from models.user import User
from models.domain import Domain
from services.user import register_service, login_service, \
    get_user_by_domain, get_all_users, get_user_by_id
import datetime


@pytest.fixture
def mock_user():
    return User(
        fullname='John Doe',
        email='john@saline.com',
        password='password',
        role_id=1,
        domain_id=1)


@pytest.fixture
def mock_user_list(mock_user) -> list:
    return [mock_user, mock_user]


@pytest.fixture
def mock_register_data():
    return {
        'email': 'test@saline.com',
        'fullname': 'John Doe',
        'password': 'password',
        'role_id': 1,
        'domain_id': 1
    }


@pytest.fixture
def mock_login_data():
    return {
            'email': 'valentin@saline.com',
            'password': 'password'
    }


@pytest.fixture
def mock_missing_data():
    return {
        'email': 'test@saline.com',
        'password': 'password',
    }


@pytest.fixture
def mock_domain():
    return Domain(name='redaction')


def test_register_service_valid_data(mock_register_data):
    # Test creation of a new user
    with patch('models.user.User.get_by', return_value=None):
        with patch('werkzeug.security.generate_password_hash',
                   return_value='hashed_password'):
            with patch('models.user.User.create'):
                response = register_service(mock_register_data)
                assert response == ({'message': 'User created successfully'},
                                    201)


def test_register_service_existing_user(mock_register_data, mock_user):
    # Test creation of an existing user
    with patch('models.user.User.get_by', return_value=mock_user):
        response = register_service(mock_register_data)
        assert response == ({'message': 'User already exists'}, 409)


def test_register_service_missing_data(mock_register_data, mock_missing_data):
    # Test creation with missing datas
    with patch('models.user.User.get_by', return_value=None):
        response = register_service(mock_missing_data)
        assert response == ({'message': 'Missing parameters'}, 400)


def test_get_user_by_domain_invalid_domain(mock_domain):
    # Test non existing domain
    with patch('models.domain.Domain.get_by', return_value=None):
        response = get_user_by_domain(mock_domain.name)
        assert response == ({'message': 'Domain not found'}, 404)


def test_get_user_by_domain_valid_domain(mock_domain, mock_user_list):
    # Test user found with valid domain
    with patch('models.domain.Domain.get_by', return_value=mock_domain):
        with patch('models.user.User.get_all_by', return_value=mock_user_list):
            response = get_user_by_domain(mock_domain.name)
            assert response == ({'users': mock_user_list}, 200)


def test_get_user_by_domain_valid_domain_user_unknown(mock_domain):
    # Test user not found with valid domain
    with patch('models.domain.Domain.get_by', return_value=mock_domain):
        with patch('models.user.User.get_all_by', return_value=[]):
            response = get_user_by_domain(mock_domain.name)
            assert response == ({'users': []}, 200)


def test_get_all_users(mock_user_list):
    #  Test with users
    with patch('models.user.User.get_all', return_value=mock_user_list):
        response = get_all_users()
        assert response == ({'users': mock_user_list}, 200)


def test_get_all_users_empty(mock_user_list):
    # Test without users
    with patch('models.user.User.get_all', return_value=[]):
        response = get_all_users()
        assert response == ({'users': []}, 200)


def test_login_service_invalid_credentials(mock_login_data):
    # Test login with invalid credentials
    with patch('helpers.auth.AuthHandler.authenticate', return_value=None):
        response = login_service(mock_login_data)
        assert response == ({'message': 'Invalid email or password'}, 401)


def test_login_service_valid_credentials(mock_login_data, mock_user):
    # Test login with valid credentials
    with patch('helpers.auth.AuthHandler.authenticate',
               return_value=mock_user):
        with patch('helpers.auth.AuthHandler.generate_token',
                   return_value='token'):
            with patch('datetime.datetime') as mock_datetime:
                mock_datetime.now.return_value = datetime.datetime(2023, 7, 12)
                response = login_service(mock_login_data)
                assert response[0] == {'token': 'token',
                                       'user': mock_user}
                assert response[1] == 200
                assert response[2][0][1] == 'authorization=token; ' \
                                            'max-age=2592000; path=/'


def test_get_user_by_id(mock_user):
    with patch('models.user.User.get_by', return_value=mock_user):
        response = get_user_by_id(1)
        assert response == (mock_user, 200)


def test_get_user_by_id_not_found():
    with patch('models.user.User.get_by', return_value=[]):
        response = get_user_by_id(999)
        assert response == ({'message': 'User not found'}, 404)
