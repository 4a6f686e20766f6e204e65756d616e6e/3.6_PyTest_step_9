import pytest
from selenium import webdriver
import time

def test_guest_should_see_login_link(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    browser.get(link)
    button = browser.find_element_by_css_selector("button.btn-add-to-basket")
    # time.sleep(30) - раскоментировать для проверки 
    assert button.is_displayed(), "Button add to basket not displayed."
