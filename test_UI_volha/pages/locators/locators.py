from selenium.webdriver.common.by import By


class RegisterPage:
    FIRSTNAME = (By.CSS_SELECTOR, '#firstname')
    LASTNAME = (By.CSS_SELECTOR, '#lastname')
    EMAIL = (By.CSS_SELECTOR, '#email_address')
    PASSWORD = (By.CSS_SELECTOR, '#password')
    CONFIRMPASSWORD = (By.CSS_SELECTOR, '#password-confirmation')
    CREATEACCOUNTBTN = (By.CSS_SELECTOR, '.action.submit.primary')

    FIRSTNAMEERR = (By.CSS_SELECTOR, '#firstname-error')
    LASTNAMEERR = (By.CSS_SELECTOR, '#lastname-error')
    EMAILERR = (By.CSS_SELECTOR, '#email_address-error')
    PASSWORDERR = (By.CSS_SELECTOR, '#password-error')
    CONFIRMPASSWORDERR = (By.CSS_SELECTOR, '#password-confirmation-error')
    CREATEACCOUNTBTNERR = (By.CSS_SELECTOR, '.action.submit.primary')


class AccountPage:
    ACCOUNT = (By.XPATH, '//*[@class = "box-content"][1]')


class EcoFriendly:
    PAGETITLE = (By.XPATH, '//*[@data-ui-id="page-title-wrapper"]')
    PAGECATEGORY = (By.CSS_SELECTOR, '.item.category36')
    # DEFAULTNUMOFITEMS = (By.CSS_SELECTOR, '.products.list.items.product-items')
    DEFAULTNUMOFITEMS = (By.CSS_SELECTOR, '.item.product.product-item')


class Sale:
    PAGETITLE = (By.XPATH, '//*[@data-ui-id="page-title-wrapper"]')
    PAGECATEGORY = (By.CSS_SELECTOR, '.item.category37')

    CATEGORYMENU1 = (By.XPATH, '//*[@class="categories-menu"]/strong [@class="title"][1]')
    CATEGORYMENU2 = (By.XPATH, '//*[@class="categories-menu"]/strong [@class="title"][2]')
    CATEGORYMENU3 = (By.XPATH, '//*[@class="categories-menu"]/strong [@class="title"][3]')
