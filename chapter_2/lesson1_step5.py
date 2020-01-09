from selenium import webdriver
import math
def calc_value(x):
    res2 = str(math.log(abs(12*math.sin(int(x)))))
    return res2


try:
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_value = browser.find_element_by_id('input_value')
    answer = calc_value(x_value.text)
    print(answer)
    input = browser.find_element_by_id("answer")
    input.send_keys(answer)

    chekbox = browser.find_element_by_id("robotCheckbox")
    chekbox.click()

    radiobutton = browser.find_element_by_id("robotsRule")
    radiobutton.click()

    button = browser.find_element_by_class_name("btn-default")
    button.click()

finally:
    print("что-то пошло не так(")

