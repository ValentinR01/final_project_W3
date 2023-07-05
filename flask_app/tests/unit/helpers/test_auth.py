import jwt, sys
from datetime import datetime, timedelta

sys.path.append( '/flask_app/src/' )
from helpers.auth import AuthHandler
from models.user import User
from conf import TOKEN_SECRET, TOKEN_EXPIRATION_HOURS

class TestAuthHelper:
    @staticmethod
    def test_decode_token():
        token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6bnVsbCwiZnVsbG5hbWUiOiJWYWxlbnRpbiIsImVtYWlsIjoidmFsZW50aW5Ac2FsaW5lLmNvbSIsImV4cCI6MTY4ODU0OTYxMywiaWF0IjoxNjg4NTEzNjEzfQ.-Pq5mDh_qscLM-TaHDQ30ER9856yVR6RsH17-ZnFRaI"

        result = AuthHandler.decode_token(token)

        # Perform assertions to validate the result
        assert isinstance(result, dict) #TODO


    @staticmethod
    def test_generate_token():
        # Create a user object for testing
        user = User(fullname="Valentin", email="valentin@saline.com", password="123", domain_id=1)
        
        # Call the generate_token method and get the token
        token = AuthHandler.generate_token(user)
        
        # Verify that the token is not empty
        assert token is not None
        
        # Verify that the token can be decoded using the TOKEN_SECRET
        decoded = jwt.decode(token, key=TOKEN_SECRET, algorithms=['HS256'])
        
        # Verify that the decoded payload contains the expected information
        assert decoded['id'] == user.id
        assert decoded['fullname'] == user.fullname
        assert decoded['email'] == user.email
        
        # Verify that the token expiration time is set correctly
        expiration_time = datetime.utcnow() + timedelta(hours=TOKEN_EXPIRATION_HOURS)
        difference = (expiration_time - datetime.utcfromtimestamp(decoded['exp'])).total_seconds()
        assert (difference < 5) #in seconds

        # Verify that the token issue time is set correctly
        assert 'iat' in decoded  # Check if 'iat' key exists in the decoded payload
        


