from Domain.rezervare import  getClasa, getPret, getId
from Logic.CRUD import getById, adaugaRezervare
from Logic.functionalitate import clasaSuperioara, ieftinire, pretMaxim, ordonareDupaPret, sumaPretPeNume

def testClasaSuperioara():
    lista = []
    lista = adaugaRezervare("1", "rezervare1", "economy", 100, "da", lista)
    lista = adaugaRezervare("2", "rezervare2", "business", 120, "nu", lista)
    lista = adaugaRezervare("3", "rezervare1", "economy plus", 120, "nu", lista)

    lista = clasaSuperioara("rezervare1", lista)

    assert getClasa(getById("1", lista)) == "economy plus"
    assert getClasa(getById("2", lista)) == "business"
    assert getClasa(getById("3", lista)) == "business"

def testIeftinire():
    lista = []
    lista = adaugaRezervare("1", "rezervare1", "economy", 100, "da", lista)
    lista = adaugaRezervare("2", "rezervare2", "business", 120, "nu", lista)
    lista = adaugaRezervare("3", "rezervare1", "economy plus", 120, "nu", lista)

    lista = ieftinire(10, lista)

    assert getPret(getById("1", lista)) == 90.0
    assert getPret(getById("2", lista)) == 120
    assert getPret(getById("3", lista)) == 120

def testPretMaxim():
    lista = []
    lista = adaugaRezervare("1", "rezervare1", "economy", 100, "da", lista)
    lista = adaugaRezervare("2", "rezervare2", "business", 120, "nu", lista)
    lista = adaugaRezervare("3", "rezervare3", "economy", 125, "nu", lista)

    rezultat = pretMaxim(lista)

    assert len(rezultat) == 2
    assert rezultat["economy"] == 125
    assert rezultat["business"] == 120

def testOrdonareDupaPret():
    lista = []
    lista = adaugaRezervare("1", "rezervare1", "economy", 100, "da", lista)
    lista = adaugaRezervare("2", "rezervare2", "business", 120, "nu", lista)
    lista = adaugaRezervare("3", "rezervare1", "economy plus", 125, "nu", lista)

    rezultat = ordonareDupaPret(lista)

    assert getId(rezultat[0]) == "3"
    assert getId(rezultat[1]) == "2"
    assert getId(rezultat[2]) == "1"

def testSumaPretPeNume():
    lista = []
    lista = adaugaRezervare("1", "rezervare1", "economy", 100, "da", lista)
    lista = adaugaRezervare("2", "rezervare2", "business", 120, "nu", lista)
    lista = adaugaRezervare("3", "rezervare1", "economy plus", 125, "nu", lista)

    rezultat = sumaPretPeNume(lista)

    assert len(rezultat) == 2
    assert rezultat["rezervare1"] == 225
    assert rezultat["rezervare2"] == 120