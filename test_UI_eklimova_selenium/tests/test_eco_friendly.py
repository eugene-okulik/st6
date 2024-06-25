# searching works
# adding to cart with chosen size
# adding to cart without size

def test_check_searching_works(eco_friendly):
    eco_friendly.open()
    eco_friendly.send_search_data("tank")
    eco_friendly.check_that_searching_works()


def test_check_adding_to_cart(eco_friendly):
    eco_friendly.open()
    eco_friendly.add_first_element_to_cart()
    eco_friendly.success_message_is_appeared()
    eco_friendly.check_item_in_the_cart()


def test_adding_purchase_without_size(eco_friendly):
    eco_friendly.open()
    eco_friendly.add_purchase_without_size_and_color()
    eco_friendly.check_message_about_necessity_to_choose_options()
