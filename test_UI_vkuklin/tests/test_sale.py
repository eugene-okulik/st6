import pytest


@pytest.mark.regression
def test_header(sale_page):
    sale_page.open()
    sale_page.check_header_sale()


@pytest.mark.regression
def test_img_promo_block(sale_page):
    sale_page.open()
    sale_page.check_image_promo_block()


@pytest.mark.regression
def test_my_wish_list(sale_page):
    sale_page.open()
    sale_page.check_my_wish_list()
