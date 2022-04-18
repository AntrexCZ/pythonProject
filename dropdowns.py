from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

# Testing code, not for the web

link = "http://suninjuly.github.io/selects1.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element_by_tag_name("select").click()
    browser.find_element_by_css_selector("option:nth-child(2)").click()
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value("1") # find element with text Python

finally:
    browser.quit()