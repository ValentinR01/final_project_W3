from db import db
from models.base import Base


class Speaker(Base):
    """This class represents the speakers table."""
    __tablename__ = 'speaker'

    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(50), unique=True, nullable=False)
    biography = db.Column(db.String(5000), nullable=True)
    last_update = db.Column(db.DateTime, default=db.func.current_timestamp())
    publishable = db.Column(db.Boolean, default=False)
    # FK
    # speaker_parent = db.relationship('Speaker', backref='speaker',
    # lazy=True) #To Check
    # language = db.relationship('Language', backref='id', lazy=True) #To Check

    def __init__(self, fullname, biography, last_update, publishable):
        self.fullname = fullname
        self.biography = biography
        self.last_update = last_update
        self.publishable = publishable
