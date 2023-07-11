from db import db
from models.base import Base


class Speaker(Base):
    """This class represents the speakers table"""
    __tablename__ = 'speaker'

    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(50), unique=True, nullable=False)
    biography = db.Column(db.String(5000), nullable=True)
    last_update = db.Column(db.DateTime, default=db.func.current_timestamp())
    publishable = db.Column(db.Boolean, default=False)
    # FK
    speaker_parent = db.Column(
        db.Integer, db.ForeignKey('speaker.id'), nullable=True, default=id
    )
    language_id = \
        db.Column(db.Integer, db.ForeignKey('language.id'), nullable=False)

    def __init__(self, fullname, biography, last_update, publishable,
                 language_id, speaker_parent=None):
        self.fullname = fullname
        self.biography = biography
        self.last_update = last_update
        self.publishable = publishable
        self.speaker_parent = speaker_parent or id
        self.language_id = language_id
