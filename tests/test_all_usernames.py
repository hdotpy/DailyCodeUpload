from pages.logincredentials import LoginCredentials
from pages.loginaction import LoginAction
from playwright.sync_api import Page, expect
import pytest


@pytest.mark.parametrize("idx", [0, 1, 2, 3, 4, 5])
def test_all_user_login(page: Page, idx: int):
    action = LoginAction(page)
    action.load()
    usernames = action.get_usernames()
    password = action.get_password()

    username = usernames[idx]

    action.login_user(username, password)

    if username == "locked_out_user":
        expect(page.locator("[data-test='error']")).to_be_visible()
    else:
        expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
        # Clean up for the next param run
        page.click("#react-burger-menu-btn")
        page.click("#logout_sidebar_link")
