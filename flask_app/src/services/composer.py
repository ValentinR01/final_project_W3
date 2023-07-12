from models.composer import Composer
from models.domain import Domain
from werkzeug.security import generate_password_hash
from helpers.auth import AuthHandler
from flask_restx import abort
import logging
import re


def register_service(data):
    if Composer.get_by(fullname=data['fullname']):
        return {'message': 'Composer already exists'}, 409

    new_composer = Composer(fullname=data['fullname'])
    new_composer.create()

    return {'message': 'Composer well created'}, 201
