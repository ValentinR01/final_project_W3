from flask import request
from flask_restx import Namespace, Resource, fields, Api
from services.speaker import create_speaker, get_all_speakers, \
    get_speaker_by_id, update_speaker


namespace = Namespace('speakers', 'Speaker related endpoints')

api = Api()

speaker_register_model = namespace.model(
    'speaker_register_model', {
        'fullname': fields.String(required=True),
        'biography': fields.String(required=False),
        'language_id': fields.Integer(required=True, default=1),
        'speaker_parent': fields.Integer(required=False),
        'publishable': fields.Boolean(required=False, default=False)
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


@namespace.route('/<int:speaker_id>', methods=['GET', 'PUT'])
@api.doc(params={'speaker_id': 'The speaker id'})
class GetBySpeakerId(Resource):
    @namespace.marshal_with(speaker_model, skip_none=True)
    def get(self, speaker_id):
        """Get speaker by id"""
        return get_speaker_by_id(speaker_id)

    @namespace.expect(speaker_register_model)
    def put(self, speaker_id):
        """Update a speaker"""
        data = request.json
        return update_speaker(data, speaker_id)


@namespace.route('', methods=['GET', 'POST'])
class Speakers(Resource):
    @namespace.marshal_with(speakers_list_model)
    def get(self):
        """Get all speakers"""
        return get_all_speakers()

    @namespace.expect(speaker_register_model)
    @namespace.response(201, 'Speaker well created')
    def post(self):
        """Register a new speaker"""
        data = request.json
        return create_speaker(data)
