# pages/logincredentials.py
from playwright.sync_api import Page


class LoginCredentials:
    def __init__(self, page: Page):
        self.page = page
        self.accepted_usernames = page.locator("#login_credentials")
        self.accepted_password = page.locator("div.login_password")

    def load(self):
        self.page.goto("https://www.saucedemo.com/")

    def _clean_lines(self, raw: str):
        after_colon = raw.partition(":")[2]
        return [tok.strip() for tok in after_colon.replace("\n", " ").split() if tok.strip()]

    def get_usernames(self):
        text = self.accepted_usernames.inner_text()
        return self._clean_lines(text)

    def get_password(self):
        # Return a single string, not a list
        text = self.accepted_password.inner_text()
        lines = self._clean_lines(text)
        return lines[0] if lines else ""
