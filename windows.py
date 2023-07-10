from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import math,time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/redirect_accept.html")
browser.find_element(By.CSS_SELECTOR, ".trollface.btn.btn-primary").click()
try:
  browser.switch_to.window(browser.window_handles[1])
  WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "#simple_text")))
  a = browser.find_element(By.CSS_SELECTOR, "#input_value").text
  print(a)
  y = calc(int(a))
  print(y)
  browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(y)
  WebDriverWait(browser, 5).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "button.btn"))).click()
  time.sleep(15)
  browser.quit()

except:
    print('Не удалось перейти в новое окно')