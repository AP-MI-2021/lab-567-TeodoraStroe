from Domain.rezervare import getId, getPret, getClasa
from Logic.CRUD import adaugaRezervare, getById
from Logic.functionalitate import ordonareDupaPret, clasaSuperioara, ieftinire


def test_undo_redo():
    # 1. lista goala
    lista = []
    undo_list = []
    redo_list = []

    # 2. se adauga prima rezervare
    rezultat = adaugaRezervare("1", "rezervare1", "economy", 100, "da", lista)
    undo_list.append(lista)
    lista = rezultat

    # 3. se adauga a doua rezervare
    rezultat = adaugaRezervare("2", "rezervare2", "business", 120, "nu", lista)
    undo_list.append(lista)
    lista = rezultat

    # 4. se adauga a treia rezervare
    rezultat = adaugaRezervare("3", "rezervare3", "economy plus", 125, "nu", lista)
    undo_list.append(lista)
    lista = rezultat

    # 5. primul undo scoate ultima rezervare adaugata
    redo_list.append(lista)
    lista = undo_list.pop()
    assert len(lista) == 2
    assert getId(lista[1]) == "2"
    assert getId(lista[0]) == "1"

    # 6. inca un undo scoate penultima rezervare adaugata
    redo_list.append(lista)
    lista = undo_list.pop()
    assert len(lista) == 1
    assert getId(lista[0]) == "1"
    assert undo_list == [[]]

    # 7. inca un undo scoate prima rezervare adaugata
    redo_list.append(lista)
    lista = undo_list.pop()
    assert len(lista) == 0
    assert undo_list == []

    # 8. inca un undo care nu face nimic
    if len(undo_list) > 0:
        redo_list.append(lista)
        lista = undo_list
    assert len(lista) == 0
    assert undo_list == []

    # 9. se adauga trei rezervari
    rezultat = adaugaRezervare("1", "rezervare1", "economy", 100, "da", lista)
    undo_list.append(lista)
    lista = rezultat
    redo_list.clear()

    rezultat = adaugaRezervare("2", "rezervare2", "business", 120, "nu", lista)
    undo_list.append(lista)
    lista = rezultat

    rezultat = adaugaRezervare("3", "rezervare3", "economy plus", 125, "nu", lista)
    undo_list.append(lista)
    lista = rezultat

    assert len(redo_list) == 0
    assert len(undo_list) == 3
    assert len(lista) == 3

    # 10. se face redo (fara sa faca nimic)
    if len(redo_list) > 0:
        undo_list.append(lista)
        lista = redo_list.pop()
    assert len(redo_list) == 0
    assert len(undo_list) == 3
    assert len(lista) == 3

    # 11. se fac 2 undo-uri
    redo_list.append(lista)
    lista = undo_list.pop()
    assert len(lista) == 2
    assert getId(lista[1]) == "2"
    assert getId(lista[0]) == "1"

    redo_list.append(lista)
    lista = undo_list.pop()
    assert len(lista) == 1
    assert getId(lista[0]) == "1"
    assert undo_list == [[]]

    # 12. se face redo
    undo_list.append(lista)
    lista = redo_list.pop()
    assert len(redo_list) == 1
    assert len(undo_list) == 2
    assert len(lista) == 2

    # 13. se face redo
    undo_list.append(lista)
    lista = redo_list.pop()
    assert len(redo_list) == 0
    assert len(undo_list) == 3
    assert len(lista) == 3

    # 14. se fac 2 undo-uri
    redo_list.append(lista)
    lista = undo_list.pop()
    assert len(lista) == 2
    assert getId(lista[1]) == "2"
    assert getId(lista[0]) == "1"

    redo_list.append(lista)
    lista = undo_list.pop()
    assert len(lista) == 1
    assert getId(lista[0]) == "1"
    assert undo_list == [[]]

    # 15. se adauga a patra rezervare
    rezultat = adaugaRezervare("4", "rezervare4", "economy plus", 250, "da", lista)
    undo_list.append(lista)
    lista = rezultat
    redo_list.clear()

    # 16. se face redo (fara sa faca nimic)
    if len(redo_list) > 0:
        undo_list.append(lista)
        lista = redo_list.pop()
    assert len(lista) == 2
    assert len(undo_list) == 2

    # 17. se face undo
    redo_list.append(lista)
    lista = undo_list.pop()
    assert len(lista) == 1
    assert len(undo_list) == 1
    assert len(redo_list) == 1

    # 18. se face undo
    redo_list.append(lista)
    lista = undo_list.pop()
    assert len(lista) == 0
    assert len(undo_list) == 0
    assert len(redo_list) == 2

    # 19. se face 2 redo-uri
    undo_list.append(lista)
    lista = redo_list.pop()
    assert len(lista) == 1

    undo_list.append(lista)
    lista = redo_list.pop()
    assert len(lista) == 2
    assert len(redo_list) == 0

    # 20. se face ultimul redo, care nu face nimic
    if len(redo_list) > 0:
        undo_list.append(lista)
        lista = redo_list.pop()
    assert len(lista) == 2
    assert len(redo_list) == 0
    assert len(undo_list) == 2

