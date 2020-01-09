from selenium import webdriver
import os
import time

link = "http://suninjuly.github.io/file_input.html"

browser = webdriver.Chrome()
browser.get(link)

first_name = browser.find_element_by_name("firstname")
first_name.send_keys("Ivanov")

last_name = browser.find_element_by_name("lastname")
last_name.send_keys("Ivan")

Email = browser.find_element_by_name("email")
Email.send_keys("test@mail.ru")

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'test.txt')           # добавляем к этому пути имя файла
download_file = browser.find_element_by_id("file")
download_file.send_keys(file_path)

button = browser.find_element_by_tag_name("button")
button.click()

time.sleep(10)
browser.quit()
