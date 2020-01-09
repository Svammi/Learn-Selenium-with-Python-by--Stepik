from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import  expected_conditions as ec
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return math.log(abs(12*math.sin(x)))

link = "http://suninjuly.github.io/explicit_wait2.html"

browser = webdriver.Chrome()
browser.get(link)

price = WebDriverWait(browser, 12).until(ec.text_to_be_present_in_element((By.ID, "price"), "$100"))

button = browser.find_element_by_id("book")
button.click()


x_value = browser.find_element_by_id("input_value")
answer = calc(int(x_value.text))

input = browser.find_element_by_id("answer")
input.send_keys(str(answer))

button = browser.find_element_by_id("solve")
button.click()

time.sleep(10)
browser.quit()

