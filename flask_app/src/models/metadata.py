from db import db
from models.base import Base


class Metadata(Base):
    """This class represents the metadata table."""
    __tablename__ = 'metadata'

    id = db.Column(db.Integer, primary_key=True)

    # FK
    meta_key_id = \
        db.Column(db.Integer, db.ForeignKey('meta_key.id'), nullable=False)
    meta_value_id = \
        db.Column(db.Integer, db.ForeignKey('meta_value.id'), nullable=False)
    asset_id = db.Column(db.Integer, db.ForeignKey('asset.id'), nullable=False)

    def __init__(self, meta_key, meta_value, asset):
        self.meta_key = meta_key
        self.meta_value = meta_value
        self.asset = asset
