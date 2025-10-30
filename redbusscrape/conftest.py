from playwright.sync_api import sync_playwright
import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name",
        action="store",
        default="chromium",
        help="Browser selection: chromium | firefox | webkit"
    )


@pytest.fixture(scope="session")
def browser(request):
    browser_name = request.config.getoption("--browser_name")

    if browser_name not in ["chromium", "firefox", "webkit"]:
        raise ValueError(
            "Invalid browser selection. Choose from: chromium, firefox, webkit")

    with sync_playwright() as p:
        if browser_name == "chromium":
            browser_instance = p.chromium.launch(headless=True, slow_mo=100)
        elif browser_name == "firefox":
            browser_instance = p.firefox.launch(headless=True, slow_mo=100)
        else:
            browser_instance = p.webkit.launch(headless=True, slow_mo=100)

        yield browser_instance
        browser_instance.close()


@pytest.fixture(scope="function")
def page(browser):
    page = browser.new_page()
    yield page
    page.close()
