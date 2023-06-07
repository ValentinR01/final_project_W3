import os
import re
from conf import SQLALCHEMY_DATABASE_URI
from flask_cors import CORS
from flask import Flask, jsonify, request
from werkzeug.security import generate_password_hash
from models.user import User, db
from auth import AuthHandler
from blueprints import blueprint as api

# Import postgres à faire ici
# from mongoengine import connect

app = Flask(__name__)
app.config['RESTPLUS_MASK_SWAGGER'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.register_blueprint(api)
CORS(app)

db.init_app(app)
with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)


# @app.route('/')
# def index():
#     return jsonify({'message': 'Hello World, SALINE IS COMING SOON...'}), 200


# @app.route('/register', methods=['POST'])
# def register():
#     data = request.form
#     email = data.get('email')
#     username = data.get('username')
#     password = data.get('password')

    # if not email or not username or not password:
    #     return jsonify({'message': 'Missing parameters'}), 400

    # if re.match(r"[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{"
    #             r"|}~-]+)*@saline.com", email) is None:
    #     return jsonify({'message': 'Invalid email'}), 400

    # if User.query.filter_by(email=email).first():
    #     return jsonify({'message': 'Email already exists'}), 409

    # hashed_password = generate_password_hash(password, method='pbkdf2')
    # new_user = User(username=username, password=hashed_password, email=email)
    # new_user.create()

    # return jsonify({'message': 'User created successfully'}), 201


# @app.route('/login', methods=['POST'])
# def login():
#     try:
#         auth_handler = AuthHandler()
#         data = request.form
#         user = auth_handler.authenticate(
#             email=data.get('email'), password=data.get('password')
#         )
#         if not user:
#             return jsonify({'message': 'Invalid email or password'}), 401

    #     token = auth_handler.generate_token(user)
    #     return jsonify(
    #         {
    #             'access_token': token,
    #             'message': 'Login successful'
    #         }
    #     ), 200
    # except Exception as e:
    #     return jsonify({'message': str(e)}), 500


# @app.route('/decode', methods=['POST'])
# def decode():
#     data = request.form
#     token = data.get('token')
#     if not token:
#         return jsonify({'message': 'Missing token'}), 400
#     try:
#         auth_handler = AuthHandler()
#         decoded_token = auth_handler.decode_token(token)
#         return jsonify({'decoded_token': decoded_token}), 200
#     except Exception as e:
#         return jsonify({'message': str(e)}), 500



# # Connexion à postgres à faire ici
# # connect(host=os.environ.get('MONGO_URI'))
