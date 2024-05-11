import allure

from test_UI_altsvetkov_selenium.pages.base_page import BasePage
from test_UI_altsvetkov_selenium.locators.locators import SalePageLoc as loc


class SalePage(BasePage):

    relative_url = '/sale.html/'

    @allure.step('Click the button [Shop Women\'s Deal]')
    def click_button_shop_women_deals(self):
        self.find(loc.BUTTON_SHOP_WOMEN_DEALS).click()

    # Проверка перенаправления на страницу распродажи после нажатия на button[Shop Women Deal's]
    @allure.step('Check the button[Shop Women\'s Deal] directs to the relevant page')
    def check_btn_shop_women_is_redirects_to_sale_page(self):
        button_shop = self.find(loc.BUTTON_SHOP_WOMEN_DEALS)
        assert button_shop.is_enabled()
        button_shop.click()
        assert self.driver.current_url == 'https://magento.softwaretestingboard.com/promotions/women-sale.html'
        self.driver.back()
        assert self.driver.current_url == 'https://magento.softwaretestingboard.com/sale.html'

    # Проверка текста блока "20% discount promotion"
    @allure.step('Check the block "20% discount promotion"')
    def check_block_20_discount_text_match(self):
        assert self.find(loc.PROMO_20_OFF).is_displayed()
        assert self.find(loc.PROMO_20_OFF_TITLE).text == '20% OFF'
        assert self.find(loc.PROMO_20_OFF_INFO).text == 'Every $200-plus purchase!'

    # Проверка названий заголовков меню Categories
    @allure.step('Check the menu[category] titles')
    def check_menu_categories_titles_match(self):
        titles = self.find_all(loc.MENU_CATEGORIES_TITLES)
        assert titles[0].text.lower() == "women's deals"
        assert titles[1].text.lower() == "mens's deals"
        assert titles[2].text.lower() == "gear deals"
