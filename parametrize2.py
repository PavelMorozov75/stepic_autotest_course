import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import time
import math


@pytest.fixture
def browser():
    browser = webdriver.Chrome()
    #browser.get(link)
    yield browser
    browser.quit()

class Testauth:
    @pytest.mark.parametrize('link', ["https://stepik.org/lesson/236896/step/1"])

    def test_authorization_in_stepic(self, browser, link):
        browser.get(link)
        mail = 'pavelvmorozov75@yandex.ru'
        password = 'Ligaliga123'
        WebDriverWait(browser,15).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, 'a#ember33'))).click()
        WebDriverWait(browser, 15).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, 'button.sign-form__btn')))
        browser.find_element(By.CSS_SELECTOR, 'input#id_login_email').clear()
        browser.find_element(By.CSS_SELECTOR, 'input#id_login_email').send_keys(mail)
        browser.find_element(By.CSS_SELECTOR, 'input#id_login_password').clear()
        browser.find_element(By.CSS_SELECTOR, 'input#id_login_password').send_keys(password)
        browser.find_element(By.CSS_SELECTOR, "button.sign-form__btn").click()
        WebDriverWait(browser, 15).until(expected_conditions.visibility_of_element_located ((By.CSS_SELECTOR, 'button.submit-submission')))
        browser.find_element(By.TAG_NAME, "textarea").clear()
        answer = str(math.log(int(time.time())))
        browser.find_element(By.TAG_NAME, "textarea").send_keys(answer)
        WebDriverWait(browser, 3).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "button.submit-submission"))).click()
        time.sleep(15)
        WebDriverWait(browser, 15).until(expected_conditions.visibility_of_element_located((By.XPATH, "//p[@class='smart-hints__hint']")))
        text = browser.find_element(By.XPATH, "//p[@class='smart-hints__hint']").text
        with open("output.txt", 'a') as f:
            f.write(text + '  ')
            f.close()

        assert 'Correct!' in text, f'test failed'



