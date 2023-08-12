from models.comment import Comment
from services.base import create_entity


def register_comment(asset_id, data):
    data["asset_id"] = asset_id
    data["posted_by"] = 1
    return create_entity(Comment, data, id=0)


def get_all_comments(asset_id):
    comments = Comment.get_all_comments(asset_id)
    comments_list = [
        {
            'id': comment.id,
            'content': comment.content,
            'created_at': comment.created_at,
            'external_name': comment.external_name,
            'posted_by': comment.posted_by,
            'fullname': comment.user.fullname,
            'asset_id': comment.asset_id
        }
        for comment in comments
    ]

    return {'comments': comments_list}, 200
