from playwright.sync_api import sync_playwright
import pytest

from tests.deneme.steps import * # important part of framework. Having more module like this is better for organisation.


@pytest.fixture
def yeni_sayfa(autouse = True):#autouse make fixture executed when the code run.
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch()
    page = browser.new_page()
    return  page