from Domain.rezervare import toString
from Logic.CRUD import adaugaRezervare, stergeRezervare, modificaRezervare
from Logic.functionalitate import clasaSuperioara, ieftinire


def printMenu():
    print("1. Adaugare rezervare")
    print("2. Stergere rezervare")
    print("3. Modificare rezervare")
    print("4. Trecerea tuturor rezervarilor facute pe un nume citit la o clasa superioara")
    print("5. Ieftinirea tuturor rezervarilor la care s-a facut check-in cu un procentaj citit")
    print("a. Afisare rezervari")
    print("x. Iesire")


def uiAdaugaRezervare(lista):
    try:
        id = input("Dati id-ul: ")
        nume = input("Dati numele: ")
        clasa = input("Dati clasa (economy, economy plus, business): ")
        pret = float(input('Dati pretul: '))
        checkin = input("Checkin (da/nu): ")
        return adaugaRezervare(id, nume, clasa, pret, checkin, lista)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def uiStergeRezervare(lista):
    try:
        id = input("Dati id-ul rezervarii de sters: ")
        return stergeRezervare(id, lista)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista



def uiModificaRezervare(lista):
    try:
        id = input("Dati id-ul rezervarii de modificat: ")
        nume = input("Dati noul nume: ")
        clasa = input("Dati noua clasa: ")
        pret = float(input('Dati noul pret: '))
        checkin = input("Dati noul checkin: ")
        return modificaRezervare(id, nume, clasa, pret, checkin, lista)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def uiClasaSuperioara(lista):
    numeOriginal = input("Dati numele asupra caruia se vor aplica schimbarile: ")
    return clasaSuperioara(numeOriginal, lista)

def uiIeftinire(lista):
    procentaj=float(input("Dati procentajul"))
    return ieftinire(procentaj, lista)

def showAll(lista):
    for rezervare in lista:
        print(toString(rezervare))



def runMenu(lista):
    while True:
        printMenu()
        optiune = input("Dati optiunea: ")

        if optiune == "1":
            lista = uiAdaugaRezervare(lista)
        elif optiune == "2":
            lista = uiStergeRezervare(lista)
        elif optiune == "3":
            lista = uiModificaRezervare(lista)
        elif optiune == "4":
            lista = uiClasaSuperioara(lista)
        elif optiune == "5":
            lista = uiIeftinire(lista)
        elif optiune == "a":
            showAll(lista)
        elif optiune == "x":
            break
        else:
            print("Optiune gresita! Reincercati: ")