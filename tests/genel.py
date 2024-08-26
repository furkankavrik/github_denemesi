import pytest
import playwright

from playwright.sync_api import sync_playwright, Playwright


def yeni_sayfa():
        
    
    
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch()
    page = browser.new_page()

    return  page
