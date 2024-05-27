import allure
from playwright.sync_api import expect

from test_UI_altsvetkov_playwright.pages.base_page import BasePage
from test_UI_altsvetkov_playwright.locators.locators import EcoCollectionPageLoc as loc


class EcoCollectionPage(BasePage):

    relative_url = '/collections/eco-friendly.html/'

    # Выбор значения из dropdown[Sort By]
    @allure.step('Select sort by')
    def select_sort_by_value(self, value):
        dropdown = self.find(loc.DROPDOWN_SORT_BY).first
        with self.page.expect_navigation():
            dropdown.select_option(value)

    # Проверка, что значение из dropdown выбрано
    @allure.step('Check sort by value is selected')
    def check_sort_by_value_is_selected(self, value):
        selected_dropdown = self.find(loc.DROPDOWN_SORT_BY).first
        expect(selected_dropdown).to_have_value(value)

    # Проверка сортировки цены по возрастанию
    @allure.step('Ascending price check')
    def check_ascending_price(self):
        prices = self.find(loc.PRICE_OF_GOODS).all()
        prices_list = [price.text_content() for price in prices]
        assert prices_list == sorted(prices_list), f'Expected price:{sorted(prices_list)}.\nActual price:{prices_list}'

    # Проверка сортировки цены по убыванию
    @allure.step('Descending price check')
    def check_descending_price(self):
        self.find(loc.BUTTON_SET_DESCENDING).first.click()
        prices = self.find(loc.PRICE_OF_GOODS).all()
        prices_list = [price.text_content() for price in prices]
        assert prices_list == sorted(prices_list, reverse=True), (f'Expected price:{sorted(prices_list, reverse=True)}.'
                                                                  f'\nActual price:{prices_list}')

    # Проверка отображения цен
    @allure.step('Check the presence of the price of goods')
    def check_price_of_goods_displayed(self):
        prices = self.find(loc.PRICE_OF_GOODS).all()
        for price in prices:
            expect(price).to_be_visible()

    # Проверка отображения image товаров
    @allure.step('Check the presence of the image of the goods')
    def check_image_of_goods_displayed(self):
        images = self.find(loc.IMAGE_PHOTO).all()
        for image in images:
            expect(image).to_be_visible()

    # Проверка перехода на другую страницу после нажатия на button "Next"
    @allure.step('Check next button')
    def check_next_button_redirect_next_page(self):
        self.find(loc.BUTTON_NEXT).click()
        expected_url = 'https://magento.softwaretestingboard.com/collections/eco-friendly.html?p=2'
        expect(self.page).to_have_url(expected_url)
