import os
from flask import Flask
from flask_cors import CORS

# Import postgres à faire ici
# from mongoengine import connect

app = Flask(__name__)
app.config['RESTPLUS_MASK_SWAGGER'] = False

CORS(app)

@app.route('/')
def home():
    app.logger.info("Hello there")
    return 'hello, world'


# Connexion à postgres à faire ici
# connect(host=os.environ.get('MONGO_URI'))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)
