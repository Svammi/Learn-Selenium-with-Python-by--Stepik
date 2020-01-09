from selenium import webdriver
import math
import time

def calc(x):
    return math.log(abs(12*math.sin(x)))

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/execute_script.html"
browser.get(link)

x_value = browser.find_element_by_id("input_value")
answer = calc(int(x_value.text))

input = browser.find_element_by_id("answer")
input.send_keys(str(answer))
browser.execute_script("arguments[0].scrollIntoView(true);", input)# скролл страницы

checkbox = browser. find_element_by_id("robotCheckbox")
checkbox.click()

radiobutton = browser.find_element_by_id("robotsRule")
radiobutton.click()

button = browser.find_element_by_tag_name("button")
button.click()

time.sleep(10)
browser.quit()