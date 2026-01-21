def test_signup_generates_api_key(client):
    response = client.post("/api/signup", {"username": "testuser"})
    assert response.status_code == 201
    assert "api_key" in response.json()
    assert response.json()["api_key"] != ""


def test_login_with_valid_api_key(client, api_key):
    response = client.post(
        "/api/login_securely",
        {},
        HTTP_AUTHORIZATION=f"Api-Key {api_key}"
    )
    assert response.status_code == 200
    assert "api_key" in response.json()


def test_login_with_invalid_api_key(client):
    response = client.post(
        "/api/login_securely",
        {},
        HTTP_AUTHORIZATION="Api-Key Icjcjc"
    )
    assert response.status_code == 403
