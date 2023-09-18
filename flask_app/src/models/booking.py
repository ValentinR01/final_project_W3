from db import db
from models.base import Base


class Booking(Base):
    """This class represents the booking table"""
    __tablename__ = 'booking'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    is_am_timeslot = db.Column(db.Boolean, default=False, nullable=False)

    # FK
    room_id = db.Column(db.Integer, db.ForeignKey('room.id'), nullable=False)

    def __init__(self, date, is_am_timeslot, room_id):
        self.date = date
        self.is_am_timeslot = is_am_timeslot
        self.room_id = room_id
