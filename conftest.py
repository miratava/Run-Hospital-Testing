# conftest.py
import pytest
from selenium import webdriver
from selenium.webdriver import chrome
from selenium.webdriver import firefox
#from get_gecko_driver import GetGeckoDriver
import geckodriver_autoinstaller

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", help="input browser (chrome/firefox)")


def get_chrome():
    options = chrome.options.Options()
    options.headless = True
    return webdriver.Chrome(options=options)


def get_firefox():
    #geckodriver_autoinstaller.install() 
    geckodriver_autoinstaller.install()
    options = firefox.options.Options()
    options.headless = True
    return webdriver.Firefox(options=options)


def get_needed_driver(input_params):
    browsers = {"firefox": get_firefox, "chrome": get_chrome}
    driver = browsers[input_params['browser']]()
    return driver


@pytest.fixture
def params(request):
    params = {}
    params['browser'] = request.config.getoption('--browser')
    if params['browser'] is None :
        params['browser'] = 'chrome'
    driver = get_needed_driver(params)

                                 
