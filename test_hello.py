import pytest
from app import app

def test_hello_string():
    #assert 1 == 1

    client = app.test_client()
    response = client.get('/')
    assert "Olá Mundo" in response.get_data(as_text=True)

def test_hello_200():
    #assert 1 == 1

    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200

