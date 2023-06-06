import jwt
from datetime import datetime, timedelta
from werkzeug.security import check_password_hash
from .models.user import User

class AuthHandler:

    SECRET_KEY = 'H€t1C'

    @staticmethod
    def authenticate(email: str, password: str):
        """
        This method authenticates a user.

        :param email: user email
        :param password: user password
        """
        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password, password):
            return user

    def generate_token(self, user: User):
        """
        This method generates a JWT token for a user.

        :param user: user object
        :return:
        """
        payload = {
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "exp": datetime.utcnow() + timedelta(seconds=30),
            "iat": datetime.utcnow()
        }
        return jwt.encode(
            payload=payload,
            key=self.SECRET_KEY,
            algorithm='HS256'
        )

    def decode_token(self, token: str):
        """
        This method decodes the JWT token

        :param token: JWT token
        :return:
        """
        try:
            payload = jwt.decode(token, self.SECRET_KEY, algorithms=['HS256'])
            return payload
        except jwt.ExpiredSignatureError:
            raise {
                'status': 401,
                'message': 'Signature expired. Please log in again.'
            }
        except jwt.InvalidTokenError as e:
            raise {
                'status': 401,
                'message': 'Invalid token.'
            }
