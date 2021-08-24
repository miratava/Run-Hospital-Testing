from navigation import Navigation
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import wait
import random
import time
from datetime import datetime, timedelta
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
   
   
class NewMedicationRequestPage(Navigation):

    def __init__(self, driver):
        self.driver = driver
        self.url = "http://demo.hospitalrun.io/#/medication"
        

    def wait(self, xpath):
        WebDriverWait(self.driver, 10).until(expected_conditions.
            visibility_of_all_elements_located((By.XPATH, xpath)))
        return

    def choose_visit(self):
        self.driver.find_element_by_xpath("//select").click()
        time.sleep(3)
        dates = self.driver.find_elements_by_xpath("//select/option")
        random.choice(dates[1:]).click()
        return

    def fill_name_field(self, name, name_in_db):
        xpath_input = "//input[@dir='auto']"
        self.wait(xpath_input)
        name_field = self.driver.find_elements_by_xpath(xpath_input)[0]
        time.sleep(9)
        name_field.send_keys(name)
        xpath = "//div[@class='tt-suggestion tt-selectable' and contains(.,'"+ name_in_db +"') and not(contains(.,'P03447'))]"
        self.wait(xpath)
        self.driver.find_elements_by_xpath(xpath)[0].click()
        return
    
    def choose_medication(self, medication):
        xpath = "//label[contains(.,'Medication')]/following-sibling::div//input"
        self.wait(xpath)
        medication_field = self.driver.find_elements_by_xpath(xpath)[1]
        medication_field.send_keys(medication)
        portions =self.driver.find_elements_by_xpath("//div[@class='tt-dataset tt-dataset-1']/div[contains(.,$medication)]")
        random.choice(portions).click()
        return

    def fill_prescription(self, text):
        field_prescription = self.driver.find_element_by_xpath("//textarea")
        field_prescription.send_keys(text)
        return

    def choose_prescription_date(self, days_number):
        today = datetime.today()
        n_days_before = today - timedelta(days=days_number)
        needed_date = str(n_days_before.strftime("%m/%d/%y"))
        date_field = self.driver.find_element_by_xpath("//label[contains(.,'Prescription Date')]/following-sibling::div/input")
        date_field.clear()
        date_field.send_keys(needed_date)
        date_field.click()
        return

    def fill_quantity_requested(self):
        xpath = "//label[contains(.,'Quantity Requested')]/following-sibling::div/input"
        self.wait(xpath)
        quantity_field = self.driver.find_element_by_xpath(xpath)
        quantity_field.send_keys(random.randint(1, 5))
        return
    
    def fill_refills(self):
        xpath = "//label[contains(.,'Refills')]/following-sibling::div/input"
        self.wait(xpath)
        refills_field = self.driver.find_element_by_xpath(xpath)
        refills_field.send_keys(random.randint(5, 10))
        return

    def submit_form(self):
        time.sleep(2)
        self.driver.find_element_by_xpath("//div[@class='panel-footer']/button[@class='btn btn-primary on-white ']").click()
        return

    def check_displaying_popup(self):
        xpath = "//div[@class='modal-body']"
        self.wait(xpath)
        popup_text = self.driver.find_element_by_xpath(xpath).get_attribute('innerText')
        print(popup_text)
        assert popup_text == "The medication record has been saved."
    
        is_cross_button = False
        if self.driver.find_element_by_xpath("//div[@class='modal-content']//button[@type='button']"):
            is_cross_button = True
        assert is_cross_button == True

        is_ok_button = False
        ok_button = self.driver.find_element_by_xpath("//div[@class='modal-content']//button[@class='btn btn-primary on-white ']")
        if ok_button:
            is_ok_button = True
        ok_button.click()
        assert is_ok_button == True

    def fill_all_fields(self, name, name_in_db, medication, prescription, days_number):
        self.driver.find_element_by_xpath("//a[@href='#/medication/edit/new']").click()
        self.fill_name_field(name, name_in_db)
        self.choose_visit()
        self.choose_medication(medication)
        self.fill_prescription(prescription)
        self.choose_prescription_date(days_number)
        self.fill_quantity_requested()
        self.fill_refills()
        self.submit_form()
        self.check_displaying_popup()
        return
    
