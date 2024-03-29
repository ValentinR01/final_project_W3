from flask import Blueprint
from flask_restx import Api
from api.user import namespace as user
from api.speaker import namespace as speaker
from api.meta_value import namespace as meta_value
from api.composer import namespace as composer
from api.asset import namespace as asset
from api.booking import namespace as booking
from api.language import namespace as language
from api.category import namespace as categories
from api.role import namespace as role
from api.domain import namespace as domain
from api.specialty import namespace as specialty
from api.comment import namespace as comment  # Do not delete this line pls


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
api.add_namespace(meta_value)
api.add_namespace(composer)
api.add_namespace(booking)
api.add_namespace(language)
api.add_namespace(asset)
api.add_namespace(categories)
api.add_namespace(role)
api.add_namespace(domain)
api.add_namespace(specialty)
