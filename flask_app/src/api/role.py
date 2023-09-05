from flask_restx import Namespace, Resource, Api
from services.base import get_all_entities
from models.role import Role


namespace = Namespace('roles', 'Roles with their id')

api = Api()


@namespace.route('/', methods=['GET'])
class GetAll(Resource):
    """Get all roles"""
    def get(self):
        """Get all roles"""
        return get_all_entities(entity=Role)
