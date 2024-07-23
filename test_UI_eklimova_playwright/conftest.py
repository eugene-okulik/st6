from playwright.sync_api import Page, BrowserContext
from test_UI_eklimova_playwright.pages.create_new_account_page import CreateNewAccount
from test_UI_eklimova_playwright.pages.eco_frienfly_page import EcoFriendlyPage
from test_UI_eklimova_playwright.pages.sale_page import SalePage
import pytest
import json


@pytest.fixture()
def page(context: BrowserContext):
    new_page: Page = context.new_page()
    return new_page


@pytest.fixture()
def create_new_account(page):
    return CreateNewAccount(page)


@pytest.fixture()
def eco_friendly(page):
    return EcoFriendlyPage(page)


@pytest.fixture()
def sale_page(page):
    return SalePage(page)


@pytest.fixture
def creds():
    with open('creds.json') as f:
        return json.load(f)
