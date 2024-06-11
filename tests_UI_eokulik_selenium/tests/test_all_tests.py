from tests_UI_eokulik_selenium.tests.data import search_phrases
import pytest


@pytest.mark.smoke
def test_yoga_button(home_page):
    home_page.open()
    home_page.check_yoga_button()


@pytest.mark.regression
def test_search(home_page, search_page):
    home_page.open()
    home_page.search_text(search_phrases.search_text)
    search_page.product_names_contain_text_(search_phrases.search_text)
