import logging
import datetime
import sqlalchemy.orm.collections as soc


def transform_single_object(
        obj: object, keys_to_remove: tuple[str] = ('_sa_', 'password')):
    """
    Transform a single object into a dictionary

    :param obj: the object to be transformed
    :param keys_to_remove: keys to remove from the dictionary
    :return: a dictionary representing the transformed object
    """
    try:
        return {
            key: (
                transform_single_object(value)
                if hasattr(value, "__dict__")
                else (
                    [transform_single_object(item) for item in value]
                    if isinstance(value, soc.CollectionAdapter)
                    else (
                        value.strftime('%Y-%m-%d %H:%M:%S')
                        if isinstance(value, datetime.datetime)
                        else value
                    )
                )
            )
            for key, value in obj.__dict__.items()
            if not key.startswith(keys_to_remove)
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
