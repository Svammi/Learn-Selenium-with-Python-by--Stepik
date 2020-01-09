from selenium import webdriver
import time
import math

def calc(x):
    return math.log(abs(12*math.sin(x)))

def button_click(browser):
    button = browser.find_element_by_tag_name("button")
    button.click()

def alert(browser):
    alert = browser.switch_to.alert
    alert.accept()

link = "http://suninjuly.github.io/alert_accept.html"

browser = webdriver.Chrome()
browser.get(link)

button_click(browser)
alert(browser)

x_value = browser.find_element_by_id("input_value")
answer = calc(int(x_value.text))

input = browser.find_element_by_id("answer")
input.send_keys(str(answer))

button_click(browser)

alert = browser.switch_to.alert
answer = alert.text.split(": ")[-1]
print(answer)



time.sleep(10)
browser.quit()