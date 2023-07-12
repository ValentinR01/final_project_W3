from db import db
from models.base import Base


class PostProd(Base):
    """This class represents the post_prod table"""
    __tablename__ = 'post_prod'

    id = db.Column(db.Integer, primary_key=True)
    rush_received = db.Column(db.Boolean, nullable=False)
    started_at = db.Column(db.DateTime, nullable=True)
    ended_at = db.Column(db.DateTime, nullable=True)
    validated_at = db.Column(db.DateTime, nullable=True)
    deposit_path = db.Column(db.String(100), nullable=True, unique=True)
    version = db.Column(db.Integer, nullable=False)

    def __init__(self, rush_received, started_at, ended_at, validated_at,
                 deposit_path, version):
        self.rush_received = rush_received
        self.started_at = started_at
        self.ended_at = ended_at
        self.validated_at = validated_at
        self.deposit_path = deposit_path
        self.version = version
