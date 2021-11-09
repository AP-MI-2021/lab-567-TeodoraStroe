from Domain.rezervare import toString
from Logic.CRUD import adaugaRezervare, stergeRezervare, modificaRezervare
from Logic.functionalitate import clasaSuperioara, ieftinire, pretMaxim, ordonareDupaPret, sumaPretPeNume


def printMenu():
    print("1. Adaugare rezervare")
    print("2. Stergere rezervare")
    print("3. Modificare rezervare")
    print("4. Trecerea tuturor rezervarilor facute pe un nume citit la o clasa superioara")
    print("5. Ieftinirea tuturor rezervarilor la care s-a facut check-in cu un procentaj citit")
    print("6. Determinarea pretului maxim pentru fiecare clasa")
    print("7. Ordonarea rezervarilor descrescator dupa pret")
    print("8. Afisarea sumelor preturilor pentru fiecare nume")
    print("u. Undo")
    print("r. Redo")
    print("a. Afisare rezervari")
    print("x. Iesire")


def uiAdaugaRezervare(lista, undo_list, redo_list):
    try:
        id = input("Dati id-ul: ")
        nume = input("Dati numele: ")
        clasa = input("Dati clasa (economy, economy plus, business): ")
        pret = float(input('Dati pretul: '))
        checkin = input("Checkin (da/nu): ")
        rezultat = adaugaRezervare(id, nume, clasa, pret, checkin, lista)
        undo_list.append(lista)
        redo_list.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def uiStergeRezervare(lista, undo_list, redo_list):
    try:
        id = input("Dati id-ul rezervarii de sters: ")
        rezultat = stergeRezervare(id, lista)
        undo_list.append(lista)
        redo_list.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista



def uiModificaRezervare(lista, undo_list, redo_list):
    try:
        id = input("Dati id-ul rezervarii de modificat: ")
        nume = input("Dati noul nume: ")
        clasa = input("Dati noua clasa: ")
        pret = float(input('Dati noul pret: '))
        checkin = input("Dati noul checkin: ")
        rezultat = modificaRezervare(id, nume, clasa, pret, checkin, lista)
        undo_list.append(lista)
        redo_list.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def uiClasaSuperioara(lista, undo_list, redo_list):
    numeOriginal = input("Dati numele asupra caruia se vor aplica schimbarile: ")
    rezultat = clasaSuperioara(numeOriginal, lista)
    undo_list.append(lista)
    redo_list.clear()
    return rezultat

def uiIeftinire(lista, undo_list, redo_list):
    procentaj=float(input("Dati procentajul: "))
    rezultat = ieftinire(procentaj, lista)
    undo_list.append(lista)
    redo_list.clear()
    return rezultat

def uiPretMaxim(lista):
    rezultat = pretMaxim(lista)
    for clasa in rezultat:
        print("Clasa {} are cel mai mare pret {}".format(clasa, rezultat[clasa]))

def uiOrdonareDupaPret(lista, undo_list, redo_list):
    rezultat = ordonareDupaPret(lista)
    undo_list.append(lista)
    redo_list.clear()
    return rezultat

def uiSumaPretPeNume(lista):
    rezultat = sumaPretPeNume(lista)
    for nume in rezultat:
        print("Numele {} are suma preturilor {}".format(nume, rezultat[nume]))

def showAll(lista):
    for rezervare in lista:
        print(toString(rezervare))



def runMenu(lista):
    undo_list = []
    redo_list = []
    while True:
        printMenu()
        optiune = input("Dati optiunea: ")

        if optiune == "1":
            lista = uiAdaugaRezervare(lista, undo_list, redo_list)
        elif optiune == "2":
            lista = uiStergeRezervare(lista, undo_list, redo_list)
        elif optiune == "3":
            lista = uiModificaRezervare(lista, undo_list, redo_list)
        elif optiune == "4":
            lista = uiClasaSuperioara(lista, undo_list, redo_list)
        elif optiune == "5":
            lista = uiIeftinire(lista, undo_list, redo_list)
        elif optiune == "6":
            uiPretMaxim(lista)
        elif optiune == "7":
            lista = uiOrdonareDupaPret(lista, undo_list, redo_list)
        elif optiune == "8":
            uiSumaPretPeNume(lista)
        elif optiune == "u":
            if len(undo_list)>0:
                redo_list.append(lista)
                lista = undo_list.pop()
            else:
                print("Nu se poate face undo!")
        elif optiune == "r":
            if len(redo_list)>0:
                undo_list.append(lista)
                lista = redo_list.pop()
            else:
                print("Nu se poate face redo!")
        elif optiune == "a":
            showAll(lista)
        elif optiune == "x":
            break
        else:
            print("Optiune gresita! Reincercati: ")