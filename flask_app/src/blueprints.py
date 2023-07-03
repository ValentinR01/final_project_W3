from flask import Blueprint
from flask_restx import Api
from flask_app.src.api.user import namespace as user
# from api.user import namespace as hello_world_ns

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
api.add_namespace(user)
# api.add_namespace(hello_world_ns)
#api.add_resource(Item, '/item/<string:name>')