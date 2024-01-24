from selenium import webdriver
import pytest

@pytest.fixture()
def setup(browser):
    if browser == 'Edge':
        driver = webdriver.Edge()
        print("Launching Microsoft Edge Browser")
    elif browser == 'Firefox':
        driver = webdriver.Firefox()
        print("Launching firefox browser")
    else:
        driver = webdriver.Chrome()
        print("Launching Google chrome Browser")
    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()

def browser(request):
    return request.config.getoption("--browser")
