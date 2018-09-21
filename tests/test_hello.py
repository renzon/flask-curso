import pytest
from flask import url_for


@pytest.fixture
def resp(client):
    response = client.get(url_for('hello'))
    return response


def test_hello_status_code(resp):
    assert resp.status_code == 200


def test_hello_msg(resp):
    assert 'Olá Mundo' in resp.get_data(as_text=True)
