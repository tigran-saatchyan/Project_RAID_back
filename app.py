import git
from flask import Flask, request
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


# Continuous deployment to pythonanywhere via WebHook
# https://www.youtube.com/watch?v=AZMQVI6Ss64
@app.route('/git_update', methods=['POST'])
def git_update():
    if request.method == 'POST':
        repo = git.Repo('./Project_RAID_back')
        origin = repo.remotes.origin
        repo.create_head(
            'master',
            origin.refs.master
        ).set_tracking_branch(origin.refs.master).checkout()
        origin.pull()
        return '', 200
    else:
        return '', 400


if __name__ == 'main':
    app.run(debug=True)
