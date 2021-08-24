from selenium import webdriver
from login_pg import LoginPage
from navigation import Navigation
from request_medications_pg import NewMedicationRequestPage
import allure
from patients_pg import PatientsPage
import pytest


@pytest.mark.parametrize("login, password", [("hr.doctor@hospitalrun.io", "HRt3st12")])
def test_sign_in(login, password, params):
    driver = params
    page = LoginPage(driver)
    navigation = Navigation(driver)
    patients_page = PatientsPage(driver)
    page.sign_in(login, password)
        #time.sleep(5)
    title = patients_page.find_title()
    login_state = navigation.find_login_assert()
    assert login_state == "Logout"
    assert title == "Patient Listing"
    driver.close()

@pytest.mark.parametrize("login, password", [("hr.doctor@hospitalrun.io", "H")])
def test_invalid_credentials(login, password, params):
    driver = params
    login_page = LoginPage(driver)
    login_page.sign_in(login, password)
    alert = login_page.find_alert()
    assert alert == "Username or password is incorrect."
    driver.close()

@pytest.mark.parametrize("login, password", [("hr.doctor@hospitalrun.io", "HRt3st12")])
def test_is_able_logout(login, password, params):
    driver = params
    login_page = LoginPage(driver)
    navigation = Navigation(driver)
    login_page.sign_in(login, password)
    navigation.logout()
    login_state = login_page.find_login_status() #browser.find_element("//button[@type='submit']").text
    login_page_header = login_page.find_page_header()# browser.find_element("//h2[@class='form-signin-heading']").text   
    assert login_state == "Sign in"
    assert login_page_header == "please sign in".upper()
    driver.close()
          
@pytest.mark.parametrize( \
    "login, password, name, name_in_db, medication, prescription, days_number", \
    [("hr.doctor@hospitalrun.io", "HRt3st12", "Test Patient", "Test Patient - P00201", "Pramoxine", "Testing prescription", 1)])
def test_request_new_medication(login, password, name, name_in_db, medication, prescription, days_number, params):
    driver = params
    navigation = Navigation(driver)
    page = LoginPage(driver)
    request = NewMedicationRequestPage(driver)
    
    page.sign_in(login, password)
    #time.sleep(9)
    navigation.find_medication_menu_item() 
    navigation.check_categories() # after_login_page.check_categories()
    request.fill_all_fields(name, name_in_db, medication, prescription, days_number)
    driver.close()
    