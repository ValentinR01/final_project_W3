from flask import Blueprint
from flask_restx import Api
from api.user import namespace as user
from api.speaker import namespace as speaker
from api.metadata import namespace as metadata
from api.composer import namespace as composers
from api.asset import namespace as asset

blueprint = Blueprint('api', __name__)
api = Api(blueprint)

blueprint = Blueprint("api", __name__, url_prefix="/api/v1")

api = Api(
    blueprint,
    version="1.0",
    title="REST API",
    description="A REST API",
)

api.add_namespace(user)
api.add_namespace(speaker)
api.add_namespace(metadata)
api.add_namespace(composers)
api.add_namespace(asset)
