
def test_add_transaction_success(client, auth_headers):
    response = client.post(
        "/api/add_transaction",
        data={
            "note": "Lunch",
            "amount": 100,
            "type": "income",
            
        },
        **auth_headers
    )

    assert response.status_code == 200
    assert response.json().get("note") == "Lunch"


def test_get_transactions(client, auth_headers):
    client.post(
        "/api/add_transaction",
        data={"note": "Lunch", "amount": 100, "type": "expense"},
        **auth_headers
    )

    response = client.get("/api/get_transaction", **auth_headers)
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_balance(client, auth_headers):
    response = client.get("/api/get_balance", **auth_headers)
    assert response.status_code == 200
    assert "total_balance" in response.json()


def test_filter_by_date_transaction(client, auth_headers):
    client.post(
        "/api/add_transaction",
        data={
            "title": "note",
            "amount": 100,
            "type": "expense",
            "date": "2024-01-01"
        },
        **auth_headers
    )

    response = client.get(
        "/api/filter_by_date_transaction?start=2024-01-01&end=2024-01-31",
        **auth_headers
    )
    assert response.status_code == 200
    assert isinstance(response.json(), list)
