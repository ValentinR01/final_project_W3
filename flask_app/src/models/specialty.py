from db import db
from models.base import Base


class Specialty(Base):
    """This class represents the specialty table"""
    __tablename__ = 'specialty'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=True)

    # FK
    domain_id = \
        db.Column(db.Integer, db.ForeignKey('domain.id'), nullable=False)
    language_id = \
        db.Column(db.Integer, db.ForeignKey('language.id'), nullable=True)

    def __init__(self, domain_id, name=None, language_id=None):
        self.name = name
        self.domain_id = domain_id
        self.language_id = language_id
