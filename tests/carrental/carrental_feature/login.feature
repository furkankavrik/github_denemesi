@bdd_all
Feature: Login


    Background:
                
        Given the user is on the login page
        """
        This is the dockstring written for the first step in feature file
        """
        Given the user clicks giris yap button

    
    @succesful @login
    Scenario: Succesful Login

        When the user enters valid credentials
        When the user clicks kabul et button
        Then the user should be logged in


    @bdd_fail
    Scenario: Failed Login
        When the user enters valid credentials
        Then the user should be logged in