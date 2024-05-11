from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.alert import Alert

import pytest

sait1 = "https://www.demoblaze.com/index.html"
sait2 = "https://magento.softwaretestingboard.com/gear/bags.html"
sait3 = "https://www.qa-practice.com/elements/popup/iframe_popup"


class TestDemo:

    @pytest.fixture()
    def driver(self):
        driver = webdriver.Firefox()
        driver.implicitly_wait(3)
        yield driver
        driver.quit()

    def test_adding_purchase_to_card(self, driver):
        driver.get(sait1)
        elements = driver.find_elements(By.CSS_SELECTOR, ".card-title")
        third_element = elements[2]
        link_element = third_element.find_element(By.TAG_NAME, "a")
        ActionChains(driver).key_down(Keys.CONTROL).click(link_element).key_up(Keys.CONTROL).perform()
        handles = driver.window_handles
        driver.switch_to.window(handles[-1])

        name_purchase = driver.find_element(By.XPATH, '//div[@id="tbodyid"]/h2').text

        wait = WebDriverWait(driver, 10)
        wait.until(
            ec.visibility_of_element_located((By.XPATH, "//div[@id='navbarExample']/ul/li[4]/a")))

        driver.find_element(By.XPATH, "//a[@class='btn btn-success btn-lg']").click()
        wait.until(ec.alert_is_present())
        Alert(driver).accept()

        driver.close()

        driver.switch_to.window(driver.window_handles[0])
        wait.until(ec.visibility_of_element_located((By.XPATH, '//a[@id="cartur"]')))
        driver.find_element(By.XPATH, '//a[@id="cartur"]').click()

        wait.until(
            ec.visibility_of_element_located((By.XPATH, "//tr[@class='success']/td[2]")))
        model = driver.find_element(By.XPATH, "//tr[@class='success']/td[2]").text
        assert name_purchase == model

    def test_check_adding_to_compare_product(self, driver):
        driver.get(sait2)
        element = driver.find_element(By.XPATH, '//div[@class="price-box price-final_price" and @data-product-id=14]')
        add_to_compare = driver.find_element(By.XPATH, '(//a[@class="action tocompare"])[1]')

        driver.execute_script("window.scrollBy(0, 500);")
        purchase_text = driver.find_element(By.XPATH, '(//a[@class="product-item-link"])[1]').text
        actions = ActionChains(driver)
        actions.move_to_element(element)
        actions.click(add_to_compare)
        actions.perform()

        wait = WebDriverWait(driver, 10)
        wait.until(ec.visibility_of_element_located((By.XPATH, '//strong[@class="product-item-name"]/a')))
        comparison_item = driver.find_element(By.XPATH, '//strong[@class="product-item-name"]/a')
        driver.execute_script("arguments[0].scrollIntoView();", comparison_item)

        comparison_text = comparison_item.text

        assert purchase_text == comparison_text

    def test_check_popup_text_coping(self, driver):
        driver.get(sait3)
        driver.find_element(By.XPATH, '//button[@data-bs-target="#exampleModal"]').click()

        iframe = driver.find_element(By.TAG_NAME, 'iframe')
        driver.switch_to.frame(iframe)
        text_iframe = driver.find_element(By.ID, 'text-to-copy').text
        driver.switch_to.default_content()
        submit_button = driver.find_element(By.XPATH, '//button[@class="btn btn-primary" and @type="submit"]')
        submit_button.click()

        input_line = driver.find_element(By.XPATH, '//input[@id="id_text_from_iframe"]')
        input_line.send_keys(text_iframe)

        driver.find_element(By.ID, "submit-id-submit").click()

        alert_text = driver.find_element(By.ID, 'check-result').text

        assert alert_text == "Correct!"
