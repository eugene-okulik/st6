import allure
# from test_UI_vkuklin.pages.base_page import BasePage
# from test_UI_vkuklin.pages.locators.locators import EcoFriendlyPage as loc
from st6.test_UI_vkuklin.pages.base_page import BasePage
from st6.test_UI_vkuklin.pages.locators.locators import EcoFriendlyPage as loc


class EcoFriendlyPage(BasePage):
    relative_url = 'collections/eco-friendly.html'

    @allure.step('Check header')
    def check_header(self):
        header = self.find(loc.HEADER_ECO_FRIENDLY)
        assert header.text == 'Eco Friendly'

    @allure.step('Check images cards')
    def check_img_cards(self):
        img_cards = self.find(loc.IMAGES_CARDS)
        assert img_cards

    @allure.step('Check stars cards')
    def check_stars_rating(self):
        stars_rating = self.find(loc.STARS_RATING)
        assert stars_rating
