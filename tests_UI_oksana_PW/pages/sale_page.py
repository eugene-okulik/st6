import allure
from playwright.sync_api import expect
from st6.tests_UI_oksana_PW.pages.base import BasePage
from st6.tests_UI_oksana_PW.pages.locators.locators import SaleProductLocators as loc


class SaleChecker(BasePage):
    relative_url = 'sale.html'

    @allure.step("Search for a product")
    def search_for_product(self, send_keys):
        search_input = self.find(loc.SEARCH_INPUT)
        search_input.click()
        search_input.fill(send_keys)
        search_input.press('Enter')

    @allure.step("Verify search results")
    def verify_search_results(self, error_message):
        search_result = self.find(loc.SEARCH_RESULT)
        expect(search_result).to_contain_text(error_message)

    @allure.step("Click on 'More' button")
    def click_more_button(self):
        button_more = self.find(loc.BUTTON_MORE)
        button_more.click()

    @allure.step("Double click on the second product")
    def double_click_second_product(self):
        product = self.find(loc.PRODUCT_CLICK)
        product.dblclick()

    @allure.step("Verify product availability")
    def verify_product_availability(self, error_message):
        find_sale_text = self.find(loc.IN_STOCK)
        expect(find_sale_text).to_have_text(error_message)

    @allure.step("Navigate to the category 'Shorts'")
    def navigate_to_shorts(self):
        find_shorts = self.find(loc.FIND_SHORTS)
        find_shorts.click()

    @allure.step("Verify presence of product images")
    def verify_product_images(self):
        product_images = self.find(loc.PRODUCT_IMAGE_PHOTO)
        count_product = product_images.count()
        assert count_product > 0, "No product images found."

    @allure.step("Verify presence of 'Add to Cart' buttons")
    def verify_add_to_cart_buttons(self):
        add_to_cart_buttons = self.find(loc.ADD_TO_CART_BUTTON)
        count_button = add_to_cart_buttons.count()
        assert count_button > 0, "No product images found."
