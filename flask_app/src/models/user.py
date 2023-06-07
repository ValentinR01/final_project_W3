from . import db
from .crud import CRUD


class User(db.Model, CRUD):
    """This class represents the users table."""
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(1000), nullable=False)

    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password = password
