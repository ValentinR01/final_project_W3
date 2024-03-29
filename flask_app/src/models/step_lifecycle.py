from db import db
from models.base import Base


class StepLifecycle(Base):
    """This class represents the step_lifecycle table"""
    __tablename__ = 'step_lifecycle'

    id = db.Column(db.Integer, primary_key=True)
    step = db.Column(db.String(100), unique=True, nullable=False)

    def __init__(self, step):
        self.step = step
