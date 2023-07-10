from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import math, time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")
WebDriverWait(browser, 20).until(expected_conditions.text_to_be_present_in_element((By.CSS_SELECTOR, "#price"),"$100"))
browser.find_element(By.CSS_SELECTOR, "button#book").click()

a = browser.find_element(By.XPATH, "//label/span[2]").text
print(a)
y = calc(a)
print(y)
browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(y)
WebDriverWait(browser, 5).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "#solve"))).click()

time.sleep(15)
browser.quit()
