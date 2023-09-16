from flask_restx import Namespace, Resource, Api
from services.specialty import \
    get_specialties, get_specialties_by_user, post_user_specialty


namespace = Namespace('specialties', 'Specialties by user')

api = Api()


@namespace.route('/', methods=['GET'])
class GetAll(Resource):
    def get(self):
        """Get all specialties"""
        return get_specialties()


@namespace.route('/user/<int:user_id>', methods=['GET'])
class GetByUser(Resource):
    def get(self, user_id):
        """Get all specialties by user"""
        return get_specialties_by_user(user_id)


@namespace.route(
    '/user/<int:user_id>/specialty/<int:specialty_id>', methods=['POST']
)
class AddUserToSpecialty(Resource):
    def post(self, user_id, specialty_id):
        """Add a new user to a specialty"""
        return post_user_specialty(user_id, specialty_id)
