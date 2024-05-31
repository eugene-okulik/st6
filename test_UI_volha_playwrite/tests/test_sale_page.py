def test_menu_categories(sale_page):
    sale_page.open()
    sale_page.check_menu_categories()


def test_page_title(sale_page):
    sale_page.open()
    sale_page.check_page_title_is_sale()


def test_page_category(sale_page):
    sale_page.open()
    sale_page.check_page_category_is_sale()
