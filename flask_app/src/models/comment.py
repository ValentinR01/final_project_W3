from db import db
from models.base import Base
from sqlalchemy.orm import relationship
from models.user import User


class Comment(Base):
    """This class represents the comment table"""
    __tablename__ = 'comment'

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(1000), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    external_name = db.Column(db.String(100), nullable=True)

    # FK
    posted_by = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    asset_id = db.Column(db.Integer, db.ForeignKey('asset.id'), nullable=False)

    user = relationship(User, backref='comment')

    def __init__(self, content, posted_by, asset_id,
                 created_at=None, external_name=None):
        self.content = content
        self.created_at = created_at
        self.external_name = external_name
        self.posted_by = posted_by
        self.asset_id = asset_id

    @classmethod
    def get_all_comments(cls: db.Model, asset_id):
        """Get all comments for a given asset, with join on user info"""
        return cls.query \
            .join(User, Comment.posted_by == User.id) \
            .filter(Comment.asset_id == asset_id) \
            .all()
