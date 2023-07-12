from db import db
from models.base import Base


class Metadata(Base):
    """This class represents the metadata table"""
    __tablename__ = 'metadata'

    id = db.Column(db.Integer, primary_key=True)

    # FK
    meta_value_id = \
        db.Column(db.Integer, db.ForeignKey('meta_value.id'), nullable=False)
    asset_id = db.Column(db.Integer, db.ForeignKey('asset.id'), nullable=False)

    def __init__(self, meta_value_id, asset_id):
        self.meta_value_id = meta_value_id
        self.asset_id = asset_id
