from flask_app.src.db import db


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

    @classmethod
    def init_value(cls, init_values: list):
        """
        This method will be used to initialize the values of a table.

        :param init_values : The values to initialize the table with.
        :return:
        """
        for init_value in init_values:
            domain = cls(init_value)
            domain.create()
