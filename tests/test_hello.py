from app import app

def test_root_status_code():
  """Testing status code from root"""
  client = app.test_client()
  response = client.get('/')
  assert response.status_code == 200

def test_root_message():
  client = app.test_client()
  response = client.get('/')
  assert "Hello World" in response.get_data(as_text=True)