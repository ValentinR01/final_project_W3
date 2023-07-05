from db import db
from models.base import Base


class Role(Base):
    """This class represents the role table."""
    __tablename__ = 'role'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)

    # Relationships
    users = db.relationship('User', backref='role', lazy=True)

    def __init__(self, name):
        self.name = name
