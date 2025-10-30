from playwright.sync_api import Page
import time


class HomePage:
    def __init__(self, page: Page):
        self.page = page
        self.from_box_click = page.locator(
            "(//div[contains(@class,'srcDestWrapper')])[1]")
        self.search_box_type = page.locator("//input[@id='srcDest']")
        self.from_options = page.locator(
            "//div[contains(@class,'leftContent')]/div[contains(@class,'listHeader')]")
        self.to_box_click = page.locator(
            "(//div[contains(@class,'srcDestWrapper')])[2]")
        self.to_search_box = page.locator(
            "//input[contains(@class, 'inputField___a5ec46')]")

        self.to_options = page.locator(
            "//div[contains(@class,'leftContent')]/div[contains(@class,'listHeader')]")

        self.date_cal = page.locator(
            "(//div[@class='dateWrapper___5e7fce']/div/div)[1]")
        self.next_button = page.locator("(//i[@role='button'])[2]")
        self.select_date = page.locator("div[data-date='1765823400000']")
        self.search_bus_button = page.locator(
            "//button[contains(text(),'Search buses')]")

    def load(self):
        self.page.goto("https://www.redbus.in")

    def select_from_forum(self):
        self.from_box_click.click()
        self.search_box_type.fill("Che")
        self.page.wait_for_timeout(2000)
        option = self.from_options.all()
        for o in option:
            text = o.inner_text()
            if "Chennai" in text:
                o.click()
                break

    def to_from_forum(self):
        self.to_box_click.click()
        self.to_search_box.fill("Bang")
        self.page.wait_for_timeout(2000)
        to_option = self.to_options.all()
        for t in to_option:
            text1 = t.inner_text()
            print(text1)
            if "Bangalore" in text1:
                t.click()
                break

    def calender_selection(self):
        self.date_cal.click()
        for i in range(2):
            self.next_button.click()
            time.sleep(0.5)
        self.select_date.click()
        time.sleep(2)

    def search_bus(self):
        self.search_bus_button.click()
