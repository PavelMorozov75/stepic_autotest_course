from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

class TestTest:
    def test_window(self):
        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/registration1.html")
        browser.find_element(By.CSS_SELECTOR, "div.first_block div.first_class&gt;label+input").send_keys("Ivan")
        browser.find_element(By.CSS_SELECTOR, "div.first_block div.second_class&gt;label+input" ).send_keys("Petrov")
        browser.find_element(By.CSS_SELECTOR, "div.first_block div.third_class&gt;label+input ").send_keys("Ivan@mail.ru")
        WebDriverWait(browser, 5).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "button.btn"))).click()

        WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located((By.XPATH,
                                                                                 "//h1[contains(text(), "
                                                                                 "'Congratulations! You have "
                                                                                 "successfully registered!')]")))
