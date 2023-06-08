from db import db
from .crud import CRUD


class User(db.Model, CRUD):
    """This class represents the users table."""
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    fullname = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(1000), nullable=False)
    profile_picture = db.Column(db.String(1000), nullable=True)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    count_assigning_asset = db.Column(db.Integer, default=0)
    # FK
    role = db.relationship('role', backref='user', lazy=True)
    # domain_id = db.Column(db.Integer, db.ForeignKey('domain.id'))


    def __init__(self, email, fullname, password):
        self.email = email
        self.fullname = fullname
        self.password = password

    @classmethod
    def find_by_email(cls, email):
        return cls.query.filter_by(email=email).first()


class Domain(db.Model):
    """This class represents the domain table."""
    __tablename__ = 'domain'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    users = db.relationship('user', backref='domain')