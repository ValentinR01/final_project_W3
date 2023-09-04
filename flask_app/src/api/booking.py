from flask import request
from flask_restx import Namespace, Resource, Api
# from helpers.decorators import rights_manager
from services.booking import create_booking
from services.asset import update_asset

namespace = Namespace('bookings', 'Booking related to an asset')

api = Api()


@namespace.route('/create', methods=['POST'])
class Create(Resource):
    """Create a new booking for an asset"""
    @api.doc(
        params={
            # Required parameters
            'asset_id': {
                'description': 'Asset id', 'required': True, 'type': 'integer'
            },
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
        booking = create_booking(data=request.json)
        if not booking:
            return {'message': 'Booking not created'}, 400
        # TODO : thinking about a better way to do this
        update_asset(
            data={
                "id": request.json.get('asset_id'), "booking_id": booking.id
            }
        )
        return {'message': 'Booking created'}, 201
