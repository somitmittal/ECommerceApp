from starlette.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_insufficient_stock():
    response = client.post(
        "/orders", json={"products": [{"product_id": 1, "quantity": 99999}]}
    )
    assert response.status_code == 400
