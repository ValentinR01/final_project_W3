from flask import jsonify, request, Blueprint
from flask_restx import Namespace, fields

api = Namespace('user', description='Users endpoints')

# cat = api.model('Cat', {
#     'id': fields.String(required=True, description='The cat identifier'),
#     'name': fields.String(required=True, description='The cat name'),
# })


@api.route('/register', methods=['POST'])
def register():
    data = request.form
    email = data.get('email')
    username = data.get('username')
    password = data.get('password')

    if not email or not username or not password:
        return jsonify({'message': 'Missing parameters'}), 400

    if re.match(r"[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{"
                r"|}~-]+)*@saline.com", email) is None:
        return jsonify({'message': 'Invalid email'}), 400

    if User.query.filter_by(email=email).first():
        return jsonify({'message': 'Email already exists'}), 409

    hashed_password = generate_password_hash(password, method='pbkdf2')
    new_user = User(username=username, password=hashed_password, email=email)
    new_user.create()

    return jsonify({'message': 'User created successfully'}), 201


@app.route('/login', methods=['POST'])
def login():
    try:
        auth_handler = AuthHandler()
        data = request.form
        user = auth_handler.authenticate(
            email=data.get('email'), password=data.get('password')
        )
        if not user:
            return jsonify({'message': 'Invalid email or password'}), 401

        token = auth_handler.generate_token(user)
        return jsonify(
            {
                'access_token': token,
                'message': 'Login successful'
            }
        ), 200
    except Exception as e:
        return jsonify({'message': str(e)}), 500
