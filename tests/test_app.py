from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

def test_root():
    # Arrange: (client is already set up)

    # Act
    response = client.get("/")

    # Assert
    assert response.status_code == 200
    assert "Mergington" in response.text

def test_get_activities():
    # Arrange

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    assert all("description" in v for v in data.values())
