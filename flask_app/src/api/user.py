import re
from models.user import User
from flask import request
from flask_restx import Namespace, Resource, fields
from services.user_service import register_service, login_service, get_user_by_domain, get_all_users


namespace = Namespace('users', 'User related endpoints')

register_model = namespace.model('Register', {
    'fullname': fields.String(),
    'email': fields.String(),
    'password': fields.String()
})

login_model = namespace.model('Login', {
    'email': fields.String(),
    'password': fields.String()
})

 # @namespace.marshal_list_with(register_model)
 # @namespace.response(200, 'Successfully register')


@namespace.route('/register', methods=['POST'])
class Register(Resource):
    @namespace.expect(register_model)
    @namespace.response(201, 'Successfully register')
    def post(self):
        """Register a new user"""
        data = request.json
        return register_service(data)

    
@namespace.route('/login', methods=['POST'])
class Login(Resource):
    @namespace.expect(login_model)
    @namespace.response(200, 'Successfully login')
    def post(self):
        """Login a user"""
        data = request.json
        return login_service(data)
    

@namespace.route('/domain/{domain_name}', methods=['GET'])
class Domain(Resource):
    def get(self, domain_name):
        """Filter users by domain name"""
        return get_user_by_domain(domain_name) #TODO


@namespace.route('', methods=['GET'])
class Users(Resource):
    def get(self):
        """Get all users"""
        return get_all_users() #TODO
    