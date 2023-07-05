from db import db
from models.base import Base


class Comment(Base):
    """This class represents the comment table."""
    __tablename__ = 'comment'

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(1000), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    external_name = db.Column(db.String(100), nullable=False)

    # FK
    posted_by = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    asset_id = db.Column(db.Integer, db.ForeignKey('asset.id'), nullable=False)


    def __init__(self, content, created_at, external_name, posted_by, asset):
        self.content = content
        self.created_at = created_at
        self.external_name = external_name
        self.posted_by = posted_by
        self.asset = asset
