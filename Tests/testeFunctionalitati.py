from Domain.rezervare import  getClasa, getPret
from Logic.CRUD import getById, adaugaRezervare
from Logic.functionalitate import clasaSuperioara, ieftinire

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