"""Main application module"""
import json

import git
from flask import Flask
from flask_cors import CORS
from flask_restx import Api

from main.config import Config
from main.setup_db import db
from main.views.places import places_ns


def create_app() -> Flask:
    """
    Create Flask application
    :return:    - flask application
    """
    app_config = Config()
    application = Flask(__name__)
    application.config.from_object(app_config)
    application.app_context().push()
    CORS(application, supports_credentials=True)
    return application


def register_extensions(application: Flask):
    """
    Register extensions for Flask application
    :param application:  - flask application
    """
    db.init_app(application)
    api_config = Api(
        application,
        version='1.0.0',
        title='SKYRENT APP API',
        description='API for SKYRENT service',
        contact='mr.saatchyan@yandex.com'
    )
    api_config.add_namespace(places_ns)
    return api_config


app = create_app()
api = register_extensions(app)


# Continuous deployment to pythonanywhere via WebHook
# https://www.youtube.com/watch?v=AZMQVI6Ss64
@app.route('/git_update', methods=['POST'])
def git_update():
    """
    WebHook for GitHub Continuous Deployment to pythonanywhere
    """
    repo = git.Repo('./Project_RAID_back')
    origin = repo.remotes.origin
    repo.create_head(
        'master',
        origin.refs.master
    ).set_tracking_branch(origin.refs.master).checkout()
    origin.pull()
    return '', 200


@app.route('/api/')
def api_docs():
    """
    API to Postmen Collection
    :return:
    """
    urlvars = False  # Build query strings in URLs
    swagger = True  # Export Swagger specifications
    data = api.as_postman(urlvars=urlvars, swagger=swagger)
    return json.dumps(data), 200


if __name__ == '__main__':
    app.run(debug=True)
