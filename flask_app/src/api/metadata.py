import re
from models.user import User
from flask import request
from flask_restx import Namespace, Resource, fields
from services.metadata_service import get_all_metadatas

namespace = Namespace('metadatas', 'Metadata related endpoints')


@namespace.route('', methods=['GET'])
class GetAll(Resource):
    def get(self):
        """Get all metadatas"""
        return get_all_metadatas()
    
