from selenium import webdriver
import math
import time

def input_date_in_form(browser): # заполнение формы

    input1 = browser.find_element_by_tag_name("input")  # поиск по атрибуту
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name("last_name")  # поиск по атрибуту name
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_class_name("city")  # поиск по классу
    input3.send_keys("Smolensk")
    input4 = browser.find_element_by_id("country")  # поиск по id
    input4.send_keys("Russia")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

link = "http://suninjuly.github.io/find_link_text"
href = str(math.ceil(math.pow(math.pi, math.e)*10000))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    search_href = browser.find_element_by_link_text(href) # поиск по тексту ссылки
    search_href.click() # нажать на ссылку

    input_date_in_form(browser)

finally:

    time.sleep(30)
    browser.quit()

