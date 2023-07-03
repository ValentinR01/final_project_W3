from flask_app.src.db import db
from flask_app.src.models.crud import CRUD


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
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'), nullable=False)
    domain_id = \
        db.Column(db.Integer, db.ForeignKey('domain.id'), nullable=False)

    def __init__(self, email, fullname, password):
        self.email = email
        self.fullname = fullname
        self.password = password

    @classmethod
    def find_by_email(cls, email):
        return cls.query.filter_by(email=email).first()
