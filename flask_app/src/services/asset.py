from flask import request
import logging

from models.asset import Asset
from models.comment import Comment
from models.metadata import Metadata
from models.meta_value import MetaValue
from helpers.auth import AuthHandler
from services.base import get_all_entities, search_entities,\
    get_entity_by_id, update_entity


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
    # - comment yes # à modifier pour créer un commentaire dans la table
    # commentaire
    # - instruments yes # à modifier pour créer une/des key value
    # - category yes # à modifier pour créer une key value

    # 1. Récupérer dans le token l'id de l'user en cours et l'assigner à
    # created_by_id et updated_by_id
    # 2. Vérifier si le titre est unique
    # 3. Créer l'asset
    # 4. Créer le commentaire si il y en a un
    # 5. Assicier le/les instruments si il y en a à l'asset
    # 6. Associer la catégorie si il y en a une à l'asset

    check_title = Asset.get_all_by(title=data['title'])
    if len(check_title) > 0:
        return {'There is already an asset existing with this title':
                    data['title']}, 409

    if not request:
        token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6NSwiZnVsbG5hb" \
                "WUiOiJzYWxpbmUiLCJlbWFpbCI6InNhbGluZUBzYWxpbmUuY29tIiwicm9s" \
                "ZSI6IndvcmtlciIsImRvbWFpbiI6InJlZGFjdGlvbiIsImV4cCI6MTY5NzI" \
                "yMDE2NSwiaWF0IjoxNjk0NjI4MTY1fQ.duieAudQgx8JGmWMdksZkgxL2kP" \
                "djd_J-64pUXq_Hqw"
    else:
        token = request.cookies.get('authorization')
    decode_token = AuthHandler.decode_token(token)

    user_id = decode_token['id']

    new_asset = Asset(title=data['title'],
                      music_title=data['music_title'],
                      created_by_id=user_id,
                      updated_by_id=user_id,
                      composer_id=data.get('composer_id'),
                      speaker_id=data.get('speaker_id'),
                      student_fullname=data.get('student_fullname'),
                      status_by_domain_id=1,
                      step_lifecycle_id=1)
    new_asset.create()

    asset_id = Asset.get_by(title=data['title']).id

    if 'comment' in data:
        new_comment = Comment(asset_id=asset_id, content=data['comment'],
                              posted_by=user_id)
        new_comment.create()

        #
        check_comment = Comment.get_by(content=data['comment'])
        logging.info(check_comment)
        #

    if 'instruments' in data:
        for instrument in data['instruments']:
            meta_value = MetaValue.get_by(value=instrument)
            new_instrument = Metadata(asset_id=asset_id,
                                      meta_value_id=meta_value.id)
            new_instrument.create()

        #
        check_instruments = Metadata.get_by(asset_id=asset_id)
        logging.info(f'check instruments : {check_instruments}')
        #

    # TODO : Faire le new category si elle existe une fois que val a fait
    #  l'endpoint category et a modifié le modèle

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
