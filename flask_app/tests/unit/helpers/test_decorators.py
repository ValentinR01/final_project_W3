# Import necessary modules and functions
from unittest.mock import Mock

import pytest

from helpers.auth import AuthHandler
from models.domain import Domain
from models.role import Role
from helpers.decorators import rights_manager


# Set up a mock request object
class MockRequest:
    def __init__(self, cookies=None):
        self.cookies = cookies


# Define test cases
def test_rights_manager_no_request():
    # Create a mock request without cookies
    request = None

    # Define the role and domain parameters for the test
    role = "worker"
    domain = "redaction"

    # Create a mock function to decorate
    @rights_manager(request, role, domain)
    def mock_function():
        return {"message": "Role passed to decorator doesn't exist"}, 404

    # Call the decorated function
    result = mock_function()

    # Assertions
    assert result == (
        {"message": "Role passed to decorator doesn't exist"}, 404
    )


def test_rights_manager_valid_request():
    # Create a mock request with valid authorization token
    authorization_token = "valid_token"
    request = MockRequest(cookies={"authorization": authorization_token})

    # Define the role and domain parameters for the test
    role = "worker"
    domain = "redaction"

    # Create a mock function to decorate
    @rights_manager(request, role, domain)
    def mock_function():
        return "Mock function executed"

    # Mock the necessary dependencies
    AuthHandler.decode_token = Mock(return_value={"role": "worker",
                                                  "domain": "redaction"})
    Role.get_all = Mock(return_value=[Role(name="worker")])
    Domain.get_all = Mock(return_value=[Domain(name="redaction")])

    # Call the decorated function
    result = mock_function()

    # Assertions
    assert result == "Mock function executed"


def test_rights_manager_no_role():
    # Create a mock request with a valid authorization token
    authorization_token = "valid_token"
    request = MockRequest(cookies={"authorization": authorization_token})

    # Define the role and domain parameters for the test
    role = "invalid_role"
    domain = "redaction"

    # Create a mock function to decorate
    @rights_manager(request, role, domain)
    def mock_function():
        return "Mock function executed"

    # Mock the necessary dependencies
    AuthHandler.decode_token = Mock(return_value={"role": "worker",
                                                  "domain": "redaction"})
    Role.get_all = Mock(return_value=[Role(name="worker")])
    Domain.get_all = Mock(return_value=[Domain(name="redaction")])

    # Call the decorated function
    result = mock_function()

    # Assertions
    assert result == (
        {"message": "Role passed to decorator doesn't exist"},
        404
    )


def test_rights_manager_no_domain():
    # Create a mock request with a valid authorization token
    authorization_token = "valid_token"
    request = MockRequest(cookies={"authorization": authorization_token})

    # Define the role and domain parameters for the test
    role = "worker"
    domain = "invalid_domain"

    # Create a mock function to decorate
    @rights_manager(request, role, domain)
    def mock_function():
        return "Mock function executed"

    # Mock the necessary dependencies
    AuthHandler.decode_token = Mock(return_value={"role": "worker",
                                                  "domain": "redaction"})
    Role.get_all = Mock(return_value=[Role(name="worker")])
    Domain.get_all = Mock(return_value=[Domain(name="redaction")])

    # Call the decorated function
    result = mock_function()

    # Assertions
    assert result == (
        {"message": "Domain passed to decorator doesn't exist"},
        404
    )


# Run the tests
pytest.main()
