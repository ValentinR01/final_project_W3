from flask import Blueprint
from flask_restx import Api

blueprint = Blueprint('api', __name__)
api = Api(blueprint)

blueprint = Blueprint("api", __name__, url_prefix="/api/v1")

api = Api(
    blueprint,
    version="1.0",
    title="REST API",
    description="A REST API",
)
ns = api.namespace("items", description="Item operations")
