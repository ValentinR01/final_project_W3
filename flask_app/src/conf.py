import os


DEBUG = os.environ.get("DEBUG", 0)

# JWT
TOKEN_EXPIRATION_HOURS = os.environ.get("TOKEN_EXPIRATION_HOURS", 10)
TOKEN_SECRET = os.environ.get("TOKEN_SECRET", "H€t1C")

# DB
SQLALCHEMY_DATABASE_URI = os.environ.get(
    "SQLALCHEMY_DATABASE_URI",
    "postgresql://postgres:postgres@postgresql:5432/data"
)
