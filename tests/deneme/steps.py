from pytest_bdd import given, when, then

# --------------steps of feature file----------------


# ----------------   carrental_step_defs/test_login.py --------------------

@given('the user is on the login page')
def on_login_page(sayfa, docstring):
    """the user in on the login page."""
    print("\nthe step 1 is executed")
    
    # sayfa.goto("https://www.economybookings.com/")
    # deger = sayfa.title()
    # sayfa.wait_for_load_state(state="load")
    # print(f"\n\n\t********{deger}*******")
    
    # print(f"\n docstring is: {docstring} \n")# Docstring written in feature file can be used this way as fixture.


@given('the user clicks giris yap button')
def _(sayfa):
    """the user clicks giris yap button."""
    print("\nthe step 2 is executed")
    # sayfa.locator("span[class='wl-hide']").wait_for(state="visible")
    # sayfa.locator("span[class='wl-hide']").click()
    

    
@when('the user enters valid credentials')
def enter_valid_credentials(sayfa):
    """the user enters valids credentials."""
    print("\nthe step 3 is executed")
    # sayfa.locator("#auth-email").fill("furkankavrik@gmail.com")
    


@when('the user clicks kabul et button')
def _(sayfa):
    """the user clicks kabul et button."""
    print("\nthe step 4 is executed")
    # sayfa.get_by_test_id("user-modal-sign-in-component-code-btn").click()
    

@then('the user should be logged in')
def logged_in():
    """the user should be logged in."""
    print("\nthe step 5 is executed")








    """ Araç kiralamanın daha akıllı yolu. Doğru araç, en iyi fiyat. """