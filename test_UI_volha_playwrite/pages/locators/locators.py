class RegisterPage:
    FIRSTNAME = '#firstname'
    LASTNAME = '#lastname'
    EMAIL = '#email_address'
    PASSWORD = '#password'
    CONFIRMPASSWORD = '#password-confirmation'
    CREATEACCOUNTBTN = '.action.submit.primary'

    FIRSTNAMEERR = '#firstname-error'
    LASTNAMEERR = '#lastname-error'
    EMAILERR = '#email_address-error'
    PASSWORDERR = '#password-error'
    CONFIRMPASSWORDERR = '#password-confirmation-error'
    CREATEACCOUNTBTNERR = '.action.submit.primary'


class AccountPage:
    # ACCOUNT = '//*[@class = "box-content"][1]'
    ACCOUNT = '[class ="box-content"] p'


class EcoFriendly:
    PAGETITLE = '//*[@data-ui-id="page-title-wrapper"]'
    PAGECATEGORY = '.item.category36'
    DEFAULTNUMOFITEMS = '.item.product.product-item'


class Sale:
    PAGETITLE = '//*[@data-ui-id="page-title-wrapper"]'
    PAGECATEGORY = '.item.category37'

    CATEGORYMENU1 = '//*[@class="categories-menu"]/strong [@class="title"][1]'
    CATEGORYMENU2 = '//*[@class="categories-menu"]/strong [@class="title"][2]'
    CATEGORYMENU3 = '//*[@class="categories-menu"]/strong [@class="title"][3]'
