import logging
import datetime
import sqlalchemy


def transform_single_object(obj: object) -> dict:
    """
    Transform a single object into a dictionary

    :param obj: the object to be transformed
    :return: a dictionary representing the transformed object
    """
    try:
        return {
            key: (
                transform_single_object(value)
                if hasattr(value, "__dict__")
                else (
                    [transform_single_object(item) for item in value]
                    if isinstance(
                        value, sqlalchemy.orm.collections.CollectionAdapter
                    )
                    else (
                        value.strftime('%Y-%m-%d %H:%M:%S')
                        if isinstance(value, datetime.datetime)
                        else value
                    )
                )
            )
            for key, value in obj.__dict__.items()
            if not key.startswith('_sa_')
        }
    except Exception as e:
        logging.error(f"Error while transforming a single object: {e}")


def transformation(raw_data) -> list:
    """
    Transforms raw data into a list of dictionaries to be jsonified

    :param raw_data: raw data to be transformed
    :return: list of dictionaries
    """
    try:
        if not isinstance(raw_data, list):
            raw_data = [raw_data]
        transformed_data = [
            transform_single_object(obj) for obj in raw_data
        ]
        return transformed_data
    except Exception as e:
        logging.error(f"Error while transforming data: {e}")
        return raw_data
