from flask import request
from flask_restx import Namespace, Resource, fields, Api
from services.composer import \
    register_service
from helpers.decorators import rights_manager

namespace = Namespace('composers', 'Composer related endpoints')

api = Api()

register_model = namespace.model('Register', {
    'fullname': fields.String()
})

@namespace.route('/register', methods=['POST'])
class Register(Resource):
    @namespace.expect(register_model)
    @namespace.response(201, 'Composer well created')
    def post(self):
        """Register a new composer"""
        data = request.json
        return register_service(data)