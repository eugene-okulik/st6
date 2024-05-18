from playwright.sync_api import Page, expect
from time import sleep


def test_by_test_id(page):
    sleep(3)
    page.goto('https://www.airbnb.com/')
    sleep(2)
    page.get_by_test_id('header-tab-search-block-tab-EXPERIENCES').click()
    sleep(3)


def test_by_locator(page: Page):
    page.goto('https://magento.softwaretestingboard.com/')
    # basket = page.locator('//*[@class="action showcart"]')
    basket = page.locator('.action.showcart')
    basket.click()
    sleep(3)


def test_strength(page: Page):
    page.goto('https://magento.softwaretestingboard.com/customer/account/create/')
    input_field = page.locator('#password')
    # input_field.fill('!Qa%56aO)ZZ12')
    input_field.press_sequentially('!Qa%56aO)ZZ12', delay=100)
    sleep(2)
    input_field.press('Control+a')
    sleep(2)
    input_field.press('Backspace')
    sleep(3)


def test_is_visble(page: Page):
    page.goto('https://www.qa-practice.com/elements/input/simple')
    header = page.locator('#req_header')
    reqs = page.locator('#req_text')
    expect(reqs).not_to_be_visible()
    header.click()
    expect(reqs).to_be_visible()  # Здесь мы проверяем ожидаемый результат
    expect(reqs).not_to_have_class('collapsing')  # А здесь мы ждем пока элемент придет в нужное состояние
    header.click()
    expect(reqs).not_to_be_visible()


def test_enabled_and_select(page: Page):
    page.goto('https://www.qa-practice.com/elements/button/disabled')
    button = page.locator('#submit-id-submit')
    expect(button).to_be_disabled()
    page.locator('#id_select_state').select_option('enabled')
    expect(button).to_be_enabled()
    expect(button).to_have_text('Submit')
    expect(button).to_contain_text('ubm')


def test_value(page: Page):
    text = 'qiwuetyr'
    page.goto('https://www.qa-practice.com/elements/input/simple')
    input_field = page.locator('#id_text_string')
    input_field.fill(text)
    expect(input_field, f'Intput value is not {text}').to_have_value(text)


def test_url(page: Page):
    page.goto('https://www.qa-practice.com/')
    page.get_by_role('link', name='Contact').click()
    expect(page).to_have_url('https://www.qa-practice.com/contact/')


def test_hover(page: Page):
    page.goto('https://magento.softwaretestingboard.com/')
    men = page.locator('#ui-id-5')
    tops = page.locator('#ui-id-17')
    jackets = page.locator('#ui-id-19')
    men.hover()
    tops.hover()
    jackets.click()
    sleep(3)


def test_d_n_d(page: Page):
    page.goto('https://www.qa-practice.com/elements/dragndrop/boxes')
    drag_me = page.locator('#rect-draggable')
    drop_here = page.locator('#rect-droppable')
    drag_me.drag_to(drop_here)
    sleep(3)


def test_iframe(page: Page):
    page.goto('https://www.qa-practice.com/elements/iframe/iframe_page')
    iframe = page.frame_locator('iframe')
    burger = iframe.locator('.navbar-toggler-icon')
    page.get_by_role('link', name='Iframe', exact=True).click()
    # burger = page.locator('.navbar-toggler-icon')
    burger.click()
    sleep(3)
