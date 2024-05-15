import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
from st6.tests_UI_oksana_selenium.pages.base import BasePage
from st6.tests_UI_oksana_selenium.pages.locators.locators import ProductCheckerLocators as loc


class ProductChecker(BasePage):
    relative_url = 'collections/eco-friendly.html'

    @allure.step("Hover over the second product image")
    def hover_over_product(self):
        element_to_hover_over = self.find(loc.HOVER_ELEMENT)
        self.scroll_down()
        hover = ActionChains(self.driver).move_to_element(element_to_hover_over)
        hover.perform()

    @allure.step("Click on 'Add to Wish List' for the second product")
    def add_to_wishlist(self):
        add_to_wishlist_button = WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable(self.find(loc.WISHLIST_BUTTON))
        )
        add_to_wishlist_button.click()

    @allure.step("Check for the login requirement message")
    def check_login_message(self):
        page_message = self.find(loc.LOGIN_MESSAGE)
        expected_message = 'You must login or register to add items to your wishlist.'
        assert page_message.text == expected_message

    @allure.step("Hover over and click on the third product")
    def select_third_product(self):
        element_to_hover_over = self.find(loc.SELECT_THIRD_PRODUCT)
        element_to_hover_over.click()

    @allure.step("Select product size")
    def select_product_size(self):
        size_button = WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable(self.find(loc.PRODUCT_SIZE)))
        size_button.click()

    @allure.step("Add product to cart without selecting color")
    def add_to_cart(self):
        add_button = self.find(loc.ADD_TO_CART)
        add_button.click()

    @allure.step("Verify color selection error message")
    def verify_color_error_message(self):
        color_error = WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located((By.CSS_SELECTOR, "#super_attribute\\[93\\]-error")))
        assert color_error.text == "This is a required field."

    @allure.step("Verify color selection")
    def select_color(self):
        color = self.find(loc.SELECT_COLOR)
        color.click()

    @allure.step("Set the product quantity")
    def set_product_quantity(self):
        quantity_items = self.find(loc.PRODUCT_QUANTITY)
        quantity_items.clear()
        search_word = '10200'
        quantity_items.send_keys(search_word)

    @allure.step("Verify error message for quantity limit")
    def verify_quantity_error_message(self):
        error_message_element = self.find(loc.VERIFY_QUANTITY_ERROR_MESSAGE)
        expected_message = 'The maximum you may purchase is 10000.'
        assert error_message_element.text == expected_message, \
            f"Expected error message '{expected_message}', but got '{error_message_element.text}'"
