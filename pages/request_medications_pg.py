from selenium.webdriver.support import wait
from .navigation import Navigation
import random
import time
from datetime import datetime, timedelta
from .locators import MedicationRequestLocator
from .components import Record

class NewMedicationRequestPage(Navigation):

    def __init__(self, driver):
        super().__init__(driver)
        self.url = "http://demo.hospitalrun.io/#/medication"
        

    def choose_visit(self):
        self.wait(MedicationRequestLocator.LOCATOR_FIELD_VISIT)
        self.find_element(MedicationRequestLocator.LOCATOR_FIELD_VISIT).click()
        time.sleep(3)
        #wait()
        dates = self.find_elements(MedicationRequestLocator.LOCATOR_VISITS_LIST)
        random.choice(dates[1:]).click()
        return

    def fill_name_field(self, name, name_in_db):
        self.wait(MedicationRequestLocator.LOCATOR_FIELD_NAME)
        name_field = self.find_elements(MedicationRequestLocator.LOCATOR_FIELD_NAME)[0]
        time.sleep(9)
        name_field.send_keys(name)
        self.wait(MedicationRequestLocator.LOCATOR_NAMES_LIST)
        records = [Record(x) for x in self.find_elements(MedicationRequestLocator.LOCATOR_NAMES_LIST)]
        for i in records:
            if i.get_text() == name_in_db:
                i.select()
                break
            else:
                continue
        return
    
    def choose_medication(self, medication):
        self.wait(MedicationRequestLocator.LOCATOR_FIELD_MEDICATION)
        medication_field = self.find_elements(MedicationRequestLocator.LOCATOR_FIELD_MEDICATION)[1]
        medication_field.send_keys(medication)
        medication_portions = [Record(x) for x in self.find_elements(MedicationRequestLocator.LOCATOR_ITEMS_MEDICATION_LIST)]
        random.choice(medication_portions).select()
        return

    def fill_prescription(self, text):
        field_prescription = self.find_element(MedicationRequestLocator.LOCATOR_PRESCRIPTION)
        field_prescription.send_keys(text)
        return

    def choose_prescription_date(self, days_number):
        today = datetime.today()
        n_days_before = today - timedelta(days=days_number)
        needed_date = str(n_days_before.strftime("%m/%d/%y"))
        date_field = self.find_element(MedicationRequestLocator.LOCATOR_FIELD_DATE)
        date_field.clear()
        date_field.send_keys(needed_date)
        date_field.click()
        return

    def fill_quantity_requested(self):
        self.wait(MedicationRequestLocator.LOCATOR_FIELD_QUANTITY)
        quantity_field = self.find_element(MedicationRequestLocator.LOCATOR_FIELD_QUANTITY)
        quantity_field.send_keys(random.randint(1, 5))
        return
    
    def fill_refills(self):
        self.wait(MedicationRequestLocator.LOCATOR_FIELD_REFILLS)
        refills_field = self.find_element(MedicationRequestLocator.LOCATOR_FIELD_REFILLS)
        refills_field.send_keys(random.randint(5, 10))
        return

    def submit_form(self):
        time.sleep(2)
        self.find_element(MedicationRequestLocator.LOCATOR_BUTTON_SUBMIT).click()
        return

    def check_displaying_popup(self):
        self.wait(MedicationRequestLocator.LOCATOR_POPUP)
        popup_text = self.find_element(MedicationRequestLocator.LOCATOR_POPUP).get_attribute('innerText')
        print(popup_text)
        assert popup_text == "The medication record has been saved."
    
        is_cross_button = False
        if self.find_element(MedicationRequestLocator.LOCATOR_BUTTON_CROSS):
            is_cross_button = True
        assert is_cross_button == True

        is_ok_button = False
        ok_button = self.find_element(MedicationRequestLocator.LOCATOR_BUTTON_OK)
        if ok_button:
            is_ok_button = True
        ok_button.click()
        assert is_ok_button == True

    def fill_all_fields(self, name, name_in_db, medication, prescription, days_number):
        
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
    
