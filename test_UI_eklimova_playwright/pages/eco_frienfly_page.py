from playwright.sync_api import expect
from test_UI_eklimova_playwright.pages.base_page import BasePage
from test_UI_eklimova_playwright.pages.locators import EcoFriendlyPage as loc

import allure


class EcoFriendlyPage(BasePage):
    related_url = "/collections/eco-friendly.html"

    @allure.step("Send data to search field")
    def send_search_data(self, text):
        searching = self.find(loc.SEARCHING)
        searching.fill(text)
        searching.press('Enter')

    @allure.step("Check that searching works")
    def check_that_searching_works(self, text):
        purchase = self.page.locator(loc.PURCHASE).first
        expect(purchase).to_be_visible()
        names = self.find(loc.PURCHASE).all()

        assert len(list(filter(lambda x: text in x.text_content().lower(), names))) > 0

    @allure.step("Add first element to cart")
    def add_first_element_to_cart(self):
        element = self.find(loc.ELEMENT)
        add_to_cart = self.find(loc.ADD_TO_CART)
        size_29 = self.find(loc.SIZE_29)
        orange_color = self.find(loc.ORANGE_COLOR)

        element.scroll_into_view_if_needed()
        self.page.evaluate("window.scrollBy(0, 300);")
        size_29.click()
        orange_color.click()
        add_to_cart.click()

    @allure.step("Message about success adding is appeared")
    def success_message_is_appeared(self):
        success = self.page.locator(loc.SUCCESS_ADDING_MES)
        expect(success).to_be_visible()

    @allure.step("Check item in the cart")
    def check_item_in_the_cart(self):
        item_title = self.page.locator(loc.ITEM_TITLE).text_content()
        self.find(loc.CART_LINK).click()
        item_in_the_cart = self.page.locator(loc.ITEM_IN_CART)
        expect(item_in_the_cart).to_be_visible()

        expect(item_in_the_cart).to_have_text(item_title)

    @allure.step("Adding purchase without size and color")
    def add_purchase_without_size_and_color(self):
        element = self.find(loc.ELEMENT)
        element.scroll_into_view_if_needed()
        self.page.evaluate("window.scrollBy(0, 300);")
        element.hover()
        self.find(loc.ADD_TO_CART).click()

    @allure.step("Check message about necessity to choose of options")
    def check_message_about_necessity_to_choose_options(self):
        expect(self.find(loc.MES_NEED_TO_CHOOSE)).to_be_visible()

        waring_text = self.find(loc.MES_NEED_TO_CHOOSE)

        expect(waring_text).to_have_text("You need to choose options for your item.")
