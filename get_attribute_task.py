from selenium import webdriver
import time
import math

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/get_attribute.html")

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))


    treasure = browser.find_element_by_id("treasure")
    treasure_value = treasure.get_attribute("valuex")

    y = calc(treasure_value)
    print(y)

    answer = browser.find_element_by_id("answer").send_keys(y)
    robotCheckbox = browser.find_element_by_id("robotCheckbox").click()
    robots_rules = browser.find_element_by_id("robotsRule").click()
    button = browser.find_element_by_tag_name("button").click()

finally:
    time.sleep(5)
    browser.quit()





