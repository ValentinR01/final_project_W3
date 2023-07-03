from db import db
from .crud import CRUD


class Speaker(db.Model, CRUD):
    """This class represents the speakers table."""
    __tablename__ = 'speaker'

    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(50), unique=True, nullable=False)
    biography = db.Column(db.String(5000), nullable=True)
    last_update = db.Column(db.DateTime, default=db.func.current_timestamp())
    publishable = db.Column(db.Boolean, default=False)
    # FK
    speaker_parent = db.relationship('`Speaker', backref='speaker', lazy=True) #To Check
    language = db.relationship('Language', backref='id', lazy=True) #To Check


    def __init__(self, fullname):
        self.fullname = fullname
    
    @classmethod
    def get_all(cls):
        return cls.query.all()
    
    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()
    

