from selenium import webdriver
import time
import os

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/file_input.html")

    name = browser.find_element_by_name("firstname").send_keys("Andrii")
    lastname = browser.find_element_by_name("lastname").send_keys("Iesmienieiev")
    email = browser.find_element_by_name("email").send_keys("lala@gg.cz")
    directory = "C:/Users/antre/PycharmProjects/pythonProject/"
    file_name = "gg.txt"
    file_path = os.path.join(directory, file_name)
    file = browser.find_element_by_id("file")
    file.send_keys(file_path)
    button = browser.find_element_by_tag_name("button").click()
finally:
    time.sleep(3)
    browser.quit()
