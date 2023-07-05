from models.speaker import Speaker
import logging
import re


def register_service(speakerdata):
    if Speaker.find_by_name(speakerdata['fullname']):
        return {'message': 'Speaker already exists'}, 409

    new_speaker = Speaker(fullname=speakerdata['fullname'])
    new_speaker.create()

    return {'message': 'Speaker well created'}, 201


def get_all_speakers():
    speaker_list = Speaker.get_all()
    return speaker_list, 200 

def get_speaker_by_id(speaker_id):
    speaker = Speaker.find_by_id(speaker_id)
    return speaker, 200 

