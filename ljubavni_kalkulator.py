

def unos(poruka):
    while True:
            ime = input(poruka)
            if ime.strip()=='':
                print('Unos obavezan')
            elif ime.isalpha():
                return ime
            else:
                print('Unos ne smije sadržavati brojeve')


def ucitaj_imena():
    while True:
        ime1=unos('Unesi svoje ime: ')
        ime2=unos('Unesi ime za provjeru: ')
        if ime1!=ime2:
            return {'ime1':ime1, 'ime2':ime2}
        else:
            print('Imena moraju biti različita')


def sortiraj(imena):
    
    lista = []
    for slovo in imena['ime1'].lower():
        lista.append(slovo)
    for slovo in imena['ime2'].lower():
        lista.append(slovo)
    lista.sort()
    return lista


def prebroji(lista):
    rjecnik = dict((i, lista.count(i)) for i in lista)
    brojevi=[]
    for slovo in rjecnik:
        brojevi.append(rjecnik[slovo])
    return brojevi


def izracunaj_postotak(brojevi):
    broj = int(''.join(str(b) for b in brojevi))
    if broj < 100:
        return broj
    else:
        zbroj=[]
        if len(brojevi) % 2 == 0:
            for i in range(0,len(brojevi),2):
                suma = brojevi[i] + brojevi[i+1]
                if suma >= 10:
                    suma=suma % 10
                zbroj.append(suma)
        else:
            for i in range(0,len(brojevi)-1,2):
                suma = brojevi[i] + brojevi[i+1]
                if suma >= 10:
                    suma=suma % 10
                zbroj.append(suma)
            zbroj.append(brojevi[-1])
        return izracunaj_postotak(zbroj)



# preglednije
def ljk():
    rjecnik_imena = ucitaj_imena()
    sortirana_lista = sortiraj(rjecnik_imena)
    brojevi_slova=prebroji(sortirana_lista)
    postotak = izracunaj_postotak(brojevi_slova)
    print (rjecnik_imena['ime1'],'i',
           rjecnik_imena['ime2'],'se vole',
           postotak,'%')


# općenito
while True:
    ljk()
    if input('Unos -1 za prekid: ') == '-1':
        break




