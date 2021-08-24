import pytest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import wait
#from browser import Browser
#from datetime import datetime, timedelta
from selenium.webdriver.chrome.webdriver import WebDriver
#from login_pg import LoginPage
import time
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class Navigation:

    def __init__(self, driver):
        self.driver = driver
        #self.browser = Browser(driver)

    def find_medication_menu_item(self):
        xpath = "//a[@href='#/medication']"
        WebDriverWait(self.driver, 10).until(expected_conditions.
            visibility_of_all_elements_located((By.XPATH, xpath)))
        self.driver.find_element_by_xpath(xpath).click()
        
    def check_categories(self):
        xpath = "//div[@class='category-sub-items']/div/a"
        WebDriverWait(self.driver, 10).until(expected_conditions.
            visibility_of_all_elements_located((By.XPATH, xpath)))
        categories = self.driver.find_elements_by_xpath(xpath)
        category_names = ["Requests", "Completed", "New Request", "Return Medication"]
        for i in categories:
            if i.text != "Dispense":
                assert i.text in category_names 

    def logout(self):
        xpath = "//a[@class='settings-trigger ']"
        WebDriverWait(self.driver, 10).until(expected_conditions.
            visibility_of_all_elements_located((By.XPATH, xpath)))
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
    
        


