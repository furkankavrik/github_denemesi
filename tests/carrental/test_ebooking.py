from tests.genel import yeni_sayfa


def test_deneme():

    sayfa = yeni_sayfa()


    sayfa.goto("https://www.economybookings.com/")

    deger = sayfa.title()

    print(deger)

