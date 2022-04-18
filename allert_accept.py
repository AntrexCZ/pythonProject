from selenium import webdriver
import time
import math

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    submit_button = browser.find_element_by_tag_name("button").click()
    
    # Check which other method to use for switch to alert
    confirm_button = browser.switch_to_alert()
    confirm_button.accept()

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



