
import random as r
import zajednicki_modul as m

sb = r.randint(1,100)

while True:
    b = m.ulaz('Pogodi broj: ',int)
    if sb == b:
        print('Čestitam')
        break
    else:
        if b < sb:
            print('Zamišljeni broj je veći')
        else:
            print('Zamišljeni broj je manji')
