from flask_restx import Namespace, Resource, Api
from services.base import get_all_entities
from models.specialty import Specialty
from models.user import specialties_users


namespace = Namespace('specialties', 'Specialties by user')

api = Api()


@namespace.route('/', methods=['GET'])
class GetAll(Resource):
    """Get all specialties"""
    def get(self):
        """Get all specialties"""
        return get_all_entities(entity=Specialty)


@namespace.route('/<int:user_id>', methods=['GET'])
class GetByUser(Resource):
    """Get all specialties by user"""
    def get(self, user_id):
        """Get all specialties by user"""
        return specialties_users(user_id=user_id)
