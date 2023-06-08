from db import db


class Role(db.Model):
    """This class represents the role table."""
    __tablename__ = 'role'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
