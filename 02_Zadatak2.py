
# Program unosi dva cijela broja
# Program ispisuje sve brojeve između dva
# unesena broja

b1 = int(input('Unesi prvi broj: '))
b2 = int(input('Unesi drugi broj: '))

manji=b1 if b1<b2 else b2
veci=b1 if b1>b2 else b2
veci=veci+1

for i in range(manji,veci):
    print(i)
