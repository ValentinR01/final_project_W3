from models.type import Type


def get_all_categories():
    categories = Type.get_all()
    return {'categories': categories}, 200
