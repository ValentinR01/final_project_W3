from models.composer import Composer


def register_service(data):
    if Composer.get_by(fullname=data['fullname']):
        return {'message': 'Composer already exists'}, 409

    new_composer = Composer(fullname=data['fullname'])
    new_composer.create()

    return {'message': 'Composer well created'}, 201


def get_composer_by_id(composer_id):
    composer = Composer.get_by(id=composer_id)
    if not composer:
        return {'message': 'Composer not found'}, 404
    return composer, 200
