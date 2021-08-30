from selenium.webdriver.common.by import By


class LoginPageLocator:
    LOCATOR_USERNAME_FIELD = (By.ID, "identification")
    LOCATOR_PASSWORD_FIELD = (By.XPATH, "//input[@type='password']")
    LOCATOR_SUBMIT_BUTTON = (By.XPATH, "//button[@type='submit']")
    LOCATOR_ALLERT = (By.XPATH, "//div[@role='alert']")
    LOCATOR_FORM_HEADER = (By.XPATH, "//h2[@class='form-signin-heading']")



class PatientsPageLocator():
    LOCATOR_TITLE = (By.XPATH, "//h1[@class='view-current-title']")



class NavigationLocator:
    LOCATOR_MENU_ITEM_MEDICATION = (By.XPATH, "//a[@href='#/medication']")
    LOCATOR_MEDICATION_CATEGORIES = (By.XPATH , "//div[@class='category-sub-items']/div/a")
    LOCATOR_LOGOUT_EREA = (By.CSS_SELECTOR, "a.settings-trigger")
    LOCATOR_LOGOUT_BUTTON = (By.CSS_SELECTOR, "a.logout")
    LOCATOR_MEDICATION_NEW = (By.XPATH, "//a[@href='#/medication/edit/new']")


class MedicationRequestLocator:
    name_in_db = ''
    medication = ''
    LOCATOR_FIELD_MEDICATION = (By.XPATH, "//label[contains(.,'Medication')]/following-sibling::div//input")
    LOCATOR_FIELD_NAME = (By.XPATH, "//input[@dir='auto']")
    LOCATOR_NAME_FROM_LIST = (By.XPATH, "//div[@class='tt-suggestion tt-selectable' and contains( \
                                .,'"+ name_in_db +"') and not(contains(.,'P03447'))]")
    LOCATOR_MEDICATIONS_LIST = (By.XPATH, "//div[@class='tt-dataset tt-dataset-1']/div[contains(.,'"+ medication +"')]")
    LOCATOR_FIELD_VISIT = (By.XPATH, "//select")
    LOCATOR_VISITS_LIST = (By.XPATH, "//select/option")
    LOCATOR_PRESCRIPTION = (By.XPATH, "//textarea")
    LOCATOR_FIELD_DATE = (By.XPATH, "//label[contains(.,'Prescription Date')]/following-sibling::div/input")
    LOCATOR_FIELD_QUANTITY = (By.XPATH, "//label[contains(.,'Quantity Requested')]/following-sibling::div/input")
    LOCATOR_FIELD_REFILLS = (By.XPATH, "//label[contains(.,'Refills')]/following-sibling::div/input")
    LOCATOR_BUTTON_SUBMIT = (By.XPATH, "//div[@class='panel-footer']/button[@class='btn btn-primary on-white ']")
    LOCATOR_POPUP = (By.XPATH, "//div[@class='modal-body']")
    LOCATOR_BUTTON_CROSS = (By.XPATH, "//div[@class='modal-content']//button[@type='button']")
    LOCATOR_BUTTON_OK = (By.XPATH, "//div[@class='modal-content']//button[@class='btn btn-primary on-white ']")
    
   