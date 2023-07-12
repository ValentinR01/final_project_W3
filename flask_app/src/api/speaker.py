import re
from models.user import User
from flask import request
from flask_restx import Namespace, Resource, fields, Api
from services.speaker import register_service, get_all_speakers, get_speaker_by_id

namespace = Namespace('speakers', 'Speaker related endpoints')

api = Api()

register_model = namespace.model('Register', {
    'fullname': fields.String()
})

@namespace.route('/register', methods=['POST'])
class Register(Resource):
    @namespace.expect(register_model)
    @namespace.response(201, 'Speaker well created')
    def post(self):
        """Register a new speaker"""
        data = request.json
        return register_service(data)
    

@namespace.route('', methods=['GET'])
class GetAll(Resource):
    @namespace.response(200, 'Speaker list')
    def get(self):
        """Get all speakers"""
        return get_all_speakers(self)
    

@namespace.route('/<speaker_id>', methods=['GET'])
class GetBySpeakerId(Resource):
    @api.doc(
        params={
            'speaker_id': {
                'description': 'The speaker id', 'required': True,
                'type': 'integer'
            }
        }
    )
    def get(self, speaker_id):
        """Get speaker by id"""
        return get_speaker_by_id(speaker_id)