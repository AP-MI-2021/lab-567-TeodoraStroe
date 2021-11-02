from Logic.CRUD import adaugaRezervare
from Tests.testAll import runAllTests
from UI.console import runMenu

def main():
    runAllTests()
    lista = []
    lista = adaugaRezervare("1", "rezervare1", "economy", 100, "da", lista)
    lista = adaugaRezervare("2", "rezervare2", "business", 120, "nu", lista)
    lista = adaugaRezervare("3", "rezervare1", "economy plus", 120, "nu", lista)
    runMenu(lista)

if __name__ == '__main__':
    main()
