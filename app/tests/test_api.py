from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_classify_number():
    response = client.get("/api/classify-number?number=371")
    assert response.status_code == 200
    assert response.json()["number"] == 371
    assert "armstrong" in response.json()["properties"]
