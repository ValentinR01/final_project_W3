from db import db
from models.base import Base


class Domain(Base):
    """This class represents the domain table"""
    __tablename__ = 'domain'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)

    # Relationships
    users = db.relationship('User', backref='domain', lazy=True)
    specialties = db.relationship('Specialty', backref='domain', lazy=True)

    def __init__(self, name):
        self.name = name
