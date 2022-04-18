from selenium import webdriver
import time
import math

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/redirect_accept.html")
    button_click = browser.find_element_by_class_name("trollface").click()
    new_window = browser.window_handles[1]
    browser.switch_to_window(new_window)

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    input_value = browser.find_element_by_id("input_value")
    x = input_value.text
    y = calc(x)

    answer = browser.find_element_by_id("answer").send_keys(y)
    submit_button_final = browser.find_element_by_css_selector("body > form > div > div > button").click()

finally:
    time.sleep(5)
    browser.quit()