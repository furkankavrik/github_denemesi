from pytest_bdd import given, when, then

# --------------steps of feature file----------------


# ----------------   carrental_step_defs/test_login.py --------------------

@given('the user is on the login page')
def on_login_page(sayfa, docstring):
    """the user in on the login page."""

    
    sayfa.goto("https://www.economybookings.com/")
    sayfa.wait_for_timeout(5000)
    deger = sayfa.title()
    sayfa.wait_for_load_state(state="load")
    print(f"\n\n\t********{deger}*******")
    print("\nthe step 1 is executed")

    # print(f"\n docstring is: {docstring} \n")# Docstring written in feature file can be used this way as fixture.


@given('the user clicks giris yap button')
def _(sayfa):
    """the user clicks giris yap button."""
    sayfa.locator("span[class='wl-hide']").wait_for(state="visible")
    sayfa.locator("span[class='wl-hide']").click()

    
@when('the user enters valid credentials')
def enter_valid_credentials(sayfa):
    """the user enters valids credentials."""
    # print("the step 3 is executed")


@when('the user clicks kabul et button')
def _():
    """the user clicks kabul et button."""
    pass
    

@then('the user should be logged in')
def logged_in():
    """the user should be logged in."""
    # print("the step 5 is executed")










    """ Araç kiralamanın daha akıllı yolu. Doğru araç, en iyi fiyat. """