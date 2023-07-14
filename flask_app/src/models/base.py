import logging
import datetime
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
        This method will be used to get a record from a table.

        :param cls: class to check
        :param kwargs: values to check
        :return: all matching records
        """
        raw_data = cls.query.filter_by(**kwargs).all()
        if raw_data:
            try:
                list_data = [
                    {
                        key: value.strftime('%Y-%m-%d %H:%M:%S')
                        if isinstance(value, datetime.datetime)
                        else value
                        for key, value in data.__dict__.items()
                        if key != '_sa_instance_state'
                    }
                    for data in raw_data
                ]
                logging.info(list_data)
                return list_data
            except Exception as e:
                logging.error(e)
