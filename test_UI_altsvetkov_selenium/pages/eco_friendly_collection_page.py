from selenium.common import TimeoutException
from test_UI_altsvetkov_selenium.pages.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select
import allure


from test_UI_altsvetkov_selenium.locators.locators import EcoCollectionPageLoc as loc


class EcoCollectionPage(BasePage):

    relative_url = '/collections/eco-friendly.html/'

    # Выбор значения из dropdown[Sort By]
    @allure.step('Select sort by')
    def select_sort_by_value(self, value):
        dropdown = WebDriverWait(self.driver, 2).until(ec.visibility_of_element_located(loc.DROPDOWN_SORT_BY))
        select = Select(dropdown)
        select.select_by_value(value)

    # Проверка, что значение из dropdown выбрано
    @allure.step('Check sort by value is selected')
    def check_sort_by_value_is_selected(self):
        dropdown = self.find(loc.DROPDOWN_SORT_BY)
        select = Select(dropdown)
        assert select.first_selected_option.is_selected()

    # Проверка сортировки цены по возрастанию
    @allure.step('Ascending price check')
    def check_ascending_price(self):
        wait = WebDriverWait(self.driver, 3)
        try:
            wait.until(ec.url_contains('product_list_order=price'))
        except TimeoutException:
            raise AssertionError("The URL did not contain 'product_list_order=price' after choosing to sort by price")
        prices = self.find_all(loc.PRICE_OF_GOODS)
        prices_list = [price.text for price in prices]
        assert prices_list == sorted(prices_list), f'Expected price:{sorted(prices_list)}.\nActual price:{prices_list}'

    # Проверка сортировки цены по убыванию
    @allure.step('Descending price check')
    def check_descending_price(self):
        wait = WebDriverWait(self.driver, 3)
        wait.until(ec.presence_of_element_located(loc.BUTTON_SET_DESCENDING)).click()
        prices = self.find_all(loc.PRICE_OF_GOODS)
        prices_list = [price.text for price in prices]
        assert prices_list == sorted(prices_list, reverse=True), (f'Expected price:{sorted(prices_list, reverse=True)}.'
                                                                  f'\nActual price:{prices_list}')

    # Проверка отображения цен
    @allure.step('Check the presence of the price of goods')
    def check_price_of_goods_displayed(self):
        assert self.find(loc.PRICE_OF_GOODS).is_displayed()

    # Проверка отображения image товаров
    @allure.step('Check the presence of the image of the goods')
    def check_image_of_goods_displayed(self):
        assert self.find(loc.IMAGE_PHOTO).is_displayed()

    # Проверка перехода на другую страницу после нажатия на button "Next"
    @allure.step('Check next button')
    def check_next_button_redirect_next_page(self):
        WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located(loc.BUTTON_NEXT)).click()
        assert 'eco-friendly.html?p=2' in self.driver.current_url
