import os, sys; sys.path.extend([os.path.dirname(os.path.dirname(__file__))])
import pytest
from selenium import webdriver


# def pytest_addoption(parser):
#     parser.addoption("--browser", default="chrome")
def pytest_addoption(parser):
    parser.addoption(
        "--browser-name", default="chrome", choices=['chrome', 'ff'], 
        help="Specify the browser: chrome or ff"
        )


@pytest.fixture
def browser(request):
    browser_name = request.config.getoption("--browser-name")

    driver = None

    match browser_name:
        case 'chrome':
            driver = webdriver.Chrome()
        case 'ff':
            driver = webdriver.Firefox()


    driver.implicitly_wait(2)
    driver.maximize_window()
    yield driver
    driver.quit()