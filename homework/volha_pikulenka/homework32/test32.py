import json
from playwright.sync_api import Page, BrowserContext, expect, Dialog, Request, Route
import pytest


@pytest.fixture
def page(context: BrowserContext):
    page: Page = context.new_page()
    page.set_viewport_size({"width": 1920, "height": 1080})
    return page


def test_task1(page):
    page.on('dialog', lambda alert: alert.accept('Ok'))
    page.goto('https://www.qa-practice.com/elements/alert/confirm')
    page.get_by_role('link', name='Click').click()
    res = page.locator('.result p:nth-child(2)')

    expect(res).to_contain_text('Ok')


def test_task2(page, context: BrowserContext):
    page.goto('https://www.qa-practice.com/elements/new_tab/button')
    click_btn = page.get_by_role('link', name='Click')
    with context.expect_page() as new_page_event:
        click_btn.click()
        page2 = new_page_event.value

    res = page2.locator('.result-text')
    expect(res).to_contain_text('I am a new page in a new tab')
    expect(click_btn).to_be_enabled()


def test_task3(page):

    def update_resp(route: Route):
        response = route.fetch()
        body = response.json()
        body['body']['digitalMat'][0]['familyTypes'][0]['tabTitle'] = 'яблокофон 15 про'
        body = json.dumps(body)
        route.fulfill(response=response, body=body)

    page.route('https://www.apple.com/shop/api/digital-mat?path=library/step0_iphone/digitalmat', update_resp)

    page.goto(' https://www.apple.com/shop/buy-iphone')
    page.get_by_role('link', name='All Models').click()
    page.locator('[src="https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/iphone-card-40-iphone15prohero-202309?wid=680&hei=528&fmt=p-jpg&qlt=95&.v=1693086290312"]').click()
