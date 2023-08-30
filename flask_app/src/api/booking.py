from flask import request
from flask_restx import Namespace, Resource, Api
# from helpers.decorators import rights_manager
from services.booking import create_booking


namespace = Namespace('bookings', 'Booking related to an asset')

api = Api()


@namespace.route('/create', methods=['POST'])
class Create(Resource):
    """Create a new booking for an asset"""
    @api.doc(
        params={
            'date': {
                'description': 'Booking date', 'required': True, 'type':
                    'string'
            },
            'is_am_timeslot': {
                'description': 'Booking timeslot', 'required': True, 'type':
                    'boolean', 'default': False
            },
            'room_id': {
                'description': 'Room id', 'required': True, 'type': 'integer'
            }
        }
    )
    def post(self):
        """Create a new booking for an asset"""
        return create_booking(data=request.json)



