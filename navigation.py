#from selenium import webdriver
#from selenium.webdriver.support import wait
from selenium.webdriver.chrome.webdriver import WebDriver
import time
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class Navigation:

    def __init__(self, driver):
        self.driver = driver

    def wait(self, xpath):
        WebDriverWait(self.driver, 10).until(expected_conditions.
            visibility_of_all_elements_located((By.XPATH, xpath)))
        return
    
    def find_medication_menu_item(self):
        xpath = "//a[@href='#/medication']"
        self.wait(xpath)
        self.driver.find_element_by_xpath(xpath).click()
        
    def check_categories(self):
        xpath = "//div[@class='category-sub-items']/div/a"
        self.wait(xpath)
        categories = self.driver.find_elements_by_xpath(xpath)
        category_names = ["Requests", "Completed", "New Request", "Return Medication"]
        for i in categories:
            if i.text != "Dispense":
                assert i.text in category_names 

    def logout(self):
        xpath = "//a[@class='settings-trigger ']"
        self.wait(xpath)
        self.driver.find_element_by_xpath(xpath).click()
        time.sleep(3)
        self.driver.find_element_by_xpath("//a[@class='logout']").click()
        return

    def find_login_assert(self):
        try:
            self.driver.find_element_by_xpath("//a[@class='settings-trigger ']").click()
            return self.driver.find_element_by_xpath("//a[@class='logout']").text
        except:
            NoSuchElementException
            return ""
    
        


