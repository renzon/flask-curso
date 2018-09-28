from flask import Blueprint

from blueprints.posts.models import Post
from ext.db import db

bp = Blueprint('posts', __name__)


def init_app(app, url_prefix='/posts'):
    app.register_blueprint(bp, url_prefix=url_prefix)


@bp.route('/new', methods=['GET', 'POST'])
def new():
    post = Post(title='Meu Post', content='Meu conteúdo')
    db.session.add(post)
    db.session.commit()
    return repr(post)
