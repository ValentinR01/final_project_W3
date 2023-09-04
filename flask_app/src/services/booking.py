from models.booking import Booking
from services.base import create_entity


def create_booking(data: dict):
    """Create a new booking"""
    return create_entity(
        data=data, entity=Booking, date=data.get('date'),
        is_am_timeslot=data.get('is_am_timeslot'), room_id=data.get('room_id')
    )
