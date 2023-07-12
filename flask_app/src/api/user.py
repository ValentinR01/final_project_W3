from flask import request
from flask_restx import Namespace, Resource, fields, Api
from helpers.decorators import rights_manager
from services.user import \
    register_service, login_service, get_user_by_domain, get_all_users


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
        'password': fields.String(),
        'profile_picture': fields.String(),
        'created_at': fields.DateTime(),
        'count_assigning_asset': fields.String(),
        'role_id': fields.Integer(),
        'domain_id': fields.Integer()
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

    token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6NCwiZnVsbG5hbWU" \
            "iOiJzYWxpbiIsImVtYWlsIjoic2FsaW5Ac2FsaW5lLmNvbSIsInJvbGUiOiJ" \
            "3b3JrZXIiLCJkb21haW4iOiJyZWRhY3Rpb24iLCJleHAiOjE2ODkwMjk5MDI" \
            "sImlhdCI6MTY4ODk5MzkwMn0.r4UalimTKPHVIDABZei3px6armJdAd_TOVA" \
            "M_uEazTM"

    """Filter users by domain name"""
    @api.doc(
        params={
            'domain_name': {
                'description': 'The domain name', 'required': True,
                'type': 'string'
            }
        }
    )
    @rights_manager(token=token, role='worker', domain='redaction')
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