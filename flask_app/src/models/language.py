from db import db
from models.base import Base


class Language(Base):
    """This class represents the language table"""
    __tablename__ = 'language'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    code = db.Column(db.String(2), unique=True, nullable=False)

    # Relationships
    speakers = db.relationship('Speaker', backref='language', lazy=True)
    composers = db.relationship('Composer', backref='language', lazy=True)
    assets_translated = \
        db.relationship('AssetTranslated', backref='language', lazy=True)
    subtitles = db.relationship('Subtitle', backref='language', lazy=True)

    def __init__(self, name, code=None):
        self.name = name
        self.code = code or name[:2].lower()
