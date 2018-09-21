from flask import Flask

from blueprints.names.bp import bp as names_bp

app = Flask(__name__)

app.register_blueprint(names_bp, url_prefix='/')
