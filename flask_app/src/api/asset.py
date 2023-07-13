from flask import request
from flask_restx import Namespace, Resource, Api
from helpers.decorators import rights_manager
from services.asset import create_asset, get_all_assets

namespace = Namespace('assets', 'Asset related endpoints')

api = Api()


@namespace.route('/', methods=['GET'])
class GetAll(Resource):
    """Get all assets"""
    @api.doc(
        params={

        }
    )
    def get(self, **kwargs):
        """Get all assets"""
        return get_all_assets(**kwargs)


@namespace.route('/create', methods=['POST'])
class Create(Resource):
    """Create a new asset"""
    token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MTcsImZ1bGxuYW1lIjoid29ya2VyIiwiZW1haWwiOiJ3b3JrZXJAc2FsaW5lLmNvbSIsInJvbGUiOiJ3b3JrZXIiLCJkb21haW4iOiJyZWRhY3Rpb24iLCJleHAiOjE2ODkyNzU2MDEsImlhdCI6MTY4OTIzOTYwMX0.PthvqrWTOjIX8Wk7pMxKiGEfTqvzIEEJcLQROVAfjqc"
    @api.doc(
        params={
            # Required parameters
            'title': {
                'description': 'Asset title', 'required': True, 'type':
                    'string'
            },
            'music_title': {
                'description': 'Music title', 'required': True, 'type':
                    'string'
            },
            'composer_id': {
                'description': 'Composer id', 'required': True, 'type':
                    'integer'
            },
            'current_assigned_user_id': {
                'description': 'Current assigned user id', 'required': True,
                'type': 'integer'
            },
            'created_by_id': {
                'description': 'Created by id', 'required': True, 'type':
                    'integer'
            },
            'updated_by_id': {
                'description': 'Updated by id', 'required': True, 'type':
                    'integer'
            },
            'speaker_id': {
                'description': 'Speaker id', 'required': True, 'type':
                    'integer'
            },
            'status_by_domain_id': {
                'description': 'Status by domain id', 'required': True,
                'type': 'integer'
            },
            'step_lifecycle_id': {
                'description': 'Step lifecycle id', 'required': True,
                'type': 'integer'
            },
            'booking_id': {
                'description': 'Booking id', 'required': True, 'type':
                    'integer'
            },
            # Optional parameters
            'captation_id': {
                'description': 'Captation id', 'type': 'integer'
            },
            'post_prod_id': {
                'description': 'Post prod id', 'type': 'integer'
            },
            'transformation_id': {
                'description': 'Transformation id', 'type': 'integer'
            },
            'has_high_priority': {
                'description': 'Has high priority', 'type': 'boolean',
                'default': False
            },
            'published': {
                'description': 'Published', 'type': 'boolean', 'default':
                    False
            },
            'created_at': {
                'description': 'Created at', 'type': 'datetime'
            },
            'updated_at': {
                'description': 'Updated at', 'type': 'datetime'
            },
            'published_at': {
                'description': 'Published at', 'type': 'datetime'
            },
            'last_assignment_at': {
                'description': 'Last assignment at', 'type': 'datetime'
            },
            'student_fullname': {
                'description': 'Student fullname', 'type': 'string'
            },
            'art_description': {
                'description': 'Art description', 'type': 'string'
            },
            'asset_description': {
                'description': 'Asset description', 'type': 'string'
            },
            'link_partitions': {
                'description': 'Link partitions', 'type': 'string'
            },
            'thumbnail': {
                'description': 'Thumbnail', 'type': 'string'
            },
            'resumed': {
                'description': 'Resumed', 'type': 'string'
            }
        }
    )
    @rights_manager(token=token, role='worker', domain='redaction')
    @namespace.response(200, '')
    def post(self):
        return create_asset(request.json)
