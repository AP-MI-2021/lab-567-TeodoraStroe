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