import allure
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
from st6.tests_UI_oksana_selenium.pages.base import BasePage
from st6.tests_UI_oksana_selenium.pages.locators.locators import SaleProductLocators as loc


class SaleChecker(BasePage):
    relative_url = 'sale.html'

    @allure.step("Search for a product")
    def search_for_product(self, send_keys):
        search_input = self.find(loc.SEARCH_INPUT)
        search_input.click()
        search_input.send_keys(send_keys)
        search_input.send_keys(Keys.ENTER)

    @allure.step("Verify search results")
    def verify_search_results(self, error_message):
        search_result = self.find(loc.SEARCH_RESULT)
        expected_error_text = error_message
        assert expected_error_text in search_result.text

    @allure.step("Click on 'More' button")
    def click_more_button(self):
        button_more = WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable(loc.BUTTON_MORE))
        button_more.click()

    @allure.step("Double click on the second product")
    def double_click_second_product(self):
        product = self.find(loc.PRODUCT_CLICK)
        actions = ActionChains(self.driver)
        actions.double_click(product).perform()

    @allure.step("Verify product availability")
    def verify_product_availability(self, error_message):
        find_sale_text = WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located(loc.IN_STOCK))
        expected_error_text = error_message
        assert find_sale_text.text == expected_error_text

    @allure.step("Navigate to the category 'Shorts'")
    def navigate_to_shorts(self):
        find_shorts = self.find(loc.FIND_SHORTS)
        find_shorts.click()

    @allure.step("Verify presence of product images")
    def verify_product_images(self):
        product_images = WebDriverWait(self.driver, 10).until(
            ec.presence_of_all_elements_located(loc.PRODUCT_IMAGE_PHOTO))
        assert len(product_images) > 0, "Product descriptions are missing."

    @allure.step("Verify presence of 'Add to Cart' buttons")
    def verify_add_to_cart_buttons(self):
        add_to_cart_buttons = WebDriverWait(self.driver, 10).until(
            ec.presence_of_all_elements_located(loc.ADD_TO_CART_BUTTON))
        assert len(add_to_cart_buttons) > 0, "Add to Cart buttons are missing."
