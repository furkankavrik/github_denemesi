from playwright.sync_api import sync_playwright
import pytest

@pytest.fixture
def yeni_sayfa(autouse = True):#autouse make fixture executed when the code run.
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch()
    page = browser.new_page()
    return  page