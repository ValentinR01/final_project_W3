from db import db
from models.base import Base


class Metadata(db.Model, Base):
    """This class represents the metadata table."""
    __tablename__ = 'metadata'

    id = db.Column(db.Integer, primary_key=True)
    # FK
    # meta_key = db.relationship('`meta_key', backref='id', lazy=True) #To Check
    # meta_value = db.relationship('`meta_value', backref='id', lazy=True) #To Check
    # asset = db.relationship('asset', backref='asset', lazy=True) #To Check

    def __init__(self, meta_key, meta_value, asset):
        self.meta_key = meta_key
        self.meta_value = meta_value
        self.asset = asset
