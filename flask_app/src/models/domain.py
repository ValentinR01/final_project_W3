from flask_app.src.db import db
from flask_app.src.models.crud import CRUD


class Domain(db.Model, CRUD):
    """This class represents the domain table."""
    __tablename__ = 'domain'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    user = db.relationship('User', backref='domain', lazy=True)

    def __init__(self, name):
        self.name = name

    # @classmethod
    # def init_domain(cls):
    #     init_values = ['redaction', 'translation', 'management', 'development']
    #     for init_value in init_values:
    #         domain = cls(init_value)
    #         domain.create()
    #     return True

    @classmethod
    def init_domain(cls):
        CRUD.init_value(
            ['redaction', 'translation', 'management', 'development']
        )

