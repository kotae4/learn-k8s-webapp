import sys
sys.path.append("webapp")
sys.path.append("webapp/votingApi")
sys.path.append("learn-k8s-webapp")
sys.path.append("learn-k8s-webapp/votingApi")
sys.path.append(".")

import os
from logging.config import dictConfig
from flask import Flask


def create_app(test_config=None):
    dictConfig({
        'version': 1,
        'formatters': {'default': {
            'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
        }},
        'handlers': {'wsgi': {
            'class': 'logging.StreamHandler',
            'stream': 'ext://flask.logging.wsgi_errors_stream',
            'formatter': 'default'
        }},
        'root': {
            'level': 'INFO',
            'handlers': ['wsgi']
        }
    })
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    if test_config is None:
        # the FLASK_CONFIG envvar should point to a file
        # this file should then contain 'UPPERCASE=value' config values
        # python-style comments are allowed in the config file
        app.config.from_envvar('FLASK_CONFIG', True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from . import polls
    app.register_blueprint(polls.bp)
    app.add_url_rule('/', endpoint='index')

    return app