# conftest.py
import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", help="input browser (chrome/firefoxf)")
   

def get_driver(input_params):
        browsers = {"firefoxf": lambda : webdriver.Firefox(), "chrome": lambda : webdriver.Chrome()}
        driver = browsers[input_params['browser']]()
        return driver


@pytest.fixture
def params(request):
    params = {}
    params['browser'] = request.config.getoption('--browser')
    if params['browser'] is None :
        params['browser'] = 'chrome'
    driver = get_driver(params)
    return driver