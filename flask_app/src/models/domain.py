from db import db
from models.crud import CRUD


class Domain(db.Model, CRUD):
    """This class represents the domain table."""
    __tablename__ = 'domain'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    user = db.relationship('User', backref='domain', lazy=True)

    def __init__(self, name):
        self.name = name
