from models.asset import Asset
from services.base import \
    create_entity, get_all_entities, search_entities, get_entity_by_id, \
    update_entity


def create_asset(data: dict):
    """Create a new asset"""
    return create_entity(
        data=data, entity=Asset, title=data.get('title')
    )


def get_asset(**kwargs):
    """Get all assets"""
    if kwargs.get('id'):
        return get_entity_by_id(
            entity=Asset,
            entity_id=kwargs.get('id')
        )
    return get_all_entities(entity=Asset, **kwargs)


def search_asset(search: str):
    """Search assets"""
    return search_entities(Asset, search, "title", "music_title")


def update_asset(data: dict):
    """Update an asset"""
    return update_entity(
        data=data, entity=Asset, entity_id=data.get('id')
    )
