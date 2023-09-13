import os


DEBUG = os.environ.get("DEBUG")
ENV = os.environ.get("ENV")

# JWT
TOKEN_EXPIRATION_HOURS = os.environ.get("TOKEN_EXPIRATION_HOURS", 720)
TOKEN_SECRET = os.environ.get("TOKEN_SECRET", "H€t1C")

# DB
POSTGRESQL_DATABASE_URI = \
    "postgresql://postgres:postgres@dam-postgresql:5432/data"
