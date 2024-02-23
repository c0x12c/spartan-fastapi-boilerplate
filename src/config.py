import os

from dotenv import load_dotenv

basedir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
env = os.path.join(basedir, ".env")
if os.path.exists(env):
    load_dotenv(env)
else:
    print("Warning: .env file not found")


class Config(object):
    DEBUG: bool = False
    TESTING: bool = False
    SECRET_KEY: str = os.environ.get("SECRET_KEY", "my-secret-key")
    JWT_SECRET_KEY: str = os.environ.get("JWT_SECRET_KEY", SECRET_KEY)
    JWT_ALGORITHM: str = os.getenv("JWT_ALGORITHM", "HS256")
    SQLALCHEMY_DATABASE_URI: str = os.environ.get(
        "DATABASE_URL", "sqlite:///" + os.path.join(basedir, "db.sqlite")
    )
    SQLALCHEMY_TRACK_MODIFICATIONS: bool = False


class DevConfig(Config):
    pass
