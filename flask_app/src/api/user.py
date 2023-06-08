import re
from models.user import User
from flask import request
from flask_restx import Namespace, Resource, fields
from werkzeug.security import generate_password_hash
from auth import AuthHandler

namespace = Namespace('user', ' User related endpoints')

register_model = namespace.model('Register', {
    'username': fields.String(),
    'email': fields.String(),
    'password': fields.String()
})


# hello_world_example = {'message': 'Hello World!'}


# @namespace.route('')
# class HelloWorld(Resource):
#     @namespace.marshal_list_with(hello_world_model)
#     @namespace.response(500, 'Internal Server error')
#     def get(self):
#         """Hello world message endpoint"""
#
#         return hello_world_example


@namespace.route('/register', methods=['POST'])
class Register(Resource):
    # @namespace.marshal_list_with(register_model)
    @namespace.expect(register_model)
    # @namespace.response(200, 'Successfully register')
    def post(self, data):
        email = data.get('email')
        username = data.get('username')
        password = data.get('password')

        if not email or not username or not password:
            return {'message': 'Missing parameters'}, 400

        if re.match(r"[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{"
                    r"|}~-]+)*@saline.com", email) is None:
            return {'message': 'Invalid email'}, 400

        if User.query.filter_by(email=email).first():
            return {'message': 'Email already exists'}, 409

        hashed_password = generate_password_hash(password, method='pbkdf2')
        new_user = User(username=username, password=hashed_password, email=email)
        new_user.create()

        return {'message': 'User created successfully'}, 201


@namespace.route('/login', methods=['POST'])
class Login(Resource):
    @namespace.response(200, 'Successfully register')
    def post(self):
        try:
            auth_handler = AuthHandler()
            data = request.form
            user = auth_handler.authenticate(
                email=data.get('email'), password=data.get('password')
            )
            if not user:
                return {'message': 'Invalid email or password'}, 401

            token = auth_handler.generate_token(user)
            return {
                    'access_token': token,
                    'message': 'Login successful'
                }, 200
        except Exception as e:
            return {'message': str(e)}, 500
