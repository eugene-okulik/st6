import pytest
from playwright.sync_api import Page, BrowserContext
from st6.tests_UI_oksana_PW.pages.create_account_page import CreateNewAccount
from st6.tests_UI_oksana_PW.pages.eco_friendly_page import ProductChecker
from st6.tests_UI_oksana_PW.pages.sale_page import SaleChecker


@pytest.fixture()
def page(context: BrowserContext):
    new_page: Page = context.new_page()
    return new_page


@pytest.fixture()
def create_account(page):
    return CreateNewAccount(page)


@pytest.fixture()
def eco_friendly_page(page):
    return ProductChecker(page)


@pytest.fixture()
def sale_page(page):
    return SaleChecker(page)
