from playwright.sync_api import Page
from pages.logincredentials import LoginCredentials


class LoginAction(LoginCredentials):
    def __init__(self, page: Page):
        super().__init__(page)
        self.username_field = page.locator("#user-name")
        self.password_field = page.locator("#password")
        self.login_button = page.locator("#login-button")

    def login_user(self, username: str, password: str):
        self.username_field.fill(username)
        self.password_field.fill(password)
        self.login_button.click()
