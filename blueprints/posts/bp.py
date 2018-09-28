from flask import Blueprint, redirect, render_template, request, url_for

from blueprints.posts.models import Post
from ext.db import db

bp = Blueprint('posts', __name__, template_folder='templates')


def init_app(app, url_prefix='/posts'):
    app.register_blueprint(bp, url_prefix=url_prefix)


@bp.route('/new', methods=['GET', 'POST'])
def new():
    if request.method == 'GET':
        return render_template('posts/form.html')
    form = request.form
    post = Post(title=form['title'], content=form['content'])
    db.session.add(post)
    db.session.commit()
    return redirect(url_for('posts.list_posts'))


@bp.route('/', )
def list_posts():
    query = Post.query.order_by(Post.title.asc())
    posts = query[:10]
    return render_template('posts/index.html', posts=posts)
