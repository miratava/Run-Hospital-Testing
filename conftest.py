# conftest.py
import pytest
from selenium import webdriver
from selenium.webdriver import chrome
from selenium.webdriver import firefox
from selenium.webdriver.chrome.options import Options
#from selenium.webdriver.firefox.options import Options


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", help="input browser (chrome/firefox)")
    

#def get_chrome_options():
#    options = chrome.options.Options()
#    options.add_argument('--headless')
#    options.add_argument('--disable-gpu')  
#    options.headles = True
#    return options

#def get_firefox_options():
#    options = firefox.options.Options()
#    options.headless = True
#    return options

def get_driver(input_params):
    #firefox_options = firefox.options.Options()
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    browsers = {"firefox": lambda : webdriver.Firefox(), "chrome": lambda : webdriver.Chrome(chrome_options=options)}
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