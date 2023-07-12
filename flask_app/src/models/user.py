from db import db
from models.base import Base


class User(Base):
    """This class represents the users table"""
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

    def __init__(self, email, fullname, password, domain_id, role_id,
                 created_at=None, profile_picture=None,
                 count_assigning_asset=0):
        self.email = email
        self.fullname = fullname
        self.password = password
        self.profile_picture = profile_picture
        self.created_at = created_at
        self.count_assigning_asset = count_assigning_asset
        self.role_id = role_id
        self.domain_id = domain_id
