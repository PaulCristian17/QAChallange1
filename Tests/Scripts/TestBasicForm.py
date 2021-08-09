import sys
import os
sys.path.append(sys.path[0] + "/...")
sys.path.append(os.getcwd())
from Src.PageObject.Pages.BasePage.BasePage import Home
from Src.PageObject.Pages.BasePage.SimpleForm import HomeSimpleForm
from Src.TestBase.WebDriverSetup import WebDriverSetup
import unittest


class SimpleForm(WebDriverSetup):

    def test_Base_Page_input_forms(self):
        driver = self.driver
        self.driver.get("https://www.seleniumeasy.com/test/")
        self.driver.set_page_load_timeout(30)

        web_page_title = "Selenium Easy - Best Demo website to practice Selenium Webdriver Online"

        try:
            if driver.title == web_page_title:
                print("WebPage loaded successfully")
                self.assertEqual(driver.title, web_page_title)
        except Exception as error:
            print(error + "WebPage Failed to load")

        base_page = Home(driver)
        base_page.getclosePopUp().click()
        base_page.getbasicFormExample().click()
        base_page.getsimpleFormDemo().click()
        base_page = HomeSimpleForm(driver)
        #send text to input fiels
        base_page.getinputMessage().send_keys("some text")
        base_page.getshowMessageButton().click()
        #check input field is the text sent
        if base_page.getuserMessage().get_attribute("innerHTML") == "some text":
            print("success")
        else:
            print("Error")

if __name__ == '__main__':

    unittest.main()