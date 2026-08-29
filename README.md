# SneakDoc Test Suite

Automated test suite for [SneakDoc](https://sneakdoc.com), a Pakistan-based sneaker care e-commerce brand. Built to practice and demonstrate SDET (Software Development Engineer in Test) skills against a real, live application.

## What This Covers

- **UI Automation** — Playwright-based browser tests for the SneakDoc storefront
- **Page Object Model (POM)** — page interactions are abstracted into reusable classes (`pages/`), keeping test logic clean and maintainable
- **API Testing** *(in progress)* — pytest + requests tests against the SneakDoc RAG chatbot's FastAPI backend

## Tech Stack

- Python
- Playwright (browser automation)
- pytest (test framework)

## Project Structure
```
sneakdoc-test-suite/
├── pages/          # Page Object classes
│   └── homepage.py
├── tests/
│   ├── ui/         # Playwright browser tests
│   └── api/        # API tests (upcoming)
└── pytest.ini
```

## Running the Tests

```bash
python -m venv venv
source venv/Scripts/activate   # Windows Git Bash
pip install pytest playwright requests
playwright install
pytest tests/ui/ -v
```
## Known CI Limitation

The GitHub Actions CI pipeline may show test failures that do **not** occur locally. This is because SneakDoc's hosting has bot-protection (challenge/verification pages) that treats GitHub's shared cloud IP ranges as suspicious traffic, and serves a "Security Verification" page instead of the real site.

This is an infrastructure-level constraint, not a bug in the tests themselves — the same test suite passes reliably when run locally, where requests come from a normal residential IP. Handling this properly (e.g. IP allowlisting on the hosting side, or running against a staging environment without bot protection) is a common real-world CI/CD challenge for testing production sites with security layers.

## Related Project

The chatbot under test is a live RAG-powered customer support bot built with FastAPI, ChromaDB, and Gemini embeddings — see [sneakdoc-chatbot](https://github.com/alimehboob313/sneakdoc-chatbot).