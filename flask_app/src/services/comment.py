from models.comment import Comment
from services.base import create_entity


# Todo: Complete with user Token data
def register_comment(asset_id, data):
    data["asset_id"] = asset_id
    data["posted_by"] = 1
    return create_entity(Comment, data, id=0)


def get_all_comments(asset_id):
    comments = Comment.get_all_by(asset_id=asset_id)
    return {'comments': comments}, 200
