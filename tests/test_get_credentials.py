import pytest
from pages.logincredentials import LoginCredentials
from playwright.sync_api import Page


def test_get_credentials(page: Page):
    credentials = LoginCredentials(page)
    credentials.load()
    credentials.get_usernames()
    credentials.get_password()
    
