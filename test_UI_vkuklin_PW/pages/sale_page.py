import allure
from test_UI_vkuklin_PW.pages.base_page import BasePage
from test_UI_vkuklin_PW.pages.locators.locators import SalePage as loc
from playwright.sync_api import expect


class SalePage(BasePage):
    relative_url = 'sale.html'

    @allure.step('Check header sale')
    def check_header_sale(self):
        header_sale = self.find(loc.HEADER_SALE)
        expect(header_sale).to_have_text('Sale')

    @allure.step('Check image promo block')
    def check_image_promo_block(self):
        img_promo_block = self.find(loc.IMG_PROMO)
        expect(img_promo_block).to_be_visible()

    @allure.step('Check my wish list')
    def check_my_wish_list(self):
        my_wish_list = self.find(loc.MY_WISH_LIST)
        expect(my_wish_list).to_be_visible()
