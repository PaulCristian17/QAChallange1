import os
import sys
from selenium.webdriver.common.by import By
from Src.PageObject.Pages.BasePage.SimpleFormLocators import Locator

sys.path.append(os.getcwd())
class HomeSimpleForm(object):

    def __init__(self,driver):

        self.inputMessage = driver.find_element(By.XPATH, Locator.inputMessage)
        self.showMessageButton = driver.find_element(By.XPATH, Locator.showMessageButton)
        self.userMessage = driver.find_element(By.XPATH, Locator.userMessage)

    def getinputMessage(self):
        return self.inputMessage

    def getshowMessageButton(self):
        return self.showMessageButton

    def getuserMessage(self):
        return self.userMessage