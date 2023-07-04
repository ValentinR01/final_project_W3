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

    @staticmethod
    def init_db_value(init_values: list, table: db.Model()):
        """
        This method will be used to initialize the values of a table.

        :param init_values: list of values to initialize
        :param table: table to initialize
        :return:
        """
        for init_value in init_values:
            try:
                domain = table.query.filter_by(name=init_value).first()
                if domain:
                    continue
                else:
                    domain = table(name=init_value)
                    domain.create()
            except Exception as e:
                print(e)
                continue

    @classmethod
    def get_by(cls: db.Model(), **kwargs):
        """
        This method will be used to get a record from a table.

        :param cls: table to check
        :param kwargs: value to check
        :return:
        """
        return cls.query.filter_by(**kwargs).first()

