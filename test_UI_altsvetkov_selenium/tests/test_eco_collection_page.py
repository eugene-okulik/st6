from time import sleep
import pytest


def test_dropdown_sort_selected(eco_collection_page):
    eco_collection_page.open()
    eco_collection_page.select_sort_by_value('price')
    eco_collection_page.check_sort_by_value_is_selected()
    eco_collection_page.select_sort_by_value('name')
    eco_collection_page.check_sort_by_value_is_selected()
    eco_collection_page.select_sort_by_value('position')
    eco_collection_page.check_sort_by_value_is_selected()


@pytest.mark.bug('The product "Helios EverCool™ Tee" product is not sorted after selecting "sort by price" '
                 'in dropdown[Sort By]')
def test_ascending_price_check(eco_collection_page):
    eco_collection_page.open()
    eco_collection_page.select_sort_by_value('price')
    sleep(5)
    eco_collection_page.check_ascending_price()


@pytest.mark.bug('The product "Ana Running Short" is not sorted after clicking button[Set Descending Direction]')
def test_descending_price_check(eco_collection_page):
    eco_collection_page.open()
    eco_collection_page.select_sort_by_value('price')
    eco_collection_page.check_descending_price()


def test_check_price_of_goods_displayed(eco_collection_page):
    eco_collection_page.open()
    eco_collection_page.check_price_of_goods_displayed()


def test_check_image_photo_displayed(eco_collection_page):
    eco_collection_page.open()
    eco_collection_page.check_image_of_goods_displayed()


def test_check_next_button_redirects_next_page(eco_collection_page):
    eco_collection_page.open()
    eco_collection_page.check_next_button_redirect_next_page()
