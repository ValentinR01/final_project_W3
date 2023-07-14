from flask_restx import Namespace, Resource, fields, Api
from services.meta_value import get_all_meta_values

namespace = Namespace('meta_value', 'Metadata related endpoints')

api = Api()

meta_values_model = namespace.model(
    'meta_values_model', {
        'value': fields.String(),
        'meta_key_id': fields.Integer()
    }
)

meta_values_list_model = namespace.model(
    'meta_values_list_model', {
        'meta_values': fields.List(fields.Nested(meta_values_model, default={}))
    }
)


@namespace.route('', methods=['GET'])
@namespace.response(200, meta_values_list_model)
class MetaValues(Resource):
    @namespace.marshal_with(meta_values_list_model)
    def get(self):
        """Get all meta_values"""
        return get_all_meta_values()
