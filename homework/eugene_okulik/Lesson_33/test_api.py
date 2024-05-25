from playwright.sync_api import Page, expect, APIResponse
# import requests
import re


def test_api(page: Page):
    response = page.request.get('https://jsonplaceholder.typicode.com/posts/42')
    # response = requests.get('https://jsonplaceholder.typicode.com/posts/42').json()
    # print(response)
    print(response.status)
    expect(response).to_be_ok()


def test_catch_response(page: Page):
    page.goto('https://www.airbnb.ru/')
    with page.expect_response(re.compile('/autosuggestions')) as reponse_event:
        page.get_by_test_id('header-tab-search-block-tab-EXPERIENCES').click()
        response = reponse_event.value

    expect(APIResponse(response)).to_be_ok()
    print(response.json())
    assert response.json()['show_nearby'] is False
