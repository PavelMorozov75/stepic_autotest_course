from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time, math

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/execute_script.html")

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
#button = browser.find_element(By.TAG_NAME, "button")
#button.submit()

a = browser.find_element(By.CSS_SELECTOR, "#input_value").text

y = calc(a)

browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(y)
button_submit = browser.find_element(By.CSS_SELECTOR, "button.btn")
browser.execute_script("return arguments[0].scrollIntoView(true);", button_submit)
browser.find_element(By.CSS_SELECTOR, "#robotCheckbox").click()
browser.find_element(By.CSS_SELECTOR, "#robotsRule").click()

WebDriverWait(browser, 5).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "button.btn"))).click()

time.sleep(15)
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

