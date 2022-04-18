import time

# webdriver это и есть набор команд для управления браузером
from selenium import webdriver

# Initialise browser driver
driver = webdriver.Chrome()

# Command sleep
time.sleep(5)

# Methdod that opens browser
driver.get("https://stepik.org/lesson/25969/step/12")

time.sleep(5)
# Method find_element_by_css_selector
textarea = driver.find_element_by_css_selector(".textarea")

# Write some text
textarea.send_keys("get()")
time.sleep(5)

#Find button which sends message
submit_button = driver.find_element_by_css_selector(".submit-submission")

#What to do with the button. After that we should see message about correct answer
submit_button.click()
time.sleep(5)

#Close browser
driver.quit()