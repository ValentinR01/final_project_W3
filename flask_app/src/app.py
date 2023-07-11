import os
from flask import Flask
from flask_cors import CORS
from db import db, migrate
from models import all_tables  # Don't erase !!
from blueprints import blueprint as api
import logging
from conf import POSTGRESQL_DATABASE_URI, DEBUG, ENV
from sqlalchemy import text
from sqlalchemy.exc import IntegrityError
import fnmatch

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)

app.config['RESTPLUS_MASK_SWAGGER'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = POSTGRESQL_DATABASE_URI


CORS(app)

app.register_blueprint(api)


if __name__ == "__main__":
    debug = bool(DEBUG)
    if ENV == 'TEST':
        app.run(debug=debug)
    else:
        with app.app_context():
            db.init_app(app)
            db.create_all()
            migrate.init_app(app, db)

            session = db.session()
            for file in os.listdir('src/query/'):
                if fnmatch.fnmatch(file, 'init_layer_*.sql'):
                    logging.info(f"Executing {file}")
                    with open(f'src/query/{file}', 'r') as query:
                        try:
                            session.execute(text(query.read()))
                            session.commit()
                            logging.info(f"Layer {file} been executed "
                                         f"successfully")
                        except IntegrityError as e:
                            session.rollback()
                            logging.error(f"Error: {e}")

        app.run(host='0.0.0.0', port=8000, debug=debug)
