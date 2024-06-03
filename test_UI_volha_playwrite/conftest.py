import pytest
from playwright.sync_api import Page, BrowserContext
from test_UI_volha_playwrite.pages.register_page import RegisterPage
from test_UI_volha_playwrite.pages.account_page import AccountPage
from test_UI_volha_playwrite.pages.eco_friendly_page import EcoFriendlyPage
from test_UI_volha_playwrite.pages.sale_page import SalePage


@pytest.fixture()
def page(context: BrowserContext):
    page: Page = context.new_page()
    return page


@pytest.fixture()
def register_page(page):
    return RegisterPage(page)


@pytest.fixture()
def account_page(page):
    return AccountPage(page)


@pytest.fixture()
def eco_page(page):
    return EcoFriendlyPage(page)


@pytest.fixture()
def sale_page(page):
    return SalePage(page)
