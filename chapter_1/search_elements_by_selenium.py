from selenium import webdriver

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/simple_form_find_task.html")
#найти элемент по id
button = browser.find_element_by_id("submit_button")

#закрыть браузер
browser.quit()

