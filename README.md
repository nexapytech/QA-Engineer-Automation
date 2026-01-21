![CI](https://github.com/nexapytech/QA-Engineer-Automation/actions/workflows/ci.yml/badge.svg)

# Expense Tracker QA Automation Repo

This repository contains QA automation for the **Expense Tracker API** built with **Django REST Framework**.

## What is covered

This repo includes:

### API Tests (pytest)
- Auth flow (API key generation + login)
- Expense flow
- Validation checks
- Public endpoint checks

###  UI Smoke Tests (Selenium)
- Open UI page
- Generate API key
- Verify core UI elements

###  Postman Collection
- Auth
- Add Transaction
- Get Transactions
- Get Balance


###  CI (GitHub Actions)
Runs tests on every push and shows a green badge.


---

##  How to run tests locally

### 1. Install dependencies

```bash
pip install -r requirements.txt
pytest  -v 

```


###  UI Smoke Tests (web)
- Open the UI view at `127.0.0.1:8000/ui/`
- Generate API key using UI form
- Verify key is displayed
- login with the api key 
- add trasanction 
- get balance
- get transaction history 

### Postman Collection
```md
To run Postman collection:

Open Postman

Import postman/ExpenseTracker.postman_collection.json

Set environment variable:

api_key

```

**api will be accessible at**
```bash
http://locahost:8000
```

##  Example code
GET /api/transactions/
X-API-KEY: your_api_key_here


## 1. DOWNLOAD APK FILE 
```bash
http://locahost:8000/downoad_nexpenz

```
