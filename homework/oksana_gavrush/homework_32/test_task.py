from playwright.sync_api import Page, BrowserContext, Route, expect
import json
import pytest
import re


@pytest.fixture
def page(context: BrowserContext) -> Page:
    page: Page = context.new_page()
    page.set_viewport_size({"width": 1920, "height": 1080})
    return page


def test_alert(page):
    page.on('dialog', lambda alert: alert.accept())
    page.goto('https://www.qa-practice.com/elements/alert/confirm')
    page.get_by_role('link', name='Click').click()
    check_ok = page.locator('#result-text')
    expect(check_ok).to_have_text('Ok')


def test_open_link(page, context: BrowserContext):
    page.goto('https://www.qa-practice.com/elements/new_tab/button')
    with context.expect_page() as new_page_event:
        button = page.locator('#new-page-button')
        button.click()
        page_2 = new_page_event.value
    result = page_2.locator('#result-text')
    expect(result).to_have_text('I am a new page in a new tab')
    expect(button).to_be_enabled()


def test_rename_name(page):

    def change_response(route: Route):
        response = route.fetch()
        body = response.json()
        body['body']['digitalMat'][0]['familyTypes'][0]['productName'] = 'яблокофон 15 про'
        route.fulfill(response=response, body=json.dumps(body))

    page.route(re.compile('library/step0_iphone/digitalmat'), change_response)
    page.goto('https://www.apple.com/shop/buy-iphone')
    page.locator('[data-trigger-id="digitalmat-1"]').click()
    product_name = page.locator('[data-autom="DigitalMat-overlay-header-0-0"]')
    expect(product_name).to_have_text('яблокофон 15 про')
