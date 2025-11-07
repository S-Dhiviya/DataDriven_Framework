# Importing By classes from selenium for locators
from selenium.webdriver.common.by import By
# To use the methods from base_page importing Class BasePage.
# from folder_name.file_name import Class_name
from pages.base_page import BasePage


# LoginPage inherits BasePage. LoginPage contains locators and methods to interact with locators.
class LoginPage(BasePage):


    # LOCATORS - Uses find_element() from BasePage to locate these elements while doing interactions.
    # Username and password box,login button locator using XPATH
    USERNAME_INPUT = (By.XPATH, '//input[@name="username"]')
    PASSWORD_INPUT = (By.XPATH, '//input[@name="password"]')
    LOGIN_BUTTON = (By.XPATH, '//button[@type="submit"]')


    # METHODS TO INTERACT WITH THE ELEMENTS
    # login() is used to find username and password and enter the valid data and to click login button
    def login(self, username, password):

        # self.USERNAME_INPUT,self.PASSWORD_INPUT are locators. username,password are the text to be entered.
        self.enter_text(self.USERNAME_INPUT, username)
        self.enter_text(self.PASSWORD_INPUT, password)

        #Clicks the login button after locating the self.LOGIN_BUTTON
        self.click_element(self.LOGIN_BUTTON)

