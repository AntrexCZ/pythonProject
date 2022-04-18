from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    first_name = browser.find_element_by_class_name("first")
    first_name.send_keys("Andrey")
    last_name = browser.find_element_by_class_name("second")
    last_name.send_keys("Iesmienieiev")
    email = browser.find_element_by_class_name("third")
    email.send_keys("antrex@email.cz")
    phone = browser.find_element_by_xpath("/html/body/div/form/div[2]/div[1]/input")
    phone.send_keys("773 175 874")
    address = browser.find_element_by_xpath("/html/body/div/form/div[2]/div[2]/input")
    address.send_keys("Prague 9, Letovska 777, 199 00")

    #Send form
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Checking it is registered
    # Waiting for the page to load
    time.sleep(1)

    #Search for element that contains text
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    #Write variable text to the welcome_element_elt
    welcome_text = welcome_text_elt.text

    #With the help of assert checking the text with the expected ones
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()




