# from models.user import User
from models.user import User
from werkzeug.security import generate_password_hash
from auth import AuthHandler
import logging
import re


def register_service(userdata):
    if not userdata['email']  or not userdata['fullname']  or not userdata['password'] :
        return {'message': 'Missing parameters'}, 400

    if re.match(r"[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{"
                r"|}~-]+)*@saline.com", userdata['email']) is None:
        return {'message': 'Invalid email'}, 400

    if User.find_by_email(userdata['email']):
        return {'message': 'Email already exists'}, 409

    hashed_password = generate_password_hash(userdata['password'], method='pbkdf2')
    new_user = User(fullname=userdata['fullname'], password=hashed_password,
                    email=userdata['email'])
    new_user.create()

    return {'message': 'Successfully register'}, 201

def login_service(userdata):
        try:
            auth_handler = AuthHandler()
            user = auth_handler.authenticate(
                email=userdata['email'], password=userdata['password']
            )
            if not user:
                return {'message': 'Invalid email or password'}, 401

            token = auth_handler.generate_token(user)
            return {
                    'access_token': token,
                    'message': 'Login successful'
                }, 200
        except Exception as e:
            logging.error(e)
            return {}, 500
        
def get_user_by_domain(domain_name):
    user_list = User.find_by_domain(domain_name)
    return user_list, 200 #TODO

def get_all_users():
    user_list = User.get_all()
    return user_list, 200 #TODO

# def signup_service(userdata):
#     try:
#         email_check = User.objects[:1](email=userdata['email'])
#         if email_check:
#             return {"status": 404, "message": "email already exists"}
#         else:
#             name = userdata['name']
#             email = userdata['email']
#             image = userdata['image']
#             mobile = userdata['mobile']
#             password = encrypt_password(userdata['password'])
#
#             user = User(name=name, email=email, image=image,
#                         mobile=mobile, password=password)
#             user.save()
#
#             return make_response({'message': 'succesfully inserted'}, 200)
#
#     except Exception as e:
#         return make_response({'message': str(e)}, 404)
#
#
# def login_service(user_credentials):
#     try:
#         email_check = User.objects[:1](email=user_credentials['email'])
#         if not email_check:
#             return {"status": 404, "message": "email does not exists"}
#         else:
#             for user in email_check:
#                 payload = {"email": user['email'], "_id": str(user['id']), 'exp': datetime.datetime.utcnow(
#                 ) + datetime.timedelta(minutes=60)}
#                 secret = os.environ.get('TOKEN_SECRET')
#                 if compare_passwords(user_credentials['password'], user['password']):
#                     token = generate_token(payload, secret)
#                     return make_response({'token': token}, 200)
#                 else:
#                     return make_response({'message': 'Invalid password'}, 403)
#
#     except Exception as e:
#         return make_response({'message': str(e)}, 404)
