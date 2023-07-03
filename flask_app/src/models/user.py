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
    role = db.relationship('`Role', backref='user', lazy=True)
    domain = db.relationship('Domain', backref='user', lazy=True)


    def __init__(self, email, fullname, password):
        self.email = email
        self.fullname = fullname
        self.password = password

    @classmethod
    def find_by_email(cls, email):
        return cls.query.filter_by(email=email).first()
    
    @classmethod
    def get_all(cls, domain):
        return cls.query.all()
    

