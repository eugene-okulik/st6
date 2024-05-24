import json

from playwright.sync_api import Page, expect, BrowserContext, Route
import pytest
import re


@pytest.fixture
def page(context: BrowserContext):
    page: Page = context.new_page()
    page.set_viewport_size({"width": 1920, "height": 1080})
    return page


def test_alert(page):
    page.on('dialog', lambda alert: alert.accept())
    page.goto('https://www.qa-practice.com/elements/alert/confirm')
    page.get_by_role('link', name='Click').click()
    result_text = page.locator('#result-text')
    expect(result_text).to_have_text('Ok')


def test_new_tab(page, context: BrowserContext):
    page.goto('https://www.qa-practice.com/elements/new_tab/button')
    with context.expect_page() as new_page_event:
        button_click = page.locator('#new-page-button')
        button_click.click()
        page2 = new_page_event.value
    result_text = page2.locator('#result-text')
    expect(result_text).to_have_text('I am a new page in a new tab')
    expect(button_click).to_be_enabled()


def test_yablokofon(page):
    changed_product_name = 'яблокофон 15 про'

    def change_response(route: Route):
        response = route.fetch()
        body = response.json()
        body['body']['digitalMat'][0]['familyTypes'][0]['productName'] = changed_product_name
        route.fulfill(response=response, body=json.dumps(body))

    page.route(re.compile('/step0_iphone/'), change_response)
    page.goto('https://www.apple.com/shop/buy-iphone')
    page.locator('[data-trigger-id="digitalmat-1"]').click()
    product_name = page.locator('[data-autom="DigitalMat-overlay-header-0-0"]')
    expect(product_name).to_have_text(changed_product_name)
