from db import db
from models.specialty import Specialty
from models.user import User, specialties_users
from services.base import get_all_entities, get_entity_by_id


def get_specialties():
    """Get all specialties"""
    return get_all_entities(entity=Specialty)


def get_specialty_by_id(specialty_id):
    """Get specialty by id"""
    return get_entity_by_id(entity=Specialty, entity_id=specialty_id)


def get_specialties_by_user(user_id):
    """Get all specialties by user"""
    try:
        user_exist = get_entity_by_id(entity=User, entity_id=user_id)
        if 404 in user_exist:
            return {"message": "User not found"}, 404
    except Exception as e:
        return {"error": str(e)}, 500
    result = \
        db.session.query(specialties_users).filter_by(user_id=user_id).all()
    specialties = [r.specialty_id for r in result]
    return {"user_id": user_id, "specialties": specialties}, 200


def post_user_specialty(user_id, specialty_id):
    """Add a new user to a specialty"""
    try:
        user_exist = get_entity_by_id(entity=User, entity_id=user_id)
        if 404 in user_exist:
            return {"message": "User not found"}, 404
        specialty_exist = \
            get_entity_by_id(entity=Specialty, entity_id=specialty_id)
        if 404 in specialty_exist:
            return {"message": "Specialty not found"}, 404
    except Exception as e:
        return {"error": str(e)}, 500
    try:
        specialty = Specialty.query.get(specialty_id)
        specialty.users.append(User.query.get(user_id))
        db.session.commit()
    except Exception as e:
        return {"error": str(e)}, 500
    return {"message": "User added to specialty"}, 200
