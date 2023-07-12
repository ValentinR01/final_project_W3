# import pytest
# import datetime
# from unittest.mock import patch
# from models.user import User
# from models.domain import Domain
# from services.user import register_service, login_service, get_user_by_domain, \
#     get_all_users
# import datetime
#
#
# @pytest.fixture
# def mock_user():
#     return User(
#         fullname='John Doe',
#         email='john@saline.com',
#         password='password',
#         role_id=1,
#         domain_id=1)
#
#
# @pytest.fixture
# def mock_domain():
#     return Domain(name='saline.com')


# # Mock register_service function
# def test_register_service(mocker):
#     mocker.patch('your_module.User.get_by', return_value=None)
#     mocker.patch('your_module.generate_password_hash',
#                  return_value='hashed_password')
#     mocker.patch('your_module.User.create')
#
#     data = {
#         'email': 'test@saline.com',
#         'fullname': 'John Doe',
#         'password': 'password',
#         'role_id': 1,
#         'domain_id': 1
#     }
#
#     response = register_service(data)
#     assert response == {'message': 'User created successfully'}, 201
#
#
# Mock login_service function
#
#
# # Mock get_user_by_domain function
# def test_get_user_by_domain(mocker, mock_domain, mock_user):
#     mocker.patch('your_module.Domain.get_by', return_value=mock_domain)
#     mocker.patch('your_module.User.get_all_by', return_value=[mock_user])
#
#     domain_name = 'saline.com'
#
#     response = get_user_by_domain(domain_name)
#     assert response == {'users': [mock_user]}, 200
#
#
# # Mock get_all_users function
# def test_get_all_users(mocker, mock_user):
#     mocker.patch('your_module.User.get_all', return_value=[mock_user])
#
#     response = get_all_users()
#     assert response == {'users': [mock_user]}, 200
#


# Import the login_service function here


# Mock AuthHandler class for testing
# class MockAuthHandler:
#     def authenticate(self, email, password):
#         return {'user_id': 1, 'email': email} if email == 'test@example.com' and password == 'password' else None
#
#     def generate_token(self, user):
#         return 'mock_token'
#
#
# # Mock make_response function for testing
# def mock_make_response(data, status_code):
#     return {'data': data, 'status_code': status_code}
#
#
# @pytest.fixture
# def mock_auth_handler():
#     with patch('__main__.AuthHandler', return_value=MockAuthHandler()) as mock_handler:
#         yield mock_handler
#
#
# @pytest.fixture
# def mock_make_response_func():
#     with patch('__main__.make_response', side_effect=mock_make_response) as mock_func:
#         yield mock_func
#
#
# def test_login_service_valid_credentials(mock_auth_handler, mock_make_response_func):
#     userdata = {'email': 'test@example.com', 'password': 'password'}
#
#     response = login_service(userdata)
#
#     assert response == {
#         'access_token': 'mock_token',
#         'message': 'Login successful'
#     }
#     assert response['status_code'] == 200
#     assert response['data']['access_token'] == 'mock_token'
#     assert response['data']['message'] == 'Login successful'
#     assert response['data']['authorization'] == 'mock_token'
#
#
# def test_login_service_invalid_credentials(mock_auth_handler, mock_make_response_func):
#     userdata = {'email': 'test@example.com', 'password': 'incorrect_password'}
#
#     response = login_service(userdata)
#
#     assert response == ({'message': 'Invalid email or password'}, 401)
#     assert response['status_code'] == 401
#     assert response['data']['message'] == 'Invalid email or password'
#
#
# def test_login_service_exception(mock_auth_handler, mock_make_response_func):
#     userdata = {'email': 'test@example.com', 'password': 'password'}
#
#     # Simulate an exception during the execution of login_service
#     with patch('__main__.datetime.datetime') as mock_datetime:
#         mock_datetime.now.side_effect = Exception('Test exception')
#
#         response = login_service(userdata)
#
#     assert response == ({'message': 'Test exception'}, 500)
#     assert response['status_code'] == 500
#     assert response['data']['message'] == 'Test exception'
