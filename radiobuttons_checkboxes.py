from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import math, time

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/get_attribute.html")

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

x_element = browser.find_element(By.CSS_SELECTOR, "img#treasure")
x = x_element.get_attribute('valuex')
y = calc(x)

browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(y)
browser.find_element(By.CSS_SELECTOR, "#robotCheckbox").click()
browser.find_element(By.CSS_SELECTOR, "#robotsRule").click()
a = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
b = a.get_attribute('checked') # будет true с маленькой буквы !!!!!!!!
print(b)
a = browser.find_element(By.CSS_SELECTOR, "#peopleRule")
b = a.get_attribute('checked') # будет None !!!!!!!!
print(b)
WebDriverWait(browser, 5).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "button.btn"))).click()

time.sleep(10)
#browser.quit()
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

