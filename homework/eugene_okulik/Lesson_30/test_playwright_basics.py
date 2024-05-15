from playwright.sync_api import Page, expect
import re


def test_first_test(page: Page):
    page.goto('https://www.google.com/')
    search_field = page.get_by_role('combobox')
    search_field.fill('cat')
    search_field.press("Enter")
    # assert 'cat' in page.title()
    # assert page.title().startswith('cat')
    expect(page).to_have_title(re.compile('cat'))
    expect(page).to_have_title(re.compile('^cat'))
    # expect(page).to_have_title(re.compile('cat$')) # cat дожно быть в конце


def test_by_role(page: Page):
    page.goto('https://magento.softwaretestingboard.com/')
    whats_new = page.get_by_role('menuitem', name='What\'s New')
    whats_new.click()
    search_terms = page.get_by_role('link', name='Search Terms')
    search_terms.click()
