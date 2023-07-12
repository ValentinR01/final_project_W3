from db import db
from models.base import Base


class Subtitle(Base):
    """This class represents the subtitle table"""
    __tablename__ = 'subtitle'

    id = db.Column(db.Integer, primary_key=True)
    file_path = db.Column(db.String(100), nullable=False)
    published = db.Column(db.Boolean, nullable=False)

    # FK
    translated_by = \
        db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    language_id = \
        db.Column(db.Integer, db.ForeignKey('language.id'), nullable=False)
    asset_id = \
        db.Column(db.Integer, db.ForeignKey('asset.id'), nullable=False)

    def __init__(self, file_path, published, translated_by,
                 language_id, asset_id):
        self.file_path = file_path
        self.published = published
        self.translated_by = translated_by
        self.language_id = language_id
        self.asset_id = asset_id
