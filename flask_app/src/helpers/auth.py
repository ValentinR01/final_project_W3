import jwt
from flask_restx import abort
from datetime import datetime, timedelta
from werkzeug.security import check_password_hash

from models.user import User
from models.role import Role
from models.domain import Domain
from conf import TOKEN_SECRET, TOKEN_EXPIRATION_HOURS


class AuthHandler:
    """
    This class handles user authentication.
    """

    @staticmethod
    def authenticate(email: str, password: str):
        """
        This method authenticates a user.

        :param email: user email
        :param password: user password
        """
        user = User.get_by(email=email)

        if user and check_password_hash(user.password, password):
            return user

    @staticmethod
    def generate_token(user: User):
        """
        This method generates a JWT token for a user.

        :param user: user object
        :return:
        """
        user_role_id = user.role_id
        role = Role.get_by(id=user_role_id)
        role_name = role.name

        user_domain_id = user.domain_id
        domain = Domain.get_by(id=user_domain_id)
        domain_name = domain.name

        payload = {
            "id": user.id,
            "fullname": user.fullname,
            "email": user.email,
            "role": role_name,
            "domain": domain_name,
            "exp": datetime.utcnow() + timedelta(hours=TOKEN_EXPIRATION_HOURS),
            "iat": datetime.utcnow()
        }
        return jwt.encode(
            payload=payload,
            key=TOKEN_SECRET,
            algorithm='HS256'
        )

    @staticmethod
    def decode_token(token: str) -> dict:
        """
        This method decodes the JWT token

        :param token: JWT token
        :return: Decoded payload
        """
        try:
            payload = jwt.decode(token, key=TOKEN_SECRET,
                                 algorithms=['HS256'])
            return payload
        except jwt.ExpiredSignatureError:
            abort(401, "Token has expired.")
        except jwt.InvalidTokenError:
            abort(401, "Invalid token.")
