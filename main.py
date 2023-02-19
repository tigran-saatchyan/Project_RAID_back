from flask import Flask
from flask_restx import Api

from app.config import Config
from app.setup_db import db
from app.views.places import places_ns


def create_app(config: Config) -> Flask:
    application = Flask(__name__)
    application.config.from_object(config)
    application.app_context().push()
    return application


def register_extensions(application: Flask):
    db.init_app(application)
    api = Api(application)
    api.add_namespace(places_ns)


if __name__ == '__main__':
    app_config = Config()
    app = create_app(app_config)

    register_extensions(app)

    app.run()
