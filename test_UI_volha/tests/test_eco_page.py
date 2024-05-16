def test_page_title(eco_page):
    eco_page.open()
    eco_page.check_page_title_is_eco()


def test_page_category(eco_page):
    eco_page.open()
    eco_page.check_page_category_is_eco()


def test_default_num_items(eco_page):
    eco_page.open()
    eco_page.check_default_number_of_items()
