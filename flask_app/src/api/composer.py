from flask import request
from flask_restx import Namespace, Resource, fields, Api
from services.composer import \
    register_service, get_composer_by_id, get_all_composers
# from helpers.decorators import rights_manager

namespace = Namespace('composers', 'Composer related endpoints')

api = Api()

register_model = namespace.model('Register', {
    'fullname': fields.String()
})

composer_model = namespace.model(
    'composer', {
        'id': fields.Integer(),
        'fullname': fields.String(required=True),
        'biography': fields.String(required=True),
        'last_update': fields.DateTime(),
        'publishable': fields.Boolean(),
        'composer_parent': fields.Integer(),
        'language_id': fields.Integer()
    }
)

composers_list_model = namespace.model(
    'composers_list', {
        'composers': fields.List(fields.Nested(composer_model))
    }, default={}
)


@namespace.route('/register', methods=['POST'])
class Register(Resource):
    @namespace.expect(register_model)
    @namespace.response(201, 'Composer well created')
    def post(self):
        """Register a new composer"""
        data = request.json
        return register_service(data)


@namespace.route('/<composer_id>', methods=['GET'])
class GetByComposerId(Resource):
    @api.doc(
        params={
            'composer_id': {
                'description': 'The composer id', 'required': True,
                'type': 'integer'
            }
        }
    )
    @namespace.marshal_with(composer_model, skip_none=True)
    def get(self, composer_id):
        """Get composer by id"""
        return get_composer_by_id(composer_id)


@namespace.route('', methods=['GET'])
class Composers(Resource):
    @namespace.marshal_with(composers_list_model)
    def get(self):
        """Get all composers"""
        return get_all_composers()
