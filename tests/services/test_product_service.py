# Unit Tests
from starlette.testclient import TestClient

from app.main import app

client = TestClient(app)

def test_create_product():
    response = client.post("/products", json={"name": "Test Product", "description": "A test item", "price": 10.99, "stock": 50})
    assert response.status_code == 200
    assert response.json()["name"] == "Test Product"

def test_get_products():
    response = client.get("/products")
    assert response.status_code == 200