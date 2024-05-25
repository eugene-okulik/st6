from playwright.sync_api import Page, BrowserContext
import pytest
from tests_UI_eokulik_PW.pages.home_page import HomePage
from tests_UI_eokulik_PW.pages.search_page import SearchPage


@pytest.fixture()
def page(context: BrowserContext):
    new_page: Page = context.new_page()
    return new_page


@pytest.fixture()
def home_page(page):
    return HomePage(page)


@pytest.fixture()
def search_page(page):
    return SearchPage(page)
