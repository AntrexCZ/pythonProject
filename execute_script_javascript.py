import math
from selenium import webdriver
import time

try:
    link = "http://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)


    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))


    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    answer = browser.find_element_by_id("answer").send_keys(y)
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    robotCheckbox = browser.find_element_by_id("robotCheckbox").click()
    robotsRule = browser.find_element_by_id("robotsRule").click()
    button.click()

finally:
    time.sleep(5)
    browser.quit()
