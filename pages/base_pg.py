from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
import chromedriver_binary

class BasePage():

    def __init__(self, driver):
        self.driver = driver

    def wait(self, locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_all_elements_located(locator))
        return

    def find_element(self, by:tuple):
        return self.driver.find_element(by[0], by[1])


    def find_elements(self, by: tuple):
        return self.driver.find_elements(by[0], by[1])

    def open(self, url):
        self.driver.get(url)
