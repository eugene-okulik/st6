from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import pytest
import pyperclip


@pytest.fixture()
def driver():
    options = Options()
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.close()


def test_add_to_car_samsung(driver):
    driver.get('https://www.demoblaze.com/index.html')
    samsung_link = WebDriverWait(driver, 5).until(ec.presence_of_element_located((By.LINK_TEXT, 'Samsung galaxy s6')))
    ActionChains(driver).key_down(Keys.COMMAND).click(samsung_link).key_up(Keys.COMMAND).perform()
    tab = driver.window_handles
    driver.switch_to.window(tab[1])
    add_to_cart = (
        WebDriverWait(driver, 5).until(ec.presence_of_element_located((By.CSS_SELECTOR, '.btn.btn-success'))))
    add_to_cart.click()
    confirm = (WebDriverWait(driver, 5).until(ec.alert_is_present()))
    confirm.accept()
    driver.close()
    driver.switch_to.window((tab[0]))
    open_cart = driver.find_element(By.CSS_SELECTOR, '#cartur')
    open_cart.click()
    WebDriverWait(driver, 5).until(ec.presence_of_element_located((By.CSS_SELECTOR, '.success')))
    samsung_added = driver.find_element(By.XPATH, '//*[@id="tbodyid"]/tr/td[2]')
    assert samsung_added.text == 'Samsung galaxy s6'


def test_magento(driver):
    driver.get('https://magento.softwaretestingboard.com/gear/bags.html')
    item = WebDriverWait(driver, 5).until(
        ec.presence_of_element_located((By.XPATH, '//*[contains(text(), "Push It Messenger Bag")]')))
    actions = ActionChains(driver)
    actions.move_to_element(item)
    add_to_compare = WebDriverWait(driver, 1).until(ec.presence_of_element_located(
        (By.XPATH, '//*[@title="Add to Compare"][1]')))
    actions.move_to_element(add_to_compare).click().perform()
    compare = WebDriverWait(driver, 3).until(
        ec.presence_of_element_located((By.CSS_SELECTOR, '#compare-items li strong a')))
    assert compare.text == 'Push It Messenger Bag'


def test_qa_practice(driver):
    driver.get('https://www.qa-practice.com/elements/popup/iframe_popup')
    button_launch = driver.find_element(By.XPATH, '//*[@class="btn btn-primary"]')
    button_launch.click()
    iframe = driver.find_element(By.CSS_SELECTOR, 'iframe')
    driver.switch_to.frame(iframe)
    find_text = driver.find_element(By.ID, 'text-to-copy')
    copy_text = WebDriverWait(driver, 3).until(ec.visibility_of(find_text)).text
    driver.switch_to.default_content()
    check_btn = driver.find_element(By.XPATH, '//*[@class="modal-footer"]//*[@class="btn btn-primary"]')
    check_btn.click()
    pyperclip.copy(copy_text)
    input_field = driver.find_element(By.CSS_SELECTOR, '#id_text_from_iframe')
    input_field.send_keys(Keys.COMMAND + 'v')
    btn_submit = driver.find_element(By.ID, 'submit-id-submit')
    btn_submit.click()
    correct_result = driver.find_element(By.ID, 'check-result')
    assert correct_result.text == "Correct!"
