from flask import request
from flask_restx import Namespace, Resource, fields, Api
# from helpers.decorators import rights_manager
from services.user import \
    register_service, login_service, get_user_by_domain, get_all_users, \
    get_user_by_id


namespace = Namespace('users', 'User related endpoints')

api = Api()

user_register_model = namespace.model(
    'user_register_model', {
        'fullname': fields.String(required=True, default='saline'),
        'email': fields.String(required=True, default='saline@saline.com'),
        'password': fields.String(required=True, default='Sªl1nĒ'),
        'role_id': fields.Integer(required=True, default=1),
        'domain_id': fields.Integer(required=True, default=1)
    }
)

user_login_model = namespace.model(
    'user_login', {
        'email': fields.String(required=True, default='saline@saline.com'),
        'password': fields.String(required=True, default='Sªl1nĒ')
    }
)

users_model = namespace.model(
    'users_model', {
        'id': fields.Integer(),
        'email': fields.String(),
        'fullname': fields.String(),
        'profile_picture': fields.String(),
        'created_at': fields.DateTime(),
        'count_assigning_asset': fields.String(),
        'role': fields.String(attribute='role.name'),
        'domain': fields.String(attribute='domain.name')
    }
)

user_list_model = namespace.model(
    'user_list_model', {
        'users': fields.List(fields.Nested(users_model, default={}))
    }
)


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

    token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6NSwiZnVsbG5hbWUiO" \
            "iJzYWxpbmUiLCJlbWFpbCI6InNhbGluZUBzYWxpbmUuY29tIiwicm9sZSI6Indv" \
            "cmtlciIsImRvbWFpbiI6InJlZGFjdGlvbiIsImV4cCI6MTY5NzIyMDE2NSwiaWF" \
            "0IjoxNjk0NjI4MTY1fQ.duieAudQgx8JGmWMdksZkgxL2kPdjd_J-64pUXq_Hqw"

    """Filter users by domain name"""
    @api.doc(
        params={
            'domain_name': {
                'description': 'The domain name', 'required': True,
                'type': 'string'
            }
        }
    )
    # @rights_manager(token=token, role='worker', domain='redaction')
    @namespace.marshal_with(user_list_model)
    @namespace.response(200, '')
    def get(self, domain_name):
        """Filter users by domain name"""
        return get_user_by_domain(domain_name)


@namespace.route('', methods=['GET'])
@namespace.response(200, user_list_model)
class Users(Resource):
    @namespace.marshal_with(user_list_model)
    def get(self):
        """Get all users"""
        return get_all_users()


@namespace.route('/<int:user_id>', methods=['GET'])
@namespace.response(200, users_model)
class UserByID(Resource):
    @namespace.marshal_with(users_model)
    def get(self, user_id):
        """Get user by ID"""
        return get_user_by_id(user_id)
