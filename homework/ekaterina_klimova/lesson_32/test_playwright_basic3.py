import json
from playwright.sync_api import Page, BrowserContext, expect, Route
import pytest
import re


@pytest.fixture
def page(context: BrowserContext):
    page: Page = context.new_page()
    # page.set_viewport_size({"width": 1920, "height": 1080})
    return page


def test_alert(page):
    page.on('dialog', lambda dialog: dialog.accept())
    page.goto("https://www.qa-practice.com/elements/alert/confirm")
    page.locator("//*[@class='a-button']").click()
    result_text = page.locator("//*[@id='result-text']")
    expect(result_text).to_have_text('Ok')


def test_button(page, context: BrowserContext):
    page.goto("https://www.qa-practice.com/elements/new_tab/button")
    button = page.locator('//*[@id="new-page-button"]')
    with context.expect_page() as new_page_event:
        button.click()
        page2 = new_page_event.value
    result_text = page2.locator('//*[@id="result-text"]')
    expect(result_text).to_have_text('I am a new page in a new tab')
    expect(button).to_be_enabled()


def test_change_name(page):
    def change_response(route: Route):
        response = route.fetch()
        body = response.json()
        body['body']['digitalMat'][0]['familyTypes'][0]['productName'] = 'яблокофон 15 про'
        body = json.dumps(body)
        route.fulfill(response=response, body=body)

    page.route(re.compile('library/step0_iphone/digitalmat'), change_response)
    page.goto('https://www.apple.com/shop/buy-iphone')
    page.locator('//*[@data-trigger-id="digitalmat-1"]').click()
    name_phone = page.locator('//*[@id="rf-digitalmat-overlay-label-0"]').first
    expect(name_phone).to_have_text('яблокофон 15 про')
