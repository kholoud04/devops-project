from fastapi.testclient import TestClient
from app.main import app

def test_home_page():
    with TestClient(app) as client:
        response = client.get("/")
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "success"
        assert "version" in data