from main.constants import SQLITE_DB_NAME


class Config:
    # main.run configuration
    DEBUG = True

    # SQLALCHEMY configuration
    SQLALCHEMY_DATABASE_URI = SQLITE_DB_NAME
    SQLALCHEMY_TRACK_MODIFICATIONS = False
