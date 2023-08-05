import logging
import datetime


def transform(raw_data):
    """
    Transform raw data to a list of dict to be jsonified

    :param raw_data: raw data to transform
    """
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
        return list_data
    except Exception as e:
        logging.error(e)
