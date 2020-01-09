from selenium import webdriver
import math
import time

def calc(x):
    return math.log(abs(12*math.sin(x)))

def button(browser):
    button = browser.find_element_by_tag_name("button")
    button.click()

link = "http://suninjuly.github.io/redirect_accept.html"

browser = webdriver.Chrome()
browser.get(link)

button(browser)

windows = browser.window_handles
new_window = browser.switch_to.window(windows[1])

x_value = browser.find_element_by_id("input_value")
answer = calc(int(x_value.text))

input = browser.find_element_by_id("answer")
input.send_keys(str(answer))

button(browser)

alert = browser.switch_to.alert
answer = alert.text.split(": ")[-1]
print(answer)

time.sleep(10)
browser.quit()
