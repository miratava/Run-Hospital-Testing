#from home.miratava.test.study_pytest.browser import Browser
from navigation import Navigation
#from browser import Browse
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class PatientsPage(Navigation):

    def __init__(self, driver):
        self.driver = driver

    def find_title(self):
        try:
            xpath = "//h1[@class='view-current-title']"
            WebDriverWait(self.driver, 10).until(expected_conditions.
                visibility_of_all_elements_located((By.XPATH, xpath)))
            return self.driver.find_element_by_xpath(xpath).get_attribute('innerText')
        except:
            NoSuchElementException
            return ""
        

