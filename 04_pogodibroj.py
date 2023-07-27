
import random as r
import zajednicki_modul as m

sb = r.randint(1,100)
pokusaji=0
pogadali=[]
while True:
    b = m.ulaz('Pogodi broj: ',int)
    pokusaji=pokusaji+1
    if b in pogadali:
        print('To si već probao, daj se skoncentriraj')
    else:
        pogadali.append(b)
        if sb == b:
            print('Čestitam')
            break
        else:
            print('Do sada si probao',pogadali,sep='\n')
            if b < sb:
                print('Zamišljeni broj je veći')
            else:
                print('Zamišljeni broj je manji')
print('Pogodili ste iz',pokusaji,'. pokušaja')
