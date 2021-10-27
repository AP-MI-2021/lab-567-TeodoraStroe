from Domain.rezervare2 import creeazaRezervare, getId


def adaugaRezervare(id, nume, clasa, pret, checkin, lista):
    '''
    adauga o rezervare intr-o lista
    :param id: string
    :param nume: string
    :param clasa: string
    :param pret: float
    :param checkin: string
    :param lista: lista de rezervari
    :return: o lista continand atat elementele vechi, cat si noua rezervare
    '''
    rezervare = creeazaRezervare(id, nume, clasa, pret, checkin)
    return lista + [rezervare]

def getById(id, lista):
    '''
    gaseste o rezervare cu id-ul dat intr-o lista
    :param id: string
    :param lista: lista de rezervari
    :return: rezervare cu id-ul dat din lista sau None, daca aceasta nu exista
    '''
    for rezervare in lista:
        if getId(rezervare) == id:
            return rezervare
    return None

def stergeRezervare(id, lista):
    """
    sterge o rezervare cu id-ul dat din lista
    :param id: id-ul rezervarii care se va sterge
    :param lista: lista de rezervari
    :return: o lista de rezervari fara elementul cu id-ul dat
    """
    return [rezervare for rezervare in lista if getId(rezervare) != id]

def modificaRezervare(id, nume, clasa, pret, checkin, lista):
    """
    modifica a rezervare cu id-ul dat
    :param id: id-ul rezervarii
    :param nume: numele rezervarii
    :param clasa: clasa rezervarii
    :param pret: pretul rezervarii
    :param checkin: checkinul rezervarii
    :param lista: O lista de rezervari.
    :return: lista modificata.
    """
    listaNoua = []
    for rezervare in lista:
        if getId(rezervare) == id:
            rezervareNoua = creeazaRezervare(id, nume, clasa, pret, checkin)
            listaNoua.append(rezervareNoua)
        else:
            listaNoua.append(rezervare)
    return listaNoua