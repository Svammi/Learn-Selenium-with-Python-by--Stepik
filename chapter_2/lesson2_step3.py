from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

def sum(num1, num2):
    return num1+num2

link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)
time.sleep(2)
try:
    num1 = browser.find_element_by_id("num1")
    num2 = browser.find_element_by_id("num2")
    answer = sum(int(num1.text), int(num2.text))

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_visible_text(str(answer))

    button = browser.find_element_by_tag_name("button")
    button.click()

finally:
    time.sleep(10)
    browser.quit()
