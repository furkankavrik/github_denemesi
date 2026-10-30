from pytest_bdd import given, when, then, scenario, scenarios, parsers

scenarios("../carrental_feature/arguments.feature") # This method is used for binding multi scenarios in a feature file

# -------------------------------Following step definiton functions are copied to the conftest file for better  organisation.

# @given(parsers.parse('there are {cuc:d} cucumbers'), target_fixture= "cucumber_fix")
# def _(cuc):
#     """there are 5 cucumbers."""
#     print(f"\nnumber of cucumber: {cuc}" )
#     return {"cucumber": cuc, "eat": 0}
    
# @when(parsers.parse('I eat {eat:d} cucumbers'))
# def _(eat, cucumber_fix):
#     """I eat 2 cucumbers."""
#     print(f"\nnumber of eaten cucmber: {eat}" )
#     cucumber_fix["eat"] += eat
#     return

# @then(parsers.parse('I should have {left:d} cucumbers'))
# def _(left, cucumber_fix):
#     """I should have 0 cucumbers."""
#     print(f"\n remaining cucumbers guess from scenario step {left}")
#     assert cucumber_fix["cucumber"] - cucumber_fix["eat"] == left
    

# -------------------------------Following  step definitons  are for scenario ouline feature.

# @given(parsers.parse('I bought {add:d} kiwi'))
# def _(add):
#     """I bought <add> kiwi."""
#     print(f"\nadd: {add}")


# @given(parsers.parse('there are {begin} kiwi'))
# def _(begin):
#     """there are <begin> kiwi."""
#     print(f"\nbegin: {begin}")


# @when(parsers.parse('I ate {eat} kiwi'))
# def _(eat):
#     """I ate <eat> kiwi."""
#     print(f"\neat: {eat}")


# @when(parsers.parse('My bro {bro_eat} kiwi'))
# def _(bro_eat):
#     """My bro <bro_eat> kiwi."""
#     print(f"\nbro_eat: {bro_eat}")


# @then(parsers.parse('There should left {left} kiwi'))
# def _(left):
#     """There should left <left> kiwi."""
#     print(f"\nleft: {left}")