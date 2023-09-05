from flask import request
import logging

from models.asset import Asset
from helpers.auth import AuthHandler
from services.base import get_all_entities, search_entities, get_entity_by_id, \
    update_entity


def create_asset(data: dict):
    """Create a new asset"""
    logging.info(data)
    # Necéssaire:
    # - title yes
    # - music_title yes
    # - created_by_id
    # - updated_by_id
    # - step_lifecycle_id yes
    # - status_by_domain_id yes
    #
    # Facultatif:
    # - composer_id yes
    # - speaker_id yes
    # - student_fullname yes
    # - comment yes # à modifier pour créer un commentaire dans la table commentaire
    # - instruments yes # à modifier pour créer une/des key value
    # - category yes # à modifier pour créer une key value

    # 1. Récupérer dans le token l'id de l'user en cours et l'assigner à created_by_id et updated_by_id
    # 2. Créer l'asset
    # 3. Créer le commentaire si il y en a un
    # 4. Assicier le/les instruments si il y en a à l'asset
    # 5. Associer la catégorie si il y en a une à l'asset

    del data['instruments']
    del data['category']

    if not request:
        token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6NCwiZn" \
                "VsbG5hbWUiOiJzYWxpbiIsImVtYWlsIjoic2FsaW5Ac2FsaW5lL" \
                "mNvbSIsInJvbGUiOiJ3b3JrZXIiLCJkb21haW4iOiJyZWRhY3Rp" \
                "b24iLCJleHAiOjE2ODkwMjk5MDIsImlhdCI6MTY4ODk5MzkwMn" \
                "0.r4UalimTKPHVIDABZei3px6armJdAd_TOVAM_uEazTM"
    else:
        token = request.cookies.get('authorization')
    decode_token = AuthHandler.decode_token(token)

    user = decode_token['id']

    new_asset = Asset(title=data['title'], music_title=data['music_title'],
                      created_by_id=user, updated_by_id=user,
                      composer_id=data['composer_id'])
    new_asset.create()


    return {'Asset created successfully': data}, 200


def get_asset(**kwargs):
    """Get all assets"""
    if kwargs.get('id'):
        return get_entity_by_id(
            entity=Asset,
            entity_id=kwargs.get('id')
        )
    return get_all_entities(entity=Asset, **kwargs)


def search_asset(search: str):
    """Search assets"""
    return search_entities(Asset, search, "title", "music_title")


def update_asset(data: dict):
    """Update an asset"""
    return update_entity(
        data=data, entity=Asset, entity_id=data.get('id')
    )
