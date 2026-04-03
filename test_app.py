import pytest
from app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_quote_endpoint(client):
    response = client.get("/quote")
    assert response.status_code == 200
    data = response.get_json()
    assert "quote" in data
    assert "author" in data
    assert data["status"] == "success"

def test_health_endpoint(client):
    response = client.get("/health")
    assert response.status_code == 200
    data = response.get_json()
    assert data["status"] == "ok"
    assert data["service"] == "quoteapi"
