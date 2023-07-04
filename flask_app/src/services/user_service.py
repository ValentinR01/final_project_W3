from models.user import User
from werkzeug.security import generate_password_hash
from helpers.auth import AuthHandler
import logging
import re


def register_service(data):
    """
    Register a new user

    :param data: json data from request
    :return: json response
    """
    email = data.get('email')
    fullname = data.get('fullname')
    password = data.get('password')
    role = data.get('role')
    domain = data.get('domain')

    if not email or not fullname or not password or not role or not domain:
        return {'message': 'Missing parameters'}, 400

    if re.match(r"[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{"
                r"|}~-]+)*@saline.com", email) is None:
        return {'message': 'Invalid email'}, 400

    if User.get_by(fullname=fullname) or User.get_by(email=email):
        return {'message': 'User already exists'}, 409

    # TODO: HS256 or pbkdf2
    hashed_password = generate_password_hash(password, method='pbkdf2')
    new_user = User(
        fullname=fullname, password=hashed_password, email=email,
        domain_id=domain, role_id=role
    )
    new_user.create()

    return {'message': 'User created successfully'}, 201


def login_service(userdata):
    try:
        auth_handler = AuthHandler()
        user = auth_handler.authenticate(
            email=userdata.get('email'), password=userdata.get('password')
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
    user_list = User.get_by(name=domain_name)
    return user_list, 200 #TODO


def get_all_users():
    user_list = User.get_all()
    return user_list, 200 #TODO
