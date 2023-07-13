from flask import request
from models.composer import Composer
from flask_restx import Namespace, Resource, fields, Api
from services.composer import \
    register_service, get_composer_by_id
from helpers.decorators import rights_manager

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
        """Get speaker by id"""
        return get_composer_by_id(composer_id)
