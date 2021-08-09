import os
import sys
from selenium.webdriver.common.by import By
from Src.PageObject.Pages.BasePage.BasePageLocators import Locator

sys.path.append(os.getcwd())

class Home(object):
    def __init__(self, driver):
        self.driver = driver
        self.basicFormExample = driver.find_element(By.XPATH, Locator.basicFormExample)
        self.simpleFormDemo = driver.find_element(By.XPATH, Locator.simpleFormDemo)
        self.simpleList = driver.find_element(By.XPATH, Locator.simpleList)
        self.javascriptAlerts = driver.find_element(By.XPATH, Locator.javascriptAlerts)
        self.closePopUp = driver.find_element(By.XPATH,Locator.closePopup)
        self.bootstrapModals = driver.find_element(By.XPATH,Locator.bootstrapModals)
        self.lists = driver.find_element(By.XPATH,Locator.lists)

    def getbasicFormExample(self):
        return self.basicFormExample

    def getsimpleFormDemo(self):
        return self.simpleFormDemo

    def getsimpleList(self):
        return self.simpleList

    def getjavascriptAlerts(self):
        return  self.javascriptAlerts

    def getbootstrapModals(self):
        return  self.bootstrapModals

    def getlists(self):
        return self.lists

    def getclosePopUp(self):
        return  self.closePopUp


