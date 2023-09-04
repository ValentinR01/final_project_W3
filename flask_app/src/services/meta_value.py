from models.meta_value import MetaValue
from models.meta_key import MetaKey
import logging


def get_all_meta_values(meta_key=None):
    if meta_key is None:
        meta_value_list = MetaValue.get_all()

        if meta_value_list is None:
            return {'meta_values': []}, 200
        return {'meta_values': meta_value_list}, 200

    meta_key_id = MetaKey.get_by(key=meta_key)
    if meta_key_id is None:
        logging.error("---- Meta-key id not found, invalid meta_key name ---")
        return {'meta_values': []}, 404

    meta_value_list = MetaValue.get_all_by(meta_key_id=meta_key_id.id)
    if meta_value_list is None:
        return {'meta_values': []}, 200
    return {'meta_values': meta_value_list}, 200
