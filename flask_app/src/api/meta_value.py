from flask_restx import Namespace, Resource, fields
from services.meta_value import get_all_meta_values

namespace = Namespace('meta_value', 'Metadata related endpoints')


@namespace.route('', methods=['GET'])
class GetAll(Resource):
    def get(self):
        """Get all metadatas"""
        return get_all_meta_values()
    
