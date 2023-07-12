from models.speaker import Speaker
import logging
import re


def register_service(data):
    if Speaker.get_by(fullname=data['fullname']):
        return {'message': 'Speaker already exists'}, 409

    new_speaker = Speaker(fullname=data['fullname'])
    new_speaker.create()

    return {'message': 'Speaker well created'}, 201


def get_all_speakers(self):
    speaker_list = Speaker.get_all(self)
    return speaker_list, 200 

def get_speaker_by_id(speaker_id):
    speaker = Speaker.find_by_id(speaker_id)
    return speaker, 200 

