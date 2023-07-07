from db import db


class Base(db.Model):
    """This class will be used to perform Base operations on the database"""

    __abstract__ = True

    def __init__(self, id):
        self.id = id

    def create(self):
        if self.id is None:
            db.session.add(self)
        return db.session.commit()

    def get_all(self):
        return self.query.all()

    def update(self):
        return db.session.commit()

    def delete(self):
        db.session.delete(self)
        return db.session.commit()

    @classmethod
    def get_by(cls: db.Model, **kwargs):
        """
        This method will be used to get a record from a table.

        :param cls: class to check
        :param kwargs: values to check
        :return: the first matching record
        """
        return cls.query.filter_by(**kwargs).first()

    @classmethod
    def get_all_by(cls: db.Model, **kwargs):
        """
        This method will be used to get a record from a table.

        :param cls: class to check
        :param kwargs: values to check
        :return: the first matching record
        """
        return cls.query.filter_by(**kwargs).all()

    @classmethod
    def init_db_value(cls: db.Model, init_values: list):
        """
        This method will be used to initialize the values of a table.

        :param cls: table to initialize
        :param init_values: list of values to initialize
        :return:
        """
        for init_value in init_values:
            try:
                domain = cls.query.filter_by(name=init_value).first()
                if domain:
                    continue
                else:
                    domain = cls(name=init_value)
                    domain.create()
            except Exception as e:
                print(e)
                continue
