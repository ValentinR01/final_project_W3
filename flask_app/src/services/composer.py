from models.composer import Composer
from services.base import create_entity, update_entity


def create_composer(data):
    return create_entity(
        data=data, entity=Composer, fullname=data.get('fullname')
    )


def update_composer(data, composer_id):
    return update_entity(
        data=data, entity=Composer, entity_id=composer_id
    )


def get_composer_by_id(composer_id):
    composer = Composer.get_by(id=composer_id)
    if not composer:
        return {'message': 'Composer not found'}, 404
    return composer, 200


def get_all_composers():
    composers = Composer.get_all()
    return {'composers': composers}, 200
