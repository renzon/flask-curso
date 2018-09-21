from app import app


def test_hello_status_code():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200


def test_hello_msg():
    client = app.test_client()
    response = client.get('/')
    assert 'Olá Mundo' in response.get_data(as_text=True)
