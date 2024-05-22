import json

from playwright.sync_api import Page, BrowserContext, expect, Dialog, Request, Route
import pytest
from time import sleep
import re


@pytest.fixture
def page(context: BrowserContext):
    page: Page = context.new_page()
    page.set_viewport_size({"width": 1920, "height": 1080})
    return page


def test_new_tab(page, context: BrowserContext):
    page.goto('https://www.qa-practice.com/elements/new_tab/link')
    with context.expect_page() as new_page_event:
        page.locator('#new-page-link').click()
        page2 = new_page_event.value

    result = page2.locator('#result-text')
    expect(result).to_have_text('I am a new page in a new tab')
    with context.expect_page() as new_page_event:
        page.locator('#new-page-link').click()
        page3 = new_page_event.value
        page3.close()

    sleep(3)


def test_alert(page):

    def handle_alert(alert: Dialog):
        print(alert.type)
        print(alert.message)
        alert.accept('Some text')

    # page.on('dialog', handle_alert)
    page.on('dialog', lambda alert: alert.accept('another text'))
    page.goto('https://www.qa-practice.com/elements/alert/prompt')
    page.get_by_role('link', name='Click').click()
    sleep(3)


def test_listen(page):

    def print_request(request: Request):
        print('REQUEST:', request.post_data, request.url)

    page.on('request', print_request)
    page.on('response', lambda response: print('RESPONSE:', response.status, response.url))
    page.goto('https://www.qa-practice.com/')


def test_catch_response(page):
    page.goto('https://www.airbnb.ru/')
    with page.expect_response(re.compile('/autosuggestions')) as reponse_event:
        page.get_by_test_id('header-tab-search-block-tab-EXPERIENCES').click()
        response = reponse_event.value

    print(response.json())
    assert response.json()['show_nearby'] is False


def test_pogoda(page):

    def change_response(route: Route):
        response = route.fetch()
        body = response.json()
        body['icon'] = 'A2'
        body['temperature'] = '+28'
        body = json.dumps(body)
        route.fulfill(response=response, body=body)

    page.route('**/pogoda/**', change_response)
    page.goto('https://www.onliner.by/')
    page.locator('[name="query"]').click()
    sleep(5)


def test_change_request(page):

    def change_req(route: Route):
        url = route.request.url
        if '&filter4=09z01' in url:
            url = url.replace('&filter4=09z01', '')
            print(url)
        route.continue_(url=url)

    page.route(re.compile('/product/finder'), change_req)
    page.goto('https://www.samsung.com/au/smartphones/galaxy-z')
    sleep(3)
    page.locator('[for="checkbox-series09z01"]').click()
    sleep(5)
