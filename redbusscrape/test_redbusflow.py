from playwright.sync_api import Page, expect
import pytest
import time


def test_redbusflow(page: Page):
    page.goto("https://www.redbus.in")
    page.locator("(//div[contains(@class,'srcDestWrapper')])[1]").click()
    page.locator("//input[@id='srcDest']").fill("che")
    page.wait_for_timeout(2000)
    from_options = page.locator(
        "//div[contains(@class,'leftContent')]/div[contains(@class,'listHeader')]").all()
    for f in from_options:
        print(f.inner_text())
        if "Chennai" in f.inner_text():
            f.click()
            break
    page.locator("(//div[contains(@class,'srcDestWrapper')])[2]").click()
    page.locator(
        "//input[contains(@class, 'inputField___a5ec46')]").fill("Bang")
    page.wait_for_timeout(2000)
    to_options = page.locator(
        "//div[contains(@class,'leftContent')]/div[contains(@class,'listHeader')]").all()
    for t in to_options:
        expect(t).to_have_text("Bangalore")
        if "Bangalore" in t.text_content():
            t.click()
            break
    date_cal = "(//div[@class='dateWrapper___5e7fce']/div/div)[1]"
    page.locator(date_cal).click(button="left")
    print("clicked")
    next_button = page.locator("(//i[@role='button'])[2]")
    for i in range(2):
        next_button.click()
        time.sleep(0.5)
    page.locator("div[data-date='1765823400000']").click()
    page.locator("//button[contains(text(),'Search buses')]").click()
    time.sleep(2)
    page.locator(
        "//div[contains(@class,'mainContainer') and contains(@aria-label,'SLEEPER (7')] ").click()
    time.sleep(2)
    bus_details = page.locator("div[class='timeFareBoWrap___73e322']").all()
    count = len(bus_details)
    for i in range(count):
        bus = bus_details[i]
        name = bus.locator(
            "//div[@class='travelsName___d34747']").text_content()
        price = bus.locator("p.finalFare___634549").text_content()
        print(f"{name} - {price}")

    page.close()
