import json

from playwright.sync_api import Page, BrowserContext, expect, Route
import pytest
from time import sleep
import re


@pytest.fixture
def page(context: BrowserContext):
    page: Page = context.new_page()
    page.set_viewport_size({"width": 1920, "height": 1080})
    return page


def test_alert(page: Page):
    page.on('dialog', lambda alert: alert.accept())
    page.goto('https://www.qa-practice.com/elements/alert/confirm')
    button = page.locator('.a-button')
    button.click()
    result_text = page.locator('#result-text')
    expect(result_text).to_have_text('Ok')
    sleep(3)


def test_new_tab(page, context: BrowserContext):
    page.goto('https://www.qa-practice.com/elements/new_tab/button')
    with context.expect_page() as new_page_event:
        button = page.locator('#new-page-button')
        button.click()
        page2 = new_page_event.value

    result = page2.locator('#result-text')
    expect(result).to_have_text('I am a new page in a new tab')
    expect(button).to_be_enabled()
    sleep(3)


def test_iphone_rename(page):
    def change_response(route: Route):
        response = route.fetch()
        body = response.json()
        body['body']['digitalMat'][0]['familyTypes'][0]['productName'] = 'ЯблокоФон 15 про'
        body = json.dumps(body)
        route.fulfill(response=response, body=body)

    page.route(re.compile('/step0_iphone/'), change_response)
    page.goto('https://www.apple.com/shop/buy-iphone')
    page.locator('[data-trigger-id="digitalmat-1"]').click()
    sleep(10)
