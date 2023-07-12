from flask import request
from flask_restx import Namespace, Resource, fields, Api
from services.speaker import register_service, get_all_speakers, get_speaker_by_id


namespace = Namespace('speakers', 'Speaker related endpoints')

api = Api()

speaker_register_model = namespace.model(
    'speaker_register_model', {
        'fullname': fields.String(required=True)
    }
)

speaker_model = namespace.model(
    'speaker', {
        'id': fields.Integer(),
        'fullname': fields.String(required=True),
        'biography': fields.String(required=True),
        'last_update': fields.DateTime(),
        'publishable': fields.Boolean(),
        'speaker_parent': fields.Integer(),
        'language_id': fields.Integer()
    }
)

speakers_list_model = namespace.model(
    'speakers_list', {
        'speakers': fields.List(fields.Nested(speaker_model))
    }, default={}
)


@namespace.route('/register', methods=['POST'])
class Register(Resource):
    @namespace.expect(speaker_register_model)
    @namespace.response(201, 'Speaker well created')
    def post(self):
        """Register a new speaker"""
        data = request.json
        return register_service(data)


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
    @namespace.marshal_with(speaker_model, skip_none=True)
    def get(self, speaker_id):
        """Get speaker by id"""
        return get_speaker_by_id(speaker_id)


@namespace.route('', methods=['GET'])
class Speakers(Resource):
    @namespace.marshal_with(speakers_list_model)
    def get(self):
        """Get all speakers"""
        return get_all_speakers()
