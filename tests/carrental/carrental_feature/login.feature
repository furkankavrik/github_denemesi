Feature: Login
    
    Scenario: Succesful Login
        Given the user in on the login page
        When the user enters valid credentials
        Then the user should be logged in