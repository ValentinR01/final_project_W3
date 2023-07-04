from db import db
from models.base import Base


class Domain(db.Model, Base):
    """This class represents the domain table."""
    __tablename__ = 'domain'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    users = db.relationship('User', backref='domain_id', lazy=True)

    def __init__(self, name):
        self.name = name
