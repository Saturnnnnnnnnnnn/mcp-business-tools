
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    r = client.get('/health')
    assert r.status_code == 200

def test_get_exchange_rate():
    r = client.post('/tool/get_exchange_rate', json={'from_currency':'USD','to_currency':'RUB'})
    assert r.status_code in (200, 500)
    data = r.json()
    assert 'success' in data
