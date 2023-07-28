
# Za dva unesena imena
# Program ispisuje koliko se posto vole

import random as r

def izracunaj(i1,i2):
    s = i1.lower() + i2.lower()
    print(s)
    slova=[]
    for z in s:
        slova.append(z)
    slova.sort()
    print(slova)

ime1 = input('Unesi svoje ime: ')

while True:
    ime2 = input('Unesi ime simpatije: ')
    if (ime1.lower()=='tomislav' and ime2.lower()=='nataša') or \
        (ime2.lower()=='tomislav' and ime1.lower()=='nataša'):
        print('99 %')
    else:
        izracunaj(ime1,ime2)
    if input('Nastaviti? (ne za prekid): ')=='ne':
             break;
