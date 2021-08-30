import time

from selenium.webdriver.support import wait
from .base_pg import BasePage
from selenium.common.exceptions import NoSuchElementException
from .locators import NavigationLocator


  
class Navigation(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
    
    def find_medication_menu_item(self):
        self.wait(NavigationLocator.LOCATOR_MENU_ITEM_MEDICATION)
        self.find_element(NavigationLocator.LOCATOR_MENU_ITEM_MEDICATION).click()
        
    def check_categories(self):
        self.wait(NavigationLocator.LOCATOR_MEDICATION_CATEGORIES)
        categories = self.find_elements(NavigationLocator.LOCATOR_MEDICATION_CATEGORIES)
        category_names = ["Requests", "Completed", "New Request", "Return Medication"]
        for i in categories:
            if i.text != "Dispense":
                assert i.text in category_names 

    def logout(self):
        self.wait(NavigationLocator.LOCATOR_LOGOUT_EREA)
        self.find_element(NavigationLocator.LOCATOR_LOGOUT_EREA).click()
        time.sleep(3)
        self.find_element(NavigationLocator.LOCATOR_LOGOUT_BUTTON).click()
        return

    def find_login_assert(self):
        try:
            #time.sleep(3)
            self.wait(NavigationLocator.LOCATOR_LOGOUT_EREA)
            self.find_element(NavigationLocator.LOCATOR_LOGOUT_EREA).click()
            self.wait(NavigationLocator.LOCATOR_LOGOUT_BUTTON)
            return self.find_element(NavigationLocator.LOCATOR_LOGOUT_BUTTON).get_attribute('innerText')
        except:
            NoSuchElementException
            return ""
    
    def go_to_new_medication_request(self):
        self.find_element(NavigationLocator.LOCATOR_MEDICATION_NEW).click()
        


