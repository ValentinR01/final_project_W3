from models.user import User
from models.domain import Domain
from werkzeug.security import generate_password_hash
from helpers.auth import AuthHandler
from flask_restx import abort
from flask import make_response
from conf import TOKEN_EXPIRATION_HOURS
import logging, datetime
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
    role_id = data.get('role_id')
    domain_id = data.get('domain_id')

    if not email or not fullname or not password or not role_id or not \
            domain_id:
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
        domain_id=domain_id, role_id=role_id
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
        # TODO : Secure cookie set
        headers = [
            (
                'Set-Cookie',
                f'authorization={token}; '
                f'max-age={TOKEN_EXPIRATION_HOURS * 60 * 60}; path=/'
            )
        ]
        return (
            {'access_token': token, 'message': 'Login successful'},
            200, headers
        )

    except Exception as e:
        logging.error(e)
        return {e}, 500


def get_user_by_domain(domain_name):
    domain = Domain.get_by(name=domain_name)
    if domain is None:
        return {'message': 'Domain not found'}, 404

    domain_id = domain.id
    user_list = User.get_all_by(domain_id=domain_id)

    if user_list is None:
        return {'users': []}, 200

    return {'users': user_list}, 200


def get_all_users():
    user_list = User.get_all()
    return {'users': user_list}, 200
