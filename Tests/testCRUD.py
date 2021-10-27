from Domain.rezervare2 import getId, getNume, getClasa, getCheckin, getPret
from Logic.CRUD import adaugaRezervare, getById, stergeRezervare, modificaRezervare


def testAdaugaRezervare():
    lista = []
    lista = adaugaRezervare("1", "rezervare1", "economy", 100, "da", lista)

    assert len(lista) == 1
    assert getId(getById("1", lista)) == "1"
    assert getNume(getById("1", lista)) == "rezervare1"
    assert getClasa(getById("1", lista)) == "economy"
    assert getPret(getById("1", lista)) == 100
    assert getCheckin(getById("1", lista)) == "da"

def testStergeRezervare():
    lista = []
    lista = adaugaRezervare("1", "rezervare1", "economy", 100, "da", lista)
    lista = adaugaRezervare("2", "rezervare2", "business", 100, "nu", lista)

    lista = stergeRezervare("1", lista)

    assert len(lista) == 1
    assert getById("1", lista) is None
    assert getById("2", lista) is not None

    lista = stergeRezervare("3", lista)

    assert len(lista) == 1
    assert getById("2", lista) is not None

def testModificaRezervare():
    lista = []
    lista = adaugaRezervare("1", "rezervare1", "economy", 100, "da", lista)
    lista = adaugaRezervare("2", "rezervare2", "business", 100, "nu", lista)

    lista = modificaRezervare("1", "rezervare3", "economy plus", 500, "da", lista)

    rezervareUpdatata = getById("1", lista)
    assert getId(rezervareUpdatata) == "1"
    assert getNume(rezervareUpdatata) == "rezervare3"
    assert getClasa(rezervareUpdatata) == "economy plus"
    assert getPret(rezervareUpdatata) == 500
    assert getCheckin(rezervareUpdatata) == "da"

    rezervareNeupdatata = getById("2", lista)
    assert getId(rezervareNeupdatata) == "2"
    assert getNume(rezervareNeupdatata) == "rezervare2"
    assert getClasa(rezervareNeupdatata) == "business"
    assert getPret(rezervareNeupdatata) == 100
    assert getCheckin(rezervareNeupdatata) == "nu"

    lista = []
    lista = adaugaRezervare("1", "rezervare1", "economy", 100, "da", lista)

    lista = modificaRezervare("3", "rezervare3", "economy plus", 500, "da", lista)

    rezervareNeupdatata = getById("1", lista)
    assert getId(rezervareNeupdatata) == "1"
    assert getNume(rezervareNeupdatata) == "rezervare1"
    assert getClasa(rezervareNeupdatata) == "economy"
    assert getPret(rezervareNeupdatata) == 100
    assert getCheckin(rezervareNeupdatata) == "da"
