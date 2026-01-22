![CI](https://github.com/nexapytech/QA-Engineer-Automation/actions/workflows/ci.yml/badge.svg)

# Expense Tracker – QA Automation

This repository contains a **comprehensive QA automation framework** for the **Expense Tracker API**, built with **Django REST Framework (DRF)**.

It is designed to validate **API correctness**, **UI stability**, and **end-to-end workflows**, while demonstrating **real-world QA engineering practices** such as CI integration, test layering, and environment-based execution.

---
## 🧰 Tech Stack

### 🧪 Test Automation
- **Python** – Core language for writing automated tests
- **Pytest** – Primary test framework for API and UI automation


### 🌐 API & Backend
- **Django REST Framework (DRF)** – Backend API under test
- **RESTful APIs** – Stateless service communication

### 📮 API Testing Tools
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

---

### 🧪 API Automation (Pytest)

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

### 🖥 UI Smoke Tests

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
###Run API Tests
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
**Download APK**
```bash
http://localhost:8000/download_nexpenz
```

