from flask import Flask

import settings
from blueprints.names.bp import bp as names_bp

app = Flask(__name__)
app.config.from_object(settings)
app.debug = app.config['DEBUG']

app.register_blueprint(names_bp, url_prefix='/')
