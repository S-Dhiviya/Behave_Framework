# Behave framework using Gherkin syntax[Given,When,Then]
# Feature file contains the sceanrios for the login functionality of ZEN portal
# Feature represents which part of the application is being tested
Feature:Login functionality of ZEN portal


  # Sceanrio is like a specific situation or a test case 
  # Scenarios represent the different test cases for the login functionality
  

  # Positive case:Test case for valid credentials
  Scenario: Successful login with valid credentials

    #Given is context of a test case.The context is to be on the login page
    Given I am on the login page
    
    # When is the action that is being performed in the test case
    # In this case, the action is to enter valid username and password
    When I enter a valid username and password

    # Then is the expected outcome of the test case
    # In this case, the expected outcome is to be redirected to the dashboard page
    Then I should be redirected to the dashboard page


  # Negative case:Test case for valid credentials with error message
  Scenario: Error message for valid credentials
    Given I am on the login page
    When I enter a valid username and password
    Then I should see an error message instead of dashboard


  # Negative case: Test case for invalid credentials
  Scenario: Unsuccessful login with invalid credentials
    Given I am on the login page
    When I enter an invalid username and password
    Then I should remain on the login page


  # Positive case:Validation of email and password fields
  Scenario: Username and password fields are visible and editable
    Given I am on the login page
    When I check the visibility of username and password fields
    Then username and password fields should be visible and editable


  # Positive case:Validation of login button
  # When is not used here since it includes only validation step
  Scenario: Login button is visible and clickable
    Given I am on the login page
    Then the login button should be visible and clickable
  

  # Positive case:Validation of logout button
  Scenario: Functionality of Logout button
    Given I logged in to the ZEN portal using valid credentials
    When I click on the logout button under the profile icon
    Then I should be redirected to the login page


   