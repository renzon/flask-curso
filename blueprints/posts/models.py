from ext.db import db


class Post(db.Model):
    __tablename__ = 'post'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    content = db.Column(db.Text(), nullable=False)

    def __repr__(self):
        return f'Post(id={self.id}, title={self.title!r}, content={self.content!r})'

    def __str__(self):
        return f'Post {self.title}'
