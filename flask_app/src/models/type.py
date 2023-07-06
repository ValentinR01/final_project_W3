from db import db
from models.base import Base


class Type(Base):
    """This class represents the type table"""
    __tablename__ = 'type'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)

    # Relationships
    captations = db.relationship('Captation', backref='type', lazy=True)

    def __init__(self, name):
        self.name = name
