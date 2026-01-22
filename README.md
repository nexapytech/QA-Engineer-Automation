![CI](https://github.com/nexapytech/QA-Engineer-Automation/actions/workflows/ci.yml/badge.svg)

# Expense Tracker – QA Automation

This repository contains a **comprehensive QA automation framework** for the **Expense Tracker API**, built with **Django REST Framework (DRF)**.

It is designed to validate **API correctness**, **UI stability**, and **end-to-end workflows**, while demonstrating **real-world QA engineering practices** such as CI integration, test layering, and environment-based execution.

---
##  Tech Stack

###  Test Automation
- **Python** – Core language for writing automated tests
- **Pytest** – Primary test framework for API and UI automation

### 🌐 API & Backend
- **Django REST Framework (DRF)** – Backend API under test
- **RESTful APIs** – Stateless service communication

###  API Testing Tools
- **Postman** – Manual and exploratory API testing
- **Postman Collections** – Reusable API request definitions

### ⚙️ CI / DevOps
- **GitHub Actions** – Continuous Integration for automated test execution
- **YAML** – CI workflow configuration

### 📦 Dependency Management
- **pip** – Python package manager
- **requirements.txt** – Dependency version control

### 🖥️ Environment
- **Localhost (development)** – Local execution and debugging
- **Linux-based CI runners** – GitHub-hosted runners for automation


## API Endpoints
| Action                     | Method | Endpoint |
|---------------------------|--------|----------|
| Generate API Key           | POST   | /api/signup |
| Login with API Key         | POST   | /api/login_securely |
| View API Settings          | GET    | /api/settings |
| Get Supported Currencies   | GET    | /api/get_currency |
| Add Expense Transaction    | POST   | /api/add_transaction |
| Get All Transactions       | GET    | /api/get_transaction |
| Get Account Balance        | GET    | /api/get_balance |
| Filter Transactions by Date| GET    | /api/filter_by_date_transaction |
| Get API Version            | GET    | /api/version_control |


---
## Example
```bash
GET https://api.nexapytechnologies.com/api/get_balance
API-KEY: your_api_key_here
```
**📌 Note: Requests to these endpoints must include a valid API key in the header.**

---

## 🌍 Environments
###  Production
```bash
https://api.nexapytechnologies.com
```

### Development
```bash
http://localhost:8000
```
⚠️ Localhost is strictly for development and testing.
All real usage should point to the production API.

🚫 What Happens Without an API Key?

❌ Missing API key → 401 Unauthorized

❌ Invalid API key → 403 Forbidden

✅ Valid API key → 200 OK
---

###  API Automation (Pytest)

Covers critical backend workflows and edge cases, including:

- **Authentication**
  - API key generation
  - API key–based authorization
  - Invalid / missing key handling
- **Expense Management**
  - Create expense transactions
  - Retrieve transaction history
  - Validate account balance calculations
- **Validation & Error Handling**
  - Required field checks
  - Invalid payloads
  - Unauthorized access attempts
- **Public Endpoints**
  - Endpoint availability and response integrity

---

###  UI Smoke Tests

Lightweight UI tests to ensure **core user flows are not broken**:

- Open Expense Tracker UI
- Generate API key via UI form
- Verify API key visibility and format
- Authenticate using generated API key
- Add a transaction
- Retrieve balance
- View transaction history
  
---

### 📮 Postman Collection

Includes ready-to-run Postman requests for manual or exploratory testing:

- Authentication
- Add transaction
- Get transactions
- Get balance

File location:
  ```bash
  postman/expense_tracker_api.postman_collection.json
```
### Run API Tests
pytest -v

**Ensure the application is running locally, then:**

Open the UI at:
 ```bash
 http://localhost:8000/ui/
```

**API Usage Example**
```bash
 GET /api/transactions/
X-API-KEY: your_api_key_here
```
**Download Nexpenz APK**
```bash
https://api.nexapytechnologies.com/download_nexpenz
```



