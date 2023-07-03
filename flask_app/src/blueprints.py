from flask import Blueprint
from flask_restx import Api
from api.user import namespace as user
from api.speaker import namespace as speaker

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