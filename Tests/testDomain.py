from Domain.rezervare2 import creeazaRezervare, getId, getNume, getClasa, getPret, getCheckin


def testRezervare():
    rezervare = creeazaRezervare("1", "rezervare1", "economy", 100, "da")

    assert getId(rezervare) == "1"
    assert getNume(rezervare) == "rezervare1"
    assert getClasa(rezervare) == "economy"
    assert getPret(rezervare) == 100
    assert getCheckin(rezervare) == "da"
