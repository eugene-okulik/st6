import allure
from playwright.sync_api import expect
from st6.tests_UI_oksana_PW.pages.base import BasePage
from st6.tests_UI_oksana_PW.pages.locators.locators import ProductCheckerLocators as loc


class ProductChecker(BasePage):
    relative_url = 'collections/eco-friendly.html'

    @allure.step("Hover over the second product image")
    def hover_over_product(self):
        element_to_hover_over = self.find(loc.HOVER_ELEMENT)
        element_to_hover_over.hover()

    @allure.step("Click on 'Add to Wish List' for the second product")
    def add_to_wishlist(self):
        add_to_wishlist_button = self.find(loc.WISHLIST_BUTTON)
        add_to_wishlist_button.click()

    @allure.step("Check for the login requirement message")
    def check_login_message(self, login_message):
        page_message = self.find(loc.LOGIN_MESSAGE).first
        expect(page_message).to_have_text(login_message)

    @allure.step("Hover over and click on the third product")
    def select_third_product(self):
        select_third_element = self.find(loc.SELECT_THIRD_PRODUCT)
        select_third_element.click()

    @allure.step("Select product size")
    def select_product_size(self):
        size_button = self.find(loc.PRODUCT_SIZE)
        size_button.click()

    @allure.step("Add product to cart without selecting color")
    def add_to_cart(self):
        add_button = self.find(loc.ADD_TO_CART)
        add_button.click()

    @allure.step("Verify color selection error message")
    def verify_color_error_message(self, error_message):
        color_error = self.find(loc.COLOR_ERROR)
        expect(color_error).to_have_text(error_message)

    @allure.step("Verify color selection")
    def select_color(self):
        color = self.find(loc.SELECT_COLOR)
        color.click()

    @allure.step("Set the product quantity")
    def set_product_quantity(self, search_word):
        quantity_items = self.find(loc.PRODUCT_QUANTITY)
        quantity_items.fill('')
        quantity_items.fill(search_word)

    @allure.step("Verify error message for quantity limit")
    def verify_quantity_error_message(self, error_message):
        error_message_element = self.find(loc.VERIFY_QUANTITY_ERROR_MESSAGE)
        expect(error_message_element).to_have_text(error_message)
