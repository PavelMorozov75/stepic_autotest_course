from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/selects1.html")



a  = browser.find_element(By.CSS_SELECTOR, "#num1").text
b = browser.find_element(By.CSS_SELECTOR, "#num2").text
c =str(int(a) + int(b))
select = Select(browser.find_element(By.TAG_NAME, "select"))
select.select_by_value(c)


WebDriverWait(browser, 5).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "button.btn"))).click()

time.sleep(10)
browser.quit()
'''
browser.find_element(By.CSS_SELECTOR, "div.first_block div.first_class>label+input").send_keys("Ivan")
browser.find_element(By.CSS_SELECTOR, "div.first_block div.second_class>label+input" ).send_keys("Petrov")
browser.find_element(By.CSS_SELECTOR, "div.first_block div.third_class>label+input ").send_keys("Ivan@mail.ru")
WebDriverWait(browser, 5).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "button.btn"))).click()

WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located((By.XPATH,
                                                                                 "//h1[contains(text(), "
                                                                                 "'Congratulations! You have "
                                                                                 "successfully registered!')]")))
'''

