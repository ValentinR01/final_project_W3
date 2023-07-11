from db import db
from models.base import Base


class MetaValue(Base):
    """This class represents the meta_value table"""
    __tablename__ = 'meta_value'

    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.String(100), unique=True, nullable=False)

    meta_key_id = \
        db.Column(db.Integer, db.ForeignKey('meta_key.id'), nullable=False)

    # Relationships
    metadatas = db.relationship('Metadata', backref='meta_value', lazy=True)

    def __init__(self, value, meta_key_id):
        self.value = value
        self.meta_key_id = meta_key_id
