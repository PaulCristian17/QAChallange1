import os
import sys
from selenium.webdriver.common.by import By
from Src.PageObject.Pages.BasePage.ListsLocators import Locator

sys.path.append(os.getcwd())

class Lists(object):

    def __init__(self, driver):
        self.driver = driver
        self.selectDropDown = driver.find_element(By.XPATH, Locator.selectDropDown)
        self.daySelected = driver.find_element(By.XPATH, Locator.daySelected)

    def getselectDropDown(self):
        return self.selectDropDown

    def getDaySelected(self):
        return self.daySelected


