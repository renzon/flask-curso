import pytest
from flask import url_for

from blueprints.posts.models import Post


@pytest.fixture
def resp(client, db):
    return client.post(
        url_for('posts.new'),
        data={'title': 'HU', 'content': 'Travel'}
    )


def test_status_code(resp):
    assert resp.status_code == 302


def test_post_created(resp):
    assert Post.query.count() == 1
