import sys
import os
sys.path.append(sys.path[0] + "/...")
sys.path.append(os.getcwd())
from Src.PageObject.Pages.BasePage.BasePage import Home
from Src.PageObject.Pages.BasePage.Alerts import Alerts, Modals
from Src.TestBase.WebDriverSetup import WebDriverSetup
import unittest


class BaseAlertsModals(WebDriverSetup):

    def test_alerts(self):
        driver = self.driver
        self.driver.get("https://www.seleniumeasy.com/test/")
        self.driver.set_page_load_timeout(30)
        # check if correct webpage loaded
        web_page_title = "Selenium Easy - Best Demo website to practice Selenium Webdriver Online"

        try:
            if driver.title == web_page_title:
                print("WebPage loaded successfully")
                self.assertEqual(driver.title, web_page_title)
        except Exception as error:
            print(error + "WebPage Failed to load")

        base_page = Home(driver)
        # close window pop_up // did not use try/except because every new session throws popup
        base_page.getclosePopUp().click()
        base_page.getbasicFormExample().click()
        base_page.getjavascriptAlerts().click()
        base_page = Alerts(driver)
        try :
            if base_page.getclickMeButton().text == "Click Me!":
                base_page.getclickMeButton().click()
                assert driver.switch_to_alert().text == "I am an alert box!"
        except base_page.getclickMeButton().isNotVisible():
            print("Error!")

    def test_modals(self):
        driver = self.driver
        self.driver.get("https://www.seleniumeasy.com/test/")
        self.driver.set_page_load_timeout(30)
        # check if correct webpage loaded
        web_page_title = "Selenium Easy - Best Demo website to practice Selenium Webdriver Online"
        try:
            if driver.title == web_page_title:
                print("WebPage loaded successfully")
                self.assertEqual(driver.title, web_page_title)
        except Exception as error:
            print(error + "WebPage Failed to load")
            # close window pop_up // did not use try/except because every new session throws popup
        base_page = Home(driver)
        base_page.getclosePopUp().click()
        base_page.getbasicFormExample().click()
        base_page.getbootstrapModals().click()
        base_page = Modals(driver)
        try:
            if base_page.getlaunchModalButton().text == "Launch Modal":
                    base_page.getlaunchModalButton().click()
                    assert base_page.getmodalText().text == "This is the place where the content for the modal dialog displays"
        except base_page.getlaunchModalButton().isNotVisible():
                print("Error!")


if __name__ == '__main__':

    unittest.main()