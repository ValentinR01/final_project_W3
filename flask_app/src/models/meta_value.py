from db import db
from models.base import Base


class MetaValue(Base):
    """This class represents the meta_value table."""
    __tablename__ = 'meta_value'

    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.String(100), unique=True, nullable=False)

    # FK
    metadata = db.relationship('Metadata', backref='meta_value', lazy=True)

    def __init__(self, value):
        self.value = value
