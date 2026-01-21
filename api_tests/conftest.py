import pytest


@pytest.fixture
def client(db):
    """
    DRF API client with database access enabled.
    """
    from rest_framework.test import APIClient
    return APIClient()


@pytest.fixture
def api_key(client):
    """
    Creates a user API key via the signup endpoint.
    """
    response = client.post(
        "/api/signup",
        {"username": "testuser_qa"},
        format="json"
    )

    assert response.status_code == 201
    assert "api_key" in response.data

    return response.data["api_key"]


@pytest.fixture
def auth_headers(api_key):
    """
    Authorization header for API-key protected endpoints.
    """
    return {
        "HTTP_AUTHORIZATION": f"Api-Key {api_key}"
    }
