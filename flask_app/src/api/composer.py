from flask import request
from flask_restx import Namespace, Resource, fields, Api
from services.composer import \
    create_composer, get_composer_by_id, get_all_composers, update_composer
# from helpers.decorators import rights_manager

namespace = Namespace('composers', 'Composer related endpoints')

api = Api()

composer_register_model = namespace.model('Register', {
    'fullname': fields.String(required=True),
    'biography': fields.String(required=False),
    'language_id': fields.Integer(required=True, default=1),
    'composer_parent': fields.Integer(required=False),
    'publishable': fields.Boolean(required=False, default=False)
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


@namespace.route('/<int:composer_id>', methods=['GET', 'PUT'])
@api.doc(params={'composer_id': 'The composer id'})
class GetByComposerId(Resource):
    @namespace.marshal_with(composer_model, skip_none=True)
    def get(self, composer_id):
        """Get composer by id"""
        return get_composer_by_id(composer_id)

    @namespace.expect(composer_register_model)
    def put(self, composer_id):
        """Update a composer"""
        data = request.json
        return update_composer(data, composer_id)


@namespace.route('', methods=['GET', 'POST'])
class Composers(Resource):
    @namespace.marshal_with(composers_list_model)
    def get(self):
        """Get all composers"""
        return get_all_composers()

    @namespace.expect(composer_register_model)
    @namespace.response(201, 'Composer well created')
    def post(self):
        """Register a new composer"""
        data = request.json
        return create_composer(data)
