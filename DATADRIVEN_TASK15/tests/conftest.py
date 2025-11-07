# Conftest.py is used to define fixtures that can be reused across multiple test files.
# conftest.py is stored globally to be accessed by all other folders
#To import pytest modules
import pytest
#Importing Webdriver module from Selenium library
from selenium import webdriver
# Importing Chrome driver options to add different arguments like headless,disable pop-up
from selenium.webdriver.chrome.options import Options


# Fixtures are functions in pytest used to prepare environment for test execution.
#Scope="function" defines set up and tear down for each test
@pytest.fixture(scope="function")
# request is a built-in pytest fixture that gives you access to the test context. setup is fixture name
def setup(request):

    #Lets to customize how Chrome behaves when test runs.
    chrome_options=Options()
    # This runs the browser in headless mode which runs in background.
    chrome_options.add_argument('--headless')
    # To disable pop-up notifications
    chrome_options.add_argument('--disable-notifications')


    #Creating WebDriver instance to open Chrome browser
    driver = webdriver.Chrome(options=chrome_options)
    # get() navigates to orange hrm and opens in Chrome Browser
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    #This is used to view the Chrome Browser in maximized window
    driver.maximize_window()


    # request.cls.driver = driver lets self.driver to be used inside test class methods.
    request.cls.driver = driver
    # yield is used for setup and teardown logic
    yield
    # Closes the Chrome Window and ends the WebDriver session
    driver.quit()


