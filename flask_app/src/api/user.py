from flask import request
from flask_restx import Namespace, Resource, fields, Api
from services.user import \
    register_service, login_service, get_user_by_domain, get_all_users


namespace = Namespace('users', 'User related endpoints')

api = Api()

user_register_model = namespace.model(
    'user_register', {
        'fullname': fields.String(required=True, default='saline'),
        'email': fields.String(required=True, default='saline@saline.com'),
        'password': fields.String(required=True, default='Sªl1nĒ'),
        'role': fields.Integer(required=True, default=1),
        'domain': fields.Integer(required=True, default=1)
    }
)

user_login_model = namespace.model(
    'user_login', {
        'email': fields.String(required=True, default='saline@saline.com'),
        'password': fields.String(required=True, default='Sªl1nĒ')
    }
)

 # @namespace.marshal_list_with(register_model)
 # @namespace.response(200, 'Successfully register')


@namespace.route('/register', methods=['POST'])
class Register(Resource):
    """Register a new user"""
    @namespace.expect(user_register_model)
    @namespace.response(201, 'Successfully register')
    def post(self):
        """Register a new user"""
        data = request.json
        return register_service(data)

    
@namespace.route('/login', methods=['POST'])
class Login(Resource):
    """Login a user"""
    @namespace.expect(user_login_model)
    @namespace.response(200, 'Successfully login')
    def post(self):
        """Login a user"""
        data = request.json
        return login_service(data)
    

@namespace.route('/domain/<domain_name>', methods=['GET'])
class Domain(Resource):
    """Filter users by domain name"""
    @api.doc(
        params={
            'domain_name': {
                'description': 'The domain name', 'required': True,
                'type': 'string'
            }
        }
    )
    def get(self, domain_name):
        """Filter users by domain name"""
        return get_user_by_domain(domain_name) #TODO


@namespace.route('', methods=['GET'])
class Users(Resource):
    def get(self):
        """Get all users"""
        return get_all_users() #TODO
