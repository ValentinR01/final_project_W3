from db import db
from models.base import Base


class Transformation(Base):
    """This class represents the transformation table"""

    id = db.Column(db.Integer, primary_key=True)
    deposit_path = db.Column(db.String(100), nullable=True, unique=True)

    def __init__(self, deposit_path):
        self.deposit_path = deposit_path
