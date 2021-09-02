from .locators import PatientsPageLocator
from .navigation import Navigation
from selenium.common.exceptions import NoSuchElementException
import time

class PatientsPage(Navigation):

    def __init__(self, driver):
        super().__init__(driver)
        self.url = "http://demo.hospitalrun.io/#/patients"


    def find_title(self):
        try:
            time.sleep(25)
            self.wait(PatientsPageLocator.LOCATOR_TITLE)
            return self.find_element(PatientsPageLocator.LOCATOR_TITLE).get_attribute('innerText')
        except:
            NoSuchElementException
            return ""
        
