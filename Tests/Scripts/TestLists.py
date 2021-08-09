import sys
import os
sys.path.append(sys.path[0] + "/...")
sys.path.append(os.getcwd())
from Src.PageObject.Pages.BasePage.BasePage import Home
from Src.PageObject.Pages.BasePage.ListsPage import Lists
from Src.TestBase.WebDriverSetup import WebDriverSetup
import unittest


class List(WebDriverSetup):

    def test_lists(self):
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
        base_page.getlists().click()
        base_page = Lists(driver)
        base_page.getselectDropDown().click()
        assert base_page.getDaySelected().get_attribute("innerHTML") == 'Day selected :- Sunday'

if __name__ == '__main__':

    unittest.main()