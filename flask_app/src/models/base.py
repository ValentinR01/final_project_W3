from db import db
from sqlalchemy import or_
from sqlalchemy.orm import joinedload
from helpers.etl import transformation


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
        return transformation(raw_data)

    @classmethod
    def get_entities_by_search_values(cls, search, *columns):
        filters = or_(*[
            getattr(cls, column).ilike(f'%{search}%') for column in columns
        ])
        raw_data = cls.query.filter(filters).all()
        return transformation(raw_data)

    @classmethod
    def get_entity_with_joins(cls, entity_id: int):
        """
        Join the entity with the related entities

        :param cls: class of the entity you want to get
        :param entity_id: id of the entity you want to get
        """
        query = db.session.query(cls).filter(cls.id == entity_id)
        for relationship_name in cls.__mapper__.relationships:
            query = query.options(joinedload(relationship_name))
        return transformation(query.first())
