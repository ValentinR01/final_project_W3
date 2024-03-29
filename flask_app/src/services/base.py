from db import db
from helpers.etl import transformation


def create_entity(entity: db.Model, data: dict, **kwargs):
    """
    Base to create entity

    :param data: json data
    :param entity: entity to create
    :param kwargs: values to check
    """
    if not data:
        return {'message': 'Missing parameters'}, 400
    if entity.get_by(**kwargs):
        return {'message': f'{entity.__tablename__} already exists'}, 409
    try:
        entity_inst = entity(**data)
        entity_inst.create()
        # created_id = entity_inst.create()
    except Exception as e:
        return {'error': str(e)}, 500
    return {
               'message':
               f'The {entity.__tablename__} has been successfully created'},\
        200


def get_all_entities(entity: db.Model, **filters):
    """
    Base to get all entities

    :param entity: entity to get
    :param filters: filter to apply
    """
    try:
        entity_list = entity.get_all_by(**filters)
        if not entity_list:
            return {'message': 'No entities found'}, 404
        return {f"all_{entity.__tablename__}": transformation(entity_list)}, \
            200
    except Exception as e:
        return {'error': str(e)}, 500


def search_entities(entity, search: str, *columns):
    """
    Base to search entities from some specific columns with a search value

    :param entity: entity
    :param search: search value
    :param columns: columns to search
    """
    try:
        entity_list = entity.get_entities_by_search_values(search, columns)
        if not entity_list:
            return {'message': 'No entities found'}, 404
        return {f"all_{entity.__tablename__}": entity_list}, 200
    except Exception as e:
        return {'error': str(e)}, 500


def get_entity_by_id(entity: db.Model, entity_id: int):
    """
    Base to get entity by id, with all joins

    :param entity: entity to get
    :param entity_id: entity id
    """
    try:
        entity_inst = entity.get_entity_with_joins(entity_id)
        if not entity_inst:
            return {'message': 'Entity not found'}, 404
        return {f"{entity.__tablename__}": entity_inst}, 200
    except Exception as e:
        return {'error': str(e)}, 500


def update_entity(entity: db.Model, data: dict, entity_id: int):
    """Base to update entity"""
    if not data:
        return {'message': 'Missing parameters'}, 400
    try:
        entity_inst = entity.get_by(id=entity_id)
        if not entity_inst:
            return {'message': 'Entity not found'}, 404
        for key, value in data.items():
            setattr(entity_inst, key, value)
        entity_inst.update()
    except Exception as e:
        return {'error': str(e)}, 500
    return {'message':
            f'The {entity.__tablename__} has been successfully updated'}, 200


def delete_entity(entity: db.Model, entity_id: int):
    """Base to delete entity"""
    try:
        entity_inst = entity.get_by(id=entity_id)
        if not entity_inst:
            return {'message': 'Entity not found'}, 404
        entity_inst.delete()
    except Exception as e:
        return {'error': str(e)}, 500
    return {'message':
            f'The {entity.__tablename__} has been successfully deleted'}, 200