def test_undo_redo_clasa_superioara():
    # 1. lista goala
    lista = []
    undo_list = []
    redo_list = []

    # 2. se adauga prima rezervare
    rezultat = adaugaRezervare("1", "rezervare1", "economy", 100, "da", lista)
    undo_list.append(lista)
    lista = rezultat

    # 3. se adauga a doua rezervare
    rezultat = adaugaRezervare("2", "rezervare2", "business", 120, "nu", lista)
    undo_list.append(lista)
    lista = rezultat

    # 4. se adauga a treia rezervare
    rezultat = adaugaRezervare("3", "rezervare3", "economy plus", 125, "nu", lista)
    undo_list.append(lista)
    lista = rezultat

    # 5. se modifica clasa
    rezultat = clasaSuperioara("rezervare1", lista)
    undo_list.append(lista)
    lista = rezultat
    assert getClasa(getById("1", lista)) == "economy plus"

    # 6. primul undo intoarce la clasa originala
    redo_list.append(lista)
    lista = undo_list.pop()
    assert getClasa(getById("1", lista)) == "economy"

    # 7. se face redo
    undo_list.append(lista)
    lista = redo_list.pop()
    assert getClasa(getById("1", lista)) == "economy plus"


def test_undo_redo_ieftinire():
    # 1. lista goala
    lista = []
    undo_list = []
    redo_list = []

    # 2. se adauga prima rezervare
    rezultat = adaugaRezervare("1", "rezervare1", "economy", 100, "da", lista)
    undo_list.append(lista)
    lista = rezultat

    # 3. se adauga a doua rezervare
    rezultat = adaugaRezervare("2", "rezervare2", "business", 120, "nu", lista)
    undo_list.append(lista)
    lista = rezultat

    # 4. se adauga a treia rezervare
    rezultat = adaugaRezervare("3", "rezervare3", "economy plus", 125, "nu", lista)
    undo_list.append(lista)
    lista = rezultat

    # 5. se aplica ieftinirea
    rezultat = ieftinire(10, lista)
    undo_list.append(lista)
    lista = rezultat
    assert getPret(getById("1", lista)) == 90
    assert getPret(getById("2", lista)) == 120
    assert getPret(getById("3", lista)) == 125

    # 6. primul undo intoarce la pretul original
    redo_list.append(lista)
    lista = undo_list.pop()
    assert getPret(getById("1", lista)) == 100
    assert getPret(getById("2", lista)) == 120
    assert getPret(getById("3", lista)) == 125

    # 7. se face redo
    undo_list.append(lista)
    lista = redo_list.pop()
    assert getPret(getById("1", lista)) == 90
    assert getPret(getById("2", lista)) == 120
    assert getPret(getById("3", lista)) == 125

def test_undo_redo_OrdonareDupaPret():
    # 1. lista goala
    lista = []
    undo_list = []
    redo_list = []

    # 2. se adauga prima rezervare
    rezultat = adaugaRezervare("1", "rezervare1", "economy", 100, "da", lista)
    undo_list.append(lista)
    lista = rezultat

    # 3. se adauga a doua rezervare
    rezultat = adaugaRezervare("2", "rezervare2", "business", 120, "nu", lista)
    undo_list.append(lista)
    lista = rezultat

    # 4. se adauga a treia rezervare
    rezultat = adaugaRezervare("3", "rezervare3", "economy plus", 125, "nu", lista)
    undo_list.append(lista)
    lista = rezultat

    # 5. se ordoneaza lista
    rezultat = ordonareDupaPret(lista)
    undo_list.append(lista)
    lista = rezultat
    assert getId(lista[0]) == "3"
    assert getId(lista[1]) == "2"
    assert getId(lista[2]) == "1"

    # 6. primul undo intoarce la lista originala
    redo_list.append(lista)
    lista = undo_list.pop()
    assert getId(lista[0]) == "1"
    assert getId(lista[1]) == "2"
    assert getId(lista[2]) == "3"

    # 7. se face redo
    undo_list.append(lista)
    lista = redo_list.pop()
    assert getId(lista[0]) == "3"
    assert getId(lista[1]) == "2"
    assert getId(lista[2]) == "1"