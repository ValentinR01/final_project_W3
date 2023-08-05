from flask import request
from flask_restx import Resource, fields, Api
from services.comment import register_comment, get_all_comments
from api.asset import namespace as namespace

api = Api()

comment_register_model = namespace.model('CommentRegister', {
    'content': fields.String(required=True)})

comment_model = namespace.model(
    'comment', {
        'id': fields.Integer(),
        'content': fields.String,
        'created_at': fields.DateTime(),
        'external_name': fields.String(),
        'posted_by': fields.Integer(),
        'fullname': fields.String(),
        'asset_id': fields.Integer()
    }
)

comment_list_model = namespace.model(
    'comment_list', {
        'comments': fields.List(fields.Nested(comment_model))
    }, default={}
)


@namespace.route('/<int:asset_id>/comments', methods=["GET", "POST"])
class Comment(Resource):
    @namespace.marshal_with(comment_list_model)
    def get(self, asset_id):
        """Get comments from an asset"""
        return get_all_comments(asset_id)

    @namespace.expect(comment_register_model)
    def post(self, asset_id):
        """Post a comment to an asset"""
        comment = request.json
        return register_comment(asset_id, comment)
