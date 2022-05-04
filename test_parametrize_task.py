import time
import math
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#@pytest.fixture(scope="function")
#def browser():
#    print("\nstart browser test...")
#    browser = webdriver.Chrome()
#    yield browser
#    print("\nquite browser")
#    browser.quit()


@pytest.mark.parametrize('todo', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def testik(browser, todo):
    link = f"https://stepik.org/lesson/{todo}/step/1/"
    browser.get(link)
    answer = math.log(int(time.time()))
    answer_str = str(answer)
    browser.implicitly_wait(5)
    print(answer_str)
    browser.find_element_by_tag_name("textarea").send_keys(answer_str)
    button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "div.attempt__actions > button")))
    button.click()

    feedback = browser.find_element_by_css_selector(".smart-hints__hint")
    correct = feedback.text

    assert "Correct!" == correct, "Wrong Answer"
