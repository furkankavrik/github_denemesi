from playwright.sync_api import sync_playwright


def yeni_sayfa():
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch()
    page = browser.new_page()
    return  page