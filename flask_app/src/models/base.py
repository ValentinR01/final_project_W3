from db import db
from sqlalchemy import or_
from helpers.etl import transform


class Base(db.Model):
    """This class will be used to perform Base operations on the database"""

    __abstract__ = True

    def __init__(self, id):
        self.id = id

    def create(self):
        if self.id is None:
            db.session.add(self)
        return db.session.commit()

    def update(self):
        return db.session.commit()

    def delete(self):
        db.session.delete(self)
        return db.session.commit()

    @classmethod
    def get_all(cls: db.Model):
        return cls.query.all()


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
        This method will be used to get all record from a table with filter.

        :param cls: class to check
        :param kwargs: values to check
        :return: all matching records
        """
        raw_data = cls.query.filter_by(**kwargs).all()
        return raw_data

    @classmethod
    def get_entities_by_search_values(cls, search, *columns):
        filters = or_(*[
            getattr(cls, column).ilike(f'%{search}%') for column in columns
        ])
        raw_data = cls.query.filter(filters).all()
        if raw_data:
            return transform(raw_data)
