from models.asset import Asset
from services.base import create_entity, get_all_entities


def create_asset(data):
    """Create a new asset"""
    return create_entity(
        data=data, entity=Asset, title=data.get('title')
    )


def get_all_assets(**kwargs):
    """Get all assets"""
    return get_all_entities(entity=Asset, **kwargs)
