# ci-cd-test-pipeline
# E2E Test Pipeline

![Tests](https://github.com/VivekanandUsingh/ci-cd-test-pipeline/actions/workflows/e2e-tests.yml/badge.svg)
![Python](https://img.shields.io/badge/Python-3.11-blue)
![Playwright](https://img.shields.io/badge/Playwright-1.44-green)
![License](https://img.shields.io/badge/license-MIT-lightgrey)

A production-grade end-to-end UI test automation pipeline built with Python and Playwright. Demonstrates the Page Object Model pattern, reusable fixtures, CI/CD integration with GitHub Actions, screenshot capture on failure, and scheduled regression runs.

---

## Framework Architecture

```
ci-cd-test-pipeline/
├── config/
│   └── config.yaml              # URLs, users, timeouts — no hardcoded values
├── pages/
│   ├── base_page.py             # Shared page utilities and navigation
│   ├── login_page.py            # Login page locators and actions
│   ├── inventory_page.py        # Product page locators and actions
│   └── cart_page.py             # Cart page locators and actions
├── tests/
│   ├── test_login.py            # Login E2E test suite (8 tests)
│   └── test_inventory.py        # Products & cart E2E test suite (12 tests)
├── reports/                     # Auto-generated HTML reports + screenshots
├── .github/
│   └── workflows/
│       └── e2e-tests.yml        # GitHub Actions CI/CD pipeline
├── conftest.py                  # Shared pytest-playwright fixtures
├── pytest.ini                   # pytest configuration
└── requirements.txt             # Dependencies
```

---

## What This Framework Demonstrates

- **Page Object Model (POM)** — clean separation of locators, actions, and tests
- **Base page inheritance** — shared utilities inherited across all page objects
- **Config-driven design** — all URLs, credentials, and timeouts in YAML
- **Fixture composition** — session, function, and pre-authenticated fixtures
- **Headless browser execution** — Chromium running in CI with no display
- **Screenshot on failure** — automatic capture when tests fail in pipeline
- **Scheduled regression** — daily 9AM automated run catches environment drift
- **HTML report generation** — downloadable artifact on every pipeline run

---

## Test Coverage

| Suite | Tests | Scenarios |
|---|---|---|
| Login | 8 tests | Valid login, invalid credentials, locked user, empty fields, logout |
| Products | 8 tests | Item count, titles, prices, add to cart, sorting (A-Z, price asc/desc) |
| Cart | 4 tests | Navigation, item appears, count matches, remove item |
| **Total** | **20 tests** | |

---

## Setup & Run

**1. Clone the repo**
```bash
git clone https://github.com/VivekanandUsingh/ci-cd-test-pipeline.git
cd ci-cd-test-pipeline
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
playwright install chromium
```

**3. Run all tests**
```bash
pytest
```

**4. Run a specific suite**
```bash
pytest tests/test_login.py -v
pytest tests/test_inventory.py -v
```

**5. Run with headed browser (see the browser open)**
```bash
pytest --headed
```

---

## CI/CD Pipeline

Runs automatically via GitHub Actions on:
- Every push to `main`
- Every pull request to `main`
- Daily at 9:00 AM UTC

On failure, screenshots are automatically captured and uploaded as a separate artifact for immediate debugging.

---

## Tech Stack

| Tool | Purpose |
|---|---|
| Python 3.11 | Core language |
| Playwright | Browser automation |
| pytest-playwright | Playwright fixtures for pytest |
| pytest-html | HTML report generation |
| GitHub Actions | CI/CD automation |

---

## Author

**Vivekanand Singh** — QA Architect with 20 years across Web, Mobile, API, and Platform Migration
[LinkedIn](https://www.linkedin.com/in/vivekanand09/) · [GitHub](https://github.com/VivekanandUsingh)
