def creeazaRezervare(id, nume, clasa, pret, checkin):
    '''
    creaza un dictiionar ce reprezinta o rezervare
    :param id: string
    :param nume: string
    :param clasa: string
    :param pret: float
    :param checkin: string
    :return: un dictionar ce contine o rezervare
    '''
    return {
        "id": id,
        "nume": nume,
        "clasa": clasa,
        "pret": pret,
        "checkin": checkin
    }

def getId(rezervare):
    '''
    da id-ul unei rezervari
    :param rezervare: dictionar ce contine o rezervare
    :return: id-ul rezervarii
    '''
    return rezervare["id"]

def getNume(rezervare):
    return rezervare["nume"]

def getClasa(rezervare):
    return rezervare["clasa"]

def getPret(rezervare):
    return rezervare["pret"]

def getCheckin(rezervare):
    return rezervare["checkin"]


def toString(rezervare):
    return "Id: {}, Nume: {}, Clasa: {}, Pret: {}, Checkin: {}".format(
        getId(rezervare),
        getNume(rezervare),
        getClasa(rezervare),
        getPret(rezervare),
        getCheckin(rezervare)
    )