from pytest_bdd import given, when, then, scenario, scenarios

scenarios("../carrental_feature/login.feature") # This metis used for binding multi scenarios in a feature file


# @scenario("../carrental_feature/login.feature", 'Succesful Login')#i changed the path of feature file to fix problem.
# def test_succesful_login():
#     print("\n\nEnd of --Succesfull Login-- scenario")
    
    
# Following step definitons run without problem if you need. But i prefere to expose them via conftest file ;)


# @given('the user in on the login page')
# def on_login_page():
#     """the user in on the login page."""
#     print("\nthe step 1 is executed")

    

# @when('the user enters valid credentials')
# def enter_valid_credentials():
#     """the user enters valids credentials."""
#     print("the step 2 is executed")
    


# @then('the user should be logged in')
# def logged_in():
#     """the user should be logged in."""
#     print("the step 3 is executed")
    
