import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from playwright.sync_api import sync_playwright
from pages.homepage import HomePage

def test_homepage_loads():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        home = HomePage(page)
        home.goto()

        assert "SneakDoc" in page.title() or page.url == home.url

        browser.close()

def test_shop_now_navigates_to_store():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        home = HomePage(page)
        home.goto()
        home.click_shop_now()

        assert "/store" in page.url

        browser.close()