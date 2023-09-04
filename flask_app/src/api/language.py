from flask_restx import Namespace, Resource, fields, Api
from services.language import get_all_languages

namespace = Namespace('languages', 'Language related endpoints')

api = Api()

language_model = namespace.model(
    'language', {
        'id': fields.Integer(),
        'name': fields.String,
        'code': fields.String()
    }
)

language_list_model = namespace.model(
    'language_list', {
        'languages': fields.List(fields.Nested(language_model))
    }, default={}
)


@namespace.route('', methods=["GET"])
class Language(Resource):
    @namespace.marshal_with(language_list_model)
    def get(self):
        """Get all languages"""
        return get_all_languages()
