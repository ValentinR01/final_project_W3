# from mongoengine import Document, StringField, EmailField
# Refaire les imports à partir de postgres

# class User(Document):
#     name = StringField(required=True, max_length=256)
#     email = EmailField(required=True, max_length=1024)
#     image = StringField(required=True, max_length=1024)
#     mobile = StringField(required=True, max_length=256)
#     password = StringField(required=True, max_length=1024)

from . import db
from .crud import CRUD


class User(db.Model, CRUD):
    """This class represents the users table."""
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password = password


