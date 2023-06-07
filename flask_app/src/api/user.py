from flask import request
from flask_restx import Namespace, Resource, fields
# from services.user_service import signup_service, login_service

namespace = Namespace('hello_world', 'Hello World related endpoints')

hello_world_model = namespace.model('HelloWorld', {
    'message': fields.String(
        readonly=True,
        description='Hello world message'
    )
})

hello_world_example = {'message': 'Hello World!'}


@namespace.route('')
class HelloWorld(Resource):
    @namespace.marshal_list_with(hello_world_model)
    @namespace.response(500, 'Internal Server error')
    def get(self):
        """Hello world message endpoint"""

        return hello_world_example

# @user_route.route("/api/v2/user/signup", methods=['POST'])
# def signup():
#     data = request.get_json()
#     return signup_service(data)
#
#
# @user_route.route("/api/v2/user/login", methods=['POST'])
# def login():
#     data = request.get_json()
#     return login_service(data)
