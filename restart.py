import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def dr():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    return browser
    browser.quit()

link = "http://selenium1py.pythonanywhere.com/"

def test_guest_should_see_login_link_pass(dr):
    dr.get(link)
    dr.find_element(By.CSS_SELECTOR, "#login_link")

def test_guest_should_see_login_link_fail(dr):
    dr.get(link)
    dr.find_element(By.CSS_SELECTOR, "#magic_link")