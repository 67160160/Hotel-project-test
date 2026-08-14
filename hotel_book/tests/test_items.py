from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_and_read_item():
    # 1. ทดสอบการ Create
    response = client.post(
        "/api/v1/items/",
        json={"name": "Test Item", "price": 99.99, "description": "Test Description"}
    )
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Test Item"
    assert "id" in data

    item_id = data["id"]

    # 2. ทดสอบการ Read ID
    get_response = client.get(f"/api/v1/items/{item_id}")
    assert get_response.status_code == 200
    assert get_response.json()["name"] == "Test Item"