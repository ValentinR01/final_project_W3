from flask_restx import Resource, fields, Api
from services.language import get_all_languages
from api.asset import namespace as namespace

api = Api()

language_model = namespace.model(
    'language', {
        'id': fields.Integer(),
        'content': fields.String,
        'created_at': fields.DateTime(),
        'external_name': fields.String(),
        'posted_by': fields.Integer(),
        'fullname': fields.String(attribute='user.fullname'),
        'asset_id': fields.Integer()
    }
)

language_list_model = namespace.model(
    'language_list', {
        'languages': fields.List(fields.Nested(language_model))
    }, default={}
)


@namespace.route('/language', methods=["GET"])
class Language(Resource):
    # @namespace.marshal_with(language_list_model)
    def get(self):
        """Get all languages"""
        return get_all_languages()
