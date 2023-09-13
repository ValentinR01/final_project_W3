from flask import request
from flask_restx import Namespace, Resource, Api, fields
# from helpers.decorators import rights_manager
from services.asset import create_asset, get_asset, search_asset

namespace = Namespace('assets', 'Asset related endpoints')

api = Api()


create_asset_model = namespace.model(
    'create_asset_model',
    {
        'title': fields.String(required=True),
        'music_title': fields.String(required=True),
        'speaker_id': fields.Integer(required=False),
        'composer_id': fields.Integer(required=False),
        'student_fullname': fields.Integer(required=False),
        'comment': fields.String(required=False),
        'instruments': fields.List(fields.String(), required=False),
        'category': fields.String(required=False)
    }
)


@namespace.route('/', methods=['GET'])
class GetAll(Resource):
    """Get all assets"""
    @api.doc(
        params={
            'status_by_domain_id': {
                'description': 'Status by domain ID', 'type': 'int',
                'required': False
            }

        }
    )
    def get(self):
        """Get all assets"""
        kwargs = request.args.to_dict()
        return get_asset(**kwargs)


@namespace.route('/create', methods=['POST'])
class Create(Resource):
    """Create a new asset"""
    # @rights_manager(token=token, role='worker', domain='redaction')
    @api.expect(create_asset_model)
    def post(self):
        """Create a new asset"""
        return create_asset(data=request.json)


@namespace.route('/id/<int:asset_id>', methods=['GET'])
class GetById(Resource):
    """Get asset by id"""
    @api.doc(
        params={
            'asset_id': {
                'description': 'Asset id', 'required': True, 'type':
                    'integer'
            }
        }
    )
    def get(self, asset_id):
        """Get asset by id"""
        return get_asset(id=asset_id)


@namespace.route('/search', methods=['GET'])
class Search(Resource):
    """Search assets"""
    @api.doc(
        params={
            'search': {
                'description': 'Search', 'required': True, 'type':
                    'string'
            }
        }
    )
    def get(self):
        """Search assets"""
        search = request.args.get('search')
        return search_asset(search)
