from playwright.sync_api import Page
import time


class ProductPage:
    def __init__(self, page: Page):
        self.page = page
        self.seater_filter = page.locator(
            "//div[contains(@class,'mainContainer') and contains(@aria-label,'SLEEPER (7')] ")
        self.parent_details = page.locator(
            "div[class='timeFareBoWrap___73e322']")
        self.bus_name = "//div[@class='travelsName___d34747']"
        self.bus_price = "p.finalFare___634549"

    def seat_filter(self):
        self.seater_filter.click()
        self.page.wait_for_timeout(2000)

    def bus_details(self):
        self.page.wait_for_selector(
            "div[class='timeFareBoWrap___73e322']")
        details = self.parent_details.element_handles()
        for bus in details:
            name = bus.query_selector(self.bus_name).text_content()
            price = bus.query_selector(self.bus_price).text_content()
            print(f"{name} -- {price}")
