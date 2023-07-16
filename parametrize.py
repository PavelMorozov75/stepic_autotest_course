import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture(scope="function")
def driver():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('language', ["ru", "en-gb"])
def test_guest_should_see_login_link(driver, language):
    link = f"http://selenium1py.pythonanywhere.com/{language}/"
    driver.get(link)
    #print('avg')
    driver.find_element(By.CSS_SELECTOR, "#login_link")

