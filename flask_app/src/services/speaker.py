from models.speaker import Speaker
from services.base import create_entity, update_entity


def create_speaker(data):
    """Create a new speaker"""
    return create_entity(
        data=data, entity=Speaker, fullname=data.get('fullname')
    )


def update_speaker(data, speaker_id):
    """Update a speaker"""
    return update_entity(
        data=data, entity=Speaker, entity_id=speaker_id
    )


def get_speaker_by_id(speaker_id):
    speaker = Speaker.get_by(id=speaker_id)
    if not speaker:
        return {'message': 'Speaker not found'}, 404
    return speaker, 200


def get_all_speakers():
    speakers_list = Speaker.get_all()
    return {'speakers': speakers_list}, 200
