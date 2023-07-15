from models.asset import Asset
from services.base import create_entity, get_all_entities, search_entities


def create_asset(data: dict):
    """Create a new asset"""
    return create_entity(
        data=data, entity=Asset, title=data.get('title')
    )


def get_asset(**kwargs):
    """Get all assets"""
    return get_all_entities(entity=Asset, **kwargs)


def search_asset(search: str, *columns):
    """Search assets"""
    return search_entities(entity=Asset, search=search, *columns)
