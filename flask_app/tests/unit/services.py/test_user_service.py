# import pytest
# from pytest_mock import mocker
# from models.user import User
# from models.domain import Domain
# from services.user import register_service, login_service, get_user_by_domain, \
#     get_all_users
#
#
# @pytest.fixture
# def mock_user():
#     return User(fullname='John Doe', email='john@saline.com', domain_id=1)
#
#
# @pytest.fixture
# def mock_domain():
#     return Domain(name='saline.com')
#
#
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
# # Mock login_service function
# def test_login_service(mocker, mock_user):
#     mocker.patch('your_module.AuthHandler.authenticate', return_value=mock_user)
#     mocker.patch('your_module.AuthHandler.generate_token',
#                  return_value='<generated_token>')
#
#     userdata = {
#         'email': 'test@saline.com',
#         'password': 'password'
#     }
#
#     response = login_service(userdata)
#     assert response == {
#         'access_token': '<generated_token>',
#         'message': 'Login successful'
#     }, 200
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
