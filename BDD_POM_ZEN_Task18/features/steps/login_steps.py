# Step definition file for login functionality of ZEN portal
# This file contains the step definitions for the scenarios in "login.feature" file.


# Importing Given, When, Then from behave to use in step definitions
from behave import *
# Importing webdriver from selenium to interact with the browser
from selenium import webdriver
# Importing By classes from selenium for locators
from selenium.webdriver.common.by import By


# Importing Options from selenium to run the browser in headless mode
from selenium.webdriver.chrome.options import Options
# Importing Class LoginPage from login_page under pages folder
from pages.login_page import LoginPage
# Importing Selenium exceptions to raise when error occurs
from selenium.common.exceptions import TimeoutException


# @given,@when,@then are decorators used to define the step definitions
# First five sceanrios contains same @given step
# These are generated automatically from "settings.json" file
@given('I am on the login page')

# open_login_page() opens the login page of ZEN portal
# context is an object used to share data between steps
def open_login_page(context):

    # Setting up Chrome options to run the browser in headless mode
    chrome_options=Options()
    chrome_options.add_argument("--headless") 
    # context.driver is the Webdriver instance for Chrome browser
    context.driver=webdriver.Chrome(options=chrome_options)

    # Navigating to the login page of ZEN portal
    context.driver.get("https://v2.zenclass.in/login")
    context.driver.maximize_window()

    # context.login_page is an object to interact with LoginPage class
    context.login_page = LoginPage(context.driver)


# valid_login_data() locates the element and enters the valid data
@when('I enter a valid username and password')
def valid_login_data(context):
    context.login_page.login("dhiviyainbox01@gmail.com", "$Flowering92")


# successful_login() checks whether the user is directed to dashboard page
# context.driver.current_url shows the current URL of the page
@then('I should be redirected to the dashboard page')
def successful_login(context):
    assert context.driver.current_url == "https://v2.zenclass.in/dashboard"


# assertion_failure() is used to assert using valid credentials 
# Displays assertion error 
@then('I should see an error message instead of dashboard')
def assertion_failure(context):
    assert "login" in context.driver.current_url, "Test failed:Expected to stay on login page, but redirected to dashboard"


# invalid_login_data() locates the element and enters the invalid data
# This is to test the negative scenario where user enters invalid credentials
# Displays the timeout exception if the user is not redirected to the dashboard page
@when('I enter an invalid username and password')
def invalid_login_data(context):
    context.login_page.login("dhivyainbox@gmail.com", "$Floering")


# unsuccessful_login() checks whether the user remains on the login page
# This step gets skipped because @when throws Timeout Exception 
@then('I should remain on the login page')
def unsuccessful_login(context):
    print("Current URL:", context.driver.current_url)
    assert context.driver.current_url == "https://v2.zenclass.in/login", "Provide valid credentials to login"
    

# input_box() checks the visibility of email and password fields
@when('I check the visibility of username and password fields')
def input_box(context):
    context.input_fields=context.login_page.input_displayed()


# validate_input_box() asserts the email and password fields are visible and editable
@then('username and password fields should be visible and editable')
def validate_input_box(context):
    assert context.input_fields, "Username and password fields are not visible or editable"
        

# when is not used here since it is a validation step
# login_button() checks the visibility of login button
@then('the login button should be visible and clickable')
def validate_login_button(context):
    assert context.login_page.signin_button_enabled(), "Login button is not visible or clickable"


# valid_credentials() logs in to the ZEN portal using valid credentials
# This is used to test the logout functionality
@given('I logged in to the ZEN portal using valid credentials')
def valid_credentials(context):

    # Setting up Chrome options to run the browser in headless mode
    chrome_options=Options()
    chrome_options.add_argument("--headless") 
    context.driver=webdriver.Chrome(options=chrome_options)

    # Navigating to the login page of ZEN portal
    context.driver.get("https://v2.zenclass.in/login")
    context.driver.maximize_window()

    # context.login_page is an object to interact with LoginPage class
    context.login_page = LoginPage(context.driver)
    # Logging in to the ZEN portal using valid credentials
    context.login_page.login("dhiviyainbox01@gmail.com", "$Flowering92")


# logout_button() clicks on the logout button under the profile icon
# After logging in, the user can see the profile icon and dashboard pop-up
# Under theprofile icon the logout button appears
@when('I click on the logout button under the profile icon')
def logout_button(context):

    # Exception handling to catch TimeoutException if logout button is not found
    try:
        context.login_page.logout()
    except TimeoutException:
        print("Logout button not found")
      

# validate_logout() checks whether the user is redirected again to the login page
@then('I should be redirected to the login page')
def validate_logout(context):
    assert context.driver.current_url == "https://v2.zenclass.in/login", "Logout failed, still on dashboard page"
    context.driver.quit()

# ALLURE REPORT GENERATION
# JSON FORMAT:
# behave -f allure_behave.formatter:AllureFormatter -o reports/ features/

# To open json report in browser:
# allure serve reports/

# HTML report:
# allure generate reports/ -o html-report --clean

# To open HTML report in browser:
# allure open html-report
        