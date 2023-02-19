from flask import Flask
from flask_restx import Api

from main.config import Config
from main.setup_db import db
from main.views.places import places_ns


def create_app(config: Config) -> Flask:
    application = Flask(__name__)
    application.config.from_object(config)
    application.app_context().push()
    return application


def register_extensions(application: Flask):
    db.init_app(application)
    api = Api(application)
    api.add_namespace(places_ns)


app_config = Config()
app = create_app(app_config)

register_extensions(app)

app.run()
