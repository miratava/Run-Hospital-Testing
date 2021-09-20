# conftest.py
from _pytest.fixtures import fail_fixturefunc
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
    #options.add_argument("--no-sandbox")
    return webdriver.Chrome(options=options)


def get_firefox():
    geckodriver_autoinstaller.install()
    options = firefox.options.Options()
    options.headless = True
    return webdriver.Firefox(options=options)


@pytest.fixture
def params(request):
    params = {}
    params['browser'] = request.config.getoption('--browser')
    param = params['browser']
    if param is None or param == 'chrome':
        return get_chrome()
    elif param == 'firefox':
        return get_firefox()

                                 
