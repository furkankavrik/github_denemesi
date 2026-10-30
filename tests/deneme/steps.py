from pytest_bdd import given, when, then, parsers

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



# ----------------   carrental_step_defs/test_arguments.py --------------------

# ---------------------------------------step_arguments scenario---------------
@given(parsers.parse('there are {cuc:d} cucumbers'), target_fixture= "cucumber_fix")
def _(cuc):
    """there are 5 cucumbers."""
    print(f"\nnumber of cucumber: {cuc}" )
    return {"cucumber": cuc, "eat": 0}
    
@when(parsers.parse('I eat {eat:d} cucumbers'))
def _(eat, cucumber_fix):
    """I eat 2 cucumbers."""
    print(f"\nnumber of eaten cucmber: {eat}" )
    cucumber_fix["eat"] += eat
    return

@then(parsers.parse('I should have {left:d} cucumbers'))
def _(left, cucumber_fix):
    """I should have 0 cucumbers."""
    print(f"\n remaining cucumbers guess from scenario step {left}")
    assert cucumber_fix["cucumber"] - cucumber_fix["eat"] == left


# -------------------------------------scenario outlines scenario--------------------

@given(parsers.parse('I bought {add:d} kiwi'))
def _(add):
    """I bought <add> kiwi."""
    print(f"\nadd: {add}")


@given(parsers.parse('there are {begin} kiwi'))
def _(begin):
    """there are <begin> kiwi."""
    print(f"\nbegin: {begin}")


@when(parsers.parse('I ate {eat} kiwi'))
def _(eat):
    """I ate <eat> kiwi."""
    print(f"\neat: {eat}")


@when(parsers.parse('My bro {bro_eat} kiwi'))
def _(bro_eat):
    """My bro <bro_eat> kiwi."""
    print(f"\nbro_eat: {bro_eat}")


@then(parsers.parse('There should left {left} kiwi'))
def _(left):
    """There should left <left> kiwi."""
    print(f"\nclealeft: {left}")