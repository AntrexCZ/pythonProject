from selenium import webdriver
import time
import math

try:
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)


    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)

    answer = browser.find_element_by_id("answer")
    answer.send_keys(y)

    checkbox = browser.find_element_by_css_selector("[for='robotCheckbox']").click()
    radiobutton = browser.find_element_by_id("robotsRule").click()

    submit = browser.find_element_by_tag_name("button").click()
    print(y)

finally:
    time.sleep(10)
    browser.quit()
