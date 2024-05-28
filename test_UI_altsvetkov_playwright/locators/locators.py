class CreateAccountPageLoc:
    FIRST_NAME = '#firstname'
    LAST_NAME = '#lastname'
    EMAIL = '#email_address'
    PASSWORD = '[title="Password"]'
    CONFIRM_PASSWORD = '#password-confirmation'
    BUTTON_CREATE_ACCOUNT = '.action.submit.primary'
    FIRST_NAME_LABEL = 'label[for="firstname"]'
    LAST_NAME_LABEL = 'label[for="lastname"]'
    EMAIL_LABEL = 'label[for="email_address"]'
    PASSWORD_LABEL = 'label[for="password"]'
    CONFIRM_PASSWORD_LABEL = 'label[for="password-confirmation"]'
    PASSWORD_ERROR_HINT = '#password-error'
    SUCCESSFUL_REGISTRATION_MESSAGE = '.message-success'


class EcoCollectionPageLoc:
    DROPDOWN_SORT_BY = '#sorter'
    PRICE_OF_GOODS = '//*[@class="price-wrapper "]'
    BUTTON_SET_DESCENDING = '//a[@title="Set Descending Direction"]'
    IMAGE_PHOTO = '.product-image-photo'
    BUTTON_NEXT = 'div:nth-child(5) > div.pages > ul > li.item.pages-item-next > a'


class SalePageLoc:
    PROMO_20_OFF_INFO = 'a.block-promo.sale-20-off > span.content > span'
    PROMO_20_OFF_TITLE = 'a.block-promo.sale-20-off > span.content > strong'
    BUTTON_SHOP_WOMEN_DEALS = '.more.button'
    PROMO_20_OFF = 'a.block-promo.sale-20-off > span.content'
    MENU_CATEGORIES_TITLES = '.categories-menu .title'
