from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from test_UI_eklimova_selenium.pages.base_page import BasePage
from test_UI_eklimova_selenium.pages.locators import EcoFriendlyPage as loc

import allure


class EcoFriendlyPage(BasePage):
    related_url = "/collections/eco-friendly.html"

    @allure.step("Send data to search field")
    def send_search_data(self, text):
        searching = self.find(loc.SEARCHING)
        searching.send_keys(text)
        searching.send_keys(Keys.ENTER)

    @allure.step("Check that searching works")
    def check_that_searching_works(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(ec.visibility_of_element_located(loc.PURCHASE))
        names = self.find_elements(loc.PURCHASE)

        result = len(list(filter(lambda x: 'tank' in x.text.lower(), names)))

        assert result > 0

    @allure.step("Add first element to cart")
    def add_first_element_to_cart(self):
        element = self.find(loc.ELEMENT)
        add_to_cart = self.find(loc.ADD_TO_CART)
        size_29 = self.find(loc.SIZE_29)
        orange_color = self.find(loc.ORANGE_COLOR)

        actions = ActionChains(self.driver)
        actions.move_to_element(element)
        self.scroll()
        # self.driver.execute_script("window.scrollBy(0, 300);")
        actions.click(size_29)
        actions.click(orange_color)
        actions.click(add_to_cart)
        actions.perform()

    @allure.step("Message about success adding is appeared")
    def success_message_is_appeared(self):
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(loc.SUCCESS_ADDING_MES))

    @allure.step("Check item in the cart")
    def check_item_in_the_cart(self):
        item_title = self.find(loc.ITEM_TITLE).text
        cart_link = self.find(loc.CART_LINK)
        cart_link.click()
        wait = WebDriverWait(self.driver, 10)
        item_in_cart = wait.until(ec.visibility_of_element_located(loc.ITEM_IN_CART)).text

        assert item_in_cart == item_title

    @allure.step("Adding purchase without size and color")
    def add_purchase_without_size_and_color(self):
        element = self.find(loc.ELEMENT)
        add_to_cart = self.find(loc.ADD_TO_CART)

        actions = ActionChains(self.driver)
        actions.move_to_element(element)
        self.driver.execute_script("window.scrollBy(0, 300);")
        actions.click(add_to_cart)
        actions.perform()

    @allure.step("Check message about necessity to choose of options")
    def check_message_about_necessity_to_choose_options(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(ec.visibility_of_element_located(loc.MES_NEED_TO_CHOOSE))

        waring_text = self.find(loc.MES_NEED_TO_CHOOSE).text

        assert waring_text == "You need to choose options for your item."
