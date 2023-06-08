from db import db


class Domain(db.Model):
    """This class represents the domain table."""
    __tablename__ = 'domain'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    users = db.relationship('user', backref='domain')
