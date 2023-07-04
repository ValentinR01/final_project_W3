from db import db
from models.crud import CRUD


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

    def __init__(self, email, fullname, password, domain_id,
                 profile_picture=None, count_assigning_asset=0, role_id=1):
        self.email = email
        self.fullname = fullname
        self.password = password
        self.profile_picture = profile_picture
        self.count_assigning_asset = count_assigning_asset
        self.role_id = role_id
        self.domain_id = domain_id
