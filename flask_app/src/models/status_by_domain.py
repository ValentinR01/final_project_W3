from db import db
from models.base import Base


class StatusByDomain(Base):
    """This class represents the status by domain table"""
    __tablename__ = 'status_by_domain'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)

    # Relationships
    assets = db.relationship('Asset', backref='status_by_domain', lazy=True)

    def __init__(self, name):
        self.name = name
