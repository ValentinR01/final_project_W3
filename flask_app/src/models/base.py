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
        try:
            list_data = [
                data.__dict__ for data in raw_data
            ]
            for data in list_data:
                data.pop('_sa_instance_state')
                for key, value in data.items():
                    if isinstance(value, datetime.datetime):
                        data[key] = value.strftime('%Y-%m-%d %H:%M:%S')
            logging.info(list_data)
            return list_data
        except Exception as e:
            logging.error(e)
