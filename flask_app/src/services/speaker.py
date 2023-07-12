from models.speaker import Speaker


def register_service(data):
    if Speaker.get_by(fullname=data['fullname']):
        return {'message': 'Speaker already exists'}, 409

    new_speaker = Speaker(fullname=data['fullname'])
    new_speaker.create()

    return {'message': 'Speaker well created'}, 201


def get_speaker_by_id(speaker_id):
    speaker = Speaker.get_by(id=speaker_id)
    if not speaker:
        return {'message': 'Speaker not found'}, 404
    return speaker, 200


def get_all_speakers():
    speakers_list = Speaker.get_all()
    return {'speakers': speakers_list}, 200
