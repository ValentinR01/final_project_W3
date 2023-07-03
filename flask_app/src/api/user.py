import re
from flask_app.src.models.user import User
from flask import request
from flask_restx import Namespace, Resource, fields, Api
from werkzeug.security import generate_password_hash
from flask_app.src.auth import AuthHandler

namespace = Namespace('user', ' User related endpoints')

api = Api()

register_model = namespace.model(
    'Register', {
        'fullname': fields.String(required=True, default='saline'),
        'email': fields.String(required=True, default='saline@saline.com'),
        'password': fields.String(required=True, default='Sªl1nĒ')
    }
)

login_model = namespace.model(
    'Login', {
        'email': fields.String(required=True, default='saline@saline.com'),
        'password': fields.String(required=True, default='Sªl1nĒ')
    }
)


@namespace.route('/register', methods=['POST'])
class Register(Resource):
    # @namespace.marshal_list_with(register_model)
    @namespace.expect(register_model)
    # @namespace.response(200, 'Successfully register')
    def post(self):
        """Register a new user"""
        data = request.json
        email = data.get('email')
        fullname = data.get('fullname')
        password = data.get('password')

        if not email or not fullname or not password:
            return {'message': 'Missing parameters'}, 400

        if re.match(r"[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{"
                    r"|}~-]+)*@saline.com", email) is None:
            return {'message': 'Invalid email'}, 400

        if User.find_by_email(email):
            return {'message': 'Email already exists'}, 409

        hashed_password = generate_password_hash(password, method='pbkdf2')
        new_user = User(
            fullname=fullname, password=hashed_password, email=email
        )
        new_user.create()

        return {'message': 'User created successfully'}, 201


@namespace.route('/login', methods=['POST'])
class Login(Resource):
    @namespace.expect(login_model)
    def post(self):
        try:
            auth_handler = AuthHandler()
            data = request.json
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


@namespace.route('/domain/<domain_name>', methods=['GET'])
class Domain(Resource):
    @api.doc(
        params={
            'domain_name': {
                'description': 'The domain name', 'required': True,
                'type': 'string'
            }
        }
    )
    def get(self, domain_name: str):
        return {'message': domain_name}, 200
