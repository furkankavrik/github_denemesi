import pytest
import json
from pathlib import Path
from pprint import pprint


def test_deneme(yeni_sayfa):

    sayfa = yeni_sayfa


    sayfa.goto("https://www.economybookings.com/")

    deger = sayfa.title()
   
    print(f"\n\t********{deger}*******")


def test_something(yeni_sayfa):

    print(f"\n\t test_something is active\n\n")
    print("\n\n\n")

    yeni_sayfa.goto("https://www.linkedin.com/")  # user go to linkedin page
    yeni_sayfa.wait_for_load_state(state="load")


    # yeni_sayfa.get_by_text("#caret-small").scroll_into_view_if_needed()
    # yeni_sayfa.locator("#caret-small").click() # user clicks the language dropdown menu
    yeni_sayfa.locator("//p[@class='lrmk8d lrmk3n lrmk0e lrmk3b lrmk5j lrmk5z lrmk6n lrmk7r lrmgeo lrmk8b lrmle7']").click()
    yeni_sayfa.locator("(//div[@role='button'])[12]").click()#user clicks the english option    
    yeni_sayfa.wait_for_load_state(state="load")
    

    
    yeni_sayfa.locator("(//span[@class='lrmk8d lrmlcn lrmlr2 lrmk57 lrmhc3 lrmk8b lrmlis'])[2]").click()#user clicks sign in 

    # //a[@componentkey='cadb46fd-6239-4f44-998f-6393d4f46ade']

    # if yeni_sayfa.locator("//input[@id='_R_1dpbpptiejj35656j6_']").to_be_checked():
    #     yeni_sayfa.locator("//input[@id='_R_1dpbpptiejj35656j6_']").checked()
    # else:
    #     pass


# /following-sibling::label

# page.get_by_role("checkbox").is_checked() (return boolean)



