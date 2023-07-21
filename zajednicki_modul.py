def unos(poruka,tip):
    while True:
        try:
            return tip(input(poruka))
        except:
            print('Greška pri unosu')
