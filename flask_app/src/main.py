import re
from conf import POSTGRESQL_DATABASE_URI
from flask_cors import CORS
from flask import Flask, jsonify, request
from werkzeug.security import generate_password_hash
from models.user import User, db
from auth import AuthHandler
from blueprints import blueprint as api


app = Flask(__name__)
app.config['RESTPLUS_MASK_SWAGGER'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = POSTGRESQL_DATABASE_URI
app.register_blueprint(api)
CORS(app)

db.init_app(app)
with app.app_context():
    db.create_all()


@app.route('/')
def index():
    return jsonify({'message': 'Hello World, SALINE IS COMING SOON...'}), 200




@app.route('/decode', methods=['POST'])
def decode():
    data = request.form
    token = data.get('token')
    if not token:
        return jsonify({'message': 'Missing token'}), 400
    try:
        auth_handler = AuthHandler()
        decoded_token = auth_handler.decode_token(token)
        return jsonify({'decoded_token': decoded_token}), 200
    except Exception as e:
        return jsonify({'message': str(e)}), 500


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
