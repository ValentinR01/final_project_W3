from db import db


class CRUD:
    """This class will be used to perform CRUD operations on the database."""
    def __init__(self, id):
        self.id = id

    def create(self):
        if self.id is None:
            db.session.add(self)
        return db.session.commit()

    def read(self):
        return self.query.all()

    def update(self):
        return db.session.commit()

    def delete(self):
        db.session.delete(self)
        return db.session.commit()