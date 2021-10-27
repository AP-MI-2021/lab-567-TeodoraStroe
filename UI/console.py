from Domain.rezervare2 import toString
from Logic.CRUD import adaugaRezervare, stergeRezervare, modificaRezervare


def printMenu():
    print("1. Adaugare rezervare")
    print("2. Stergere rezervare")
    print("3. Modificare rezervare")
    #print("4. Reducere nr. calorii")
    print("a. Afisare rezervari")
    print("x. Iesire")


def uiAdaugaRezervare(lista):
    id = input("Dati id-ul: ")
    nume = input("Dati numele: ")
    clasa = input("Dati clasa (economy, economy plus, business): ")
    pret = float(input('Dati pretul: '))
    checkin = input("Checkin (da/nu): ")
    return adaugaRezervare(id, nume, clasa, pret, checkin, lista)


def uiStergeRezervare(lista):
    id = input("Dati id-ul rezervarii de sters: ")
    return stergeRezervare(id, lista)


def uiModificaRezervare(lista):
    id = input("Dati id-ul rezervarii de modificat: ")
    nume = input("Dati noul nume: ")
    clasa = input("Dati noua clasa: ")
    pret = float(input('Dati noul pret: '))
    checkin = input("Dati noul checkin: ")
    return modificaRezervare(id, nume, clasa, pret, checkin, lista)


def showAll(lista):
    for rezervare in lista:
        print(toString(rezervare))


#def uiReducereCalorii(lista):
 #   substringNume = input("Dati substringul numelui pt. care prajiturilor li se va reduce nr. de calorii")
  #  caloriiReduse = int(input("Dati valoarea cu care vreti sa reduceti caloriile: "))
   # return reducereCalorii(substringNume, caloriiReduse, lista)


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
        #elif optiune == "4":
            #lista = uiReducereCalorii(lista)
        elif optiune == "a":
            showAll(lista)
        elif optiune == "x":
            break
        else:
            print("Optiune gresita! Reincercati: ")