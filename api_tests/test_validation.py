def test_add_transaction_missing_title(client, auth_headers):
    response = client.post("/api/add_transaction", data={
        "amount": 100,
        "type": "expense"
    }, **auth_headers)

    assert response.status_code == 400

def test_add_transaction_invalid_amount(client, auth_headers):
    response = client.post("/api/add_transaction", data={
        "title": "Lunch",
        "amount": 33333,
        "type": "expense"
    }, **auth_headers)

    assert response.status_code == 400

def test_add_expense_insufficient_balance(client, auth_headers):
    # Assuming no income exists so balance is 0
    response = client.post("/api/add_transaction", data={
        "title": "Expensive",
        "amount": 10,
        "type": "expense"
    }, **auth_headers)

    assert response.status_code == 400
    assert "Insufficient balance" in response.json().get("error", "")
