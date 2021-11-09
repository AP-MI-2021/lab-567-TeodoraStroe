from Domain.rezervare import creeazaRezervare, getId, getNume, getClasa, getPret, getCheckin

def clasaSuperioara(numeOriginal, lista):
    listaNoua = []
    for rezervare in lista:
        if numeOriginal == getNume(rezervare):
            if getClasa(rezervare)=="economy":
                rezervareNoua = creeazaRezervare(
                    getId(rezervare),
                    getNume(rezervare),
                    "economy plus",
                    getPret(rezervare),
                    getCheckin(rezervare)
                )
                listaNoua.append(rezervareNoua)
            elif getClasa(rezervare)=="economy plus":
                rezervareNoua = creeazaRezervare(
                    getId(rezervare),
                    getNume(rezervare),
                    "business",
                    getPret(rezervare),
                    getCheckin(rezervare)
                )
                listaNoua.append(rezervareNoua)
            else:
                rezervareNoua = creeazaRezervare(
                    getId(rezervare),
                    getNume(rezervare),
                    getClasa(rezervare),
                    getPret(rezervare),
                    getCheckin(rezervare)
                )
                listaNoua.append(rezervareNoua)
        else:
            listaNoua.append(rezervare)
    return listaNoua

def ieftinire(procentaj, lista):
    listaNoua=[]
    for rezervare in lista:
        if getCheckin(rezervare)=="da":
            rezervareNoua=creeazaRezervare(
                getId(rezervare),
                getNume(rezervare),
                getClasa(rezervare),
                getPret(rezervare) - (procentaj/100*getPret(rezervare)),
                getCheckin(rezervare)
            )
            listaNoua.append(rezervareNoua)
        else:
            listaNoua.append(rezervare)
    return listaNoua

def pretMaxim(lista):
    rezultat = {}
    for rezervare in lista:
        clasa = getClasa(rezervare)
        pret = getPret(rezervare)
        if clasa in rezultat:
            if pret > rezultat[clasa]:
                rezultat[clasa] = pret
        else:
                rezultat[clasa] = pret
    return rezultat

def ordonareDupaPret(lista):
    return sorted(lista, key = lambda rezervare: getPret(rezervare)*-1)

def sumaPretPeNume(lista):
    rezultat = {}
    for rezervare in lista:
        nume = getNume(rezervare)
        pret = getPret(rezervare)
        if nume in rezultat:
            rezultat[nume] = rezultat[nume] + pret
        else:
            rezultat[nume] = pret
    return rezultat

