# from tests.genel import yeni_sayfa
import pytest


def test_deneme(yeni_sayfa):

    sayfa = yeni_sayfa


    sayfa.goto("https://www.economybookings.com/")

    deger = sayfa.title()
   
    print(f"\n\t********{deger}*******")


def test_something(username):

    print(f"\n\t********{username}*******")


