from .base_pg import BasePage
from .locators import LoginPageLocator


class LoginPage(BasePage):

    def __init__(self, driver):
        super(). __init__(driver)
        self.url = "http://demo.hospitalrun.io/"

    def sign_in(self, login, password): 
        self.open(self.url)
        input()
        self.wait(LoginPageLocator.LOCATOR_USERNAME_FIELD)

        self.find_element(LoginPageLocator.LOCATOR_USERNAME_FIELD).send_keys(login)
        
        self.find_element(LoginPageLocator.LOCATOR_PASSWORD_FIELD).send_keys(password)
        
        self.find_element(LoginPageLocator.LOCATOR_SUBMIT_BUTTON).submit()
        return

    def find_alert(self):
        self.wait(LoginPageLocator.LOCATOR_ALLERT)
        return  self.find_element(LoginPageLocator.LOCATOR_ALLERT).text

    def find_page_header(self):
        self.wait(LoginPageLocator.LOCATOR_FORM_HEADER)
        return self.find_element(LoginPageLocator.LOCATOR_FORM_HEADER).text   

    def find_login_status(self):
        self.wait(LoginPageLocator.LOCATOR_SUBMIT_BUTTON)
        return self.find_element(LoginPageLocator.LOCATOR_SUBMIT_BUTTON).text   
