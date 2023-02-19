from flask import Flask
from flask_restx import Api

from main.config import Config
from main.setup_db import db
from main.views.places import places_ns


def create_app(config: Config, application) -> Flask:

    application.config.from_object(config)
    application.app_context().push()
    return application


def register_extensions(application: Flask):
    db.init_app(application)
    api = Api(application)
    api.add_namespace(places_ns)


app = Flask(__name__)

app_config = Config()
app = create_app(app_config, app)

register_extensions(app)

if __name__ == 'main':
    app.run()
