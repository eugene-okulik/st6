import allure
from test_UI_vkuklin_PW.pages.base_page import BasePage
from test_UI_vkuklin_PW.pages.locators.locators import EcoFriendlyPage as loc
from playwright.sync_api import expect


class EcoFriendlyPage(BasePage):
    relative_url = 'collections/eco-friendly.html'

    @allure.step('Check header')
    def check_header(self, message):
        header = self.find(loc.HEADER_ECO_FRIENDLY)
        expect(header).to_have_text(message)

    @allure.step('Check images cards')
    def check_img_cards(self):
        img_cards = self.find(loc.IMAGES_CARDS).first
        expect(img_cards).to_be_visible()

    @allure.step('Check stars cards')
    def check_stars_rating(self):
        stars_rating = self.find(loc.STARS_RATING).first
        expect(stars_rating).to_be_visible()
