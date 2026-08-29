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

## Related Project

The chatbot under test is a live RAG-powered customer support bot built with FastAPI, ChromaDB, and Gemini embeddings — see [sneakdoc-chatbot](https://github.com/alimehboob313/sneakdoc-chatbot).