from db import db
from models.base import Base


class Specialty(Base):
    """This class represents the specialty table"""
    __tablename__ = 'specialty'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)

    # FK
    domain_id = \
        db.Column(db.Integer, db.ForeignKey('domain.id'), nullable=False)

    def __init__(self, name, domain_id):
        self.name = name
        self.domain_id = domain_id
