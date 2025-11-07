# BASE PAGE FOR ORANGE HRM
# Page classes represents the webpage.
# Importing WebDriverWait is used to explicitly wait for elements to appear, disappear,clickable
# Explicit wait is used to wait for specific condition to occur before proceeding to next.
from selenium.webdriver.support.ui import WebDriverWait
# Importing expected_conditions like url contains,presence of element,visibility of element
from selenium.webdriver.support import expected_conditions as EC


# BasePage class contains methods to click,find,enter text in the element and get the URL of page
class BasePage:


    # Constructor method used to interact with Selenium Webdriver. Driver is passed from 'setup' code
    def __init__(self, driver):
        self.driver = driver


    # Finding the element using the locator with timeout of 5 seconds using explicit wait
    def find_element(self, locator, timeout=5):
        # Explicit wait until the element is located else raises TimeOutException
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))


    # Find and Click the element using the locator with timeout of 10 seconds using explicit wait
    def click_element(self, locator, timeout=10):
        # This uses find_element method to locate the element and then clicks it.
        element = self.find_element(locator, timeout)
        element.click()


    # Find and Enter the text using the locator with timeout of 10 seconds using explicit wait
    def enter_text(self, locator, text, timeout=10):
        # This uses find_element method to locate the element and then types the given text.
        element = self.find_element(locator, timeout)
        # Clears the element before typing the text
        element.clear()
        element.send_keys(text)


    # get_current_url returns the current page URL
    def get_current_url(self):
        return self.driver.current_url


