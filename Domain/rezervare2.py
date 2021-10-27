def creeazaRezervare(id, nume, clasa, pret, checkin):
    '''
    creaza un dictiionar ce reprezinta o rezervare
    :param id: string
    :param nume: string
    :param clasa: string
    :param pret: float
    :param checkin: string
    :return: o lista ce contine o rezervare
    '''
    list=[]
    list.append(id)
    list.append(nume)
    list.append(clasa)
    list.append(pret)
    list.append(checkin)
    return list

def getId(rezervare):
    '''
    da id-ul unei rezervari
    :param rezervare: dictionar ce contine o rezervare
    :return: id-ul rezervarii
    '''
    return rezervare[0]

def getNume(rezervare):
    return rezervare[1]

def getClasa(rezervare):
    return rezervare[2]

def getPret(rezervare):
    return rezervare[3]

def getCheckin(rezervare):
    return rezervare[4]


def toString(rezervare):
    return "Id: {}, Nume: {}, Clasa: {}, Pret: {}, Checkin: {}".format(
        getId(rezervare),
        getNume(rezervare),
        getClasa(rezervare),
        getPret(rezervare),
        getCheckin(rezervare)
    )