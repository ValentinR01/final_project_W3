from flask_restx import Namespace, Resource, fields, Api
from services.meta_value import get_all_meta_values
from flask_restx import reqparse


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

parser = reqparse.RequestParser(bundle_errors=True)
parser.add_argument("meta_key", type=str, required=False, location="args")


@namespace.route('', methods=['GET'])
@namespace.response(200, meta_values_list_model)
class MetaValues(Resource):
    @namespace.marshal_with(meta_values_list_model)
    @api.expect(parser)
    def get(self):
        args = parser.parse_args()
        """Get all meta_values"""
        meta_key = (args["meta_key"])
        return get_all_meta_values(meta_key)
