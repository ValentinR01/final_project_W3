from db import db
from models.base import Base


class Booking(Base):
    """This class represents the booking table"""
    __tablename__ = 'booking'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False)
    timeslot = db.Column(db.String(2), nullable=False)

    # FK
    room_id = db.Column(db.Integer, db.ForeignKey('room.id'), nullable=False)

    def __init__(self, date, timeslot, room_id):
        self.date = date
        self.timeslot = timeslot
        self.room_id = room_id


