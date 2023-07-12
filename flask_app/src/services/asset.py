from models.asset import Asset


def create_asset(data):
    """Create a new asset"""
    asset = Asset(**data)
    asset.create()
    return asset
