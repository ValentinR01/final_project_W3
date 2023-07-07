from unittest import mock
from helpers.auth import AuthHandler
from helpers.decorators import rights_manager


def test_rights_manager_authorized():
    # Mocking the AuthHandler.decode_token method
    token = "valid_token"
    role = "admin"
    domain = "regisseur"
    decoded_token = {"role": role, "domain": domain}

    with mock.patch("helpers.auth.AuthHandler.decode_token") as \
            mock_decode_token:
        mock_decode_token.return_value = decoded_token

        @rights_manager(token, role, domain)
        def protected_function():
            return {"message": "success"}

        result = protected_function()

    assert result == {"message": "success"}


def test_rights_manager_unauthorized():
    # Mocking the AuthHandler.decode_token method
    token = "valid_token"
    role = "admin"
    domain = "example.com"
    decoded_token = {"role": "user", "domain": "example.org"}

    with mock.patch("helpers.auth.AuthHandler.decode_token") as \
            mock_decode_token:
        mock_decode_token.return_value = decoded_token

        @rights_manager(token, role, domain)
        def protected_function():
            return {"message": "success"}

        result = protected_function()

    assert result == (
        {"message": "unauthorized: the user hasn't the right"},
        401
    )
