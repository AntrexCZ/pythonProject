import unittest
from selenium import webdriver

class TestAbs(unittest.TestCase):

    def test_registration1(self):

        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/registration1.html")

        input1 = browser.find_element_by_css_selector("input[placeholder='Input your first name']")
        input1.send_keys("Andrii")
        input2 = browser.find_element_by_css_selector("input.form-control.second")
        input2.send_keys("Yessssss")
        input3 = browser.find_element_by_css_selector("input.form-control.third")
        input3.send_keys("antrex@email.com")
        input4 = browser.find_element_by_xpath("/html/body/div/form/div[2]/div[1]/input")
        input4.send_keys("+420 777 888 999")
        input5 = browser.find_element_by_xpath("/html/body/div/form/div[2]/div[2]/input")
        input5.send_keys("Pragueeeee")
        button = browser.find_element_by_tag_name("button")
        button.click()

        first_test = browser.find_element_by_tag_name("h1")
        x = first_test.text

        self.assertEqual("Congratulations! You have successfully registered!", x)

    def test_registration2(self):

        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/registration2.html")


        input1 = browser.find_element_by_css_selector("input[placeholder='Input your first name']")
        input1.send_keys("Andrii")
        input2 = browser.find_element_by_css_selector("input.form-control.second")
        input2.send_keys("Yessssss")
        input3 = browser.find_element_by_css_selector("input.form-control.third")
        input3.send_keys("antrex@email.com")
        input4 = browser.find_element_by_xpath("/html/body/div/form/div[2]/div[1]/input")
        input4.send_keys("+420 777 888 999")
        input5 = browser.find_element_by_xpath("/html/body/div/form/div[2]/div[2]/input")
        input5.send_keys("Pragueeeee")
        button = browser.find_element_by_tag_name("button")
        button.click()

        first_test = browser.find_element_by_tag_name("h1")
        x = first_test.text

        self.assertEqual("Congratulations! You have successfully registered!", x)

if __name__ == "__main__":
   unittest.main()
