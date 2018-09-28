from flask import Flask

import settings
from blueprints.names.bp import bp as names_bp
from blueprints.posts.bp import init_app as posts_init_app
from ext.db import db


def create_app(default_settings=None):
    if default_settings is None:
        default_settings = settings
    app = Flask(__name__)
    app.config.from_object(default_settings)
    app.debug = app.config['DEBUG']
    db.init_app(app)
    app.register_blueprint(names_bp, url_prefix='/')
    posts_init_app(app)
    return app
