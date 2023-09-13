from flask import request
from flask_restx import Resource, fields, Api, Namespace
from services.category import get_all_categories


namespace = Namespace('categories', 'Asset categories related endpoints')

api = Api()

category_model = namespace.model(
    'category', {
        'id': fields.Integer(),
        'name': fields.String,
    }
)

categories_list_model = namespace.model(
    'categories_list_model', {
        'categories': fields.List(fields.Nested(category_model, default={}))
    }
)


@namespace.route('', methods=["GET"])
class Category(Resource):
    @namespace.marshal_with(categories_list_model)
    def get(self):
        """Get all categories"""
        return get_all_categories()
