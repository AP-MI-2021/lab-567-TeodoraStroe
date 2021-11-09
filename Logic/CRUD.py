from Domain.rezervare import creeazaRezervare, getId


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
    if getById(id, lista) is not None:
        raise ValueError("Id-ul exista deja")
    if int(id) < 1:
        raise ValueError("Id-ul nu poate fi nul sau negativ")
    if len(nume) == 0:
        raise ValueError("Introduceti numele!")
    if clasa != "economy" and clasa != "business" and clasa != "economy plus":
        raise ValueError("Clasa invalida! Introduceti economy, economy plus sau business")
    if pret < 0:
        raise ValueError("Pretul nu poate fi negativ")
    if checkin != "da" and checkin != "nu":
        raise ValueError("Checkin invalid! Introduceti da sau nu")
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
    if getById(id, lista) is None:
        raise ValueError("Nu exista o rezervare cu id-ul dat")
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
    if getById(id, lista) is None:
        raise ValueError("Id-ul exista deja")
    if int(id) < 1:
        raise ValueError("Id-ul nu poate fi nul sau negativ")
    if len(nume) == 0:
        raise ValueError("Introduceti numele!")
    if clasa != "economy" and clasa != "business" and clasa != "economy plus":
        raise ValueError("Clasa invalida! Introduceti economy, economy plus sau business")
    if pret < 0:
        raise ValueError("Pretul nu poate fi negativ")
    if checkin != "da" and checkin != "nu":
        raise ValueError("Checkin invalid! Introduceti da sau nu")
    listaNoua = []
    for rezervare in lista:
        if getId(rezervare) == id:
            rezervareNoua = creeazaRezervare(id, nume, clasa, pret, checkin)
            listaNoua.append(rezervareNoua)
        else:
            listaNoua.append(rezervare)
    return listaNoua