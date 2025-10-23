from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.redbus.in/")
    page.locator("//div[contains(@class,'dojWrapper')]/span[contains(text(),'Date of Journey')]").click()
    page.wait_for_timeout(5000)
    page.close()


    



