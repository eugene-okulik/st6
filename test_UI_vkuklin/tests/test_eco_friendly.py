import pytest


@pytest.mark.regression
def test_header(eco_friendly_page):
    eco_friendly_page.open()
    eco_friendly_page.check_header()


@pytest.mark.regression
def test_img_cards(eco_friendly_page):
    eco_friendly_page.open()
    eco_friendly_page.check_img_cards()


@pytest.mark.regression
def test_stars_rating(eco_friendly_page):
    eco_friendly_page.open()
    eco_friendly_page.check_stars_rating()
