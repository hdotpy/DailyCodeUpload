from pages.homepage import HomePage
from pages.productpage import ProductPage
from playwright.sync_api import Page, expect
import time


def test_homepage(page: Page):
    home = HomePage(page)
    home.load()
    home.select_from_forum()
    home.to_from_forum()
    home.calender_selection()
    home.search_bus()
    time.sleep(5)
    product = ProductPage(page)
    product.seat_filter()
    product.bus_details()
