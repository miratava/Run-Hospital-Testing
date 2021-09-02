import time
from pages.login_pg import LoginPage
from pages.navigation import Navigation
from pages.request_medications_pg import NewMedicationRequestPage
from pages.patients_pg import PatientsPage
import pytest


@pytest.mark.parametrize("login, password", [("hr.doctor@hospitalrun.io", "HRt3st12")])
def test_sign_in(login, password, params):
    driver = params
    navigation = Navigation(driver)
    patients_page = PatientsPage(driver)
    login_page = LoginPage(driver)
    login_page.sign_in(login, password)
    #time.sleep(600)
    title = patients_page.find_title()
    login_state = navigation.find_login_assert()    
    assert title == "Patient Listing"
    assert login_state == "Logout" , "Message"
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
    login_state = login_page.find_login_status() 
    login_page_header = login_page.find_page_header()
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
    navigation.find_medication_menu_item() 
    navigation.check_categories()
    navigation.go_to_new_medication_request()
    request.fill_all_fields(name, name_in_db, medication, prescription, days_number)
    driver.close()
    