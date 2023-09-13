from flask_restx import Namespace, Resource, Api
from services.base import get_all_entities
from models.domain import Domain


namespace = Namespace('domains', 'Domains with their id')

api = Api()


@namespace.route('/', methods=['GET'])
class GetAll(Resource):
    """Get all domains"""
    def get(self):
        """Get all domains"""
        return get_all_entities(entity=Domain)
