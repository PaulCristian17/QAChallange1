import os
import sys
from selenium.webdriver.common.by import By
from Src.PageObject.Pages.BasePage.AlertsModalsLocators import Locator

sys.path.append(os.getcwd())
class Alerts(object):

    def __init__(self,driver):
        self.driver = driver
        self.clickMeButton = driver.find_element(By.XPATH, Locator.clickMeButton)

    def getclickMeButton(self):
        return self.clickMeButton



class Modals(object):

    def __init__(self,driver):
        self.modalText = driver.find_element(By.XPATH, Locator.modalText)
        self.launchModalButton = driver.find_element(By.XPATH, Locator.launchModalButton)

    def getlaunchModalButton(self):
        return self.launchModalButton

    def getmodalText(self):
        return  self.modalText