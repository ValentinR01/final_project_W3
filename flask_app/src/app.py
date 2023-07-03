from flask import Flask
from flask_cors import CORS
from flask_app.src.blueprints import blueprint as api
from flask_app.src.conf import POSTGRESQL_DATABASE_URI


app = Flask(__name__)

app.config['RESTPLUS_MASK_SWAGGER'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = POSTGRESQL_DATABASE_URI
app.register_blueprint(api)

CORS(app)


def create_tables():
    from flask_app.src.db import db, migrate
    from flask_app.src.models import all_tables  # Don't erase !!

    with app.app_context():
        db.init_app(app)
        db.create_all()
        migrate.init_app(app, db)


create_tables()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)
