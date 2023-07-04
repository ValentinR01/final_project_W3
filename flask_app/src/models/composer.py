from db import db
from models.base import Base


class Composer(db.Model, Base):
    """This class represents the composer table."""
    __tablename__ = 'composer'

    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(100), unique=True, nullable=False)
    biography = db.Column(db.String(1000), nullable=True)

    publishable = db.Column(db.Boolean, default=False)

    last_update = db.Column(db.DateTime, default=db.func.current_timestamp())

    # FK
    composer_parent = \
        db.Column(db.Integer, db.ForeignKey('composer.id'), nullable=True)
    langage_id = \
        db.Column(db.Integer, db.ForeignKey('langage.id'), nullable=False)
