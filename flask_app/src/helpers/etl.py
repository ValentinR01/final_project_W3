import logging
import datetime


def transform(raw_data) -> list:
    """
    Transform raw data to a list of dict to be jsonified

    :param raw_data: raw data to transform
    :return: list of dict
    """
    try:
        if not isinstance(raw_data, list):
            raw_data = [raw_data]
        list_data = [
            {
                key: value.strftime('%Y-%m-%d %H:%M:%S')
                if isinstance(value, datetime.datetime)
                else value
                for key, value in data.__dict__.items()
                if key != '_sa_instance_state'
            }
            if isinstance(data, object)
            else data
            for data in raw_data
        ]
        return list_data
    except Exception as e:
        logging.error("Error while transforming data", e)
