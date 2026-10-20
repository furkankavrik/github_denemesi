from pytest_bdd import given, when, then

# --------------steps of feature file----------------


# ----------------   carrental_step_defs/test_login.py --------------------

@given('the user is on the login page')
def on_login_page(yeni_sayfa, docstring):
    """the user in on the login page."""

    sayfa = yeni_sayfa
    sayfa.goto("https://www.economybookings.com/")
    deger = sayfa.title()
    print(f"\n\n\t********{deger}*******")
    print("\nthe step 1 is executed")

    print(f"\n docstring is: {docstring} \n")# Docstring written in feature file can be used this way as fixture.

    
@when('the user enters valid credentials')
def enter_valid_credentials():
    """the user enters valids credentials."""
    print("the step 2 is executed")
    

@then('the user should be logged in')
def logged_in():
    """the user should be logged in."""
    print("the step 3 is executed")