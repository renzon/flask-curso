import pytest
from flask import url_for


@pytest.fixture
def resp(client):
    dct = {'name': 'Renzo', 'lastname': 'Nuccitelli'}
    return client.get(url_for('names.name_lastname'), query_string=dct)


def test_status_code(resp):
    assert resp.status_code == 200


def test_msg(resp):
    assert 'Renzo Nuccitelli' in resp.get_data(as_text=True)
