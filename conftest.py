# conftest.py
import pytest
from selenium import webdriver
from selenium.webdriver import chrome
from selenium.webdriver import firefox
#from get_gecko_driver import GetGeckoDriver
import geckodriver_autoinstaller

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", help="input browser (chrome/firefox)")


def get_chrome_options():
    options = chrome.options.Options()
    options.headless = True
    return options

def get_firefox_options():
    #geckodriver_autoinstaller.install() 
    options = firefox.options.Options()
    options.headless = True
    return options

def get_needed_driver(input_params):
    browsers = {"firefox": lambda : webdriver.Firefox(options=get_firefox_options()), "chrome": lambda : webdriver.Chrome(options=get_chrome_options())}
    if input_params == "firefox":
        geckodriver_autoinstaller.install()
        #get_driver = GetGeckoDriver()
        #get_driver.install()
    driver = browsers[input_params['browser']]()
    return driver


@pytest.fixture
def params(request):
    params = {}
    params['browser'] = request.config.getoption('--browser')
    if params['browser'] is None :
        params['browser'] = 'chrome'
    driver = get_needed_driver(params)
    return driver
                                 
