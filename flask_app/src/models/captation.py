from db import db
from models.base import Base


class Captation(Base):
    """This class represents the captation table"""
    __tablename__ = 'captation'

    id = db.Column(db.Integer, primary_key=True)
    duration = db.Column(db.Integer, nullable=False)
    filmed_at = db.Column(
        db.DateTime, nullable=False, default=db.func.current_timestamp())
    deposit_path = db.Column(db.String(1000), nullable=False)
    report = db.Column(db.String(5000), nullable=True)

    # FK
    type_id = db.Column(db.Integer, db.ForeignKey('type.id'), nullable=False)

    def __init__(self, duration, filmed_at, deposit_path, report, type_id):
        self.duration = duration
        self.filmed_at = filmed_at
        self.deposit_path = deposit_path
        self.report = report
        self.type_id = type_id
