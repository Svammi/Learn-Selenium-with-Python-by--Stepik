from selenium import webdriver
import math
import time

def calc_value(x):
    res2 = str(math.log(abs(12*math.sin(int(x)))))
    return res2

link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)
try:

    image = browser.find_element_by_tag_name("img")
    x = image.get_attribute("valuex")
    value = calc_value(x)

    input = browser.find_element_by_id("answer")
    input.send_keys(value)

    checkbox = browser.find_element_by_id("robotCheckbox")
    checkbox.click()

    radiobutton = browser.find_element_by_id("robotsRule")
    radiobutton.click()

    button = browser.find_element_by_class_name("btn-default")
    button.click()

finally:
    print("Что-то пошло не так(")
    time.sleep(10)
    browser.quit()