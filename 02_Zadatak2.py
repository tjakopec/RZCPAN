
# Program unosi dva cijela broja
# Program ispisuje sve brojeve između dva
# unesena broja
import zajednicki_modul as z
b1 = z.unos('Unesi prvi broj: ',int)
b2 = z.unos('Unesi drugi broj: ',int)

manji=b1 if b1<b2 else b2
veci=b1 if b1>b2 else b2
veci=veci+1

for i in range(manji,veci):
    print(i)
