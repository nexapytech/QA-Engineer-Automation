def test_get_app_version_public(client):
    response = client.get("/api/version_control")
    assert response.status_code == 200
    assert "latest_version" in response.json()
