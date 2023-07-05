from db import db
from models.base import Base


class Composer(Base):
    """This class represents the composer table."""
    __tablename__ = 'composer'

    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(100), unique=True, nullable=False)
    biography = db.Column(db.String(5000), nullable=True)

    publishable = db.Column(db.Boolean, default=False)

    last_update = db.Column(db.DateTime, default=db.func.current_timestamp())

    # FK
    composer_parent = \
        db.Column(db.Integer, db.ForeignKey('composer.id'), nullable=True)
    langage_id = \
        db.Column(db.Integer, db.ForeignKey('langage.id'), nullable=False)

    def __init__(self, fullname, biography, publishable, last_update,
                 composer_parent, langage):
        self.fullname = fullname
        self.biography = biography
        self.publishable = publishable
        self.last_update = last_update
        self.composer_parent = composer_parent
        self.langage = langage