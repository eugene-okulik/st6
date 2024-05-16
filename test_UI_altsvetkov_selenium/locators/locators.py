from selenium.webdriver.common.by import By


class CreateAccountPageLoc:
    FIRST_NAME = (By.CSS_SELECTOR, '#firstname')
    LAST_NAME = (By.CSS_SELECTOR, '#lastname')
    EMAIL = (By.CSS_SELECTOR, '#email_address')
    PASSWORD = (By.CSS_SELECTOR, '[title="Password"]')
    CONFIRM_PASSWORD = (By.CSS_SELECTOR, '#password-confirmation')
    BUTTON_CREATE_ACCOUNT = (By.CSS_SELECTOR, '.action.submit.primary')
    FIRST_NAME_LABEL = (By.CSS_SELECTOR, 'label[for="firstname"]')
    LAST_NAME_LABEL = (By.CSS_SELECTOR, 'label[for="lastname"]')
    EMAIL_LABEL = (By.CSS_SELECTOR, 'label[for="email_address"]')
    PASSWORD_LABEL = (By.CSS_SELECTOR, 'label[for="password"]')
    CONFIRM_PASSWORD_LABEL = (By.CSS_SELECTOR, 'label[for="password-confirmation"]')
    PASSWORD_ERROR_HINT = (By.CSS_SELECTOR, '#password-error')
    SUCCESSFUL_REGISTRATION_MESSAGE = (By.CSS_SELECTOR, '.message-success')


class EcoCollectionPageLoc:
    DROPDOWN_SORT_BY = (By.CSS_SELECTOR, '#sorter')
    PRICE_OF_GOODS = (By.XPATH, '//*[@class="price-wrapper "]')
    BUTTON_SET_DESCENDING = (By.XPATH, '//a[@title="Set Descending Direction"]')
    IMAGE_PHOTO = (By.CSS_SELECTOR, '.product-image-photo')
    BUTTON_NEXT = (By.CSS_SELECTOR, 'div:nth-child(5) > div.pages > ul > li.item.pages-item-next > a')


class SalePageLoc:
    PROMO_20_OFF_INFO = (By.CSS_SELECTOR, 'a.block-promo.sale-20-off > span.content > span')
    PROMO_20_OFF_TITLE = (By.CSS_SELECTOR, 'a.block-promo.sale-20-off > span.content > strong')
    BUTTON_SHOP_WOMEN_DEALS = (By.CSS_SELECTOR, '.more.button')
    PROMO_20_OFF = (By.CSS_SELECTOR, 'a.block-promo.sale-20-off > span.content')
    MENU_CATEGORIES_TITLES = (By.CSS_SELECTOR, '.categories-menu .title')
