from db import db
from models.base import Base


class MetaKey(Base):
    """This class represents the meta_key table."""
    __tablename__ = 'meta_key'

    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.String(100), unique=True, nullable=False)

    # Relationships
    metadatas = db.relationship('Metadata', backref='meta_key', lazy=True)

    def __init__(self, key):
        self.key = key
