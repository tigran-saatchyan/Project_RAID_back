"""Flask application configuration module"""
import dataclasses

from main.constants import SQLITE_DB_NAME


@dataclasses.dataclass
class Config:
    """
    SQLALCHEMY configuration
    """
    SQLALCHEMY_DATABASE_URI = SQLITE_DB_NAME
    SQLALCHEMY_TRACK_MODIFICATIONS = False
