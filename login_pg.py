from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        print(type(self.driver))
        self.url = "http://demo.hospitalrun.io/"

    def wait(self, xpath):
        WebDriverWait(self.driver, 10).until(expected_conditions.
            visibility_of_all_elements_located((By.XPATH, xpath)))

    def sign_in(self, login, password):
        self.driver.get(self.url)
        xpath = "//input[@id='identification']"
        self.wait(xpath)
        element_username = self.driver.find_element_by_xpath(xpath)        
        element_username.send_keys(login)
        element_password = self.driver.find_element_by_xpath("//input[@id='password']")
        element_password.send_keys(password)
        self.driver.find_element_by_xpath("//button[@type='submit']").submit()
        return


    def find_alert(self):
        xpath = "//div[@role='alert']"
        self.wait(xpath)
        return  self.driver.find_element_by_xpath(xpath).text

    def find_page_header(self):
        xpath = "//h2[@class='form-signin-heading']"
        self.wait(xpath)
        return self.driver.find_element_by_xpath(xpath).text   

    def find_login_status(self):
        xpath = "//button[@type='submit']"
        self.wait(xpath)
        return self.driver.find_element_by_xpath(xpath).text   

