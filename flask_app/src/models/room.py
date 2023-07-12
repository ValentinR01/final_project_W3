from db import db
from models.base import Base


class Room(Base):
    """This class represents the room table"""
    __tablename__ = 'room'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)

    # Relationships
    bookings = db.relationship('Booking', backref='room', lazy=True)

    def __init__(self, name, capacity, description, last_update, publishable):
        self.name = name
