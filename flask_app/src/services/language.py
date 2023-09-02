from models.language import Language


def get_all_languages():
    languages = Language.get_all()
    return {'languages': languages}, 200
