from unittest.mock import patch
from models.domain import Domain
from models.role import Role
from helpers.decorators import rights_manager


def test_rights_manager():
    # Mocking dependencies
    # mocked_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6NCwiZn" \
    #                "VsbG5hbWUiOiJzYWxpbiIsImVtYWlsIjoic2FsaW5Ac2FsaW5lL" \
    #                "mNvbSIsInJvbGUiOiJ3b3JrZXIiLCJkb21haW4iOiJyZWRhY3Rp" \
    #                "b24iLCJleHAiOjE2ODkwMjk5MDIsImlhdCI6MTY4ODk5MzkwMn" \
    #                "0.r4UalimTKPHVIDABZei3px6armJdAd_TOVAM_uEazTM"
    mocked_decode_token = {
        "id": 4,
        "fullname": "salin",
        "email": "salin@saline.com",
        "role": "worker",
        "domain": "redaction",
        "exp": 1689029902,
        "iat": 1688993902
    }

    # Mocking the Role and Domain models
    mocked_role_get_all = [
        Role(name="worker"),
        Role(name="lead"),
        Role(name="superadmin"),
    ]
    mocked_domain_get_all = [
        Domain(name="redaction"),
        Domain(name="production"),
    ]

    with patch("helpers.auth.AuthHandler.decode_token",
               return_value=mocked_decode_token):
        with patch("models.role.Role.get_all",
                   return_value=mocked_role_get_all):
            with patch("models.domain.Domain.get_all",
                       return_value=mocked_domain_get_all):
                # Test case 1: Role passed to decorator doesn't exist
                @rights_manager(request=None, role="nonexistent_role")
                def test_case_1():
                    return "Success"

                assert test_case_1() == (
                    {"message": "Role passed to decorator doesn't exist"},
                    404,
                )

                # Test case 2: Domain passed to decorator doesn't exist
                @rights_manager(request=None, role="worker",
                                domain="nonexistent_domain")
                def test_case_2():
                    return "Success"

                assert test_case_2() == (
                    {"message": "Domain passed to decorator doesn't exist"},
                    404,
                )

                # Test case 3: Unauthorized access - insufficient role
                @rights_manager(request=None, role="lead")
                def test_case_3():
                    return "Success"

                assert test_case_3() == (
                    {'message': "unauthorized: the user hasn't the right"}, 401
                )

                # Test case 4 : Authorized access dor superadmin
                @rights_manager(request=None, role="worker", domain="redaction")
                def test_case_4():
                    return "Success"

                assert test_case_4() == "Success"
