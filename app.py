"""Main application module"""
import git
from flask import Flask
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
    return application


def register_extensions(application: Flask):
    """
    Register extensions for Flask application
    :param application:  - flask application
    """
    db.init_app(application)
    api = Api(application)
    api.add_namespace(places_ns)


app = create_app()
register_extensions(app)


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


if __name__ == '__main__':
    app.run(debug=True)
