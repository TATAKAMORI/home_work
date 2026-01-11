from pages.swag_labs import SwagLabs

def test_check_icon(browser):
    saucedemo_page = SwagLabs(browser)
    saucedemo_page.visit()
    assert saucedemo_page.exist_icon()

def test_check_username(browser):
    saucedemo_page = SwagLabs(browser)
    saucedemo_page.visit()
    assert saucedemo_page.find_element(locator='#user-name')

def test_check_password(browser):
    saucedemo_page = SwagLabs(browser)
    saucedemo_page.visit()
    assert saucedemo_page.find_element(locator='#password')