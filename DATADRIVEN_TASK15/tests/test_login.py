# Test Classes contains test scripts and calling actions
# Importing pytest for test_ methods and os for path handling
import pytest
import os
# Importing pandas for data analysis and manipulation.
import pandas as pd
# Importing datetime to use datetime function
from datetime import datetime
# Importing Class LoginPage from login_page under pages folder
from pages.login_page import LoginPage


# To read the Excel file and store in login_data as list
def get_login_data():

    login_data = []
    # Get the directory of the current script
    current_dir = os.path.dirname(__file__)
    # Construct the correct path to the Excel file
    data_file = os.path.join(current_dir, '../data', 'login_data.xlsx')

    # Read the Excel file using pandas and engine='openpyxl' to handle Excel files
    df = pd.read_excel(data_file,engine='openpyxl')

    # df.iterrows()	iterates through the rows of the DataFrame
    # index=number (0, 1, 2, ...) and row= data in the particular row
    for index, row in df.iterrows():
        username = row['username']
        password = row['password']
        login_data.append((username, password))

    # returns login_data as list of[(user1,pass1),(user2,pass2)]
    return login_data


# To update or write the data in Excel file after testing, like result as Passed or Failed
def update_excel(username, password, result, tester_name):

    current_dir = os.path.dirname(__file__)
    data_file = os.path.join(current_dir, '../data', 'login_data.xlsx')

    # Throws exception if Excel file cannot be read
    try:
        df = pd.read_excel(data_file, engine='openpyxl')
    except Exception as e:
        print(f"Failed to read Excel file: {e}")


    # Find the row to update the data
    for index, row in df.iterrows():
        # Checks the table in Excel whether the username and password column name matches
        if row['username'] == username and row['password'] == password:

            # Finds the 'Date' and 'Time of Test' field and updates the datetime
            df.at[index, 'Date'] = datetime.now().strftime("%Y-%m-%d")
            df.at[index, 'Time of Test'] = datetime.now().strftime("%H:%M:%S")

            # tester_name and result value are updated to 'Name of Tester' and 'Test Result' field
            df.at[index, 'Name of Tester'] = tester_name
            df.at[index, 'Test Result'] = result
            break

    # Write backs to Excel
    # index=False means not to include row indices (0,1,2) as a separate column in the Excel file.
    df.to_excel(data_file,engine='openpyxl',index=False)


# To use setup fixture from conftest.py.
# TestLogin performs the login process with multiple data from Excel file
@pytest.mark.usefixtures("setup")
class TestLogin:


    # Calls the get_login_data() to read the excel file."username, password" passed as arguments
    @pytest.mark.parametrize("username, password", get_login_data())
    # test_login() enters data from Excel file and moves into dashboard page if data is valid
    def test_login(self, username, password):

        #Creates an instance of the LoginPage class,and passes the WebDriver instance (self.driver) to it.
        login_page = LoginPage(self.driver)
        # login_page object calls login() from login_page.py and enters username and password
        login_page.login(username, password)

        # Tester name is passed through this method
        tester_name = 'Dhiviya'

        # Checks if the username and password provided is valid or not
        # Valid data provides test result as Passed and calls update_excel() to write in Excel
        if "dashboard" in self.driver.current_url:
            update_excel(username, password, "Passed", tester_name)

        #Invalid data provides test result as Failed and calls update_excel() to write in Excel
        else:
            update_excel(username, password, "Failed", tester_name)

        # Checks whether login page moves to dashboard page
        assert "dashboard" in self.driver.current_url

#To generate HTML Report of Pytest cases:pytest -v -s tests/test_login.py --html=report.html
#report.html(to be opened in Browser)
# login_data.xlsx gets stored under data folder