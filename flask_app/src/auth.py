import jwt
from datetime import datetime, timedelta
from werkzeug.security import check_password_hash
from flask_app.src.models.user import User
from flask_app.src.conf import TOKEN_SECRET, TOKEN_EXPIRATION_HOURS


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
        user = User.find_by_email(email)

        if user and check_password_hash(user.password, password):
            return user

    @staticmethod
    def generate_token(user: User):
        """
        This method generates a JWT token for a user.

        :param user: user object
        :return:
        """
        payload = {
            "id": user.id,
            "username": user.username,
            "email": user.email,
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
        :return:
        """
        payload = jwt.decode(
            jwt=token, key=TOKEN_SECRET, algorithms=['HS256']
        )
        return payload
