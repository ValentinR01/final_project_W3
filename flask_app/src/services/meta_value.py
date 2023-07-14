from models.meta_value import MetaValue


def get_all_meta_values():
    meta_value_list = MetaValue.get_all()
    if meta_value_list is None:
        return {'meta_values': []}, 200
    return {'meta_values': meta_value_list}, 200
