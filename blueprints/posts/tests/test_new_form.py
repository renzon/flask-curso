import pytest
from flask import url_for


@pytest.fixture
def resp(client):
    return client.get(url_for('posts.new'))


def test_status_code(resp):
    assert resp.status_code == 200


@pytest.mark.parametrize(
    'content',
    [
        '<form',
        'name="title"',
        'name="content"',
        'type="submit"'
    ]
)
def test_form_content(resp, content):
    assert content in resp.get_data(as_text=True)
