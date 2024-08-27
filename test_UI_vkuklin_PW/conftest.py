from playwright.sync_api import Page, BrowserContext
from test_UI_vkuklin_PW.pages.create_page import CreatePage
from test_UI_vkuklin_PW.pages.eco_friendly_page import EcoFriendlyPage
from test_UI_vkuklin_PW.pages.sale_page import SalePage
import pytest


@pytest.fixture()
def page(context: BrowserContext):
    page: Page = context.new_page()
    return page


@pytest.fixture()
def create_page(page):
    return CreatePage(page)


@pytest.fixture()
def eco_friendly_page(page):
    return EcoFriendlyPage(page)


@pytest.fixture()
def sale_page(page):
    return SalePage(page)
