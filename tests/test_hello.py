import pytest
from app import app

@pytest.fixture
def resp():
  client = app.test_client()
  response = client.get('/')
  return response
def test_root_status_code(resp):
  """Testing status code from root"""
  assert resp.status_code == 200

def test_root_message(resp):
  assert "Hello World" in resp.get_data(as_text=True)