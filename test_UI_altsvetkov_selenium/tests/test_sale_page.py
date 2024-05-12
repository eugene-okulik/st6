def test_check_button_shop_women_deals(sale_page):
    sale_page.open()
    sale_page.click_button_shop_women_deals()
    sale_page.check_btn_shop_women_is_redirects_to_sale_page()


def test_check_block_20_discount_promotion(sale_page):
    sale_page.open()
    sale_page.check_block_20_discount_text_match()


def test_check_menu_categories_titles(sale_page):
    sale_page.open()
    sale_page.check_menu_categories_titles_match()
