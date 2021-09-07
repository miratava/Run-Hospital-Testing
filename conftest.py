# conftest.py
import pytest
from selenium import webdriver
from selenium.webdriver import chrome
from selenium.webdriver import firefox


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", help="input browser (chrome/firefoxf)")
    

def get_chrome_options():
    options = chrome.options.Options()
    #options.add_argument('--headless')
    #options.add_argument('--disable-gpu')  
    options.headles = True
    return options

def get_firefox_option():
    options = firefox.options.Options()
    options.headless = True
    return options

def get_driver(input_params):
    browsers = {"firefoxf": lambda : webdriver.Firefox(options=get_firefox_option()), "chrome": lambda : webdriver.Chrome(chrome_options=get_chrome_options())}
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