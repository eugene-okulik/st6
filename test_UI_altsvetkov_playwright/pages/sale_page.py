import allure
from playwright.sync_api import expect
from test_UI_altsvetkov_playwright.pages.base_page import BasePage
from test_UI_altsvetkov_playwright.locators.locators import SalePageLoc as loc


class SalePage(BasePage):

    relative_url = '/sale.html/'

    @allure.step('Click the button [Shop Women\'s Deal]')
    def click_button_shop_women_deals(self):
        button_women_shop = self.find(loc.BUTTON_SHOP_WOMEN_DEALS)
        expect(button_women_shop).to_be_enabled()
        button_women_shop.click()

    # Проверка перенаправления на страницу распродажи после нажатия на button[Shop Women Deal's]
    @allure.step('Check the button[Shop Women\'s Deal] directs to the relevant page')
    def check_btn_shop_women_is_redirects_to_sale_page(self):
        expect(self.page).to_have_url('https://magento.softwaretestingboard.com/promotions/women-sale.html')
        self.page.go_back()
        expect(self.page).to_have_url('https://magento.softwaretestingboard.com/sale.html')

    # Проверка текста блока "20% discount promotion"
    @allure.step('Check the block "20% discount promotion"')
    def check_block_20_discount_text_match(self):
        title_promo_20_off = self.find(loc.PROMO_20_OFF_TITLE)
        info_promo_20_off = self.find(loc.PROMO_20_OFF_INFO)
        expect(self.find(loc.PROMO_20_OFF)).to_be_visible()
        expect(title_promo_20_off).to_contain_text('20% OFF')
        expect(info_promo_20_off).to_contain_text('Every $200-plus purchase!')

    # Проверка названий заголовков меню Categories
    @allure.step('Check the menu[category] titles')
    def check_menu_categories_titles_match(self):
        titles = self.find(loc.MENU_CATEGORIES_TITLES).all()
        expect(titles[0]).to_have_text("Women's Deals")
        expect(titles[1]).to_have_text("Mens's Deals")
        expect(titles[2]).to_have_text("Gear Deals")
