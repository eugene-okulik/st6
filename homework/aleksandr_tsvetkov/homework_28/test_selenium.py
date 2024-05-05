import pytest
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


@pytest.fixture()
def driver():
    options = Options()
    options.add_argument('start-maximized')
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


def test_add_item_to_cart(driver):
    driver.get('https://www.demoblaze.com/index.html')
    wait = WebDriverWait(driver, 5)
    item = wait.until((ec.visibility_of_element_located((By.CSS_SELECTOR, 'h4 [href="prod.html?idp_=2"]'))))
    ActionChains(driver).key_down(Keys.CONTROL).click(item).key_up(Keys.CONTROL).perform()
    tabs = driver.window_handles
    driver.switch_to.window(tabs[1])
    WebDriverWait(driver, 5).until(ec.visibility_of_element_located((By.CSS_SELECTOR, '.btn.btn-success'))).click()
    WebDriverWait(driver, 5).until(ec.alert_is_present()).accept()
    driver.close()
    driver.switch_to.window((tabs[0]))
    driver.find_element(By.CSS_SELECTOR, '#cartur').click()
    WebDriverWait(driver, 5).until(ec.visibility_of_element_located((By.XPATH, '//*[@id="tbodyid"]/tr')))
    item_name = driver.find_element(By.XPATH, '//*[@id="tbodyid"]/tr/td[2]')
    item_price = driver.find_element(By.XPATH, '//*[@id="tbodyid"]/tr/td[3]')
    assert item_name.text == 'Nokia lumia 1520' and item_price.text == '820'


def test_add_item_to_cart_2(driver):
    driver.get('https://magento.softwaretestingboard.com/gear/bags.html')
    wait = WebDriverWait(driver, 5)
    items = driver.find_elements(By.CSS_SELECTOR, '.item.product.product-item')
    actions = ActionChains(driver)
    actions.move_to_element(items[0])
    add_to_compare = wait.until(ec.presence_of_element_located((By.XPATH, '//*[@title="Add to Compare"][1]')))
    actions.click(add_to_compare).perform()
    compare_section = wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, '#compare-items li strong a')))
    assert compare_section.text == 'Push It Messenger Bag'


def test_popup_and_iframe(driver):
    driver.get('https://www.qa-practice.com/elements/popup/iframe_popup')
    driver.implicitly_wait(5)
    driver.find_element(By.CSS_SELECTOR, '[data-bs-target="#exampleModal"]').click()
    iframe = driver.find_element(By.CSS_SELECTOR, 'iframe')
    driver.switch_to.frame(iframe)
    text_to_copy = WebDriverWait(driver, 5).until(ec.visibility_of_element_located((By.CSS_SELECTOR, '#text-to-copy')))
    actions = ActionChains(driver)
    actions.move_to_element(text_to_copy).move_by_offset(-150, 0)
    actions.click_and_hold().move_by_offset(300, 0).release()
    actions.key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL)
    actions.perform()
    driver.switch_to.default_content()
    driver.find_element(By.XPATH, '//*[text()="Check"]').click()
    driver.find_element(By.CSS_SELECTOR, '#id_text_from_iframe').send_keys(Keys.CONTROL, 'v')
    driver.find_element(By.CSS_SELECTOR, '#submit-id-submit').click()
    correct = driver.find_element(By.CSS_SELECTOR, '#check-result').text
    assert correct == 'Correct!'
    sleep(3)
