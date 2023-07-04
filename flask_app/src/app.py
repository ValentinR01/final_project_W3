from flask import Flask
from flask_cors import CORS
from blueprints import blueprint as api
from conf import POSTGRESQL_DATABASE_URI
from db import db, migrate
from models import all_tables  # Don't erase !!
import logging

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)

app.config['RESTPLUS_MASK_SWAGGER'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = POSTGRESQL_DATABASE_URI
app.register_blueprint(api)

CORS(app)


def init_values_in_db():
    """
    This function will be used to initialize the values of the database.

    :return:
    """
    all_tables.Domain.init_db_value(
        ['redaction', 'translation', 'management', 'development'],
        all_tables.Domain
    )
    all_tables.Role.init_db_value(
        ['worker', 'lead', 'superadmin', 'dev'],
        all_tables.Role
    )


with app.app_context():
    db.init_app(app)
    db.create_all()
    migrate.init_app(app, db)
    init_values_in_db()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)
