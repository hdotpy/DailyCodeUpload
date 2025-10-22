from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.redbus.in/")
    page.get_by_role("button", name="From").click()
    page.get_by_role("textbox", name="From").fill("Che")
    time.sleep(2)  # Wait for suggestions to load
    page.get_by_role("button", name="From Search suggestions").click()
    page.wait_for_timeout(5000)
    page.close()


    



