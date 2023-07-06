from db import db
from models.base import Base


class Language(Base):
    """This class represents the language table"""
    __tablename__ = 'language'

    id = db.Column(db.Integer, primary_key=True)
    langue = db.Column(db.String(100), unique=True, nullable=False)
    code = db.Column(db.String(2), unique=True, nullable=False)

    # Relationships
    speakers = db.relationship('Speaker', backref='language', lazy=True)

    def __init__(self, langue, code=None):
        self.langue = langue
        self.code = code or langue[:2].lower()
