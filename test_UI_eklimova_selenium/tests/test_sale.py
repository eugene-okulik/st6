# check "Shop women's deals" redirects to page
# check "Shop men's deals" redirects to page
# check "Shop Luma Gear" deals redirects to page


def test_shop_womens_deals(sale_page):
    sale_page.open()
    sale_page.click_on_womens_button()
    sale_page.check_that_page_redirected_womens_page()


def test_shop_mens_deals(sale_page):
    sale_page.open()
    sale_page.click_on_men_button()
    sale_page.check_that_page_redirected_mens_page()


def test_shop_luma_gear(sale_page):
    sale_page.open()
    sale_page.click_on_luma_button()
    sale_page.check_that_page_redirected_lumas_page()
