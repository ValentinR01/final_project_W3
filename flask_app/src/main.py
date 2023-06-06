import os
from flask import Flask
from flask_cors import CORS
from blueprints import blueprint as swagger
# Import postgres à faire ici
# from mongoengine import connect

app = Flask(__name__)
app.config['RESTPLUS_MASK_SWAGGER'] = False

CORS(app)
app.register_blueprint(swagger)

# Connexion à postgres à faire ici
# connect(host=os.environ.get('MONGO_URI'))

if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0")
