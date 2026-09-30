from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_root():

    response = client.get("/")

    assert response.status_code == 200

    assert response.json()["name"] == (
        "AniVora VPN"
    )


def test_health():

    response = client.get(
        "/health"
    )

    assert response.status_code == 200

    assert response.json()["status"] == (
        "healthy"
    )


def test_status():

    response = client.get(
        "/v1/status"
    )

    assert response.status_code == 200


def test_wireguard():

    response = client.get(
        "/v1/wireguard"
    )

    assert response.status_code == 200


def test_create_user():

    response = client.post(
        "/v1/users",
        json={
            "name": "Test User"
        }
    )

    assert response.status_code == 200

    assert response.json()["success"] is True


def test_list_users():

    response = client.get(
        "/v1/users"
    )

    assert response.status_code == 200


def test_create_peer():

    user_response = client.post(
        "/v1/users",
        json={
            "name": "Peer Test User"
        }
    )

    user_id = (
        user_response
        .json()["user"]["id"]
    )

    response = client.post(
        "/v1/peers",
        json={
            "user_id": user_id,
            "name": "Phone"
        }
    )

    assert response.status_code == 200

    assert response.json()["success"] is True


def test_list_peers():

    response = client.get(
        "/v1/peers"
    )

    assert response.status_code == 200
